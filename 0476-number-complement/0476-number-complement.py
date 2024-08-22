class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        for i in bin(num)[2:]:
            if int(i):
                binary.append("0")
            else:
                binary.append("1")
        binary = (("").join(binary))[::-1]
        sum = 0
        for i in range(len(binary)):
            sum +=int(binary[i])*(2**(i))
        return sum
        