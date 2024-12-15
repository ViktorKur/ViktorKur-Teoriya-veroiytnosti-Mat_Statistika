# Задача 4.
# В первомящике находится 10 мячей,из которых 7-белые.Во втором ящике-11
# мячей,из которых 9 белых.Из каждого ящика вытаскивают случайным образом
# по два мяча.Какова вероятность того,что все мячи беые? Какова вероятность
# того,что ровно два мяча белые? Какова вероятность того,что хотябы один мяч
# белый?  

# Эталонное решение:
from math import comb
# Данные задачи
total_balls_box1 = 10
white_balls_box1 = 7
total_balls_box2 = 11
white_balls_box2 = 9
# Вероятности извлечения двух белых мячей из первого ящика
prob_two_white_box1 = comb(white_balls_box1, 2) / comb(total_balls_box1, 2)
print(prob_two_white_box1)
# Вероятности извлечения двух белых мячей из второго ящика
prob_two_white_box2 = comb(white_balls_box2, 2) / comb(total_balls_box2, 2)
print(prob_two_white_box2)
# Вероятность, что все мячи белые
prob_all_white = prob_two_white_box1 * prob_two_white_box2
print(f"Вероятность того, что все мячи белые: {prob_all_white:.5f}")
# Вероятность того, что ровно два мяча белые
prob_one_white_box1 = (comb(white_balls_box1, 1) * comb(total_balls_box1 - white_balls_box1, 1)) /comb(total_balls_box1, 2)
print(prob_one_white_box1)
prob_one_white_box2 = (comb(white_balls_box2, 1) * comb(total_balls_box2 - white_balls_box2, 1)) /comb(total_balls_box2, 2)
print(prob_one_white_box2)
prob_two_white_exactly = (prob_two_white_box1 * prob_one_white_box2) + (prob_one_white_box1 * prob_two_white_box2)
print(f"Вероятность того, что ровно два мяча белые:{prob_two_white_exactly:.5f}")