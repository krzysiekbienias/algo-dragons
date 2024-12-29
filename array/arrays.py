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



if __name__ == '__main__':
    high_five([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])


