from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        l=0
        p=len(nums)-1
        while l<p:
           if  nums[l]==nums[p] and abs(l-p)<=k:
                return True
           l+=1
        l=0
        
            
           
        return False
    
    
containsNearbyDuplicate(nums=[4,1,2,3,1,5],k=3)