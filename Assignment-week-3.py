import pandas as pd

data = pd.read_csv('gapminder.csv',low_memory=False)

data.columns = map(str.lower, data.columns)

pd.set_option('display.float_format', lambda x:'%f'%x)


data['suicideper100th'] = data['suicideper100th'].convert_objects(convert_numeric=True)
data['breastcancerper100th'] = data['breastcancerper100th'].convert_objects(convert_numeric=True)
data['hivrate'] = data['hivrate'].convert_objects(convert_numeric=True)
data['employrate'] = data['employrate'].convert_objects(convert_numeric=True)


print("Statistics for a Suicide Rate")
print(data['suicideper100th'].describe())


sub = data[(data['suicideper100th']>12)]

sub_copy = sub.copy()


# BREAST CANCER RATE
bc_max=sub_copy['breastcancerper100th'].max() 
sub_copy['bcgroup4']=pd.cut(sub_copy.breastcancerper100th,[0*bc_max,0.25*bc_max,0.5*bc_max,0.75*bc_max,1*bc_max])

bc=sub_copy['bcgroup4'].value_counts(sort=False,dropna=False)

pbc=sub_copy['bcgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

bc1=[] 
pbc1=[] 
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    bc1.append(cf)    
    pf=cf*100/len(sub_copy)
    pbc1.append(pf)

print('Number of Breast Cancer Cases with a High Suicide Rate')
fmt1 = '%10s %9s %9s %12s %13s'
fmt2 = '%9s %9.d %10.2f %9.d %13.2f'
print(fmt1 % ('# of Cases','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(bc.keys(),bc,pbc,bc1,pbc1)):
    print(fmt2 % (key, var1, var2, var3, var4))


# HIV RATE
sub_copy['hcgroup4']=pd.qcut(sub_copy.hivrate,4,labels=["0% tile","25% tile","50% tile","75% tile"])

hc = sub_copy['hcgroup4'].value_counts(sort=False,dropna=False)

phc = sub_copy['hcgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

hc1=[] 
phc1=[] 
cf=0
cp=0
for freq in hc:
    cf=cf+freq
    hc1.append(cf)    
    pf=cf*100/len(sub_copy)
    phc1.append(pf)

print('HIV Rate with a High Suicide Rate')
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(hc.keys(),hc,phc,hc1,phc1)):
    print(fmt2 % (key, var1, var2, var3, var4))

# EMPLOYMENT RATE

def ecgroup4 (row):
    if row['employrate'] >= 32 and row['employrate'] < 51:
        return 1
    elif row['employrate'] >= 51 and row['employrate'] < 59:
        return 2
    elif row['employrate'] >= 59 and row['employrate'] < 65:
        return 3
    elif row['employrate'] >= 65 and row['employrate'] < 84:
        return 4
    else:
        return 5 

sub_copy['ecgroup4'] = sub_copy.apply(lambda row:  ecgroup4 (row), axis=1)        


ec = sub_copy['ecgroup4'].value_counts(sort=False,dropna=False)

pec = sub_copy['ecgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

ec1=[] 
pec1=[] 
cf=0
cp=0
for freq in ec:
    cf=cf+freq
    ec1.append(cf)    
    pf=cf*100/len(sub_copy)
    pec1.append(pf)

print('Employment Rate with a High Suicide Rate')
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(ec.keys(),ec,pec,ec1,pec1)):
    print(fmt2 % (key, var1, var2, var3, var4)) 
