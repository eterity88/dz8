from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

ROUND_NUMBER = 2

# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.
lon_mean = 174.2
lon_std = sqrt(25)
lon_n = 27
z = stats.norm.ppf(1-.05/2)
# print(f'Промежуточные данные z: {round(z,ROUND_NUMBER)}')
dot_1 = lon_mean - z*lon_std/sqrt(lon_n)
dot_2 = lon_mean + z*lon_std/sqrt(lon_n)
print(f'Доверительный интервал: [{round(dot_1, ROUND_NUMBER)}; {round(dot_2, ROUND_NUMBER)}]')