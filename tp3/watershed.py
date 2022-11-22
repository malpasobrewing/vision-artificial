import cv2
import numpy as np

from utils.marker import Marker
from utils.image_operations import apply_watershed

main_window = 'Main Window'
output_window = 'Output Window'

cv2.namedWindow(main_window)

image_x_size = 640
image_y_size = 597


def main():

    frame = cv2.imread('./images/buttons.png')

    markers = []
    marker_index = 49  # 1 en ASCII

    seeds = np.zeros((image_y_size, image_x_size), np.uint8)

    while True:
        cv2.setMouseCallback(main_window, add_marker_event, [markers, marker_index, seeds])

        frame_copy = frame.copy()
        seeds_copy = seeds.copy()

        for marker in markers:
            marker.draw(frame_copy)
            marker.draw(seeds_copy)

        cv2.imshow(main_window, np.hstack((frame_copy, cv2.applyColorMap(seeds_copy, cv2.COLORMAP_HOT))))

        key = cv2.waitKey(100) & 0xFF
        if key == 32:
            cv2.imshow(output_window, apply_watershed(frame.copy(), seeds))

        if ord('1') <= key <= ord('9'):
            marker_index = key

        if key == ord('r'):
            markers = []
            seeds = np.zeros((image_y_size, image_x_size), np.uint8)

        if key == ord('q'):
            break


def add_marker_event(event, x, y, _flags, _params):
    if event == cv2.EVENT_LBUTTONDOWN:

        markers = _params[0]
        marker_index = _params[1]
        segmentation = _params[2]

        marker = Marker(int(chr(marker_index)), x, y)
        markers.append(marker)
        cv2.circle(segmentation, marker.pos, 7, (marker.id, marker.id, marker.id), thickness=-1)


if __name__ == '__main__':
    main()
