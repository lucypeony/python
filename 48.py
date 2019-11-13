import pandas as pd

fileName='包河区2019-2020学年八年级第一学期期中检测.xls'
df = pd.read_excel(fileName,header=1)
print('opening file ....')
#print(df.head)

y=df[['姓名','班级','语文','数学','英语','物理','Unnamed: 7','Unnamed: 13','Unnamed: 19','Unnamed: 25','总分','Unnamed: 55']]
y=y.rename(columns={'Unnamed: 7':'语文校次','Unnamed: 13':'数学校次','Unnamed: 19':'英语校次','Unnamed: 25':'物理校次','Unnamed: 55':'总分校次'})
y=y.drop(index=0)
#temp1: to_excel


#TEMOPRARY
#y.to_excel('test1.xlsx',index=False)
#在这里，在test1.xlsx的基础上，处理掉非数字数值，手动
#保存在test2.xlsx
fileName2='test2.xlsx'
x=pd.read_excel(fileName2)

'''
在这里，计算语文、数学、英语和物理四科总分，并替换总分
然后按照总分，进行排序，并用新的顺序来替换掉原来的index

'''
sike = x['语文']+x['数学']+x['英语']+x['物理']
x['总分']=sike
#计算总分排名
#按照总分，重新排序
x=x.sort_values('总分',ascending=False)
x=x.reset_index()
x=x[x.columns[1:]]
s=list(x.index)
s=pd.Series(s)+1
x['总分校次']=s

#print(x.mean())

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
frames=[]  #用来存储要concentate 的表格banjidata
frames_keys=[]    #用来存储班级 

xcolumns=x.columns
xg=x.groupby(xcolumns[1])
for banji, banjidf in xg:
    banjidata=pd.DataFrame() 
    kemulist=['语文','数学','英语','物理','总分']
    banji_pjf=pd.Series(index=kemulist) #保存每个班级的四个科目和总分 的平均分
    banji_pjf.name=banji
    for k in kemulist:
        kemu=banjidf[k]
        #print(banji,kemu.name,pingjunfen(kemu))
        banji_pjf[kemu.name]=pingjunfen(kemu)
    banjidata['平均分']=banji_pjf
    #print(banjidata.transpose())
    banjidata=banjidata.transpose()

    dengjilist=['语文校次','数学校次','英语校次','物理校次','总分校次']
    banji_dj = pd.DataFrame()
    for d in dengjilist:
        dengji=banjidf[d]
        #print(banji,d,dengji_cal(dengji))
        dd= pd.Series(index=['A','B','C','D','E']) #用来保存每个科目的A,B,C,D,E等级数目
        dd=dengji_cal(dengji)
        dd.name=d[0:2]
        banji_dj[dd.name]=dd
    #print(banji_dj)
    banjidata=banjidata.append(banji_dj)

    '''
        准备上次考试数据放置的rows
    '''
    fenxilist=['八上月考一(100)','八上月考一A等级','月考一期中分差','月考一期中提高率','月考一期中年级提高率差','授课教师']
    fenxidf=pd.DataFrame()
    for fenxi in fenxilist:
        f=pd.Series(index=kemulist)
        fenxidf[fenxi]=f



    '''
    打开上次考试的数据
    最外层的班级： banji
    上次考试文件来源：期中成绩分析.xlsx
    导入八上月考的平均分和A等级人数
        
    '''
    shangciFile='期中成绩分析.xlsx'
    shangcidf=pd.read_excel(shangciFile)
    shangcidfg=shangcidfg=shangcidf.groupby('班级')
    for scbanji,scbanjidf in shangcidfg:
        #判断banji 是否和scbanji 一致
        if(banji[3:]==scbanji):
            scindex=scbanjidf.index
            #print(scbanjidf)
            #print(scindex)
            #print(scindex[0])
            y100=scbanjidf.loc[scindex[5],:] #八上月考一100分
            yA=scbanjidf.loc[scindex[7],:]   #八上月考一A等级
            y100=y100[1::]
            yA=yA[1::]
            fenxidf[fenxilist[0]]=y100
            fenxidf[fenxilist[1]]=yA

    fenxidf=fenxidf.transpose()
    banjidata=banjidata.append(fenxidf)

    '''
    计算分差和提高率
    分差：平均分 - 八上月考一100分
    提高率： 分差 除以 八上月考一100分

    '''
    #print(banjidata.index)
    #print(banjidata.loc['平均分'])
    bindex=banjidata.index
    fencha=banjidata.loc[bindex[0]] - banjidata.loc[bindex[6]]
    #print(fencha)
    banjidata.loc[bindex[8]]=fencha
    tigaolv=banjidata.loc[bindex[8]] / banjidata.loc[bindex[6]]
    banjidata.loc[bindex[9]]=tigaolv
   
            
    
    '''
    用于准备导出数据
    '''
    frames_keys.append(banji)
    frames.append(banjidata)
    #print(banji,banjidata)
    #banjidata.to_excel(banji+'.xlsx')

'''
导出数据
concentate的时候，保持数据来源DataFrame作为FirstLevel的index

'''
framesdf=pd.concat(frames,keys=frames_keys)
framesdf.to_excel('test3.xlsx')
