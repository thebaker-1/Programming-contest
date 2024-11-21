class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        i = 0 
        count = 0
        string = str(num)
        for j in range(k-1,len(str(num))):
            substring = int(string[i:j+1])
            if substring and not(num%substring):
                count+=1
            i+=1
        return count

            
        