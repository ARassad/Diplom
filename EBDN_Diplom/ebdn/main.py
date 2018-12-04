import os
import sys
import argparse
import cv2
import math
import time
import numpy as np
import util
from config_reader import config_reader
from scipy.ndimage.filters import gaussian_filter

from model.cmu_model import get_testing_model


if __name__ == '__main__':

    model = get_testing_model()

    oriImg = cv2.imread("4102265--28-0-1506516347-1506516351-650-861d65949c-1506927771.jpg")

    heatmap_avg = np.zeros((oriImg.shape[0], oriImg.shape[1], 19))
    paf_avg = np.zeros((oriImg.shape[0], oriImg.shape[1], 38))


