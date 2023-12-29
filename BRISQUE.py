#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:58:00 2023
A code to implement BRISQUE 
@author: amir
"""

from brisque import BRISQUE
from PIL import Image
import os 
import pandas as pd

cwd = os.getcwd()
list_files = os.listdir('/Users/amir/Projects/f231228/images/')
del list_files[1]

data = []
for i in range(0,len(list_files)):
    print(i)
    image1 = Image.open(['/Users/amir/Projects/f231228/images/' + list_files[i]][0]) 
    obj = BRISQUE(url=False) 
    data.append([list_files[i],obj.score(image1)])

df = pd.DataFrame(data, columns=['Name', 'BRISQUE score'])
print(df)
df.to_csv('/Users/amir/Projects/f231228/result.csv')  
