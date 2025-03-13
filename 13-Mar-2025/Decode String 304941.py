# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def rec(i):
            word = []
            count = []
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    count.append(s[i])
                    i += 1
                    continue
                count_num = int("".join(count)) if count else 0
                if s[i] == "[":
                    sub_i,sub_word = rec(i+1)
                    for i in range(count_num):
                        word.extend(sub_word)
                    i = sub_i
                    count_num = 0
                    count = []
                else:
                    word.append(s[i])
                i+=1
            return i,word
        return "".join(rec(0)[1])
        