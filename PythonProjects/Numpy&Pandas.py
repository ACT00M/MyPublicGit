import pandas as pd 
data = pd.Series((0.25, 0.5, 0.75, 1.0)) 
print(data[1]) 
print(data[1:3]) 
print(data[1:3:2])