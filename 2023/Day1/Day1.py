
import re


result_part1 = 0
with open('Day1Input.txt', 'r') as file:
    for line in file:
        # Process each line
        digits = [char for char in line if char.isdigit()]
        result_part1 = result_part1 + int(digits[0] + digits[-1])

print(result_part1)

#part 2

substrings = {"1": 1,
               "2": 2,
               "3": 3,
               "4": 4,
               "5":5,
               "6":6,
               "7":7,
               "8":8,
               "9":9,
               "0":0,
               "one":1,
               "two":2,
               "three":3,
               "four":4,
               "five":5,
               "six":6,
               "seven":7,
               "eight":8,
               "nine":9
               }


pattern = re.compile("|".join(map(re.escape, substrings.keys())))

result_part2 = 0
with open('Day1Input.txt', 'r') as file:
    for line in file:
        # Process each line
        matches = pattern.findall(line)
        result_part2 = result_part2 + substrings[matches[0]]*10 + substrings[matches[-1]]

print(result_part2)
