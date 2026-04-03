class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = slow_car = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            distanceTravel = (target - p) / s
            
            if distanceTravel > slow_car:
                result += 1
                slow_car = distanceTravel
        return result