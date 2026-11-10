# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

# Time Complexity: O(N) - each asteroid is pushed and popped from the stack at most once
# Space Complexity: O(N) - the stack can hold at most N asteroids (e.g. all moving right)
def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    stack = []
    for asterorid in asteroids:
        if asterorid > 0 or stack == []:
            stack.append(asterorid)
        else:
            absolute = abs(asterorid)
            isDis = False
            while len(stack) > 0 and stack[-1] > 0:
                if stack[-1] == absolute:
                    stack.pop()
                    isDis = True
                    break
                elif stack[-1] > absolute:
                    isDis = True
                    break
                else:
                    stack.pop()
            if isDis == False:
                stack.append(asterorid)
    return stack