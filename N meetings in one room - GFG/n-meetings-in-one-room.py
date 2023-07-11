#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        ans = []
        for i in range(n):
            ans.append((end[i], start[i]))

        ans.sort()
        cnt = 1
        i = 0
        j = 1
        while j < n:
            if ans[j][1] > ans[i][0]:
                cnt += 1
                i = j
                j += 1
            else:
                j += 1
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends