import cv2 as cv
import mediapipe as mp
import numpy as np
import time

# MediaPipe modules for hand detection
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

# Function to calculate Euclidean distance between two hand landmarks
def euclidean_distance(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Function to count number of fingers raised
def count_fingers(hand_landmarks, label):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb logic
    if label == "Left":
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0]-1].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0]-1].x else 0)

    # Other four fingers
    for i in range(1, 5):
        fingers.append(1 if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i]-2].y else 0)

    return fingers.count(1)

# Function to detect gestures using two hands
def detectGesture(hand1_data, hand2_data):
    (hand1, label1), (hand2, label2) = hand1_data, hand2_data


    f1 = count_fingers(hand1, label1)
    f2 = count_fingers(hand2, label2)
    i1, i2 = hand1.landmark[8], hand2.landmark[8]
    t1, t2 = hand1.landmark[4], hand2.landmark[4]

    # dist = euclidean_distance(hand1.landmark[8], hand2.landmark[8])
    

    def is_fist_and_palm(f1, f2):
        return (f1 == 0 and f2 == 5) or (f1 == 5 and f2 == 0)

    def is_l_shape(hand):
        lm = hand.landmark
        thumb_up = lm[4].x < lm[3].x or lm[4].x > lm[3].x  # depends on left/right
        index_up = lm[8].y < lm[6].y
        others_folded = all(
            lm[fid].y > lm[fid - 2].y for fid in [12, 16, 20]
        )
        return thumb_up and index_up and others_folded
    thumbs_close = euclidean_distance(hand1.landmark[4], hand2.landmark[4]) < 0.05

    if is_l_shape(hand1) and is_l_shape(hand2) and thumbs_close:
        return "-"
    
    def is_thumbs_up(hand, label):
        tip_ids = [4, 8, 12, 16, 20]
        lm = hand.landmark
        if label == "Left":
            thumb = lm[tip_ids[0]].x > lm[tip_ids[0] - 1].x
        else:
            thumb = lm[tip_ids[0]].x < lm[tip_ids[0] - 1].x
        others_folded = all(lm[tip_ids[i]].y > lm[tip_ids[i] - 2].y for i in range(1, 5))
        return thumb and others_folded

    if is_thumbs_up(hand1, label1) or is_thumbs_up(hand2, label2):
        return "+"
    

    
    def is_rock_sign(hand):
        lm = hand.landmark
        index_up = lm[8].y < lm[6].y
        pinky_up = lm[20].y < lm[18].y
        middle_folded = lm[12].y > lm[10].y
        ring_folded = lm[16].y > lm[14].y
        return index_up and pinky_up and middle_folded and ring_folded

    if is_rock_sign(hand1) and is_rock_sign(hand2):
        return "*"
    
    
    heart_index = euclidean_distance(i1, i2) < 0.05
    heart_thumb = euclidean_distance(t1, t2) < 0.05
    if heart_index and heart_thumb:
        return "exit"

    # elif (f1 == 1 and f2 == 2) or (f1 == 2 and f2 == 1):
    #     return "-"
    # elif (f1 == 1 and f2 == 3) or (f1 == 3 and f2 == 1):
    #     return "*"
        # ➗ Division: OK sign (thumb & index touch on both hands)
    thumb_index_close_1 = euclidean_distance(hand1.landmark[4], hand1.landmark[8]) < 0.04
    thumb_index_close_2 = euclidean_distance(hand2.landmark[4], hand2.landmark[8]) < 0.04

    if thumb_index_close_1 and thumb_index_close_2:
        return "/"
    
    
    elif is_fist_and_palm(f1, f2):
        return "del"

    elif (f1 == 1 and f2 == 5) or (f1 == 5 and f2 == 1):
        return "6"
    elif (f1 == 2 and f2 == 5) or (f1 == 5 and f2 == 2):
        return "7"
    elif (f1 == 3 and f2 == 5) or (f1 == 5 and f2 == 3):
        return "8"
    elif (f1 == 4 and f2 == 5) or (f1 == 5 and f2 == 4):
        return "9"
    elif f1 == 0 and f2 == 0:
        return "="
    elif f1 == 5 and f2 == 5:
        return "clear"
    return None

# Initialize variables
last_update_time = 0
delay = 1.25
expression = ""
res = ""

 
# Open webcam
cap = cv.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        continue

    image = cv.flip(image, 1)
    img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    current_time = time.time()
    hand_data = []

    # Detect hands and count fingers
    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            label = hand_handedness.classification[0].label
            hand_data.append((hand_landmarks, label))
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Single hand input for digits 0–5
        if len(hand_data) == 1:
            hand_landmarks, label = hand_data[0]
            fingers_up = count_fingers(hand_landmarks, label)
            if fingers_up in [0, 1, 2, 3, 4, 5] and current_time - last_update_time > delay:
                expression += str(fingers_up)
                last_update_time = current_time

         
        # Two-hand gestures for operations/commands
        if len(hand_data) == 2:
            gesture = detectGesture(hand_data[0], hand_data[1])

            if gesture == "exit":
                break
            elif gesture == "clear":
                expression = ""
                res = ""
                last_update_time = current_time
            elif gesture == "del" and current_time - last_update_time > delay:
                expression = expression[:-1]
                last_update_time = current_time
            elif gesture == "=" and current_time - last_update_time > delay:
                try:
                    res = str(eval(expression))
                except:
                    res = "Error"
                last_update_time = current_time
            elif gesture and current_time - last_update_time > delay:
                expression += gesture
                last_update_time = current_time

    # Display on screen
    cv.putText(image, f'Expr: {expression}', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.putText(image, f'Result: {res}', (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv.imshow("Gesture Math Solver", image)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
    elif key == ord('c'):
        expression = ""
        res = ""

# Cleanup
cap.release()
cv.destroyAllWindows()