from classes import Die

die = Die(16)

tally = []

# roll the dice 10 times:
for roll_count in range(1000):
    x = die.roll()
    tally.append(x)

print(tally)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = tally.count(value)
    frequencies.append(frequency)
print(frequencies)