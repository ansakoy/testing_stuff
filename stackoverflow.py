import random

# Generate list of random numbers of given length from given range
all_nums = range(1, 11)
sample = list()
output_length = 10

for position in range(output_length):
    sample.append(random.choice(all_nums))

print(sample)

# Count repeating numbers
num_unique_values = len(set(sample))
total_values = len(sample)
difference = total_values - num_unique_values
print('Number of extra values:', difference)
