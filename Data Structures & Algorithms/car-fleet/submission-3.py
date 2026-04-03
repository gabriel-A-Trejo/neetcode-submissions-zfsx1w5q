class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carfleet = slowCar = 0


        for p, s in sorted(zip(position, speed), reverse=True):
            currentCarTime = (target - p) /s
            if currentCarTime > slowCar:
                carfleet += 1
                slowCar = currentCarTime
        return carfleet