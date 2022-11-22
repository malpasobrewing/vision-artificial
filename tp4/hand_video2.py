import cv2
import mediapipe as mp

from model.finger import Finger
from model.hand import Hand
from utils.colors import *

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(1)

hand = Hand('BOTH', [
    Finger(4, 'Thumb'),
    Finger(8, 'Index Finger'),
    Finger(12, 'Middle Finger'),
    Finger(16, 'Ring Finger'),
    Finger(20, 'Pinky')
])


def main():

    with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
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
                for hand_landmarks in results.multi_hand_landmarks:
                    for (i, _) in enumerate(hand_landmarks.landmark):
                        finger = hand.get_finger(i)
                        if finger is not None:
                            finger.update(hand_landmarks.landmark, width, height)
                            finger.draw(frame)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
