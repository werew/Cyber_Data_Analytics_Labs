import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = np.random.random((16, 16))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()

#df = pd.read_csv(, header = 0)
