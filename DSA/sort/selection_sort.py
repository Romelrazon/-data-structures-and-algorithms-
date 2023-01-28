def selection_sort(number):
    length = len(number)
    for i in range(length):
        smallest = i
        for j in range(i, length - 1):
            if number[smallest] > number[j + 1]:
                smallest = j + 1
        if smallest != i:
            number[smallest], number[i] = number[i], number[smallest]
    return number
number = [5, 4, 3, 2, 1]
print(selection_sort(number))
