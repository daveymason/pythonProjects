import random

lotto_numbers = []

for i in range (0,7) :
    number = random.randint(1,46)
    while number in lotto_numbers:
        number = random.randint(1,46)

    lotto_numbers .append(number)

lotto_numbers.sort()

print(lotto_numbers)
