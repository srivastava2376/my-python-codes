import pandas as pd
month=('january','february','march','april','may','june')
no_days=(31,28,31,30,31,30)
s1=pd.Series(no_days,index=month)
print(s1)
