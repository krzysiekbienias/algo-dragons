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





# Tournament Winner
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

# move element to end


if __name__ == '__main__':
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results=[0,0,1]
    tournament_winner(competitions, results)
    containsNearbyDuplicate(nums=[4, 1, 2, 3, 1, 5], k=3)
