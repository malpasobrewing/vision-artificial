import numpy as np

from tp2.descriptor import get_label
from utils.contours import *


class Shape:
    def __init__(self, name, contour):
        self.name = name
        self.contour = contour
        self.match = False

    def show(self, window_name, frame):

        draw_contours(frame, self.contour, colors.BLUE, 3)
        draw_contour_title(frame, self.contour, self.name)
        cv2.imshow(window_name, frame)

    def draw(self, frame):

        if self.match:
            draw_contours(frame, self.contour, colors.GREEN, 10)
        else:
            draw_contours(frame, self.contour, colors.RED, 3)

        draw_contour_title(frame, self.contour, self.name)

    def compare(self, shape_to_compare, max_diff):
        if cv2.matchShapes(self.contour, shape_to_compare.contour, cv2.CONTOURS_MATCH_I1, 0) < max_diff / 10:
            self.match = True
            self.name = shape_to_compare.name
        return self.match

    def predict(self, classifier):
        hu_moments = get_hu_moments(self.contour)
        hu_moments = hu_moments.flatten()

        label_id = classifier.predict(np.array([hu_moments], dtype=np.float32))

        self.name = get_label(label_id)
        self.match = True


def create_shape_from_image(name, path):
    frame = cv2.imread(path)
    gray_frame = apply_color_convertion(frame, cv2.COLOR_RGB2GRAY)
    threshold_frame = apply_threshold(gray_frame, None)
    noise_frame = apply_noise(threshold_frame, None)

    return Shape(name, get_contours(noise_frame, None)[0])


def create_shapes_from_contours(contours):
    shapes = []

    for index, contour in enumerate(contours):
        shape = Shape('Unknow: ' + str(index), contour)
        shapes.append(shape)

    return shapes
