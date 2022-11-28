from final.SoundPlayer import SoundPlayer


class Piano:
    def __init__(self, notes):
        self.notes = notes
        self.show = False
        self.player = SoundPlayer()

    def on_key_pressed(self, hand, finger, hands_motion_event):

        if hands_motion_event == 0:
            for note in self.notes:
                note.finger.reset()
        else:
            note = self.get_note(hand, finger)
            if note is not None:
                if hands_motion_event == 1:
                    note.playing = False
                elif hands_motion_event == 2:
                    if note.playing is False:
                        note.play(self.player)

    def get_note(self, hand, finger):
        for note in self.notes:
            if note.finger.hand_id == hand.id and note.finger.id == finger.id:
                return note
        return None

    def draw(self, frame):
        for note in self.notes:
            note.draw(frame)
