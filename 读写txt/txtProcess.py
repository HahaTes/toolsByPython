#判断是否是数字
def isfloat(str):
    try:
        float(str)
        return True
    except:
        return False

result = []
coef = 0
#读取文件
with open('thrustweight.dat','rt') as f:
    while True:
        line = f.readline()
        
        line_n = line.strip()
        data = line_n.split('\t')
       
        if(isfloat(data[0])):
            coef = float(data[0])/100
            break
        if not line:
            break

with open('loadc.dat','rt') as f:
    while True:
        line = f.readline()
        line_n = line.strip()
        data = line_n.split('\t')
        if(data[0]=='0'):
            res = (float(data[1])+float(data[2]))/2.0*coef
            result.append(res)
            break
    
    while True:        
        if not line:
            break
        line = f.readline()
        line_n = line.strip()
        data = line_n.split('\t')
        #遇到空行跳过
        if (len(data)<3):
            continue
        res = (float(data[1])+float(data[2]))/2.0*coef
        result.append(res)

        
#写入文件
with open('TotalPushForce.dat','wt') as f:
    f.write(str(len(result)))
    for i in range(len(result)):
        f.write('\n'+str(i*10+1)+'\t')
        f.write("%.2f" %result[i])
    
    
with open('kPushForceOnCutters.dat','wt') as f:
    f.write(str(coef))