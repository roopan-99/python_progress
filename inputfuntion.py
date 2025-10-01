def add_num(a,b):
    return a+b
def mul_num(a,b):
   return a*b
def div_num(a,b):
    return a/b

#a1 = int(input("Enter thre number: "))
#a2 = int(input("Enter thr second number: "))
sum = add_num(23,50)
mul = mul_num(2,3)
div = div_num(100,2)

print (sum)
print (mul)
print (div)

def cla(*args):
    for helo in args():
        print(helo)
cla(2,6,7,8,2)