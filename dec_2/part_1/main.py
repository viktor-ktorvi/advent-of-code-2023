import sys


def main():
    with open(sys.argv[1], "r") as file:
        file_text = file.read()

    bag_contents = {"red": 12, "green": 13, "blue": 14}

    lines = file_text.split("\n")
    game_ids = []
    for line in lines:
        game, handfuls = line.split(":")

        game_id = int(game.split()[-1])

        possible = True
        for handful in handfuls.split(";"):
            number_color_pairs = handful.split(",")

            for number_color_pair in number_color_pairs:
                number, color = number_color_pair.strip().split()

                if int(number) > bag_contents[color]:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            game_ids.append(game_id)

    print(f"The sum of the IDs of possible games is {sum(game_ids)}")


if __name__ == "__main__":
    main()
