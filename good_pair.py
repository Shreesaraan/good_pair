def good_pair(A,B):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==B:
                return 1
    return 0
            
A=list(map(int,input("Enter the array elements: ").split()))
B=int(input("Enter the sum to find: "))
print(good_pair(A,B))