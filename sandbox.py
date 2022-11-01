#################
# SANDBOX       #
# Daniel Grosso #
#################
import cv2 as cv


def read_image(path):
    return cv.imread(path)


def show_source(title, source):
    # image = cv.imread(image)
    # gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # ret1, thresh1 = cv.threshold(gray, val, 255, cv.THRESH_BINARY)
    cv.imshow(title, source)


def apply_binary(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret1, thresh1 = cv.threshold(gray, 5, 255, cv.THRESH_BINARY)
    return thresh1


def find_contours(source):
    contours, hierarchy = cv.findContours(source, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    return contours


def draw_contours(resource, contours):
    cv.drawContours(resource, contours, -1, (0, 0, 255), 2)
    return resource


image = read_image('static/shapes.png')
binary = apply_binary(image)

contours = find_contours(binary)
image_with_contours = draw_contours(read_image('static/shapes.png'), contours)

show_source('Sandbox', image_with_contours)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break

