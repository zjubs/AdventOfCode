from collections import defaultdict, deque

with open('2024/Day22/Day22Input.txt', 'r') as f:
    buyers = [*map(int,f.read().split('\n'))]


def evolve(secret):
    secret ^= (secret * 64)
    secret %= 16777216

    secret ^= (secret // 32)
    secret %= 16777216

    secret ^= (secret * 2048)
    secret %= 16777216

    return secret

patterns = defaultdict(int)
part1 =0

for buyer in buyers:
    last_4_diff = deque((0,0,0,0), maxlen=4)
    price = 0
    seen = set()

    for i in range(2000):
        lastprice = price
        buyer = evolve(buyer)
        price = buyer % 10
        diff = price - lastprice
        last_4_diff.append(diff)
        if i >= 4:
            t = tuple(last_4_diff)
            if t not in seen:
                patterns[t] += price
                seen.add(t)

    part1 += buyer

print(f'Part1: {part1}')
print(f'Parrt2: {max(patterns.values())}')