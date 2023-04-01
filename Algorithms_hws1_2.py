# Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_numbers (n: int):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x

    return final_sum

test_n = 5
result = sum_numbers(test_n)
print(result)


#Find the max number from 3 values.
#Example: 124, 21, 32. Result = 124.

def max_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3

#result = max_number(10, 20, 40)
#print(result)

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10

    print(f"Odd digits: {odds}")
    print(f"Even digits: {evens}")

test_n = 35680 # odds: 2, evens:3
count_odd_even(test_n)





