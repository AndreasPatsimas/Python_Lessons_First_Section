def highest_even(numbers = [0, 1]):

    even_numbers = []

    for number in list(numbers):
        if number % 2 == 0:
            even_numbers.append(number)

    if len(even_numbers) < 1:
        even_numbers = [0]

    return max(even_numbers)

highest_even = highest_even([1, 4, 12, 15, 16, 7, 6, 11, 20, 21, 19, 23, 20])

print(highest_even)