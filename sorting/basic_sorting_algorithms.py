def insertion_sorting(array):
    #cards analogy
    for i in range(1,len(array)):
        j=i
        while j>0 and array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j-=1


def merge(left_array,right_array):
    l,r,res=0,0,[]
    while l<len(left_array) or r<len(right_array):
        al=left_array[l] if l<len(left_array) else float('inf')
        br=left_array[l] if l<len(left_array) else float('inf')
        if al<br:
            res.append(al)
            l+=1
        else:
            res.append(br)
            r+=1
        return res

def merge_sort(array):
    if len(array)<=1:
        return array
    l=merge_sort(array[:len(array)//2])
    r=merge_sort(array[len(array)//2:])
    return merge(l,r)



if __name__=='__main__':
    test_array=[3,1,5,6,7,2]
    insertion_sorting(array=test_array)
    print(test_array)