number = int(input("How many numbers you go type? "))
array: [float] = [0 for x in range (number)]
for i in range (0, number):
    array[i] = float(input("Write a number: "))
print()
print("Typed Numbers: ", end = " ")
for i in range(0, number):
    print(array[i], end = " ")
print()

sum = 0
for i in range(0, number):
    sum = sum + array[i]
print(f"Sum is: {sum}")

average = sum / number
print(f"Array is: {average}")