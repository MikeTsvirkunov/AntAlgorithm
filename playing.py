import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
# plt.style.use("seaborn-v0_8-whitegrid")

# fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
# line, = ax.plot([], [], lw=3)

# def init():
#     line.set_data([], [])
#     return line,

# def animate(i):
#     x = np.linspace(0, 4, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,

# anim = FuncAnimation(fig, animate, init_func=init,
#                      frames=200, interval=20, blit=True)

# # Создаем переменную для хранения анимации
# anim_variable = anim

# # Выводим анимацию на страницу Streamlit с помощью функции st.pyplot()
# st.pyplot(fig)

# # Запускаем анимацию с помощью функции plt.show()
# plt.show()

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
import streamlit as st
from PIL import Image
  
plt.style.use('dark_background') 
  
fig = plt.figure() 
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50)) 
line, = ax.plot([], [], lw=2) 
def init(): 
    line.set_data([], []) 
    return line, 
  
xdata, ydata = [], [] 

def animate(i): 
    t = 0.1 * i 
    x = t * np.sin(t) 
    y = t * np.cos(t) 
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
    return line, 

plt.title('Создаем спираль в matplotlib') 

plt.axis('off') 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=500, interval=20, blit=True) 
anim.save('coil.gif', writer='pillow')
gif_path = "coil.gif"
st.image(gif_path, output_format="gif")





# import streamlit as st 
# import numpy as np 
# from matplotlib import pyplot as plt 
# from matplotlib.animation import FuncAnimation 

# # Agg backend, который подходит для Streamlit 
# import matplotlib
# matplotlib.use('Agg') 

# plt.style.use("seaborn-v0_8-whitegrid") 
 
# fig = plt.figure() 
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2)) 
# line, = ax.plot([], [], lw=3) 
 
# def init(): 
#     line.set_data([], []) 
#     return line, 
 
# def animate(i): 
#     x = np.linspace(0, 4, 1000) 
#     y = np.sin(2 * np.pi * (x - 0.01 * i)) 
#     line.set_data(x, y) 
#     return line, 
 
# anim = FuncAnimation(fig, animate, init_func=init, 
#                      frames=200, interval=20, blit=True) 
# st.write(fig)


# import streamlit as st

# gif_path = "sine_wave.gif"
# st.image(gif_path, output_format="gif")