class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = set(nums)
        n1 = len(list)
        n2 = len(nums)

        if n1 == n2:
            return False
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna