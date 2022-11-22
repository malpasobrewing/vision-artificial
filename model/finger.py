import math

import cv2
import mediapipe as mp
from PIL import ImageColor

from utils.colors import *


class Finger:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.distance = 0
        self.TIP_X = None
        self.TIP_Y = None
        self.MCP_X = None
        self.MCP_Y = None

        self.has_move = False

    def update(self, landmark, width, height):
        if self.id == mp.solutions.hands.HandLandmark.THUMB_TIP:
            self.TIP_X = int(landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x * width)
            self.TIP_Y = int(landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y * height)
            self.MCP_X = int(landmark[mp.solutions.hands.HandLandmark.THUMB_MCP].x * width)
            self.MCP_Y = int(landmark[mp.solutions.hands.HandLandmark.THUMB_MCP].y * height)
            self.distance = math.hypot(self.MCP_X - self.TIP_X, self.MCP_Y - self.TIP_Y)

        elif self.id == mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP:
            self.TIP_X = int(landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x * width)
            self.TIP_Y = int(landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y * height)
            self.MCP_X = int(landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP].x * width)
            self.MCP_Y = int(landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP].y * height)
            self.distance = math.hypot(self.MCP_X - self.TIP_X, self.MCP_Y - self.TIP_Y)

        elif self.id == mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP:
            self.TIP_X = int(landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
            self.TIP_Y = int(landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
            self.MCP_X = int(landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP].x * width)
            self.MCP_Y = int(landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP].y * height)
            self.distance = math.hypot(self.MCP_X - self.TIP_X, self.MCP_Y - self.TIP_Y)

        elif self.id == mp.solutions.hands.HandLandmark.RING_FINGER_TIP:
            self.TIP_X = int(landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].x * width)
            self.TIP_Y = int(landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].y * height)
            self.MCP_X = int(landmark[mp.solutions.hands.HandLandmark.RING_FINGER_MCP].x * width)
            self.MCP_Y = int(landmark[mp.solutions.hands.HandLandmark.RING_FINGER_MCP].y * height)
            self.distance = math.hypot(self.MCP_X - self.TIP_X, self.MCP_Y - self.TIP_Y)

        elif self.id == mp.solutions.hands.HandLandmark.PINKY_TIP:
            self.TIP_X = int(landmark[mp.solutions.hands.HandLandmark.PINKY_TIP].x * width)
            self.TIP_Y = int(landmark[mp.solutions.hands.HandLandmark.PINKY_TIP].y * height)
            self.MCP_X = int(landmark[mp.solutions.hands.HandLandmark.PINKY_MCP].x * width)
            self.MCP_Y = int(landmark[mp.solutions.hands.HandLandmark.PINKY_MCP].y * height)
            self.distance = math.hypot(self.MCP_X - self.TIP_X, self.MCP_Y - self.TIP_Y)

        if self.distance > 0:
            self.has_move = self.distance < 100


    def draw(self, frame):
        if self.TIP_X is not None:
            cv2.circle(frame,
                       center=(self.TIP_X, self.TIP_Y),
                       radius=5,
                       color=ImageColor.getcolor(COLORS[5], "RGB"),
                       thickness=5)

            cv2.circle(frame,
                       center=(self.MCP_X, self.MCP_Y),
                       radius=5,
                       color=ImageColor.getcolor(COLORS[1], "RGB"),
                       thickness=5)

        if self.has_move:
            cv2.putText(frame,
                        text=self.__str__(),
                        org=(self.TIP_X - 20, self.TIP_Y - 20),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.7,
                        color=WHITE,
                        thickness=3)

    def __str__(self):
        return self.name + ' ' + str(self.has_move)
