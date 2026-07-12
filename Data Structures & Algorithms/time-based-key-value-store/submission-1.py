class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value, timestamp))
        else:
            self.timeMap[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            return self.search(self.timeMap[key], timestamp)
        else:
            return ""

    def search(self, data:list, timestamp:int) -> str:
        l = 0
        r = len(data) -1
        res = ""
        
        while l <= r:
            m = (r + l) // 2
            
            if data[m][1] <= timestamp:
                l = m + 1
                res = data[m][0]
            else:
                r = m - 1
               
            
        return res

        
