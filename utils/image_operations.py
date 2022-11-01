import cv2
from utils.trackbar import *

threshold_max_value = 151
noise_max_value = 10


def apply_color_convertion(frame, color):
    return cv2.cvtColor(frame, color)


def apply_threshold(frame, threshold_value):

    if threshold_value is None:
        threshold_value = threshold_max_value

    # _, f = cv2.threshold(frame,
    #                      trackbar_value,
    #                      threshold_max_value,
    #                      cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    f = cv2.adaptiveThreshold(frame, threshold_max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                              threshold_value,
                              10)
    return f


def apply_noise(frame, noise_value):

    if noise_value is None:
        noise_value = noise_max_value

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (noise_value, noise_value))
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing
