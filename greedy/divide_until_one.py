"""
Problem Description

You are given a number N and a divisor K.
Your goal is to reduce N to 1 by repeatedly performing one of the following two operations:
    1. Subtract 1 from N.
    2. Divide N by K, but only if N is divisible by K.

Given N and K, determine the minimum number of operations required to reduce N to 1.

Input
A single line containing two integers N and K, separated by a space. It is guaranteed that N ≥ K.
    N (2 ≤ N ≤ 100,000)
    K (2 ≤ K ≤ 100,000)
    
Output
Print a single integer: the minimum number of operations required to reduce N to 1.
"""
from timer import timer


@timer
def operations_using_single_iteration(n: int, k: int) -> int:
    counter = 0
    while True:
        target = (n // k) * k
        counter += (n - target)
        n = target

        if n < k:
            break
        n //= k
        counter += 1

    counter -= 1
    return counter


@timer
def operations_using_nested_loop(n: int, k: int) -> int:
    counter = 0
    while n >= k:
        while n % k != 0:
            n -= 1
            counter += 1
        n //= k
        counter += 1

    while n > 1:
        n -= 1
        counter += 1

    return counter


@timer
def operations_copying_recursive_with_iteration(n: int, k: int) -> int:
    counter = 0
    while n > 1:
        if n % k == 0:
            n //= k
            counter += 1
        else:
            n -= 1
            counter += 1
    return counter


@timer
def operations_using_recursive(n: int, k: int, counter: int = 0) -> int:
    if n == 1:
        return counter

    if n % k == 0:
        counter += 1
        return operations_using_recursive((n // k), k, counter)
    else:
        counter += 1
        return operations_using_recursive(n - 1, k, counter)


def main():
    """
    Drive the program.
    """
    n, k = map(int, input("Enter two integers separated by a space.\n").split())
    # print(operations_using_recursive(n, k))
    print(operations_copying_recursive_with_iteration(n, k))
    print(operations_using_nested_loop(n, k))
    print(operations_using_single_iteration(n, k))


if __name__ == "__main__":
    main()