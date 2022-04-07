import cv2
import numpy as np

from frame_processing.grabscreen import grab_screen


def process_frame(config):
    screen = grab_screen(region=config.region_coord)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(screen, cv2.COLOR_RGB2HSV)
    lower_blue = np.array(config.lower_blue)
    upper_blue = np.array(config.upper_blue)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # res = cv2.bitwise_and(screen, screen, mask=mask)
    return mask, screen
