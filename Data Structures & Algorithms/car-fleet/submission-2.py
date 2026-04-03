class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = slow_car = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            NewSlowCar = (target - p) / s
            
            if NewSlowCar > slow_car:
                result += 1
                slow_car = NewSlowCar
        return result