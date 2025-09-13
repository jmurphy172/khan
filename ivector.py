# coding: utf-8
get_ipython().run_line_magic('load', 'ivector.py')
# %load ivector.py

from khan_utils import *

import numpy as np

v_mag = 8
v_angle = 140

w_angle = 40
w_mag = 4


v_adj = v_mag * dsin(v_angle)
v_opp = v_mag * dsin(v_angle)

w_adj = w_mag * dcos(w_angle)
w_opp = w_mag * dsin(w_angle)







