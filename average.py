numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
