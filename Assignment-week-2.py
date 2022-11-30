import pandas as pd
import numpy as np

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
bc = sub_copy['breastcancerper100th'].value_counts(sort=False,bins=10)


pbc = sub_copy['breastcancerper100th'].value_counts(sort=False,bins=10,normalize=True)*100


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
fmt1 = '%s %7s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('# of Cases','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(bc.keys(),bc,pbc,bc1,pbc1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))


# HIV RATE
hc = sub_copy['hivrate'].value_counts(sort=False,bins=7)


phc = sub_copy['hivrate'].value_counts(sort=False,bins=7,normalize=True)*100


# cumulative frequency and cumulative percentage for HIV rate with a high suicide rate
hc1=[] 
phc1=[] 
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    hc1.append(cf)    
    pf=cf*100/len(sub_copy)
    phc1.append(pf)


print('HIV Rate with a High Suicide Rate')
fmt1 = '%5s %12s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(hc.keys(),hc,phc,hc1,phc1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))


# EMPLOYMENT RATE
ec = sub_copy['employrate'].value_counts(sort=False,bins=10)


pec = sub_copy['employrate'].value_counts(sort=False,bins=10,normalize=True)*100


ec1=[] 
pec1=[] 
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    ec1.append(cf)    
    pf=cf*100/len(sub_copy)
    pec1.append(pf)


print('Employment Rate with a High Suicide Rate')
fmt1 = '%5s %12s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(ec.keys(),ec,pec,ec1,pec1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))

# END
