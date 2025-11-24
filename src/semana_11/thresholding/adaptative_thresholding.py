# pylint: disable=no-member

import numpy as np
import cv2


def adaptative_thresholding(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    threst_mean = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 4)
    threst_gaussian = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 15, 3)
    return threst_mean, threst_gaussian