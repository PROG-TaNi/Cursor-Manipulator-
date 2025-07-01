# 🖐️ Gesture and Voice-Controlled Interface

An advanced Human-Computer Interaction system that lets you control mouse operations, type using your voice, and interact with multiple-choice questions using **hand gestures**. Built using **MediaPipe**, **OpenCV**, and **PyAutoGUI**, this project leverages real-time video and audio processing to offer a touch-free interface for accessibility, presentations, or futuristic applications.

---

## 📽️ Demo

https://user-images.githubusercontent.com/your-gif-or-video-demo-link.mp4

> *Shows mouse control, click gestures, drag mode, MCQ selection, and voice typing in action.*

---

## 🚀 Features

- 🎯 **Real-time Hand Gesture Recognition**
  - Mouse movement using right-hand index finger.
  - Left click & right click via intuitive finger gestures.
  - Drag mode using 3 raised fingers (left hand).
- 🔊 **Voice Typing with Speech Recognition**
  - Speak to type text when wrists are crossed.
- 📝 **MCQ Mode**
  - Toggle MCQ mode and select options (A/B/C/D) based on fingers raised.
- 🧵 **Multithreaded Voice Listening**
  - Non-blocking voice capture for seamless performance.

---

## 🧠 Tech Stack

| Tool/Library         | Purpose                              |
|----------------------|--------------------------------------|
| `OpenCV`             | Video capture and visualization      |
| `MediaPipe`          | Hand landmark tracking               |
| `PyAutoGUI`          | Mouse and keyboard automation        |
| `SpeechRecognition`  | Convert speech to text               |
| `NumPy`              | Distance and geometry calculations   |
| `Threading` (Python) | Parallel voice recognition handling  |

---

## 🖥️ How It Works

### 🎮 Gesture Controls

| Action               | Gesture                                                       |
|----------------------|---------------------------------------------------------------|
| **Move Cursor**      | Move **right hand's index finger**                            |
| **Left Click**       | Touch **right index** to **left index**                       |
| **Right Click**      | Touch **right index** to **left middle finger**               |
| **Drag Mode**        | Raise **3 fingers on left hand**                              |
| **MCQ Mode**         | Press `m` to toggle. Use 1–4 fingers (right hand) to select A–D |

### 🎙 Voice Typing

- **Trigger**: Cross **left wrist over right wrist**.
- **Action**: Speak, and the system types the detected sentence.

---

## 📦 Installation

### ✅ Prerequisites

- Python 3.7+
- Webcam & microphone enabled

### 📥 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gesture-voice-interface.git
   cd gesture-voice-interface


Install dependencies

bash:-
pip install opencv-python mediapipe pyautogui SpeechRecognition numpy pyaudio

⚠️ On Windows, you might need:

bash:-
pip install pipwin
pipwin install pyaudio

Run the project

bash:-
python gesture_voice_control.py



---

### LICENSE : MIT 

