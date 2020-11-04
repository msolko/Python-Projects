#################################################################################
#                           Secret Santa Permutations                           #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# Date:             11/4/2020                                                   #
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
        temp.append(i+1)
    return temp

# Checks whether anyone is giving gifts to themselves
def permCheck(lst,legalList):
    for i in range(len(lst)):
        if(lst[i]==i+1):
            return legalList
    legalList+=1
    return(legalList)

# Printing Format
print("=================================================================")
print("N            Total      Legal      %Legal")
print("=================================================================")
def goodPrint(n,legalList):
    nlst = math.factorial(n)
    perLegal = legalList/nlst
    print("%-13i%-11i%-11i%-15f"%(n,nlst,legalList,perLegal))


for i in range(11):
    leef = 0
    #Making a list of all permutations of N people
    plst = list(itertools.permutations(nlist(i+1)))
    for k in range(len(plst)):
        leef = permCheck(plst[k],leef)
    goodPrint(i+1,leef)

#######################Testing things######################################
##temp=list(itertools.permutations(nlist(3)))
##legalList=0
##print(temp)
##for i in range(len(temp)):
##    legalList = permCheck(temp,legalList)
##    print(temp[i], legalList)

##temp=list(itertools.permutations(nlist(3)))[3]
##print(temp)
##leef =0
##leef = permCheck(temp,leef)
##print(leef)
