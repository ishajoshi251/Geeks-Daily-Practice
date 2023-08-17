class Solution:
    def print_next_greater_freq(self,arr,n):
        # code here
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(arr[i])
                continue
            else:
                while stack and d[arr[i]]>=d[stack[-1]]:
                    stack.pop()
                if not stack:
                    stack.append(arr[i])
                else:
                    ans[i] = stack[-1]
                    stack.append(arr[i])
        return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends