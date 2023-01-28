from turtle import position


position = -1
attempts = 1

# WHILE LOOP
def linear_search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()["position"] = i
            return True
        i = i + 1
        globals()["attempts"] = attempts + 1
    return False


values = input("Enter the following numbers, separated by commas (no spaces): \n")
n = int(input(" Enter the number you want to look up.: \n"))
list = values.split(",")

for i in range(0, len(list)):
    list[i] = int(list[i])


if linear_search(list, n):
    print("Did find! Index #:", position)
    print("Took", attempts, "tries to discover the number")
else:
    print("not recognized")
