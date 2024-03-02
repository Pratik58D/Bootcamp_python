def oddfunc(n):
    if n % 2 !=0:
        print("this is odd number")
    else:
        print("this is not odd number")

def rangeodd(firstnum,lastnum):
    result =[]
    for num in range(firstnum,lastnum+1):
        if num % 2!= 0:
            result.append(num)
    return result