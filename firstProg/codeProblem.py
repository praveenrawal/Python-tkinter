# cook your dish here
c=13
c_bin=bin(c).replace("0b", "")
if c_bin[0]=='1':
    a='1'
    b='0'
for i in range(1,len(c_bin)):
    if c_bin[i]=='0':
        a=a+'1'
        b=b+'1'
    else:
        a=a+'0'
        b=b+'1'
a=int(a,2)
b=int(b,2)
print(a,b)


