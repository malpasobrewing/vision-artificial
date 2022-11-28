import cv2
from PIL import ImageColor
from utils.colors import *

class Note:

    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    A = 'A'
    B = 'B'

    def __init__(self, id, finger, sound_path):
        self.id = id
        self.finger = finger
        self.sound_path = sound_path
        self.playing = False

    def play(self, player):
        self.playing = True
        player.play(self.sound_path)

    def draw(self, frame):

        if self.finger.recognized():
            cv2.putText(frame,
                        text=self.id,
                        org=(self.finger.TIP_X - 20, self.finger.TIP_Y - 20),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.7,
                        color=WHITE,
                        thickness=3)

            if self.finger.closed:
                color = ImageColor.getcolor(COLORS[2], "RGB")
            else:
                color = ImageColor.getcolor(COLORS[5], "RGB")

            cv2.circle(frame,
                       center=(self.finger.TIP_X, self.finger.TIP_Y),
                       radius=10,
                       color=color,
                       thickness=10)



