class Config:
    # length of the test
    frames = 600

    starting_sleep = 4

    region_coord = [0, 0, 1400, 600]

    # checkpoint before every shot
    starting_coords = [360, 640]

    # filters to detect blue
    lower_blue = [75, 30, 0]
    upper_blue = [200, 200, 255]

    # target locations from checkpoint
    target1 = [330, 360, 585, 615]
    target2 = [330, 360, 470, 500]
    target3 = [340, 380, 505, 545]
    target4 = [340, 380, 620, 660]
    target5 = [330, 355, 715, 745]
    target6 = [300, 315, 615, 635]
    target7 = [305, 324, 542, 562]
    target8 = [308, 325, 685, 705]
    target9 = [293, 303, 595, 605]

    target10 = [293, 302, 641, 650]
    target11 = [295, 305, 550, 560]

    # detection parameters
    confidence = 0.3
    size = 10

    # aim and shoot parameters
    sleep_time = 0.2
    mouse_actions = ['mouse_rb_press', 'mouse_lb_press', 'mouse_lb_release', 'mouse_rb_release']
    mouse_scale = 2.25

    # weapon
    ammo = 20
