class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ttf = [] # time to finish
        fleets = 0
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            ttf.append((position[i], time))
        ttf.sort()
        fleet_time = float('-inf')
        for i in range(len(ttf) - 1, -1, -1):
            if fleet_time < ttf[i][1]:
                fleets += 1
                fleet_time = ttf[i][1]
        return fleets