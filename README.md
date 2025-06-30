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

| Action      | Gesture (Both Hands)                          | Description                        |
|-------------|-----------------------------------------------|------------------------------------|
| `0–5`       | Show 0–5 fingers                              | One hand                           |
| `6–9`       | One hand (5 fingers) + Other (1–4 fingers)    | Count combined                     |
| `+`         | 👍 Thumbs up                                  | Thumbs up on both hands            |
| `-`         | 🤌 L-shape with thumbs meeting                | Index + Thumb "L", both hands      |
| `×`         | 🤘 Rock sign                                  | Thumb + Pinky extended both hands  |
| `/`         | 👌 OK sign                                    | Thumb touches index finger         |
| `=`         | 👊👊 Both fists                                | 0 fingers on both hands           |
| `clear`     | 🖐️🖐️ Both hands fully open                   | All 5 fingers up                   |
| `exit`      | ❤️ Heart with Index + Thumb tips              | Fingers curved, thumbs/index meet  |
| `del`       | ✊✋ One Fist + One Open Palm                   | 0 fingers + 5 fingers              |

---

## Credits 💫

