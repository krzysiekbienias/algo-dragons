def flatten(arr: list) -> list:
    result_arr=[]
    for el in arr:
        if isinstance(el,list):
            result_arr.extend(flatten(el))
        else:
            result_arr.append(el)
    return result_arr

def get_nth_fib(n, lookup=None):
    lookup ={} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        lookup[n]= get_nth_fib(n - 1, lookup) + get_nth_fib(n - 2, lookup)
        return lookup[n]
# from algo ekspert
def permutations(arr: list) -> list:
    pass



if __name__ == '__main__':
    print(get_nth_fib(5))