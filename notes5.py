def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
num=5
print(factorial(num))  


# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)  #stop here
# 5*4*3*2*1*factorial(0)
# 5x4x3x2x1x0xfactorial(-1)