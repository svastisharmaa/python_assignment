x=float(input('enter value'))
y=float(input('enter value'))

if x<0 or y<0:
    print('invalid value')
else:
    z=x%y
    if z>0:
        print ('not divisible')
    else:
        print('divisible')
