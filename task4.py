# При помощи библиотеки pandas создать два датафрейма с индексами 'Moscow', 'Tula', 'Yaroslavl', 'Tver' и 
# 'Moscow', 'Tula', 'Volgograd', 'Novgorod' и случайными значениями в столбцах 
# 'report' (от 1 до 10) и 'sales' (от 100 до 1000). 
# Написать программный код расчёта суммы продаж и суммарное количество отчетов по двум таблицам.

import pandas as pd
import numpy as np

df1 = pd.DataFrame(index=['Moscow', 'Tula', 'Yaroslavl', 'Tver'], 
                   columns=['report', 'sales'])
df1['report'] = np.random.randint(1, 10, size=4)
df1['sales'] = np.random.randint(100, 1000, size=4)


df2 = pd.DataFrame(np.random.randint(1, 10, (4,2)), index=['Moscow', 'Tula', 'Volgograd', 'Novgorod'], 
                   columns=['report', 'sales'])
df2['report'] = np.random.randint(1, 10, size=4)
df2['sales'] = np.random.randint(100, 1000, size=4)

print(df1)
print(df2)

common = pd.concat([df1, df2])
itog = common.groupby(common.index).sum()

print(f"Сумма продаж: {itog['sales'].sum()}")
print(f"Количество отчетов: {itog['report'].sum()}")
