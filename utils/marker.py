import cv2
from PIL import ImageColor

from utils.colors import COLORS


class Marker:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.color = ImageColor.getcolor(COLORS[id], "RGB")

    def draw(self, frame):
        cv2.circle(img=frame, center=self.pos, radius=7, color=self.color, thickness=-1)
        cv2.putText(frame, str(self.id), (self.x - 20, self.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.color, 3)

