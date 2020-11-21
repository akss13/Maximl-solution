#!/usr/bin/env python3
# -*- coding: utf-8 -*
from collections import defaultdict as dd

def findSmallestSubstring(S):  
    countOfCharacters = dd(lambda: 0)
    # count distinct elements of S
    distinctCharacters = len(set([s for s in S])) 
    stringLength = len(S) 
    count = 0
    start = 0
    oldStart = 0
    minimumLength = stringLength 
    # for every character in string
    for i in range(stringLength): 
        countOfCharacters[S[i]] += 1
        # count number of elements in string
        if countOfCharacters[S[i]] == 1: 
            count += 1
        # if count is qualt to number of distinct elememts, 
        # we reducing the substring length by checking countOfCharacters 
        if count == distinctCharacters: 
            while countOfCharacters[S[start]] > 1: 
                if countOfCharacters[S[start]] > 1: 
                    countOfCharacters[S[start]] -= 1
                start += 1
            substringLength = i - start + 1
            # replace minimumLength when substringLength is lesser
            if minimumLength > substringLength: 
                minimumLength = substringLength  
                oldStart = start 
    return str(S[oldStart: oldStart + minimumLength]) 

if __name__=='__main__':        
    print(len(findSmallestSubstring(input())))