import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import time
# # Создайте пустой DataFrame с нужными колонками
# df = pd.DataFrame(columns=["x", "y"])

# # Создайте пустой график и сохраните его объект в переменной chart
# chart = st.line_chart(df)

# # Инициализируйте переменную x
# x = 2

# for i in range(1, 4):
#     x = x**2
#     # Добавьте новую строку в DataFrame используя метод loc
#     df.loc[i] = [x, i]
#     # Обновите график, используя метод add_rows()
#     chart.add_rows(df.iloc[-1:])

import streamlit as st

# Инициализируйте переменную x
x = 2

# Создайте пустой график
chart_data = {'x':[], 'iter':[]}
chart = st.line_chart(chart_data)

# Запустите цикл
for i in range(1, 4):
    # Увеличьте переменную x на 2
    x = x**2
    # Добавьте значение x и количества итераций в списки данных для графика
    chart_data['x'].append(x)
    chart_data['iter'].append(i)
    # Обновите график передав ему обновленные данные
    chart.add_rows({'x':[x], 'iter':[i]})
    time.sleep(1)
