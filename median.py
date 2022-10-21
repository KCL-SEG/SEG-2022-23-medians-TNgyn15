"Median calculator."

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) % 2 == 0:
    index = int(len(numbers) / 2)
    median = (numbers[index - 1] + numbers[index]) / 2
else:
    index = int((len(numbers) - 1) / 2)
    median = numbers[index]

print(median)