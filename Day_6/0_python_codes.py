# First challenge
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Second challenge

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_ahead():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
for i in range(6):
    move_ahead()

