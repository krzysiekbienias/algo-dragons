# find n-thprime number
import math
from typing import List
def is_prime(n:int)->bool:
    """is_prime
    Description
    -----------
    

    Parameters
    ----------
    num : int
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if (n<=1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
            
     


# function to return nth prime number

def nth_prime_number(num:int)->int:
    value=1
    prime_number_counter=0
    while prime_number_counter!=num:
        value+=1
        if is_prime(value):
            prime_number_counter+=1
    return value


def sieve_of_eratosthenes(n:int)->List[int]:
    """sieve_of_eratosthenes
    Description
    -----------
    Function returns prime numbers up to given limit.


    Parameters
    ----------
    n : int

    Returns
    -------
    _type_
        _description_
    """
    is_prime_list=[True]*(n+1)
    is_prime_list[0]=False
    is_prime_list[1]=False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if is_prime_list[i]:         
            for j in range(i*i,n+1,2*i if i!=2 else i):
                is_prime_list[j]=False
    return [i for i in range(n+1) if is_prime_list[i]]
    
