# Задача 2.
# Исследовалось влияние препарата на уровень давления пациентов. Сначала
# измерялось давление до приема препарата, потом через 10 минут и через 30
# минут. Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

import numpy as np
import scipy.stats as stats
# Данные задач
before = [150, 160, 165, 145, 155]
after_10 = [140, 155, 150, 130, 135]
after_30 = [130, 130, 120, 130, 125]
# Тесты для парных выборок
t_stat_10, p_value_10 = stats.ttest_rel(before, after_10)
t_stat_30, p_value_30 = stats.ttest_rel(before, after_30)
t_stat_10_30, p_value_10_30 = stats.ttest_rel(after_10, after_30)
print(f"t-статистика для давления до и через 10 минут: {t_stat_10},p-значение: {p_value_10}")
print(f"t-статистика для давления до и через 30 минут: {t_stat_30},p-значение: {p_value_30}")
print(f"t-статистика для давления через 10 и 30 минут:{t_stat_10_30}, p-значение: {p_value_10_30}")
alpha = 0.05
if p_value_10 < alpha:
  print("Есть статистически значимые различия между давлением до приема и через 10 минут.")
else:
  print("Нет статистически значимых различий между давлением до приема и через 10 минут.")
if p_value_30 < alpha:
  print("Есть статистически значимые различия между давлением до приема и через 30 минут.")
else:
  print("Нет статистически значимых различий между давлением до приема и через 30 минут.")
if p_value_10_30 < alpha:
  print("Есть статистически значимые различия между давлением через 10 и 30 минут.")
else:
  print("Нет статистически значимых различий между давлением через 10 и 30 минут.")