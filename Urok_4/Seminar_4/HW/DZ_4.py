# Задача 4.
# Рост взрослого населения города X имеет нормальное распределение. Причем,
# средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек
# имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

from scipy.stats import norm
# Задача 4: Нормальное распределение с mu = 174 и sigma = 8
mu = 174
sigma = 8
# Вероятность, что рост больше 182 см
prob_gt_182 = 1 - norm.cdf(182, mu, sigma)
# Вероятность, что рост больше 190 см
prob_gt_190 = 1 - norm.cdf(190, mu, sigma)
# Вероятность, что рост от 166 см до 190 см
prob_166_to_190 = norm.cdf(190, mu, sigma) - norm.cdf(166, mu,sigma)
# Вероятность, что рост от 166 см до 182 см
prob_166_to_182 = norm.cdf(182, mu, sigma) - norm.cdf(166, mu,sigma)
# Вероятность, что рост от 158 см до 190 см
prob_158_to_190 = norm.cdf(190, mu, sigma) - norm.cdf(158, mu,sigma)
# Вероятность, что рост не выше 150 см или не ниже 190 см
prob_leq_150_or_ge_190 = norm.cdf(150, mu, sigma) + (1 -norm.cdf(190, mu, sigma))
# Вероятность, что рост не выше 150 см или не ниже 198 см
prob_leq_150_or_ge_198 = norm.cdf(150, mu, sigma) + (1 -norm.cdf(198, mu, sigma))
# Вероятность, что рост ниже 166 см
prob_lt_166 = norm.cdf(166, mu, sigma)
print(f"Вероятность, что рост больше 182 см: {prob_gt_182:.5f}")
print(f"Вероятность, что рост больше 190 см: {prob_gt_190:.5f}")
print(f"Вероятность, что рост от 166 см до 190 см:{prob_166_to_190:.5f}")
print(f"Вероятность, что рост от 166 см до 182 см:{prob_166_to_182:.5f}")
print(f"Вероятность, что рост от 158 см до 190 см:{prob_158_to_190:.5f}")
print(f"Вероятность, что рост не выше 150 см или не ниже 190 см:{prob_leq_150_or_ge_190:.5f}")
print(f"Вероятность, что рост не выше 150 см или не ниже 198 см:{prob_leq_150_or_ge_198:.5f}")
print(f"Вероятность, что рост ниже 166 см: {prob_lt_166:.5f}")