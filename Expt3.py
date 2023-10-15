nl=[]
for x in range(2000,2500):
    if(x % 17==0) and (x % 5!=0):
        nl.append(str(x))
print(','.join(nl))