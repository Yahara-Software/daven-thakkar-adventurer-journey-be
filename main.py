import math

'''
Thoughts:
    - Need to compute straight line distance.
    - If we think about this in a coordinate system then we can use pythagorean theorem (a^2 + b^2 = c^2).
    - For the theorem we just need the start and end coordinates.
'''

def get_end_coordinate(start_coordinates: list, directions: str) -> list:
    '''
    This function just computes the final end coordinates.
    Movement logic:
        F = add to y
        B = minus to y
        R = add to x
        L = minus to x

    start_coordinates: a list of start postion [x,y]
    directions: a string of the directions to travel

    returns: a list of the end postion [x,y]
    '''

    curr_position = list(start_coordinates)    # This keeps track of our postion as we move around
    curr_movement = 0    # This holds our current number of steps for each iteration
    for i in range(len(directions)):
        # Get the number(s)
        if directions[i].isdigit():
            curr_movement += int(directions[i])
        else:
            direction = directions[i]    # Check which direction we need to move
            # Since we are in coordinate system we just need to move x and y accordingly
            if direction == "F":
                # Move y up
                curr_position[1] += curr_movement
            elif direction == "B":
                # Move y down
                curr_position[1] -= curr_movement
            elif direction == "L":
                # Move x to the left
                curr_position[0] -= curr_movement
            else:
                # Move x to the right
                curr_position[0] += curr_movement
            # Reset curr_movement for next iteration
            curr_movement = 0
    return curr_position

def compute_distance(start_coordinates: list, end_coordinates: list) -> float:
    '''
    This function computes the straight line distance given starting and ending coordinates.

    start_coordinates: a list of start postion [x,y]
    end_coordinates: a list of end postion [x,y]

    returns: the computed distance (not rounded)
    '''

    # Formula: distance = square_root( (x_end - x_start)^2 + (y_end - y_start)^2 )
    a = end_coordinates[0] - start_coordinates[0]
    b = end_coordinates[1] - start_coordinates[1]
    distance = math.sqrt((a*a + b*b))
    return distance

def main():
    # The directions given to us
    directions = "15F6B6B5L16R8B16F20L6F13F11R"
    start_position = [0,0]    # using list since tuples are immutable
    end_position = get_end_coordinate(start_position, directions)
    distance_traveled = compute_distance(start_position, end_position)
    print(distance_traveled)

'''
I forgot the formal name of the if statement below but it essentially allows user to
run the file like "python main.py" and the user can import this files functions and run them
without executing any other print or testing stuff (if we had any) in this file.

NOTE Instructions to run program: in the same directory as the main.py, run the command "python main.py"
'''
if __name__ == "__main__":
    main()