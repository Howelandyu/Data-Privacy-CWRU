import pandas as pd
import numpy as np
import main
import textdistance
import numpy.matlib 

def levenshtein_distance(string_1,string_2)
	size_1=len(string_1)+1
	size_2=len(string_2)+2
	matrix=np.zero((size_1,size_1))
	for i in range(size_1):
		matrix[i,0]=i
	for j in range(size_2):
		matrix[0,j]=j
	for i in range(1,size_1):
		for j in range(1,size_2):
			if string_1[i-1]==string[j-1]:
				matrix[i,j]=min(matrix[i-1,j-1],matrix[i-1,j]+1,matrix[i,j-1]+1)
			else:
				matrix[i,j]=min(matrix[i-1,j]+1,matrix[i-1,j-1]+1,matrix[i,j-1]+1)
	print(matrix)

def makeSchema():
    schema_list = pd.read_table('user-ct-test-collection-02.txt',sep='\t')

    print(distance_score, flush=True)

if __name__ == '__main__':
	levenshtein_distance()
    # main.main()
    # makeSchema()