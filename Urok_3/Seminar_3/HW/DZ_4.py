# Задача 4.
# В университет на факультеты A и B поступило равное количество студентов, а на
# факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность
# того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента
# факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент
# сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A
# б). на факультете B
# в). на факультете C?

# Вероятности сдачи сессии
pA = 0.8
pB = 0.7
pC = 0.9
# Пропорции студентов
total_students = 2 + 2 + 4 # факультет C имеет в два раза больше студентов, чем A и B вместе
prob_A = 2 / total_students
prob_B = 2 / total_students
prob_C = 4 / total_students
# Вероятности сдачи сессии для факультетов
prob_pass_A = prob_A * pA
prob_pass_B = prob_B * pB
prob_pass_C = prob_C * pC
# Общая вероятность сдачи сессии
total_prob = prob_pass_A + prob_pass_B + prob_pass_C
# Вероятности для каждого факультета
prob_A_given_pass = prob_pass_A / total_prob
prob_B_given_pass = prob_pass_B / total_prob
prob_C_given_pass = prob_pass_C / total_prob
print(f"Вероятность, что студент учится на факультете A: {prob_A_given_pass:.5f}")
print(f"Вероятность, что студент учится на факультете B: {prob_B_given_pass:.5f}")
print(f"Вероятность, что студент учится на факультете C: {prob_C_given_pass:.5f}")