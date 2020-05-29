from pymouse import PyMouse

m = PyMouse()

# move the mouse to int x and int y (these are absolute positions)
m.move(200, 200)

# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
m.click(500, 300, 1)

# get the screen size
m.screen_size()

# get the mouse position
m.position()