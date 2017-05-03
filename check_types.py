types = ['hallo',4,'4',4.0,'4.00']
for i in types:
    print(i,'\t',end='')
    try:
        # Check of het een integer is 
        i = int(i)
        print('int')
    except ValueError:
        try:
            # Check of het een float is
            fl = float(i)
            print('float')
        except ValueError:
            # Dan is het een string
            print('string')