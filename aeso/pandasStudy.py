# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:04:32 2018

@author: Andrew Yan
"""

import pandas as pd
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
tips.info()
tips.dtypes
tips['sex_str'] = tips['sex'].astype(str)
