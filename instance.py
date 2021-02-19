from classes import Die

die = Die(16)

tally = []

# roll the dice 10 times:
for roll_count in range(10):
    x = die.roll()
    tally.append(x)

print(tally)