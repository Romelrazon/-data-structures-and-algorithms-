attempts = 1
position = -1


values = input("Enter any numbers that are comma-separated (no spaces):\n")
n = int(input("Please enter the number you want to search for: \n"))
list = values.split(",")

for i in range(0, len(list)):
    list[i] = int(list[i])


def is_sorted():
    flag = 0

    test_list = list[:]
    test_list.sort()

    if test_list == list:
        flag = 1
        return True
    else:
        return False


def binary_search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()["position"] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
                globals()["attempts"] += 1
            else:
                u = mid - 1
                globals()["attempts"] += 1

    return False


if is_sorted():
    if binary_search(list, n):
        print("Found! Index #:", position)
        print("Attempts:" + str(attempts))
    else:
        print("not found")
else:
    print("List not sorted")
