"""
Given an integer N representing the amount of change (in cents), 
return the minimum number of bills and coins needed to make up that amount.
You may use denominations of {5, 2, 1, 0.25, 0.10, 0.05} dollars, and each denomination is available infinitely.
"""


def min_coins(change: int) -> dict:
    denomination_type = (5, 2, 1, 0.25, 0.10, 0.05)
    denominations = {}
    for denomination in denomination_type:
        calculable_denomination = int(denomination * 100)
        number_of_currency_units = change // calculable_denomination
        change %= calculable_denomination
        denominations[denomination] = number_of_currency_units
    return denominations


def change_printer(change: dict):
    print()
    print(f"{"Denominations":>13} | ", end="")
    for key in change.keys():
        print(f"{float(key):.2f}", end=" | ")
    print(f"\n{"Numbers":>13} | ", end="")
    for value in change.values():
        print(f"{value:>4}", end=" | ")
    print()


def main():
    """
    Drive the program.
    """
    change = int(12.55 * 100)
    change_printer(min_coins(change))


if __name__ == "__main__":
    main()