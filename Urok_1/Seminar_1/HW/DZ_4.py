# Задача 4.
# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2
# приобретенных билета окажутся выигрышными?

import math
total_tickets = 100
winning_tickets = 2
total_combinations = math.comb(total_tickets, 2)
winning_combinations = math.comb(winning_tickets, 2)
probability_two_winning = winning_combinations / total_combinations
print(f"Вероятность того, что оба билета выигрышные:{probability_two_winning:.5f}")