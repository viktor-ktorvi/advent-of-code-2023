import sys
from typing import List, Tuple


def main():
    with open(sys.argv[1], "r") as file:
        file_text = file.read()

    lines = file_text.split("\n")
    table = []
    for line in lines:
        table.append(list(line))

    for row in table:
        assert len(row) == len(table[0])

    part_numbers = []

    table_height = len(table)
    for row_ptr in range(table_height):
        row_width = len(table[row_ptr])

        # parse row
        col_ptr = 0
        while col_ptr < row_width:
            if not table[row_ptr][col_ptr].isdigit():
                col_ptr += 1
                continue

            # localize number
            number_start = col_ptr
            number_end = number_start
            while number_end < row_width and table[row_ptr][number_end].isdigit():
                number_end += 1

            # check all neighbours
            neighbouring_row_ptrs = [row_ptr + offset for offset in range(-1, 2)]
            neighbouring_col_ptrs = [col_ptr + offset for offset in range(-1, number_end - number_start + 1)]

            valid_part_number_flag = False
            for neighbouring_row_ptr in neighbouring_row_ptrs:
                for neighbouring_col_ptr in neighbouring_col_ptrs:

                    # if out of bounds
                    if not 0 <= neighbouring_row_ptr < row_width:
                        continue

                    if not 0 <= neighbouring_col_ptr < table_height:
                        continue

                    char = table[neighbouring_row_ptr][neighbouring_col_ptr]

                    # if not a symbol
                    if char.isdigit() or char == ".":
                        continue

                    valid_part_number_flag = True
                    break

                if valid_part_number_flag:
                    break

            # save part number
            if valid_part_number_flag:
                part_number = ""
                for idx in range(number_start, number_end):
                    part_number += table[row_ptr][idx]

                part_numbers.append(int(part_number))

            col_ptr = number_end + 1

    print(part_numbers)
    print(f"The sum of part numbers is {sum(part_numbers)}")


if __name__ == "__main__":
    main()
