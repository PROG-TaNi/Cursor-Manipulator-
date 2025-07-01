🖐️ Hand Gesture & Voice Controlled Interface
A real-time hand gesture and speech recognition-based interface system built with MediaPipe, OpenCV, PyAutoGUI, and SpeechRecognition. This system lets users control their computer through gestures (mouse movement, left/right clicks, drag), switch to MCQ mode, and type using their voice when crossing their hands.

🎯 Features
✅ Real-time mouse control using right-hand index finger

🖱️ Gesture-based left & right mouse clicks

✊ Drag mode using three raised fingers on the left hand

🔈 Voice typing when both wrists cross

🧠 MCQ mode for recognizing raised fingers and selecting options (A/B/C/D)

🧵 Multithreaded voice recognition to prevent UI freeze

🧠 Technologies Used
Library	Purpose
OpenCV	Video capture and GUI display
MediaPipe	Real-time hand landmark detection
PyAutoGUI	Simulating keyboard and mouse
SpeechRecognition	Voice-to-text input
NumPy	Mathematical operations
Threading	Handling voice typing concurrently

⚙️ How It Works
🖐 Gesture Recognition
Mouse Movement: Right hand's index finger moves the cursor.

Clicking:

Left click: Right index touches left index.

Right click: Right index touches left middle finger.

Drag Mode: Raise exactly 3 fingers on the left hand.

MCQ Mode: Press m to toggle. Raised fingers show option:

1 = A, 2 = B, 3 = C, 4 = D

🎙 Voice Typing
Cross both hands (left wrist crosses right) to activate.

Dictate into the mic; text will be typed using pyautogui.typewrite().

🛠️ Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui SpeechRecognition numpy pyaudio
⚠️ Note: For pyaudio installation issues, refer to your OS-specific instructions.

Run the script

bash
Copy
Edit
python gesture_voice_control.py
⌨️ Controls
Key	Action
m	Toggle MCQ Mode
q	Quit the Application

📌 Notes
Ensure a good lighting environment for better hand tracking.

Voice typing is sensitive to background noise. Try using a headset mic.

pyautogui.FAILSAFE is disabled — move the cursor to a screen corner with caution.

📷 Demo (Optional)
(Insert GIFs or YouTube demo link here showing cursor control, click gestures, voice typing, and MCQ mode in action.)

🙌 Acknowledgements
MediaPipe by Google

OpenCV

PyAutoGUI

SpeechRecognition

📄 License
This project is open-source and available under the MIT License.
