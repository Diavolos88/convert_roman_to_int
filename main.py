class Solution:
    def getNumber(self, c):
        if (c == 'I'):
            return 1
        elif (c == 'V'):
            return 5
        elif (c == 'X'):
            return 10
        elif (c == 'L'):
            return 50
        elif (c == 'C'):
            return 100
        elif (c == 'D'):
            return 500
        elif (c == 'M'):
            return 1000
        else:
            return 0

    def romanTOInt(self, str):
        res = 0
        for i in range(len(number)):
            if (i + 1 == len(number) or self.getNumber(str[i]) >= self.getNumber(str[i + 1])):
                res += self.getNumber(str[i])
            else:
                res -= self.getNumber(str[i])
        return res

# 2956
number = "MMCMLVI"

print("res =", Solution().romanTOInt(number))