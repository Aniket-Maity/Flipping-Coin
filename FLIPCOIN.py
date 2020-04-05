# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:25:05 2020

@author: Aniket Maity
"""

'''There are N coins kept on the table, numbered from 0 to N - 1. Initially, each coin is kept tails up. You have to perform two types of operations:

1) Flip all coins numbered between A and B inclusive. This is represented by the command "0 A B"

2) Answer how many coins numbered between A and B inclusive are heads up. This is represented by the command "1 A B".

Input :

The first line contains two integers, N and Q. Each of the next Q lines are either of the form "0 A B" or "1 A B" as mentioned above.

Output :

Output 1 line for each of the queries of the form "1 A B" containing the required answer for the corresponding query.

Sample Input :
4 7
1 0 3
0 1 2
1 0 1
1 0 0
0 0 3
1 0 3 
1 3 3

Sample Output :
0
1
0
2
1

Constraints :
1 <= N <= 100000
1 <= Q <= 100000
0 <= A <= B <= N - 1 '''

def flipCoinQuery(listData):
    for i in range(listData[0],listData[1]+1):
        coinArr[i] = int(not(coinArr[i]))
    return coinArr

def headsUpCount(listData):
    count = 0
    for i in range(listData[0],listData[1]+1):
        if coinArr[i] == 1:
            count+=1
    print(count)
'''
1 0 3
0 1 2
1 0 1
1 0 0
0 0 3
1 0 3 
1 3 3'''
def main():
    coinArr = [0] *4
    quary = [
            [1, 0, 3],
            [0, 1, 2],
            [1, 0, 1],
            [1, 0, 0],
            [0, 0, 3],
            [1, 0, 3], 
            [1, 3, 3],
            ]
    for element in quary:
        if(element[0]==0):
            coinArr = flipCoinQuery(element[1:])
        else:
           headsUpCount(element[1:]) 

if __name__== '__main__':
    main()