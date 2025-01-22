import enum


class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def describe(self):
        descriptions = {
            Color.RED: "The color of passion and energy.",
            Color.GREEN: "The color of nature and tranquility.",
            Color.BLUE: "The color of calm and stability.",
        }
        return descriptions.get(self, "No description available.")


def color_to_hex(color):
    try:
        hex_values = {
            Color.RED: "#FF0000",
            Color.GREEN: "#00FF00",
            Color.BLUE: "#0000FF",
        }
        return hex_values[color]
    except KeyError:
        return "Unknown color"


def print_all_colors():
    for color in Color:
        print(f"{color.name} = {color.value}")


def main():
    print(Color.RED)  # Color.RED
    print(Color.GREEN.name)  # 'GREEN'
    print(Color.BLUE.value)  # 3
    print()

    if Color.RED == Color(1):
        print("Colors match!")  # Will print this because 1 corresponds to Color.RED

    print("\nColor to Hex Mapping:")
    for color in Color:
        print(f"{color.name}: {color_to_hex(color)}")

    print("\nDescriptions:")
    for color in Color:
        print(f"{color.name}: {color.describe()}")

    print(Color.RED == Color.GREEN)  # False, because RED != GREEN
    print(Color.RED == Color.RED)  # True, because RED == RED

    print("\nIterating over all colors:")
    print_all_colors()


if __name__ == "__main__":
    main()
