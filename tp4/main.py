import cv2
import mediapipe as mp
from pip._internal.utils.misc import enum

from model.Finger import Finger
from model.Hand import Hand
from utils.colors import *

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

hand_right = Hand(Hand.HAND_RIGHT, [
    Finger(4, 'Thumb', Hand.HAND_RIGHT),
    Finger(8, 'Index Finger', Hand.HAND_RIGHT),
    Finger(12, 'Middle Finger', Hand.HAND_RIGHT),
    Finger(16, 'Ring Finger', Hand.HAND_RIGHT),
    Finger(20, 'Pinky', Hand.HAND_RIGHT)
])

hand_left = Hand(Hand.HAND_LEFT, [
    Finger(4, 'Thumb', Hand.HAND_LEFT),
    Finger(8, 'Index Finger', Hand.HAND_LEFT),
    Finger(12, 'Middle Finger', Hand.HAND_LEFT),
    Finger(16, 'Ring Finger', Hand.HAND_LEFT),
    Finger(20, 'Pinky', Hand.HAND_LEFT)
])


def main():
    with mp_hands.Hands(
            max_num_hands=2,
            min_tracking_confidence=0.5,
            min_detection_confidence=0.5) as hands:
        while cap.isOpened():
        # while True:
            ret, frame = cap.read()
            # frame = cv2.imread('./images/hands.jpg')
            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    for idx, classification in enumerate(results.multi_handedness):
                        if classification.classification[0].index == index:
                            left_or_right_hand = classification.classification[0].index
                            for (i, _) in enumerate(hand_landmarks.landmark):
                                if left_or_right_hand == 1:
                                    hand = hand_right
                                else:
                                    hand = hand_left

                                finger = hand.get_finger(i)
                                if finger is not None:
                                    finger.on_movement(hand_landmarks.landmark, width, height)
                                    finger.draw(frame)


            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
