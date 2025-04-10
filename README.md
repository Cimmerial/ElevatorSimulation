# Elevator Simulation

A Python module that simulates a single elevator system, calculating the total travel time and recording the order of floors visited.

## Features

- Simulates a single elevator moving through a sequence of floors
- Calculates total travel time based on floor-to-floor movement
- Handles both regular and basement (negative) floors
- Includes unit tests to verify functionality
- Simple command-line interface

## Assumptions

- The elevator uses a **single call button system** (not up/down directional buttons)
- Floors are visited in the exact order specified in the input
- The first floor in the input list is the starting position
- Any negative floor is considered a basement level
- No acceleration/deceleration effects - constant speed between floors
- No door opening/closing time is factored into the calculations
- No time delay for passengers entering or exiting
- The elevator moves directly from one floor to the next without intermediate stops

## Usage

'''
python3 elevator_simulation.py FLOOR_1 FLOOR_2 ... FLOOR_N
'''

Example:

'''
python3 elevator_simulation.py 12 2 9 1 32
'''

## Functions

- `start_elevator(floors_to_visit)`: Simulates the elevator visiting floors and returns travel time and floors visited
- `main()`: Processes command line arguments and runs the simulation
- `run_tests()`: Executes unit tests to verify simulation correctness

## Testing

To run test cases:

```
python3 elevator_simulation.py --test
```

The tests verify:
1. Handling of empty floor lists
2. Single floor operation
3. Multiple floor operations
4. Support for negative floors (basement levels)
