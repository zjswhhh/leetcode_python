def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    
    result1 = []
    result2 = []

    cnt = 0
    
    for n in A:
        print(n)
        if cnt == len(A):
            break
        if n%2 != 0:
            result2.append(n)
        else:
            result1.append(n)
        cnt += 1
    
    return result1 + result2



a = [3,1,2,4]
print(sortArrayByParity(a))