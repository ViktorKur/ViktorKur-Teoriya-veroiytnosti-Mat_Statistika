# Задача 2.
# В первом ящике находится 8 мячей,из которы 5-белые.Вовтором ящике - 12 мячей,из
# которых 5 белых. Из первого ящика вытаскиваютслучайным образом два мяча,из
# второго-4.Какова вероятность того,что 3 мяча белые?

from math import comb
# Данные задачи
total_balls_box1 = 8
white_balls_box1 = 5
total_balls_box2 = 12
white_balls_box2 = 5
# Вероятности
prob_two_white_box1 = comb(white_balls_box1, 2) /comb(total_balls_box1, 2)
prob_one_white_box2 = comb(white_balls_box2, 1) * comb(total_balls_box2 - white_balls_box2, 3) / comb(total_balls_box2, 4)
# Вероятность того, что 3 мяча белые
prob_three_white = prob_two_white_box1 * prob_one_white_box2
print(prob_two_white_box1)
print(prob_one_white_box2)
print(f"Вероятность того, что 3 мяча белые: {prob_three_white:.5f}") 