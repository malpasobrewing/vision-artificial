class Hand:
    def __init__(self, id, fingers):
        self.id = id
        self.fingers = fingers

    def get_finger(self, finger_id):
        for finger in self.fingers:
            if finger.id == finger_id:
                return finger
        return None
