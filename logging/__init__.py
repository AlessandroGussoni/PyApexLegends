def log_data(pc,
             config,
             r):
    print('Target_shooted: ', pc.index(max(pc)) + 1)
    print('Confidence value: {}. Threshold is {}'.format(max(pc), config.confidence))
    print('Ammo: ', r)
