# pylint: disable=no-member

import cv2
import mahotas
import numpy as np

def otsu_thresholding(image_path):

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    T_otsu = mahotas.thresholding.otsu(blurred)

    thresh_otsu = gray.copy()
    thresh_otsu[thresh_otsu > T_otsu] = 255
    thresh_otsu[thresh_otsu < 255] = 0
    thresh_otsu = cv2.bitwise_not(thresh_otsu)

    T_rc = mahotas.thresholding.rc(blurred)

    thresh_rc = gray.copy()
    thresh_rc[thresh_rc > T_rc] = 255
    thresh_rc[thresh_rc < 255] = 0
    thresh_rc = cv2.bitwise_not(thresh_rc)

    return thresh_otsu, thresh_rc
