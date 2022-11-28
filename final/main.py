import cv2
import mediapipe as mp

from model.Finger import Finger
from model.Hand import Hand
from model.Note import Note
from model.Piano import Piano
from final.HandsMotionTracking import HandsMotionTracking

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

hands_motion_tracking = HandsMotionTracking(hand_right, hand_left)

piano = Piano([
    Note(Note.C, hand_right.get_finger(4), './sounds/c.wav'),
    Note(Note.D, hand_right.get_finger(8), './sounds/d.wav'),
    Note(Note.E, hand_right.get_finger(12), './sounds/e.wav'),
    Note(Note.F, hand_right.get_finger(16), './sounds/f.wav'),
    Note(Note.G, hand_right.get_finger(20), './sounds/g.wav'),
    Note(Note.A, hand_left.get_finger(4), './sounds/a.wav'),
    Note(Note.B, hand_left.get_finger(8), './sounds/b.wav'),
])

hands_motion_tracking.add_listener(piano.on_key_pressed)


def main():

    with mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)

            hands_motion_tracking.track(frame, hands)

            piano.draw(frame)

            cv2.imshow('TP-FINAL', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
