# Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

#User function Template for python3

def rotate(matrix): 
#code here
	n=len(matrix)
	# matrix2=[[None for i in range(0,n)] for j in range(0,n)]
	for i in range(0,n):
		for j in range(i,n):
			matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
	i=0
	h=(n-1)//2
	while i<=h:
		print(matrix[i])
		print(matrix[n-1-i])
		matrix[i],matrix[n-1-i]=matrix[n-1-i],matrix[i]
		i+=1

	return matrix


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends