class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleetStack = []

        for pos, spd in cars:
            print(pos, spd)
            time = (target -  pos) / spd

            if len(fleetStack) == 0:
                fleetStack.append(time)
            else:
                if time > fleetStack[-1]:
                    fleetStack.append(time)
        return len(fleetStack)

        
        