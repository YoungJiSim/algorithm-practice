"""
Problem Description

You are given an array of natural numbers. You want to calculate the maximum possible sum 
by adding numbers from the array exactly M times according to the "Law of the Largest Number."

Law of the Largest Number:
At each step, you can choose any number from the array to add to the sum.
You can choose the same number consecutively at most K times.
Given the array and the values of M and K, calculate the largest possible sum.

Input
1. The first line contains three integers:
    N (2 ≤ N ≤ 1,000): the number of elements in the array
    M (1 ≤ M ≤ 10,000): the total number of additions
    K (1 ≤ K ≤ 10,000): the maximum number of times the same index can be added consecutively

2. The second line contains N integers separated by spaces: the elements of the array. 
Each number is between 1 and 10,000, inclusive.

3. It is guaranteed that K ≤ M.

Output
Return a single integer: the maximum sum that can be obtained by following the Law of the Largest Number.
"""


def law_of_the_largest_number() -> int:
    n, m, k = map(int, input("Enter three integers separated by spaces.\n").split())
    array_data = list(map(int, input("Enter n-number of integers separated by spaces.\n").split()))
    sorted_array = sorted(array_data, reverse=True)

    repeat = m // (k + 1)
    additional = m % (k + 1)

    result = repeat * (k * (sorted_array[0]) + sorted_array[1]) + additional * sorted_array[0]

    return result


def law_of_the_largest_number_using_iteration() -> int:
    n, m, k = map(int, input("Enter three integers separated by spaces.\n").split())
    array_data = list(map(int, input("Enter n-number of integers separated by spaces.\n").split()))
    sorted_array = sorted(array_data, reverse=True)

    result = 0

    while m > 0:
        index = 0
        for _ in range(k):
            result += sorted_array[index]
            m -= 1
            if m <= 0:
                break

        index += 1
        result += sorted_array[index]
        m -= 1

    return result


def main():
    print(law_of_the_largest_number())


if __name__ == "__main__":
    main()