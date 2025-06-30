# ✋ Gesture-Calculator

Solve math problems **hands-free** using your webcam and hand gestures!  
Built with `OpenCV`, `MediaPipe`, and Python magic. 🔢🤖

---

## 📸 Demo
![demo gif or image placeholder]

---

## 🧠 Features

✅ Real-time hand detection using MediaPipe  
✅ Gesture recognition for numbers and math operations  
✅ Custom symbolic gestures (like thumbs up, heart sign, rock sign)  
✅ Fully interactive math expression builder and solver  
✅ Exit and delete commands using unique two-hand gestures

---

## 💻 Technologies Used

| Tool         | Purpose                            |
|--------------|-------------------------------------|
| Python       | Main programming language           |
| OpenCV       | Webcam feed + UI overlay            |
| MediaPipe    | Hand landmark tracking (21 points)  |
| NumPy        | Math + distance calculations        |
| `eval()`     | Built-in math evaluation            |

---

## 🖐️ Gesture Reference Guide

| Action      | Gesture                                       | Description                        | Meaning                         |
|-------------|-----------------------------------------------|------------------------------------|---------------------------------|
| `0–5`       | Show 0–5 fingers                              | One hand                           | Digit entry                     |
| `6–9`       | One hand (5 fingers) + Other (1–4 fingers)    | Count combined                     | Digit entry                     |
| `+`         | 👍 Thumbs up                                  | Thumbs up on both hands            | Addition                        |
| `-`         | 🤌 L-shape with thumbs meeting                | Index + Thumb "L", both hands      | Subtraction                     |
| `×`         | 🤘 Rock sign                                  | Thumb + Pinky extended both hands  | Multiplication                  |
| `/`         | 👌 OK sign                                    | Thumb touches index finger both hands | Division                        |
| `=`         | 👊👊 Both fists                                | 0 fingers on both hands            | Evaluate expression             |
| `clear`     | 🖐️🖐️ Both hands fully open                   | All 5 fingers up both hands         | Clear input                     |
| `exit`      | ❤️ Heart with Index + Thumb tips              | Fingers curved, thumbs/index meet  | Exit the application            |
| `del`       | ✊✋ One Fist + One Open Palm                   | 0 fingers + 5 fingers             | Delete last input character     |

---

## Credits 💫

