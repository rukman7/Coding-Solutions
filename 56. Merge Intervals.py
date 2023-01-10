class Solution:
    #def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        merged = []
        
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,4],[2,3]]))
