import cv2


class HandsMotionTracking:
    NO_HANDS = 0
    FINGER_CLOSE_EVENT = 1
    FINGER_OPEN_EVENT = 2
    HAND_CLOSE_EVENT = 3
    HAND_OPEN_EVENT = 4

    def __init__(self, hand_right, hand_left):
        self.listeners = []
        self.hand_right = hand_right
        self.hand_left = hand_left

    def add_listener(self, listener):
        self.listeners.append(listener)

    def on_fire_event(self, hand, finger, event_type):
        for listener in self.listeners:
            listener(hand, finger, event_type)

    def track(self, frame, hands):
        height, width, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                for idx, classification in enumerate(results.multi_handedness):
                    if classification.classification[0].index == index:
                        left_or_right_hand = classification.classification[0].index
                        for (finger_id, _) in enumerate(hand_landmarks.landmark):
                            if left_or_right_hand == 1:
                                hand = self.hand_right
                            else:
                                hand = self.hand_left

                            finger = hand.get_finger(finger_id)
                            if finger is not None:
                                height, width, _ = frame.shape
                                finger.on_movement(hand_landmarks.landmark, width, height)

                                if finger.closed:
                                    self.on_fire_event(hand, finger, HandsMotionTracking.FINGER_CLOSE_EVENT)
                                elif finger.closed is False:
                                    self.on_fire_event(hand, finger, HandsMotionTracking.FINGER_OPEN_EVENT)
        else:
            self.on_fire_event(None, None, HandsMotionTracking.NO_HANDS)
