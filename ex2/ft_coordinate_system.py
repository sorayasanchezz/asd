import math


def calculate_distance(point1: tuple[float, float, float],
                       point2: tuple[float, float, float]) -> float:
    """Calculate the 3D Euclidean distance between two points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple[float, float, float]:
    parsed_coord = coord_str.split(",")

    if len(parsed_coord) != 3:
        raise ValueError("Invalid syntax")

    coords = []
    for p in parsed_coord:
        p = p.strip()
        try:
            coords.append(float(p))
        except ValueError as e:
            raise ValueError(f"Error on parameter '{p}': {e}")

    return (coords[0], coords[1], coords[2])


def calculate_center(input_coord: str) -> tuple[float, float, float]:
    """
    Parse a coordinate string (e.g., '3,4,0') into a tuple of integers.
    Raise an error if the input does not contain exactly three numeric values.
    """
    origin = (0, 0, 0)

    try:
        parsed_coord = parse_coordinates(input_coord)
        print(
            f'Got a first tuple: {parsed_coord}\n'
            f"It includes: X={parsed_coord[0]}, Y={parsed_coord[1]}, "
            f"Z={parsed_coord[2]}")

        print(f'Distance to center: '
              f'{calculate_distance(origin, parsed_coord):.4f}')

    except (ValueError, IndexError):
        raise ValueError("Invalid syntax")

    return parsed_coord


def two_coords(input_coord: str,
               origin: tuple[float, float, float]) -> tuple[float, float, float]:

    try:
        parsed_coord = parse_coordinates(input_coord)
        print(f'Distance between the 2 sets of coordinates: '
              f'{calculate_distance(origin, parsed_coord):.4f}')

    except (ValueError, IndexError) as e:
        raise ValueError(f"{e}")

    return parsed_coord


def get_player_pos():
    print(
        "=== Game Coordinate System ===\n\n"
        "Get a first set of coordinates")

    arg = tuple()

    while len(arg) < 1:
        try:
            arg = calculate_center(
                input("Enter new coordinates as floats in format 'x,y,z': "))
        except ValueError as e:
            print(e)

    print("\nGet a second set of coordinates")
    arg2 = tuple()

    while len(arg2) < 1:
        try:
            arg2 = two_coords(
                input("Enter new coordinates as floats in format 'x,y,z': "),
                arg)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    get_player_pos()
