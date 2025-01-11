# Задание 1.
# Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks
# = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Найдите ковариацию этих двух величин с
# помощью элементарных действий, а затем с помощью функции cov из numpy Полученные
# значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью
# ковариации и среднеквадратичных отклонений двух признаков, а затем с
# использованием функций из библиотек numpy и pandas.

import numpy as np
import pandas as pd
# Данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# 1. Ковариация вручную
mean_zp = np.mean(zp)
mean_ks = np.mean(ks)
cov_manual = np.sum((zp - mean_zp) * (ks - mean_ks)) / (len(zp) - 1)
print(f"Ковариация вручную: {cov_manual}")
# 2. Ковариация с помощью numpy
cov_numpy = np.cov(zp, ks)[0, 1]
print(f"Ковариация с помощью numpy: {cov_numpy}")
# 3. Коэффициент корреляции Пирсона вручную
std_zp = np.std(zp, ddof=1)
std_ks = np.std(ks, ddof=1)
correlation_manual = cov_manual / (std_zp * std_ks)
print(f"Коэффициент корреляции Пирсона вручную:{correlation_manual}")
# 4. Коэффициент корреляции Пирсона с помощью numpy
correlation_numpy = np.corrcoef(zp, ks)[0, 1]
print(f"Коэффициент корреляции Пирсона с помощью numpy:{correlation_numpy}")
# 5. Коэффициент корреляции Пирсона с помощью pandas
correlation_pandas = pd.Series(zp).corr(pd.Series(ks))
print(f"Коэффициент корреляции Пирсона с помощью pandas:{correlation_pandas}")