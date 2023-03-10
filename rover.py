# Define the initial position and direction of the rover
try:
    x, y, direction = input(
        "Enter initial position (x, y) and direction (N/S/E/W): ").split()
except ValueError:
    raise ValueError('Input should be in this format 3 3 E')

x = int(x)
y = int(y)

# Define the plateau size
try:
    max_x, max_y = input(
        "Enter the plateau size (x, y) optional default size 50 50: "
    ) or '50 50'.split()
except ValueError:
    raise ValueError('Plateau size should be in this format 50 50')

max_x = int(max_x or 50)
max_y = int(max_y or 50)

# Define the rover's movements
movements = input("Enter rover movements: ")
acceptable_movements = set('LRM')  # Validate movements
if not set(movements).issubset(acceptable_movements):
    raise ValueError('Enter valid rover movements(L R M)')


# Define function for turning the rover
def turn(direction, side):
    if direction == 'N':
        return 'W' if side == 'L' else 'E'
    elif direction == 'S':
        return 'E' if side == 'L' else 'W'
    elif direction == 'E':
        return 'N' if side == 'L' else 'S'
    elif direction == 'W':
        return 'S' if side == 'L' else 'N'


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
