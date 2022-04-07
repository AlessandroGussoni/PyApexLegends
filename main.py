import time

import cv2
import numpy as np

import gun_control.keys as k
from frame_processing import process_frame
from frame_processing.functions import slice_array, region_confidence, scale_confidence
from logging import log_data
from gun_control import flick_to_target, shoot, reload
from config import Config

keys = k.Keys()
config = Config()
no_shoot = 0
time.sleep(config.starting_sleep)
ammo = config.ammo
start_time = time.time()
for k in range(config.frames):
    mask, screen = process_frame(config)
    targets = ['target' + str(i) for i in range(1, 12)]
    all_pos_confidence = [region_confidence(slice_array(mask, getattr(config, target))) for target in targets]
    all_pos_confidence = scale_confidence(all_pos_confidence)
    target_to_shoot = all_pos_confidence.index(max(all_pos_confidence)) + 1
    target_coords = getattr(config, 'target' + str(target_to_shoot))
    coords = [int(np.round(target_coords[0] + (target_coords[1] - target_coords[0]) / 2)),
              int(np.round(target_coords[2] + (target_coords[3] - target_coords[2]) / 2))]
    if max(all_pos_confidence) > config.confidence:
        no_shoot = 0
        flick_to_target(keys, starting_pos=config.starting_coords, target=coords, config=config, sleep_time=True)
        shoot(keys, config)
        ammo -= 1
        flick_to_target(keys, starting_pos=coords, target=config.starting_coords, config=config, sleep_time=True)
        if ammo == 1:
            reload(keys, sleep_time=config.sleep_time)
            ammo = config.ammo
            print('G7 Reloaded!')
        log_data(all_pos_confidence, config, ammo)
    else:
        print('0 target detected')
        no_shoot += 1
        print(no_shoot)

    if no_shoot > 5:
        flick_to_target(keys, starting_pos=[0, 0], target=[0.5, 0], config=config)
        print('Redirecting...')
    current_time = time.time()
    if current_time - start_time > 61:
        break
    print()

cv2.destroyAllWindows()
