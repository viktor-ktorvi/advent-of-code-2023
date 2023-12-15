import sys


def main():
    with open(sys.argv[1], "r") as file:
        file_text = file.read()

    lines = file_text.split("\n")
    powers = []
    for line in lines:
        _, handfuls = line.split(":")

        minimum_numbers_per_color = {color: number for color, number in zip(["red", "green", "blue"], [0, 0, 0])}

        for handful in handfuls.split(";"):
            number_color_pairs = handful.split(",")

            for number_color_pair in number_color_pairs:
                number, color = number_color_pair.strip().split()

                minimum_numbers_per_color[color] = max(int(number), minimum_numbers_per_color[color])
        power = 1
        for value in minimum_numbers_per_color.values():
            power *= value

        powers.append(power)

    print(f"The sum of powers in these sets is {sum(powers)}")


if __name__ == "__main__":
    main()
