
part1_result = 0
wins_per_card = {}

times_card_played = {key: 1 for key in range(1, 199)} # there are 198 cards
with open('Day4/Day4Input.txt', 'r') as file:
    for line in file:
        card_num = int(line.split(':')[0].split()[1])
        numbers = line.split(':')[1]
        winning_num, your_num = numbers.split('|')
        winning_num = set(winning_num.strip().split())
        your_num  = set(your_num.strip().split())
        intersection = winning_num & your_num
        num_matches = len(intersection)

        wins_per_card[card_num] = num_matches
        for i in range(1,num_matches+1):
            times_card_played[card_num + i] += times_card_played[card_num]

        if num_matches > 0:
            part1_result += 2 ** (len(intersection)-1)

print(part1_result)

# part 2 result
print(sum(times_card_played.values()))
