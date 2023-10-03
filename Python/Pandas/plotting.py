import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 0.3, 1.2, 2.1, 2.8, 3.6, 4.1, 4.8, 5.3, 6.0])
y = np.sin(x)

df = pd.DataFrame({'x': x, 'y': y})

df.plot(x='x', y='y', label='sin(x)')

plt.title('Plot of sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.show()