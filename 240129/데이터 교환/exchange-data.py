a,b,c = 5,6,7

temp_b, temp_c = b, c
b = a
c = temp_b
a = temp_c

# b=a
# c=b 
# a=c
print(a,'\n',b,'\n',c, sep='')