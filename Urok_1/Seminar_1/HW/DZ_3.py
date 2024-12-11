# Задача 3.
# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом
# извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

import math
vsego_detal, okrah_detal = 15, 9
veroytn_vseIzvlOkrah = round(math.comb(okrah_detal, 3)/ math.comb(vsego_detal, 3),3)
print(f"Вероятность того, что все детали окрашены = {veroytn_vseIzvlOkrah}")
