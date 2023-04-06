from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

ROUND_NUMBER = 2


# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

zp = np.asarray([35., 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.asarray([401., 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov_zp_ks = mean(zp*ks)-mean(zp)*mean(ks)
print(f'Расчетная ковариация: {round(cov_zp_ks,ROUND_NUMBER)}')
print(f'numpy:                {np.cov(ks,zp, ddof=0)}')

cof_cor_pearson = cov_zp_ks/(np.std(zp, ddof=0)*np.std(ks, ddof=0))
print(f'Расчетный коэф-т корреляции Пирсона: {round(cof_cor_pearson,ROUND_NUMBER)}')
print(f'numpy:                {np.corrcoef(ks,zp)}')

df = pd.DataFrame({'zp': [35., 45, 190, 200, 40, 70, 54, 150, 120, 110],
 'ks': [401., 574, 874, 919, 459, 739, 653, 902, 746, 832]})
pandas_cof_cor_pearson = df['zp'].corr(df['ks'], method='pearson')
print(f'pandas:              {round(pandas_cof_cor_pearson, ROUND_NUMBER)}')

plt.scatter(df['zp'], df['ks'])
plt.title("Задание 1")
plt.xlabel('zp')
plt.ylabel('ks')
plt.show()
