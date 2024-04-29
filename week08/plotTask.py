# weekly task week08
# Author : Sarabjeet Kumar

import numpy as np
import matplotlib.pyplot as plt

mean = 5
stan_dev = 2
values = 1000

values = np.random.randint(mean, stan_dev, values)

# y = x ** 3

plt.title('Hostogram')
plt.xlabel('values')
plt.ylabel('Y axis')
plt.show()