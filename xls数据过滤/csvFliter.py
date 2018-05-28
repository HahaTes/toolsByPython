"""
清理数据中的非数值
csv读取更快
写入方法改变
"""

import pandas as pd
#判断是否是数字
def isfloat(str):
    try:
        float(str)
        return True
    except:
        return False

df = pd.read_csv('TJ9_for_classification.csv')
df_bak = df
for i in df.columns:
    #df_sort = df.sort()
    df = df.drop(j for j in df.index if not isfloat(df[i][j]))

df.to_csv('fliter.csv',header=True,index=False)