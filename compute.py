# author : Bridget Solomon
# AnalyzeRe pre-interview problem
# winter 2022 co-op term

import sys

# grab values from command line
threshold = float(sys.argv[1])
limit = float(sys.argv[2])

# input numbers
numbers = sys.stdin.read().splitlines()

# running total
sum = 0

for value in numbers:
    value = float(value)

    # value is only excess of threshold
    if sum < limit and value > threshold:
        value -= threshold
        # value cannot exceed limit when adding to running total
        if limit < (sum + value):
            value = limit - sum
    else:
        value = 0.0

    sum += value

    # each value output as calculations happen
    print(value)

# n+1 total output
print(sum)
