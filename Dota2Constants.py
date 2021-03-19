# -*- coding: utf-8 -*-
"""
Import Modules
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests


"""
Load data and clean
"""

url = 'https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json'
df = pd.read_json(url)
data = df.transpose()
data = data.drop(columns=['id', 'name', 'roles', 'img', 'icon', 'cm_enabled'])

"""

"""
