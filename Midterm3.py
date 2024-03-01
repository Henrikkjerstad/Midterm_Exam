import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Removing numbers greater than 50 and replacing others with "XX"
processed_numbers = ["XX" if num <= 50 else None for num in random_numbers]
processed_numbers = [num for num in processed_numbers if num]

# Print the final list
print(processed_numbers)
