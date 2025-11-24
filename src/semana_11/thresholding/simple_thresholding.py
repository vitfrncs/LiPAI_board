# pylint: disable=no-member

import cv2
import numpy as np

def simple_thresholding(image_path, T=105):
    image = cv2.imread(image_path, 0)
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    _, thresh = cv2.threshold(blurred, T, 255, cv2.THRESH_BINARY)
    _, threshInv = cv2.threshold(blurred, T, 255, cv2.THRESH_BINARY_INV)
    masked = cv2.bitwise_and(image, image, mask=threshInv)

    return thresh, threshInv, masked
