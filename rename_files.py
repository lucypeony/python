import os

for file in os.listdir('.'):
    if file[-2:] =='py':
        continue

    name = file.replace(' ','')
    new_name = name[20:30] + name[-4:]
    os.rename(file,new_name)
    
