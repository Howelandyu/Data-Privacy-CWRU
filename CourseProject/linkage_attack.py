#build Levenshtein to get the distance (feature 1)
#date (feature 2)
#time(feature 3)
#JaccardC of the query terms (feature 4)
#
import pandas as pd
import numpy as np
from numpy import *
import main
# import textdistance
import numpy.matlib 


def levenshteinDistanceDP(token1, token2):
    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    printDistances(distances, len(token1), len(token2))
    return 0

def levenshteinDistanceDP(token1, token2):
    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()
        
def makeSchema():
    schema_list = pd.read_table('user-ct-test-collection-02.txt',sep='\t')
    # print(schema_list)
    # token_df=pd.DataFrame(columns=['token','date','time','distances','JaccardC'])
    # token_df['token']=schema_list['Query']
    # time_and_date=schema_list['QueryTime']
    # time=[]
    # date=[]
    # for i in time_and_date:
    #     i=i.split()
    #     date.append(i[0])
    #     time.append(i[1])
    # # print(time_and_date)
    # date=pd.DataFrame(date)
    # time=pd.DataFrame(time)
    # token_df['date']=date
    # token_df['time']=time
    # print(token_df)
    other_query_list=schema_list.head(10000)
    # print(type(other_query_list))
    query_list_1=other_query_list['Query'].tolist()
    query_list_2=other_query_list['Query'].tolist()
    # print(type(query_list_1))
    # distance_matrix=pd.DataFrame(header=None)

    # distance_score=np.zeros((50,50))
    # distance_score=[[0 for i in range(50)] for j in range(50)]
    distance_score=[]

    for i in query_list_1:
        # while q<=50:
        for j in query_list_2:
            distance_temp=levenshteinDistanceDP(i,j)
            # print(distance_temp)
            # for p in np.nditer(distance_score,op_flags = ['readwrite']):
            #     p=distance_temp
            # distance_score[p][q]=distance_temp
            distance_score.append(distance_temp)
    mean_distance=sum(distance_score)/len(distance_score)
    # print(mean_distance, flush=True)
    # print(distance_score, flush=True)






if __name__ == '__main__':
    distance = levenshteinDistanceDP("kelm", "hello")
    print(distance)
    # main.main()
    # makeSchema()