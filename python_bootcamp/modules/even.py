def evenfunc(n):
    if n % 2 == 0:
        return "the number is even"
    else:
        return "the number is not even"


def evenrange(start,end):
    result=[]
    for num in range(start,end+1):
        if num % 2 ==0:
            result.append(num)
    return result


            
    
