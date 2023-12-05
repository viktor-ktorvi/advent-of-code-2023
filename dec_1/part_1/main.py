import sys

from typing import Union


def find_first_digit(s: str) -> Union[str, None]:
    for char in s:
        if char.isdigit():
            return char

    return None


def main():
    with open(sys.argv[1], "r") as file:
        file_text = file.read()

    lines = file_text.split()

    calibration_values = []
    for line in lines:
        calibration_values.append(int(find_first_digit(line) + find_first_digit(line[::-1])))

    print(f"The sum of the calibration values is {sum(calibration_values)}")


if __name__ == "__main__":
    main()
