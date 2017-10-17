#!/usr/bin/env python

import numpy as np

nrows = 10000
ncols = 3

# generate draws from a normal distribution; the draws in each column
# are centered around 5.0, 10.0, and 0.0, respectively
data = np.random.normal(loc=[5.0, 10.0, 0.0], size=(nrows, ncols))

# export to a csv file
np.savetxt('simple_data.csv', data, header='x, y, z',
           delimiter=', ', comments='')
