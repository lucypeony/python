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
输入：某个班级某个科目的校次
返回：该班级该科目的ABCDE等级的人数，以   形式返回
计算方式： 去掉 - 值数据

一共有736个数据参与等级计算，（去掉空卷和没扫描的）（数据来自于总分校次排序）
'''
def dengji_cal(b):
    TOTAL=736    #可以从总分获得
    A1 = int(0.05*TOTAL)
    B1 = int(0.2*TOTAL)
    C1 = int(0.6*TOTAL)
    D1 = int(0.8*TOTAL)
    E1 = int(TOTAL)
    A1num=0
    B1num=0
    C1num=0
    D1num=0
    E1num=0
    for m in b :    #m代表某个科目某个学生的校次
        if(is_number(m)):
            m=float(m)

            if m<=A1:
                A1num+=1
            elif m<=B1:
                B1num+=1
            elif m<=C1:
                C1num+=1
            elif m<=D1:
                D1num+=1
            else:
                E1num+=1
    res=pd.Series(index=['A','B','C','D','E'])
    res['A']=A1num
    res['B']=B1num
    res['C']=C1num
    res['D']=D1num
    res['E']=E1num
    return res
    
    

'''
x:处理后的表格数据，DataFrame
xcolumns：x的列的名称
['姓名', '班级', '语文', '数学', '英语', '物理', '语文校次', '数学校次', '英语校次', '物理校次',
       '总分', '总分校次']
xg:groupby按照班级

kemu:Series 保存某个班级某个科目的分数，用来计算平均分

dengji:Series 保存某个班级某个科目的校次，用来统计ABCDE等级

'''
xcolumns=x.columns
xg=x.groupby(xcolumns[1])
for banji, banjidf in xg:
    kumulist=['语文','数学','英语','物理','总分']
    for k in kumulist:
        kemu=banjidf[k]
        print(banji,kemu.name,pingjunfen(kemu))

    dengjilist=['语文校次','数学校次','英语校次','物理校次','总分校次']
    for d in dengjilist:
        dengji=banjidf[d]
        print(banji,d,dengji_cal(dengji))
        
    
       

#计算等级
'''

'''

#输出文件
