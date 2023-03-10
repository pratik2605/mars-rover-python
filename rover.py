# Define the initial position and direction of the rover
x, y, direction = input("Enter initial position (x, y) and direction (N/S/E/W): ").split()
x = int(x)
y = int(y)

# Define the plateau size
max_x, max_y = input("Enter the plateau size (x, y): ").split()
max_x = int(max_x)
max_y = int(max_y)

# Define the rover's movements
movements = input("Enter rover movements: ")

# Define function for turning the rover
def turn(direction, side):
    if direction == 'N':
        if side == 'L':
            return 'W'
        elif side == 'R':
            return 'E'
    elif direction == 'S':
        if side == 'L':
            return 'E'
        elif side == 'R':
            return 'W'
    elif direction == 'E':
        if side == 'L':
            return 'N'
        elif side == 'R':
            return 'S'
    elif direction == 'W':
        if side == 'L':
            return 'S'
        elif side == 'R':
            return 'N'

# Define function for moving the rover forward
def move_forward(x, y, direction):
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    return x, y

# Loop through the movements and update the rover's position and direction
for movement in movements:
    if movement == 'L':
        direction = turn(direction, 'L')
    elif movement == 'R':
        direction = turn(direction, 'R')
    elif movement == 'M':
        x_new, y_new = move_forward(x, y, direction)
        # Check if the new position is within the plateau boundaries
        if 0 <= x_new <= max_x and 0 <= y_new <= max_y:
            x, y = x_new, y_new

# Print the final position of the rover
print(f"Final position: ({x}, {y}, {direction})")
