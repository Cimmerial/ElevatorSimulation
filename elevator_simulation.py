"""
Elevator Simulation
This module simulates an elevator system, calculating the total travel time
and recording the order of floors visited.
"""

import sys # for cmd line arg handling

# Constants
SINGLE_FLOOR_TRAVEL_TIME = 10 

def start_elevator(floors_to_visit):
    """
    Simulates an elevator visiting a list of floors.

    Args:
        floors_to_visit: A list of integers representing the floors to visit.
                         The first element is the starting floor.

    Returns: Tuple of (travel_time, floors_visited)
    """
    # initialize vars
    travelTimeRet = 0

    # sum difference between each floor
    for i in range(len(floors_to_visit) - 1):
        travelTimeRet += abs(floors_to_visit[i] - floors_to_visit[i + 1])

    # return tuple of calculated travel time and floors visited
    return [travelTimeRet * SINGLE_FLOOR_TRAVEL_TIME, floors_to_visit]

def main():
    """Process command line arguments and run the simulation."""

    # Check for command line arguments
    if "--test" in sys.argv:
        run_tests()
        return 
    
    # Set default floors to visit (first is start)
    floors_to_visit = [3, 0, 5, 2, 9]  

    # Run the simulation
    try:
        travel_time, floors_visited = start_elevator(floors_to_visit)

        # Format and print the output
        floors_visited_str = ",".join(str(floor) for floor in floors_visited)
        print(f"Travel Time: {travel_time} \nFloors Visited in Order: {floors_visited_str}")
    except Exception as e:
        print(f"Error: {e}")

def run_tests():
    """Run unit test cases for the elevator simulation."""
    # Test 1: Empty floor list
    floors = []
    time, visited = start_elevator(floors)
    assert time == 0, f"Expected 0, got {time}"
    assert visited == [], f"Expected [], got {visited}"
    print("Test 1 passed: Empty floor list")

    # Test 2: Single floor (start and end at the same)
    floors = [10]
    time, visited = start_elevator(floors)
    assert time == 0, f"Expected 0, got {time}"
    assert visited == [10], f"Expected [10], got {visited}"
    print("Test 2 passed: Single floor")

    # Test 3: Multiple floors
    floors = [12, 2, 9, 1, 32]
    time, visited = start_elevator(floors)
    expected_time = (abs(12 - 2) + abs(2 - 9) + abs(9 - 1) + abs(1 - 32)) * SINGLE_FLOOR_TRAVEL_TIME
    expected_visited = [12, 2, 9, 1, 32]
    assert time == expected_time, f"Expected {expected_time}, got {time}"
    assert visited == expected_visited, f"Expected {expected_visited}, got {visited}"
    print("Test 3 passed: Multiple floors")
    
    # Test 4: Negative floors (basement levels)
    floors = [-12, 2, 9, -1, 32]
    time, visited = start_elevator(floors)
    expected_time = (abs(-12 - 2) + abs(2 - 9) + abs(9 - (-1)) + abs((-1) - 32)) * SINGLE_FLOOR_TRAVEL_TIME
    expected_visited = [-12, 2, 9, -1, 32]
    assert time == expected_time, f"Expected {expected_time}, got {time}"
    assert visited == expected_visited, f"Expected {expected_visited}, got {visited}"
    print("Test 4 passed: Negative floors (basement levels)")

    print("All tests passed!")

# process
if __name__ == "__main__":
    main()
    # run_tests()
