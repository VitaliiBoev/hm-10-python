import pandas as pd 
import numpy as np 
import random
lst = ['robot'] * 10
lst += ['human'] * 10 # складываем список robot + human
random.shuffle(lst) # случайное перемешивание последовательности lst
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
print('')
# преобразовываем список в dataframe
data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int) #изменяет таблицу в pandas
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)
