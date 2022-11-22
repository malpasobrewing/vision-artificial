import math
import cv2
import mediapipe as mp
from PIL import ImageColor

from utils.colors import COLORS

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(1)


with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:

            fingers = [4, 8, 12, 16, 20]
            for hand_landmarks in results.multi_hand_landmarks:
                for (i, points) in enumerate(hand_landmarks.landmark):
                    if i in fingers:
                        x = int(points.x * width)
                        y = int(points.y * height)

                        cv2.circle(frame,
                                   center=(x, y),
                                   radius=5,
                                   color=ImageColor.getcolor(COLORS[5], "RGB"),
                                   thickness=5)

                        x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
                        y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)

                        x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * width)
                        y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * height)

                        length = math.hypot(x2 - x4, y2 - y4)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
