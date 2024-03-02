def factorial(num):
    result = 1
    for i in range(num,0,-1):
        result*=i
    return result

def factorial2(num):
    result =1 
    for i in range(1,num+1):
        result*=i
    return  result  
    