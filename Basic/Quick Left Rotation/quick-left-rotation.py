class Solution:
    def leftRotate(self, arr, k, n):
        # Your code goes here
        if k%n == 0:
            return arr
        for i in range(k%n):
            temp = arr.pop(0)
            arr.append(temp)
        return arr
            

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends