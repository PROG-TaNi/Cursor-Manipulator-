import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import speech_recognition as sr
import threading

pyautogui.FAILSAFE = False

# Initialize Mediapipe Hands and Drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Helper function to calculate distance between two points
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Helper function to count raised fingers
def count_raised_fingers(hand_landmarks):
    fingers = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y,
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y,
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y,
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y,
    ]
    return sum(fingers)

# Initialize variables
mcq_mode = False
voice_typing_active = False
drag_mode = False
last_left_click_time = 0
last_right_click_time = 0
click_delay = 0.3

# Voice typing function in a separate thread
def voice_typing_thread():
    global voice_typing_active
    while True:
        if voice_typing_active:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for your voice input...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                    print(f"Voice Input: {text}")
                    pyautogui.typewrite(text)
                except sr.UnknownValueError:
                    print("Sorry, I did not understand that.")
                except sr.RequestError:
                    print("Could not request results from Google Speech Recognition service.")
                except sr.WaitTimeoutError:
                    print("Voice recognition timeout.")
            voice_typing_active = False

# Start the voice typing thread
threading.Thread(target=voice_typing_thread, daemon=True).start()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to access the camera.")
        break

    # Flip the frame horizontally for a mirror-like effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert the frame to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Initialize hand landmarks
    left_hand, right_hand = None, None

    if result.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            label = handedness.classification[0].label  # 'Left' or 'Right'

            # Assign landmarks based on the label
            if label == 'Right':
                right_hand = hand_landmarks
            elif label == 'Left':
                left_hand = hand_landmarks

            # Draw the landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Toggle MCQ mode
    key = cv2.waitKey(1) & 0xFF
    if key == ord('m'):
        mcq_mode = not mcq_mode

    if mcq_mode:
        cv2.putText(frame, "MCQ Mode Active", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Detect crossing hands for voice typing
    if left_hand and right_hand:
        left_wrist = left_hand.landmark[mp_hands.HandLandmark.WRIST]
        right_wrist = right_hand.landmark[mp_hands.HandLandmark.WRIST]

        left_wrist_x = left_wrist.x * w
        right_wrist_x = right_wrist.x * w

        if left_wrist_x > right_wrist_x and not voice_typing_active:
            voice_typing_active = True

    # Right hand for mouse movement or MCQ mode
    if right_hand:
        fingers_raised = count_raised_fingers(right_hand)

        if mcq_mode:
            # MCQ Mode: Show option based on raised fingers
            option = ["No Option", "A", "B", "C", "D"][fingers_raised]
            cv2.putText(frame, f"Option: {option}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        else:
            # Mouse movement with speed control
            try:
                index_tip = right_hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                mouse_x = int(index_tip.x * w)
                mouse_y = int(index_tip.y * h)
                speed_multiplier = 1 + fingers_raised  # Speed increases with more raised fingers
                pyautogui.moveTo(mouse_x * speed_multiplier, mouse_y * speed_multiplier)
            except Exception as e:
                print(f"Error processing right hand: {e}")

    # Handle left and right clicks based on gestures between both hands
    if left_hand and right_hand:
        try:
            right_index = right_hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            left_index = left_hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            left_middle = left_hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Left click: right index finger touches left index finger
            if calculate_distance((right_index.x * w, right_index.y * h), (left_index.x * w, left_index.y * h)) < 30:
                if time.time() - last_left_click_time > click_delay:
                    pyautogui.click()
                    last_left_click_time = time.time()

            # Right click: left middle finger touches right index finger
            if calculate_distance((left_middle.x * w, left_middle.y * h), (right_index.x * w, right_index.y * h)) < 30:
                if time.time() - last_right_click_time > click_delay:
                    pyautogui.rightClick()
                    last_right_click_time = time.time()
        except Exception as e:
            print(f"Error processing clicks: {e}")

    # Drag gesture: 3 fingers raised on the left hand
    if left_hand:
        try:
            fingers_raised_left = count_raised_fingers(left_hand)
            if fingers_raised_left == 3:
                if not drag_mode:
                    pyautogui.mouseDown()
                    drag_mode = True
            else:
                if drag_mode:
                    pyautogui.mouseUp()
                    drag_mode = False
        except Exception as e:
            print(f"Error processing drag gesture: {e}")

    # Display the video feed
    cv2.imshow("Hand Gesture Control", frame)

    # Exit on pressing 'q'
    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
