# Теория вероятностей и математическая статистика
# Задание 1.
# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз

import math
total_cards, clubs = 52, 13
probability_all_clubs = round((math.comb(clubs, 4)) /(math.comb(total_cards, 4)), 3)
print(f"Вероятность, что все карты крести:{probability_all_clubs}")
aces = 4
probability_at_least_one_ace = 1 - round(math.comb(total_cards - aces, 4) / math.comb(total_cards, 4),3)
print(f"Вероятность, что хотя бы один туз:{probability_at_least_one_ace}")

# # Эталонное решение
# import math
# # Часть а) Вероятность, что все карты крести
# total_cards = 52
# clubs = 13
# total_combinations = math.comb(total_cards, 4)
# clubs_combinations = math.comb(clubs, 4)
# probability_all_clubs = clubs_combinations / total_combinations
# print(f"Вероятность того, что все карты крести:{probability_all_clubs:.5f}")
# # Часть б) Вероятность, что хотя бы один туз
# aces = 4
# no_aces_combinations = math.comb(total_cards - aces, 4)
# probability_no_aces = no_aces_combinations / total_combinations
# probability_at_least_one_ace = 1 - probability_no_aces
# print(f"Вероятность того, что хотя бы один туз:{probability_at_least_one_ace:.5f}")