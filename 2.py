from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

ROUND_NUMBER = 2

# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
iq_std = np.std(iq)
# print(f'Промежуточные данные iq_std: {round(iq_std,ROUND_NUMBER)}')
iq_mean = mean(iq)
# print(f'Промежуточные данные iq_mean: {round(iq_mean,ROUND_NUMBER)}')
t = stats.t.ppf(1-.05/2,len(iq)-1)
# print(f'Промежуточные данные t: {round(t,ROUND_NUMBER)}')
point_1 = iq_mean - t*iq_std/sqrt(len(iq))
point_2 = iq_mean + t*iq_std/sqrt(len(iq))
print(f'Доверительный интервал: [{round(point_1, ROUND_NUMBER)}; {round(point_2, ROUND_NUMBER)}]')