import sys
class Solution:
    def fib(self, n: int) -> int:
        self.n=n
        fib=[0,1]
        val=1
        length=len(fib)
        if self.n >=1:
            while length <= n:
                last_field=fib[-1]
                last_before_one=fib[-2]
                sum=last_field+last_before_one
                fib.append(sum)
                length=len(fib)
            return fib[n]
                
            
            
x=Solution()
print(x.fib(3)
