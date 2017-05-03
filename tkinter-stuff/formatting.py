import datetime

'Floats: {:.2f}'.format(12.34567)
'Percentage: {:.2%}'.format(0.12345)
print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))
print("int: {0:d};  hex: {0:x};  oct: {0:o};   bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x}; oct: {0:#o};  bin: {0:#b}".format(42))
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


print('{2}{1}{0}'.format(*'abc'))        
#unpacking argument sequence
print('{0}{1}{0}'.format('aaaa', 'bb'))   # arguments' indices can be repeated

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
