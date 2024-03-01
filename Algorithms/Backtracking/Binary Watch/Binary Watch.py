class Solution:
    def readBinaryWatch(self, turnedOn: int):
        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans      
    
# Time complexity  : O(12 * 60)
# Space complexity : O(12 * 60)    
# turnedOn : the number of LED lights are on. 
#            also the number of 1s in binary.
# bin()    : function to convert number into a binary.
# count()  : function to count the numbers of 1 ()
   
ans = Solution().readBinaryWatch(1)   
print(ans)