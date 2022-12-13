D={'BMW':'1111','Lamba':'0241'}
if D.get('BMW', False) != False:
    print('True') 
else:
    print('False')
print(D.get('BMW'))
D['Porshe']='129429'
print(D)