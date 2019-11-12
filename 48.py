import pandas as pd

fileName='包河区2019-2020学年八年级第一学期期中检测.xls'
df = pd.read_excel(fileName,header=1)
print('opening file ....')
#print(df.head)

x=df[['姓名','班级','语文','数学','英语','物理','Unnamed: 7','Unnamed: 13','Unnamed: 19','Unnamed: 25','总分','Unnamed: 55']]
x=x.rename(columns={'Unnamed: 7':'语文校次','Unnamed: 13':'数学校次','Unnamed: 19':'英语校次','Unnamed: 25':'物理校次','Unnamed: 55':'总分校次'})
x=x.drop(index=0)
#temp1: to_excel


#TEMOPRARY
#x.to_excel('test1.xlsx',index=False)




'''
输入：一个值
返回：布尔型
方法：如果是数字，返回True；否则，返回False

'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
'''
#计算平均分
#获得一个成绩Series
#过滤掉非数字值 （non numeric value)
#返回平均分
'''
def pingjunfen(a):
    count=0
    sum=0
    for t in a:
        if(is_number(t)):
            t=float(t)
            sum+=t;
            count+=1
    return sum/count

'''
x:处理后的表格数据，DataFrame
xcolumns：x的列的名称
['姓名', '班级', '语文', '数学', '英语', '物理', '语文校次', '数学校次', '英语校次', '物理校次',
       '总分', '总分校次']
xg:groupby按照班级

'''
xcolumns=x.columns
xg=x.groupby(xcolumns[1])
for banji, banjidf in xg:
    kumulist=['语文','数学','英语','物理','总分']
    for k in kumulist:
        kemu=banjidf[k]
        print(banji,kemu.name,pingjunfen(kemu))
    
       

#计算等级


#输出文件
