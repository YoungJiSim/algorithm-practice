"""
Problem Description

You are playing a number card game where the goal is to pick a card with the highest possible number. 
However, you must follow the rules of the game, which are as follows:
    1. The cards are arranged in an N x M grid, where N is the number of rows and M is the number of columns.
    2. First, you must choose a row from the grid.
    3. Then, from the selected row, you must pick the card with the smallest number.
    4. Your goal is to maximize the number on the card you pick, by choosing the row wisely.

In other words, for each row, the card you will end up picking is the minimum number in that row. 
You need to pick the row whose minimum number is as large as possible.

Input
1. The first line contains two integers N and M, separated by a space, 
representing the number of rows and columns, respectively.
    N (1 ≤ N ≤ 100): the number of rows
    M (1 ≤ M ≤ 100): the number of columns

2. Each of the next N lines contains M integers, representing the numbers on the cards in that row.
Each number is a natural number between 1 and 10,000 inclusive.

Output
Print a single integer: the number on the card chosen according to the game rules.
"""
from timer import timer


@timer
def number_card_game_using_max(card_grid: list) -> int:
    result = 0
    for row in card_grid:
        min_value = min(row)
        result = max(result, min_value)

    return result


@timer
def number_card_game_using_if_statement(card_grid: list) -> int:
    result = 0
    for row in card_grid:
        if result < min(row):
            result = min(row)

    return result

def main():
    """
    Drive the program.
    """
    n, m = map(int, input("Enter the numbers of the rows and columns, separated by a space, respectively.\n").split())
    card_grid = []
    for _ in range(n):
        rows = list(map(int, input("Enter the m-number of integer numbers separated by spaces.\n").split()))
        card_grid.append(rows)

    print(number_card_game_using_if_statement(card_grid))
    print(number_card_game_using_max(card_grid))


if __name__ == "__main__":
    main()