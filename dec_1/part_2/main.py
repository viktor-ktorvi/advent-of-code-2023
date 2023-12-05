import sys
from typing import Union, Dict


def find_first_digit(s: str, digit_strings: Dict) -> Union[str, None]:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]

        for digit_string in digit_strings.keys():
            if s[i: i + len(digit_string)] == digit_string:
                return digit_strings[digit_string]

    return None


def main():
    with open(sys.argv[1], "r") as file:
        file_text = file.read()

    lines = file_text.split()

    digit_strings = {"zero": "0",
                     "one": "1",
                     "two": "2",
                     "three": "3",
                     "four": "4",
                     "five": "5",
                     "six": "6",
                     "seven": "7",
                     "eight": "8",
                     "nine": "9"}

    inverse_digit_strings = {}
    for digit_string in digit_strings:
        inverse_digit_strings[digit_string[::-1]] = digit_strings[digit_string]

    calibration_values = []
    for line in lines:
        calibration_values.append(int(find_first_digit(line, digit_strings) + find_first_digit(line[::-1], inverse_digit_strings)))

    print(f"The sum of the calibration values is {sum(calibration_values)}")


if __name__ == "__main__":
    main()
