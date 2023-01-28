def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = [5, 4, 3, 2, 1]
print(bubble_sort(numbers))
