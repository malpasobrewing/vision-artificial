from utils.shape import *

main_window = 'Main Window'
roi_window = 'ROI Window'


def main():
    cv2.namedWindow(main_window)
    cv2.namedWindow(roi_window)

    # 640px x 597px
    shape = create_shape_from_image('Buttons', './images/buttons.png')

    roi = cv2.selectROI(roi_window, shape.frame, fromCenter=False, showCrosshair=False)

    cv2.imshow(main_window, apply_grabcut(shape.frame, roi))

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
