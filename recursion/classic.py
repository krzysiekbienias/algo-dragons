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

def sum_of_digits(n: int) -> int:
    # there is also iterative version->number theory

    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# from AlgoExpert
def product_sum(array,depth=1):
    total_sum=0
    for el in array:
        if isinstance(el,list):
            total_sum=product_sum(el,depth+1)
        else:
            total_sum+=el
    return total_sum*depth


if __name__ == '__main__':
    print(get_nth_fib(5))