class Solution:
    def intToRoman(self, num: int) -> str:
        # num = [int(num/1000), int(num/100)%10,int(num/10)%10,num%10]
        symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = ''
        for i in range(len(symbol)):
            ans += symbol[i]*int(num/value[i])
            num %= value[i]
        return ans