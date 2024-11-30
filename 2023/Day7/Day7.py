
with open('Day7/Day7Input.txt','r') as f:
    puzzle_input = f.read()

#count num cards
card_score = {
    'A': 14,
    'K': 13, 'Q':12,'J':11, 'T':10,'9':9,
    '8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2
}

def score_hand2(hand,part):
    card_vals = []
    card_counts = {}
    

    if part == 2:
        card_score['J'] = 0

    # iterate through hand
    for card in hand:
        card_vals.append(card_score[card]+10)
        card_counts[card] = card_counts.get(card, 0) + 1
    
    # work out score based on cards and position
    card_val = int(''.join(map(str, card_vals)))

    #adjust card counts for jokers
    if part == 2:
        num_jokers = card_counts.get('J',0)
        card_counts['J'] = 0
    else:
        num_jokers = 0 

    # determine a score for hand
    ordered_combinations = sorted(card_counts.values(), reverse = True)
    first = ordered_combinations[0] + num_jokers


    if first == 5:
        hand_val = 7        
    elif first == 4:
        hand_val =  6
    elif first == 3 and ordered_combinations[1] == 2:
        hand_val = 5
    elif first ==3:
        hand_val = 4
    elif  first == 2 and ordered_combinations[1] == 2:
        hand_val = 3
    else:
        hand_val = first
    
    # detemine overall score for ranking
    val = int(str(hand_val)+ str(card_val))
    
    return (val)      




def calc_result(input,part):
    lines = input.split('\n')
    score = {}
    bid = {}
    for i,line in enumerate(lines):
        bid[i] = int(line.split()[1])
        score[i] = score_hand2(line.split()[0],part)
    
    sorted_values = sorted(score.values())
    rank = {v: i+1 for i,v in enumerate(sorted_values)}

    result = 0
    for i in bid:
        print(f'bid{bid[i]}:rank{rank[score[i]]}')
        result += bid[i] * rank[score[i]]
    
    return result

# part 1 result
print(calc_result(puzzle_input,1))

# part 2 result
print(calc_result(puzzle_input,2))
