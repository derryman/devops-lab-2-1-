numbers = input("Enter numbers seperated b y space: ").split()
numbers = [float(num) for num in numbers]

average = sum(numbers) / len(numbers)
print(f"THe average is: {average}")

