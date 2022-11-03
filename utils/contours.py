import glob
from math import copysign, log10

from utils import colors
from utils.image_operations import *


def read_from_images(path, show):
    contours = []

    for index, img in enumerate(glob.glob(r'' + path + '*.png')):

        frame = cv2.imread(img)
        gray_frame = apply_color_convertion(frame, cv2.COLOR_RGB2GRAY)
        threshold_frame = apply_threshold(gray_frame, False, False)
        noise_frame = apply_noise(threshold_frame, False, False)

        contours.append(get_contours(noise_frame, False))

        if show:
            draw_contours(frame, contours[index], colors.BLUE, 5)
            cv2.imshow('contours-window', frame)
            if cv2.waitKey() & 0xFF:
                continue
        else:
            continue

    return contours


def find_contours(frame):
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours


def draw_contours(frame, contours, color, thickness):
    cv2.drawContours(frame, contours, -1, color, thickness)
    return frame


def draw_contour_title(frame, contour, title):
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv2.putText(frame, title, (cX - 20, cY - 20), cv2.FONT_HERSHEY_PLAIN, 2, colors.BLACK, 3)


def get_contours(frame, min_area):
    if min_area is None:
        min_area = 10000

    contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    return get_biggest_contours(contours, 3, min_area)
    # return contours


def get_biggest_contours(contours, amount, min_area):
    contours = filter(lambda x: (cv2.contourArea(x) >= min_area), contours)
    return sorted(contours, key=cv2.contourArea, reverse=True)[0:amount]


def get_hu_moments(contour):
    moments = cv2.moments(contour)
    hu_moments = cv2.HuMoments(moments)
    for i in range(len(hu_moments)):
        if hu_moments[i] != 0:
            hu_moments[i] = -1 * copysign(1.0, hu_moments[i]) * log10(abs(hu_moments[i]))
    return hu_moments


if __name__ == '__main__':
    read_from_images('../static/images/', True)
