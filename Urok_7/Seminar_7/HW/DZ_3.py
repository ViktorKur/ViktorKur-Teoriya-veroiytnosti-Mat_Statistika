# Задача 3.
# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не
# было.

import numpy as np
import scipy.stats as stats
# Данные задач
alpha = 0.05
first_measurement = [150, 160, 165, 145, 155]
second_measurement = [140, 155, 150, 130, 135]
# Тест для независимых выборок (хотя данные парные, используем t-тест для независимых выборок)
t_stat, p_value = stats.ttest_ind(first_measurement,second_measurement, equal_var=False)
print(f"t-статистика: {t_stat}")
print(f"p-значение: {p_value}")
if p_value < alpha:
  print("Есть статистически значимые различия между первым и вторым измерением.")
else:
  print("Нет статистически значимых различий между первым и вторым измерением.")