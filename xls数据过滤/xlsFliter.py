"""
清理数据中的非数值
"""

import pandas as pd
#判断是否是数字
def isfloat(str):
    try:
        float(str)
        return True
    except:
        return False

df = pd.read_excel('0.xls')
df_bak = df
for i in df.columns:
    df = df.drop(j for j in df.index if not isfloat(df[i][j]))

writer = pd.ExcelWriter('fliter.xls')
df.to_excel(writer,'sheet1',index=False)

writer.save()