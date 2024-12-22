
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

# a = 123
# for i in range(10):
#     a = evolve(a)
#     print(a)
# x =1




part1 =0
for buyer in buyers:
    for i in range(2000):
        buyer = evolve(buyer)
    #print(buyer)
    part1 += buyer

print(part1)


