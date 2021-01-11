#################################################################################
#                           Secret Santa Permutations                           #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# Date:             1/11/2021                                                   #
#                                                                               #
# DESCRIPTION:                                                                  #
# This program tests how many valid ways of doing a secret santa with N people. #
# In the list, index 0 says who person 0 gets a gift for, 1 gifts index 1, etc. #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is (c) 2020 Maxwell Solko. This is original                      #
# work, without use of outside sources.                                         #
#################################################################################
import itertools
import math

# Making a list with n people in it
def nlist(n):
    temp = []
    for i in range(n):
        temp.append(i)
    return temp

# Checks whether anyone is giving gifts to themselves
def permCheck1(lst,legalList):
    for i in range(len(lst)):
        if(lst[i]==i):
            return legalList
    legalList+=1
    return legalList

# Checks whether anyone is giving gifts to themselves or their partner.
# This assumes that 0 is with 1, 2 is with 3, etc.
# For odd numbers of people, the last person is single
def permCheck2(lst, legalList):
    for i in range(len(lst)):
        if (i%2==0):
            if((lst[i]==i) or (lst[i]==i+1)):
                return legalList
        else:
            if((lst[i]==i) or (lst[i]==i-1)):
                return legalList
    legalList+=1
    return legalList

# Checks for gifting themselves or partners, but not everyone has to be partners
# extra input delineates where partners end and singles start
# this is the number of relationships, assuming relations are at the start
# Due to variability, harder to test numerous group numbers without hard coding
# you could make a list which the for loop uses to find the deliniation each loop
def permCheck3(lst, legalList, numRelationships):
    for i in range(len(lst)):
        if(i<numRelationships*2): #if in partner area, do permcheck2
            if (i%2==0):
                if((lst[i]==i) or (lst[i]==i+1)):
                    return legalList
            else:
                if((lst[i]==i) or (lst[i]==i-1)):
                    return legalList

        else: #If we are in singles, do permcheck1
            if(lst[i]==i):
                return legalList
    legalList+=1
    return legalList
                

# Printing Format
print("=================================================================")
print("N            Total      Legal      %Legal")
print("=================================================================")
def goodPrint(n,legalList):
    nlst = math.factorial(n)
    perLegal = legalList/nlst
    print("%-13i%-11i%-11i%-15f"%(n,nlst,legalList,perLegal))


#######################Testing things######################################
# testing permcheck1 or 2 for up to N people
for i in range(10):
    temp = 0
    #Making a list of all permutations of N people
    plst = list(itertools.permutations(nlist(i+1)))
    for k in range(len(plst)):
        temp = permCheck2(plst[k],temp)
    goodPrint(i+1,temp)

# testing permcheck3 for 'groupNum' people with 'relationNum' relationships
groupNum = 8
relationNum = 2

temp = 0
#Making a list of all permutations of N people
plst = list(itertools.permutations(nlist(groupNum)))
for k in range(len(plst)):
    temp = permCheck3(plst[k],temp, relationNum)
goodPrint(groupNum,temp)

