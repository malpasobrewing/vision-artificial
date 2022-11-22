import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

    image = cv2.imread("./images/hand-right.jpg")
    height, width, _ = image.shape

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks is not None:
        # Accediendo al valor de los puntos por su índice
        index = [4, 8, 12, 16, 20]
        for hand_landmarks in results.multi_hand_landmarks:
            for (i, points) in enumerate(hand_landmarks.landmark):
                if i in index:
                    x = int(points.x * width)
                    y = int(points.y * height)
                    cv2.circle(image, (x, y), 3, (255, 0, 255), 3)

    image = cv2.flip(image, 1)
    cv2.imshow('Output', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
