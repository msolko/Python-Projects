#################################################################################
#                                   Roots                                       #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# CLASS:            MATH375                                                     #
# ASSIGNMENT:       Final Assignment                                            #
# INSTRUCTOR:       Dean Zeller                                                 #
# SEMESTER:         Spring 2019                                                 #
# SUBMISSION DATE:  April 27th, 2019                                            #
#                                                                               #
# DESCRIPTION:                                                                  #
# This program tests various methods of calculating the square root             #
# numerically. Then, it uses that to find the nth root of a number.             #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is (c) 2019 Maxwell Solko and Dean Zeller. This is original      #
# work, without use of outside sources.                                         #
#################################################################################
import random
import math

#################################################################################
# BABYLONIAN METHOD                                                             #
#                                                                               #
# The following is an implementation of the Babylonian method of calculating    #
# square roots numerically.  The formula is applied to the initial guess until  #
# either either an answer is found within the given tolerance, or the maximum   #
# number of iterations is reached.                                              #
#################################################################################
def babylonianMethod(S, x0, notate=False, NMAX=100, TOL=.000000001):
    "Babylonian method on square root"
    #INTRODUCTION
    if notate==True:
        print("Running Babylonian Method on",S,"with an initial guess of",x0)
        print("Side note: the answer is",math.sqrt(S))
        print()
    iterations, xn, absErr, relErr = 0,0,0,0
    #ALGORITHM
    if notate==True:
        print("Iteration   value       result      absolute error    relative error")
    for i in range(NMAX):
        xn = (x0+S/x0)/2
        absErr = abs(S-xn**2)
        relErr = absErr/S
        if notate==True:
            print("%5d       %-10f  %-10f  %-10f  %-8f" %(i, x0, xn, absErr, relErr)+"%")
        x0=xn
        if(relErr<TOL):
            if notate==True:
                print()
                print("After %d iterations, a solution of %f was found, with an error of %f" %(i, xn, relErr)+"%")
            return xn
    if notate==True:
        print()
        print("After %d iterations, no solution was found." %(NMAX))
        print("The final iteration yielded %f with an error of %f" %(xn, relErr)+"%")
    return xn



#################################################################################
# BAKHSHALI METHOD                                                              #
#                                                                               #
# The following is an implementation of the Bakhshali method of calculating     #
# square roots numerically.  The formula is applied to the initial guess until  #
# either either an answer is found within the given tolerance, or the maximum   #
# number of iterations is reached.                                              #
#################################################################################
def bakhshaliMethod(S, x0, notate=False, NMAX=100, TOL=.00000001):
    "Babkhshali method on square root"
    #INTRODUCTION
    if notate==True:
        print("Running Bakhshali Method on",S,"with an initial guess of",x0)

    #ALGORITHM
    iterations, xn, absErr, relErr = 0,0,0,0
    if notate==True:
        print("Iteration   value       result      absolute error    relative error")
    for i in range(NMAX):
        xn = (x0**2*(x0**2+6*S)+S**2)/(4*x0*(x0**2+S))
        absErr = abs(S-xn**2)
        relErr = absErr/S
        if notate==True:
            print("%5d       %-10f  %-10f  %-10f  %-8f" %(i, x0, xn, absErr, relErr)+"%")
        x0=xn
        if(relErr<TOL):
            if notate==True:
                print()
                print("After %d iterations, a solution of %f was found, with an error of %f" %(i, xn, relErr)+"%")
            return xn
    if notate==True:
        print()
        print("After %d iterations, no solution was found." %(NMAX))
        print("The final iteration yielded %f with an error of %f" %(xn, relErr)+"%")
    return xn


#################################################################################
# EXPONENTIAL IDENTITY                                                          #
#                                                                               #
# The following is an implementation of the exponential identity for            #
# calculating the square root of S numerically.  This is not an approximation,  #
# but a step-by-step implementation of the formula, illustrating that it works  #
# correctly.                                                                    #
#################################################################################
def exponentialIdentity(S, notate=False):
    "Exponential identity formula on square root"
    #INTRODUCTION
    if notate==True:
        print("Running Exponential Identity on",S)

    #Error Checking
    if(checkNegative(S)==True):
        return
    
    #ALGORITHM
    root = math.exp(.5*math.log(S))
    if notate==True:    
        print("the square root of %d is %f" %(S,root))
    return root


#################################################################################
# DIGIT BY DIGIT METHOD                                                         #
#                                                                               #
# This method seems like magic to most, but I am making a video to try to       #
# explain it.  Regardless, you find the highest number that squares into the    #
# the answer. Each digit of the answer corresponds to two digits of the         #
# question.  The whole premise of this method is based on expanding the square. #
# 12^2 = (10+2)(10+2) = 10^2 + 2(10*2) + 2^2                                    #
#################################################################################
def digitByDigit(S, notate=False, decimals=7):
    "Digit By Digit Method"
    #Error Checking
    if(checkNegative(S)==True):
        return
    if S==0:
        return 1
    if S==1:
        return 1
    deg = math.ceil((math.log(S,10))/2)
    answer, remainder = 0,0
    
    for i in range(deg+decimals):
        box = math.fmod(math.floor(S/(10**(2*math.floor(deg-i)-2))),100)
        remainder = remainder*100 + box
        for j in range(10):
            test = 9-j
            check = test**2 + 20*answer*test
            if((check) <= remainder):
                answer = answer*10+test
                remainder = remainder - check
                break
    answer = answer/(10**decimals)
    if notate==True:
        print("Final Answer:",answer)
    return answer



#################################################################################
# VEDIC DUPLEX METHOD                                                           #
#                                                                               #
# While the digit by digit method seems like magic to some, this method, which  #
# is a variant on the digit by didgit method, makes things a little trickier.   #
# the amount of accuracy is based on the amount of digits S has, and I haven't  #
# figured out a good way to make any number have at least X decimals.           #
#################################################################################

#Duplex method is the magic part of the vedic duplex method
def duplex(lst):
    tempList = []
    for i in range(len(lst)):
        tempList.append(lst[i]*lst[len(lst)-i-1])
    return sum(tempList)


def vedicDuplex(S, notate=False, decimals=5):
    "Vedic Duplex Method"
    # setting up all variables
    divisor, dividend, quotient, root, remainder, answer, dec = 1,0,0,0,0,0.0,0.0
    ansList, ansDup = [], []
    deg = math.floor((math.log(S,10)))+1
    boxes = math.ceil(deg/2)
    Slist = []
    offset= 1
    # SETTING UP S IN A LIST, DIGIT BY DIGIT
    # to get a specific amouont of decimals, we multiply S by 100 for each,
    # then divide by 10 for each once finished.
    if(boxes<decimals+1):
        S = S*(10**((decimals-boxes+1)*2))
        offset = 10**(decimals-boxes+1)
        if notate==True:
            print("S:",S)
            print("Offset:",offset)
    #then, remake deg and boxes
    deg = math.floor((math.log(S,10)))+1
    boxes = math.ceil(deg/2)
     
    temp = math.floor(S)
    for i in range(boxes*2):
        Slist.append(math.fmod(temp,10))
        temp = math.floor(temp/10)
    if notate==True:
        print("SLIST:",Slist)
    
    # ALGORITHM
    box = Slist.pop()*10 + Slist.pop()
    # finding the divisor
    for i in range(10):
        test = 9-i
        check = test**2 + 20*answer*test
        if((check) <= box):
            root = test
            divisor = 2*root
            ansList.append(root)
            remainder = box - check
            break
        
    # vedic duplex algorithm
    for i in range(len(Slist)):
        box = remainder*10 + Slist.pop()
        temp = box - duplex(ansDup)
        if notate==True:
            print("BOX:",box)
            print("BOX - DUPLEX:",temp)
        while(temp<0):
            ansDup.append(ansDup.pop()-1)
            box = box + divisor*10
            temp = box - duplex(ansDup)
        remainder = math.fmod(temp,divisor)
        if notate==True:
            print("REMAINDER:",remainder)
        ansDup.append(math.floor(temp/divisor))
    #formatting answer correctly
    for i in ansDup:
        ansList.append(i)
    for i in range(len(ansList)-boxes):
        dec = (dec + ansList.pop())/10
    for i in range(len(ansList)):
        answer = 10*answer+ansList[i]
    answer += dec
    answer = answer/offset
    if notate==True:
        print("ANSWER:",answer)
        print()
    return answer



#################################################################################
# Two Variable Iterative Method                                                 #
#                                                                               #
# This method approximates any square root when the square is between 0 and 3.  #
# This may sound dumb, but we can transform any number into binary, then        #
# divide out fours (or 10) until we get a number within the range.  Afterword,  #
# we multiply our answer by the amount of 4 we did, but this time with 2's      #
# since the square root of 4 is 2. This method compound errors, because errors  #
# will be muliplied by the amount of 4's we devided by, so it isn't that good.  #
#################################################################################

def twoVarIter(S, notate=False, NMAX=100, TOL=0.000000001):
    "Two Variable Iterative"
    #Error Checking
    if(checkNegative(S)==True):
        return
    
    count = 0
    while(S>2):
        S = S/4
        count+=1
    a = S
    c = S-1
    if notate==True:
        print("Iteration      A          C")
    for i in range(NMAX):
        a = a - a*c/2
        c = c*c*(c-3)/4
        if notate==True:
            print("%5f       %-10f %-10f" %(i,a,c))
        if(abs(S-a*a)<TOL):
            a=a*2**(count)
            if notate==True:
                print("After %d iterations, a solution of %f was found." %(i,a))
            return a
    a=a*2**(count)
    if notate==True:
        print("After %d iterations, the closest solution of %f was found." %(NMAX,a))
    return a





#################################################################################
# ITERATIVE METHOD FOR RECIPROCAL SQUARE ROOT METHOD                            #
#                                                                               #
# This method approximates the reciprocal, or 1/(square root).  This can be     #
# easier since no division is done. Be warned, as the initial guess can diverge #
# instead of converge if it is too far off from the actual answer.  It is       #
# recommended that other approximations are used first before using this method.#
#################################################################################

def iterRecip(S, x0, notate=False, NMAX=100, TOL = 0.00000001):
    "Iterative method for Reciprocal Square Roots"
    #Error Checking
    if(checkNegative(S)==True):
        return
    
    # Because every other function guesses the square root, I made this one
    # do that as well, and made the guess the reciprocal during the function
    x = 1/x0

    if notate==True:
        print("Iteration      1/ANSWER      ANSWER")
    for i in range(NMAX):
        x = (x/2)*(3-S*(x**2))
        ans = x*S
        if notate==True:
            print("%5d       %-10f %-10f" %(i,x,ans))
        if(abs(S-ans**2)<TOL):
            if notate==True:
                print("After %d iterations, a solution of %f was found." %(i,ans))
            return ans
    if notate==True:
        print("After %d iterations, the closest solution of %f was found." %(NMAX,ans))
    return ans
    

#################################################################################
# TAYLOR SERIES METHOD                                                          #
#                                                                               #
# This method approximates the square root using a taylor series.               #
#################################################################################

def taylor(S, x0, notate=False, depth=18, TOL=.00000001,NMAX=100):
    "Taylor Series Method"
    #Error Checking
    if(checkNegative(S)==True):
        return S
    
    n = x0
    d = 0
    count2 = 0
    series = 0
    while((abs(S-n**2)>TOL) and (count2<NMAX)):
        series = 0
        d = (S-n**2)
        # because d**i can get so large, I cap d to stop overflow errors
        if(d>10):
            d=10
        if(d<-10):
            d=-10
        if notate==True:
            print("D:",d)
        for i in range(1,depth):
            if notate==True:
                print(series)
            series += (((-1)**i)*math.factorial(2*i)*d**i)/((1-2*i)*math.factorial(i)**2*(4**i)*(n**(2*i)))
        series += 1
        n = series * n
        count2+=1
        if notate==True:
            print("ANSWER:",n)
            print()
        return n

        
#################################################################################
# CONTINUED FRACTION EXPANSION METHOD                                           #
#                                                                               #
# The continued fraction expansion is this equation:                            #
#                                                                               #
#                                (S-guess^2)                                    #
#           root(S) = guess + -----------------                                 #
#                             (guess + root(S))                                 #
#                                                                               #
# you then plug in the same equation for the root(S) in the denominator         #
# continuously, converging on the actual answer.  Recursive functions make this #
# easy to do if you know how to use recursive functions.                        #
#################################################################################

def conFraExp(S,x0, notate=False, depth=25):
    "Continued Fraction Expansion"
    #Error Checking
    if(checkNegative(S)==True):
        return
    
    r = S-x0**2
    exponentialIdentity(S)
    if notate==True:
        print("Depth     Answer")
    return cfrRecursion(S,x0,r,notate,depth)

def cfrRecursion(S,a,r,notate,d):
    if(d<1):
        return 0
    else:
        answer = a + r/(a+cfrRecursion(S,a,r,notate,d-1))
        if notate==True:
            print("%3d       %f" %(d,answer))
        return answer
    
#################################################################################
# PELL'S EQUATION METHOD                                                        #
#                                                                               #
# Pell's equation approximates a rational fraction close to the square root.    #
# The first step of finding appropriate starting values is the most dificult    #
# out of anything in these programs to do efficiently.  After that, it is just  #
# iterating a function, similar to babylonian or bakhshali methods.             #
# Note: this method only works for finding roots of integers.                   #
#################################################################################

def pell(S, notate=False, TOL=.000001):
    "Pell's Equation"
    #Error Checking
    if(checkNegative(S)==True):
        return
    if(S!=math.ceil(S)):
        if notate==True:
            print("Cannot work on decimal numbers")
        return 1
    listP = []
    listQ = []
    count = 0
    testP = S
    testQ = S
    func = 0
    if notate==True:
        print("P     Q     Sq^2-p^2")

    # This function works on all intergers except for 1 and 0,
    # so I made a catch for that.
    if(S==0):
        if notate==True:
            print("Square root of 0 is 0 you dummy.")
        return 0 
    if(S==1):
        if notate==True:
            print("Square root of 1 is 1 you dummy.")
        return 1
    
    # Finding intial values for the pell function
    if notate==True:
        print("Step 1: Finding initial values for the function.")
        print("------------------------------------------------")
    while(testQ>=0 and listP==[]):
        testP = 0
        func = 0
        while(func>=-1):
            func = S*testQ**2-testP**2
            if(abs(func)<=1):
                listP.append(testP)
                listQ.append(testQ)
                break
            testP += 1
        testQ += -1
        if (notate==True):
            print("%-5d %-5d %-5d" %(testP,testQ,func))
    if notate==True:
        print("Found proper initial values.  Finished with Step 1!")
        print()
    if listP[0]==0:
        print("The guessing method implemented for finding initial values could not find any proper values.")
        print("Please use a different method for %d" %(S))
        return 1
    if notate==True:
        print(listP, listQ)
    
    # Iterating the function to converge on the root
    if notate==True:
        print("Step 2: approximate better fractions for the root.")
        print("--------------------------------------------------")
        print("P           Q           P/Q         Error      ")
    answer = (listP[-1]/listQ[-1])
    while(abs(S-answer**2)>TOL):
        if notate==True:
            print("%-11d %-11d %-11f %-f" %(listP[-1],listQ[-1],answer,abs(S-answer**2)))
        testP = listP[0]*listP[-1] + S*listQ[0]*listQ[-1]
        testQ = listP[0]*listQ[-1] + listP[-1]*listQ[0]
        listP.append(testP)
        listQ.append(testQ)
        answer = (listP[-1]/listQ[-1])
    print(answer)
    return answer

#################################################################################
# CORDIC METHOD                                                                 #
#                                                                               #
# The CORDIC method is a bit of an anomaly.  CORDIC stands for:                 #
# COordinate Rotation DIgital Computer, which calculates various functions like #
# trig functions, or the square root, converging digit by digit, or bit by bit. #
# This method basically converts the number into binary, and tests each bit and #
# adds it to the answer if the answer squared is less than S.                   #
#################################################################################

def cordic(S, notate=False, TOL=.00000001):
    "CORDIC Method"
    #Error Checking
    if(checkNegative(S)==True):
        return
    if(S==0):
        if notate==True:
            print("Square root of 0 is 0 you dummy.")
        return 0 
    if(S==1):
        if notate==True:
            print("Square root of 1 is 1 you dummy.")
        return 1
    
    #Algorithm
    bits = 1.0
    answer = 0.0
    iterations = 0

    # this is finding the biggest value of n where 2^n<S
    if(S<1):
        while(S<=bits**2):
            bits = bits/2
        answer = bits
    elif(S>1):
        while(S>=bits**2):
            bits = bits*2
        answer = bits/2

    if notate==True:
        print("Iteration    Root")
    # for each iteration, we add the next bit if it doesn't make our answer bigger than S
    while(abs(S-(answer**2))>TOL):
        bits = bits/2
        if(((answer+bits)**2)<= S):
            answer += bits
        if notate==True:
            print("%5d        %-10f" %(iterations+1,answer))
        iterations += 1
    if notate==True:    
        print("The square root of %f approximation after %d iterations is %f" %(S,iterations,answer))
    return answer
    

    
#################################################################################
# QUALITY OF LIFE METHODS                                                       #
#                                                                               #
# These functions are just to make each other program not check for negative    #
# values of S, saving lines of code.                                            #
#################################################################################

def checkNegative(S):
    if S<0:
        print("%f is negative, there is no real square root!" %(S))
        return True

def goodPrint(S,answer,nRoot,iteration):
    anspow = answer**nRoot
    absError = abs(S-anspow)
    relError = absError/S
    print("%-16i%-13f%-13f%-13f%-13f"%(iteration,answer,anspow,absError,relError))

# These are used for finding the n'th root of a number.  I got the patterns from my excel sheet.
rootPatterns = [[],[],[1],[0,1],[0,1],[0,0,1,1],[0,1],[0,0,1],[0,0,1],[0,0,0,1,1,1],[0,0,1,1],[0,0,0,1,0,1,1,1,0,1,]]

#################################################################################
# N ROOT METHODS                                                                #
#                                                                               #
# These functions are the main show for my final project.  they find the nth    #
# root of a number by finding a specific pattern of square roots and multiplying#
# them together.  The first findNroot just uses the square root function of     #
# python, while the others use the square root method I implemented earlier.    #
#################################################################################


def findNroot(S,n, acc=0.00001):
    guess = 1
    count = 0
    root = S
    answer = math.pow(S,1/n)
    offset = 0
    temp = n
    rootPattern = rootPatterns[n]
    while(temp/2==temp//2 and temp!=1):
        offset+=1
        temp = temp/2
    for i in range(offset):
        root = math.sqrt(root)
    print("=================================================================")
    print("Finding the %f root of %f." %(n,S))
    print("Iteration   	Root         Root^Power   Abs Error    Rel Error")
    print("=================================================================")
    while(abs(guess-answer)>acc and count<=100):
        scalar = rootPattern[count%len(rootPattern)]
        root = math.sqrt(root)
        if scalar==1:
            guess = guess*root
        count += 1
        goodPrint(S,guess,n,count)
    print("Final Answer: ",guess)
    print("Actual Answer:",answer)

def findNroot2(S,n,func, acc=0.000001, *args):
    guess = 1
    count = 0
    root = S
    answer = math.pow(S,1/n)
    rootPattern = rootPatterns[n]
    #getting rid of the beginning offset
    offset = 0
    temp = n
    while(temp/2==temp//2 and temp>1):
        offset+=1
        temp = temp/2
    for i in range(offset):
        root = func(root,*args)
        count+=1
    print("=================================================================")
    print("Finding the %f root of %f." %(n,S))
    print("Method:",func.__doc__)
    print("Iteration   	Root         Root^Power   Abs Error    Rel Error")
    print("=================================================================")
    while(abs(guess-answer)>acc and count<50):
        scalar = rootPattern[count%len(rootPattern)]
        root = func(root,*args)
        if scalar==1:
            guess = guess*root
        count += 1
        goodPrint(S,guess,n,count)
    print("Final Answer: ",guess)
    print("Actual Answer:",answer)


def ndbd(S,nRoot=3,decimals=3,notate=False):
    fac = math.factorial
    deg = math.ceil((math.log(S,10))/nRoot)
    answer, remainder = 0,0
    if notate==True:
        print("=================================================================")
        print("Running Digit-By-Digit method on:", S)
        print("nth Root:",nRoot)
        print("Decimals:", decimals)
        print("Iteration   	Root         Root^Power   Abs Error    Rel Error")
        print("=================================================================")
    for i in range(deg+decimals):
        box = math.fmod(math.floor(S/(10**(nRoot*(deg-i-1)))),10**nRoot)
##        if notate==True:
##            print(deg-i)
        remainder = remainder*10**nRoot + box
        for j in range(10):
            test = 9-j
            check = 0
            for k in range(nRoot):
                check += (fac(nRoot)//fac(nRoot-k)//fac(k))*((10*answer)**k)*test**(nRoot-k)
            if((check) <= remainder):
                answer = answer*10+test
                tempAns = answer*10**(deg-i-1)
                goodPrint(S,tempAns,nRoot,i+1)
                remainder = remainder - check
##                if notate==True:
##                    print("Remainder:",remainder)
                break
    answer = answer/(10**decimals)
    if notate==True:
        print("Final Answer:",answer)
        print("Actual Root: ",math.pow(S,1/nRoot))
        print("-----------------------------------------------------------")
    return  answer

#################################################################################
#################################################################################
###                              MAIN PROGRAM                                ####
#################################################################################
#################################################################################
findNroot(420,5)
findNroot2(420,5, babylonianMethod, 0.0000001, 20,True)
findNroot2(420,5, bakhshaliMethod, 0.0000001, 20)
findNroot2(420,5, exponentialIdentity, 0.0000001)
findNroot2(420,5, digitByDigit, 0.0000001, 7)
findNroot2(420,5, vedicDuplex, 0.0000001)
findNroot2(420,5, twoVarIter, 0.0000001, 20)
findNroot2(420,5, iterRecip, 0.0000001, 20)
findNroot2(20,5, taylor, 0.0000001, 4)
findNroot2(420,5, conFraExp, 0.0000001, 2)
findNroot2(420,5, pell, 0.0000001)
findNroot2(420,5, cordic, 0.0000001, 20)
ndbd(420,5,5,True)








































