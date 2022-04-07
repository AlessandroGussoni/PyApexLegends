import time


def shoot(keyboard,
          config):
    for action in config.mouse_actions:
        getattr(keyboard, 'directMouse')(buttons=getattr(keyboard, action))
        time.sleep(config.sleep_time)


def flick_to_target(keyboard,
                    starting_pos,
                    target,
                    config,
                    sleep_time=None):
    y = starting_pos[0] - target[0]
    x = starting_pos[1] - target[1]
    keyboard.directMouse(-int(x * config.mouse_scale), -int(y * (config.mouse_scale + 0.01)))
    if not isinstance(sleep_time, type(None)):
        time.sleep(config.sleep_time + 0.05)


def reload(keyboard,
           sleep_time=None):
    keyboard.directKey('r')
    keyboard.directKey('r', keyboard.key_release)
    if not isinstance(sleep_time, type(None)):
        time.sleep(sleep_time + 0.5)
