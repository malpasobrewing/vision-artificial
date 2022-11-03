import os

from tp2 import constants
from tp2.classifier import create_classifier
from utils.shape import *
from utils.trackbar import *
from joblib import load

show_templates = False

main_window = 'Main Window'

threshold_trackbar = 'Threshold Trackbar'
noise_trackbar = 'Noise Trackbar'
area_trackbar = 'Area Trackbar'

operations_window = 'Operations Window'


def main():

    classifier = load_classifier()

    cv2.namedWindow(main_window)
    cv2.namedWindow(operations_window)

    create_trackbar(trackbar_name=threshold_trackbar, window_name=operations_window, slider_max=151, initial_value=51)
    create_trackbar(noise_trackbar, operations_window, 20, 5)
    create_trackbar(area_trackbar, main_window, 340 * 480, 10000)

    camera = cv2.VideoCapture(1)

    while True:

        _, frame = camera.read()
        gray_frame = apply_color_convertion(frame, cv2.COLOR_RGB2GRAY)
        threshold_frame = apply_threshold(gray_frame, get_trackbar_value(threshold_trackbar, operations_window))
        noise_frame = apply_noise(threshold_frame, get_trackbar_value(noise_trackbar, operations_window))

        contours = get_contours(noise_frame, get_trackbar_value(area_trackbar, main_window))

        shapes = create_shapes_from_contours(contours)

        for shape in shapes:
            shape.predict(classifier)
            shape.draw(frame)

        cv2.imshow(operations_window, np.vstack((threshold_frame, noise_frame)))
        cv2.imshow(main_window, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def load_classifier():
    if os.path.exists(r'' + constants.CLASSIFIER_FILE_NAME):
        return load(constants.CLASSIFIER_FILE_NAME)
    else:
        return create_classifier()


if __name__ == '__main__':
    main()
