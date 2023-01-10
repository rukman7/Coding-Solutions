class Solution:
    #def subsets(self, nums: List[int]) -> List[List[int]]:
    #Input: nums = [1,2,3]
    #Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    def subsets(self, nums):
        
        def dfs(index, res):
            if index >= len(nums):
                output.append(res)
                return
            
            dfs(index + 1, res + [nums[index]])

            dfs(index + 1, res)

        output = []
        dfs(0, [])
        return output


if __name__ == "__main__":
    sol = Solution()
    output = sol.subsets([1,2,3])
    print(output)
