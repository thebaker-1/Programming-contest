# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i,store):
            if len(store) == 4:
                all_elt = "".join(store)
                if len(all_elt) == len(s):
                    for ele in store:
                        if str(int(ele)) != ele or not(0 <= int(ele) <= 255):
                            break
                    else:
                        res.append(".".join(store[:]))
                return
            
            for j in range(i,len(s)):
                store.append(s[i:j+1])
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return res

        