import numpy
import csv
from tp2 import constants
from utils.contours import *
from utils.files import *

show_contours = False


def main():
    with open(r'' + constants.DESCRIPTORS_FILE_NAME, 'w') as file_to_write:
        writer = csv.writer(file_to_write)

        for file in load_files():
            frame = cv2.imread(file.path)

            gray_frame = apply_color_convertion(frame, cv2.COLOR_RGB2GRAY)
            threshold_frame = apply_threshold(gray_frame, None)
            noise_frame = apply_noise(threshold_frame, None)

            contour = get_contours(noise_frame, None)[0]

            hu_moments = get_hu_moments(contour)
            hu_moments = hu_moments.flatten()

            writer.writerow(numpy.insert(hu_moments, 0, file.label_id))

            if show_contours:
                draw_contours(frame, contour, colors.BLUE, 3)
                cv2.imshow('TP2.descriptors', frame)

            if cv2.waitKey() & 0xFF:
                continue


def get_label(label_id):
    with open(r'' + constants.LABELS_FILE_NAME, 'r') as file_to_read:
        reader = csv.reader(file_to_read, delimiter=',')
        for line in reader:
            if int(line[0]) == label_id:
                return line[1]


def load_files():
    files = []
    for data in get_files('./images/*.png'):
        data_array = data.split('/')
        data_array_name = data_array[len(data_array) - 1].split('.')
        files.append(File(id=data_array_name[0], label_id=data_array_name[1], path=data))

    return files


if __name__ == '__main__':
    main()
