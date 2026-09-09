# koko eating banana 
# piles = [3,6,7,11], h = 8 -> 4 (minimum speed to eat all bananas in h hours, here she can eat 4 bananas per hour)
# piles = [30,11,23,4,20], h = 5 -> 30
# piles = [30,11,23,4,20], h = 6 -> 23
import math 


def hourTaken(piles:list[int], n:int) -> int:
    ans = 0 
    for pile in piles:
        ans += math.ceil(pile / n) 
    return ans 

def minEatingSpeed(piles: list[int], h: int) -> int:
    low = 1 
    high = max(piles) 
    while low <= high:
        mid = low + (high - low) // 2 
        hour_taken = hourTaken(piles, mid) 
        if hour_taken > h:
            low = mid + 1 
        else:
            high = mid - 1 
    return low 


print(minEatingSpeed([82,37], 6)) 