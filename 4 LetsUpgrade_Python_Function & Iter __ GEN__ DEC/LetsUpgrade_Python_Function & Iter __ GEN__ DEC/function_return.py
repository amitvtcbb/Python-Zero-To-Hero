def get_Sum(lst):
    """
    This function return the sum of all the element in a list

    :param lst:
    :return:
    """
    _sum = 0
    for num in lst:
        _sum = _sum + num
    return _sum

s = get_Sum([1,2,3,4,5])
print(s)