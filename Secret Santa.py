#################################################################################
#                           Secret Santa Permutations                           #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# Date:             1/28/2021                                                   #
#                                                                               #
# DESCRIPTION:                                                                  #
# This program tests how many valid ways of doing a secret santa with N people. #
# In the list, index 0 says who person 0 gets a gift for, 1 gifts index 1, etc. #
# Later added functionality to do a secret santa.                               #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is (c) 2020 Maxwell Solko. This is original                      #
# work, without use of outside sources.                                         #
#################################################################################
import itertools
import math
import random

# Making a list with n people in it
def nlist(n):
    temp = []
    for i in range(n):
        temp.append(i)
    return temp

#################################################################################
#                               Checking Permutations                           #
# These functions check a certain permutation in various ways.                  #
# It started  with just seeing if people would gift themselves, but I added     #
# other functions that account for people being in relationships and not        #
# wanting to have them be their secret santa.                                   #
#################################################################################

# Checks whether anyone is giving gifts to themselves
def permCheck1(lst):
    for i in range(len(lst)):
        if(lst[i]==i):
            return False
    return True

# Checks whether anyone is giving gifts to themselves or their partner.
# This assumes that 0 is with 1, 2 is with 3, etc.
# For odd numbers of people, the last person is single
def permCheck2(lst):
    for i in range(len(lst)):
        if (i%2==0):
            if((lst[i]==i) or (lst[i]==i+1)):
                return False
        else:
            if((lst[i]==i) or (lst[i]==i-1)):
                return False
    return True

# Checks for gifting themselves or partners, but not everyone has to be partners
# extra input delineates where partners end and singles start
# this is the number of relationships, assuming relations are at the start
# Due to variability, harder to test numerous group numbers without hard coding
# you could make a list which the for loop uses to find the deliniation each loop
def permCheck3(lst, numRelationships):
    for i in range(len(lst)):
        if(i<numRelationships*2): #if in partner area, do permcheck2
            if (i%2==0):
                if((lst[i]==i) or (lst[i]==i+1)):
                    return False
            else:
                if((lst[i]==i) or (lst[i]==i-1)):
                    return False

        else: #If we are in singles, do permcheck1
            if(lst[i]==i):
                return False
    return True

#################################################################################
#                               Testing percent chance                          #
# These functions are for if you want to actually do a secret santa.            #
# We pick a random permutation, check if it's legal, then save it.              #
# In the shell you can ask who got who.                                         #
#################################################################################
                
# This function was for when I was testing the percent chance of getting a good
# secret santa with n people (also relationships if added)
# Printing Format
def goodPrint(n,legalList):
    nlst = math.factorial(n)
    perLegal = legalList/nlst
    print("%-13i%-11i%-11i%-15f"%(n,nlst,legalList,perLegal))

#################################################################################
#                                Testing permChecks                             #
#################################################################################
##print("=================================================================")
##print("N            Total      Legal      %Legal")
##print("=================================================================")
# testing permcheck1 or 2 for up to N people
##for i in range(10):
##    temp = 0
##    #Making a list of all permutations of N people
##    plst = list(itertools.permutations(nlist(i+1)))
##    for k in range(len(plst)):
##        temp = permCheck2(plst[k],temp)
##    goodPrint(i+1,temp)
##
### testing permcheck3 for 'groupNum' people with 'relationNum' relationships
##groupNum = 8
##relationNum = 2
##
##temp = 0
###Making a list of all permutations of N people
##plst = list(itertools.permutations(nlist(groupNum)))
##for k in range(len(plst)):
##    temp = permCheck3(plst[k],temp, relationNum)
##goodPrint(groupNum,temp)

#################################################################################
#                               Making a Secret Santa                           #
# This class is for if you want to actually do a secret santa.                  #
# We pick a random permutation, check if it's legal, then save it.              #
# In the shell you can ask who got who, or redo the list.                       #
#################################################################################

class SecretSanta():

    def __init__(self, people=[], target=[], relations = 0):
        self.people=people
        self.gift_targets = target
        self.relations = relations
        self.secret_santa = {}
        
# Simple get functions for bug fixing usually
    def get_people(self):
        return self.people

    def get_gift_targets(self):
        return self.gift_targets

# Printing out people and maybe who they got
    def list_index(self):
        print("#:  Name")
        for i in range(len(self.people)):
            print("%-4i%s"%(i, self.people[i]))
        return
    
    def who_got_who(self, person):
        giftee = self.secret_santa[person]
        print("{} is giving {} a gift.".format(person, giftee))
        return

    def who_got_who_full(self):
        for i in self.people:
            self.who_got_who(i)
        return
            
# Setting up the secret santa
    def set_people_manual(self, newPeople):
        self.people = newPeople
        return

    def set_secret_santa(self):
        if self.gift_targets == []:
            self.set_gift_targets()
        temp = []
        for i in self.gift_targets:
            temp.append(self.people[i])
        self.secret_santa = {gifter:giftee for gifter, giftee in zip(self.people,temp)}
        return

    # You can repeat this step if you don't like the final product.
    def set_gift_targets(self):
        # Checking if there is a list to make targets
        if self.people == []:
            self.set_people()
    ##### Finding a legal secret santa orientation ######
        good_list = False
        secret_santa_list = []
        #Making a list of all permutations of groupNum people
        perm_list = list(itertools.permutations(list(range((len(self.people))))))
        while good_list == False:
            rand_list = random.randint(0,len(perm_list)-1) #picking a random secret santa list
            good_list = permCheck3(perm_list[rand_list], self.relations) #Checking if the list is right
        self.gift_targets = perm_list[rand_list]
        return

    def set_people(self):
        print("Welcome to secret santa!")
    #### finding out how many people are participating ####
        while True:
            while True:
                try:
                    numGroup = int(input("How many people are participating? "))
                    break
                except ValueError:
                    print("That wasn't a number silly. Try again")
            if numGroup > 2:
                break
            print("you can't do a secret santa with 2 or fewer people...")
                
        while True:
            while True:
                try:
                    print("How many people are in a relationship with other people in the group?")
                    numRelations = int(input("They don't want to get each other for secret santa. Even Number:"))
                    break
                except ValueError:
                    print("That wasn't a number silly. Try again")
            if (numRelations <= numGroup):
                self.relations = numRelations//2 #If an odd number is input, it gets rounded down
                break
            print("There should be more people in the group than people in relationships!")
    ##### making a list of all participants #####
        nameList = []
        if self.relations>0:
            print("Please list the lovebirds that are partaking in secret santa.")
            print("Please put the people in by relationship")
            yn = "n"
            while yn == "n": #Putting in the people in relationships
                for i in range(self.relations*2):
                    nameList.append(input("Name: "))
                for i in range(self.relations):
                    print(nameList[i*2] + " is with " + nameList[i*2+1])
                yn = input("Is this right? y/n: ")
                if yn== "n" :
                    print("Please put people in right after the person they are with. Try Again")
                    nameList = []
            if numGroup > numRelations:
                print("Now put in everyone else, in any order")
        else:
            print("Please list the names of everyone involved in the secret Santa.")
        for i in range(numGroup-self.relations*2):
            nameList.append(input("Name: "))
        print("Here is your list of participants")
        for i in nameList:
            print(i)
        self.people = nameList
        return
