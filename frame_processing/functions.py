import numpy as np


def count_black(array, i, j, size):
    count = 0
    for k in range(size):
        for t in range(size):
            if np.array_equal(array[k + i, t + j, :], np.array([0, 0, 0])):
                count += 1
    return count


def check_square(region, size, confidence):
    pos = {}

    for i in range(region.shape[0] - size):
        for j in range(region.shape[1] - size):
            count = count_black(region, i, j, size)
            if (count / size ** 2) > confidence:
                pos[(count / size ** 2)] = [i, j]
                break
        else:
            continue
        break
    return pos


def region_confidence(array):
    flat = np.where(array == 0, True, False)
    return flat.sum() / (flat.shape[0] * flat.shape[1])


def draw_rect(array,
              coords,
              config,
              color):
    for i in range(int(coords[0] - config.size / 2), int(coords[0] + config.size / 2)):
        for j in range(int(coords[1] - config.size / 2), int(coords[1] + config.size / 2)):
            array[i, j, :] = color

    return array


def slice_array(array, coords):
    return array[coords[0]: coords[1], coords[2]:coords[3]]


def extract_target_from_pos(pos,
                            targets,
                            config):
    i, j = pos[max(pos.keys())]
    target_name = targets[max(pos.keys())]
    i += getattr(config, target_name)[0]
    j += getattr(config, target_name)[2]
    target = [int(i + config.size / 2), int(j + config.size / 2)]
    coords = [i, i + config.size, j, j + config.size]
    return target, coords


def scale_confidence(confidence):
    confidence[5] -= 0.1
    confidence[6] -= 0.05
    confidence[7] -= 0.3
    confidence[8] += 0.2
    confidence[9] -= 0.05
    return confidence
