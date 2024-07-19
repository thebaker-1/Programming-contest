class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifting_arr = [0]* len(s)
        for start,end,direction in shifts:
            direction = 1 if direction == 1 else -1
            shifting_arr[start] += direction
            if end+1<len(s): shifting_arr[end+1] -= direction
        shifting_arr = (list(accumulate(shifting_arr)))
        s_list = list(s)
        for i,letter in enumerate(s_list):
            s_list[i] = chr(((ord(letter) - ord("a") + shifting_arr[i] )%26 +ord("a") ))
        return "".join(s_list)

