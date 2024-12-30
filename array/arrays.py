from typing import List


def top_five_average(marks, threshold=5):
    return sum(marks[:threshold]) // threshold

def high_five(items: List[List[int]]) -> List[List[int]]:
    performance_dict = {}
    results=[]
    for item in items:
        if item[0] not in performance_dict:
            performance_dict[item[0]] = [item[1]]
        else:
            performance_dict[item[0]].append(item[1])
    for key in performance_dict:
        performance_dict[key].sort(reverse=True)
        results.append([key,top_five_average(performance_dict[key])])
    results_sorted=sorted(results,key=lambda x:x[0])
    return results_sorted

def kth_largest_element_in_array(array: List[int], k: int) -> List[int]:
    # version with sorting is in heap/challenges module
    array = sorted(array, reverse=True)
    return array[:k-1]

#AlgoExpert
def tournament_winner(competitions, results):
    table=dict()
    for teams in competitions:
        for name in teams:
            table[name]=0
    for competition,outcome in zip(competitions,results):
        winner=get_winner(competition,outcome)
        table[winner]+=3
    league_winner=max(table,key=table.get)
    return league_winner

def get_winner(teams, result):
    if result ==0:
        return teams[1]
    else:
        return teams[0]

# i don't know from which side it comes from.
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    l = 0
    p = len(nums) - 1
    while l < p:
        if nums[l] == nums[p] and abs(l - p) <= k:
            return True
        l += 1
    l = 0

    return False





if __name__ == '__main__':
    high_five([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])


