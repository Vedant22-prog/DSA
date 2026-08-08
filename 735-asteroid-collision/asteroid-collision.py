class Solution(object):
    def asteroidCollision(self, asteroids):

        stack = []

        for asteroid in asteroids:

            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < -asteroid:
                    stack.pop()
                    continue

                elif stack[-1] == -asteroid:
                    stack.pop()

                break

            else:
                stack.append(asteroid)

        return stack