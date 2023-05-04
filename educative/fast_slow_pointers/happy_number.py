def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum


def is_happy_number(n):
    slow = n
    fast = sum_of_squared_digits(n)

    while fast != 1 and fast != slow:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))

    return fast == 1




if __name__ == "__main__":
    print(is_happy_number(23))

