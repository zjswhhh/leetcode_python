def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    length = 1
    length_num = 9
    
    while n > length * length_num:
        n -= length*length_num
        length += 1
        length_num *= 10
        # print(length, length_num)
        
    index = int((n-1) / length)
    sub_index = (n-1) % length 

    # print(index, sub_index)
    
    num = index + pow(10, length-1)

    # print(num)
    
    return int(str(num)[sub_index])


a = 3
print(findNthDigit(a))