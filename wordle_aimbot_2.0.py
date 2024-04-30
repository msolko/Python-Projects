#################################################################################
#                               Wordle Help                                     #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# Date:             09/01/2022                                                  #
#                                                                               #
# DESCRIPTION:                                                                  #
# Stuck on wordle? This program can give insight to possible words to use!      #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is (c) 2022 Maxwell Solko. Wordle owrd list obtained from        #
# https://github.com/tabatkins/wordle-list/blob/main/words.                     #
# This is original work, without use of outside sources.                        #
#################################################################################
import time
import statistics
wordle_list_file = open("wordle_words.txt", "r") #get the 5 letter words
wordle_list = wordle_list_file.readlines() #read in them to a list
wordle_list = [x.strip() for x in wordle_list] #cut out the \n
first_guess = 'later' #hard code the first guess as LATER. went through tests to find this guess
correct_wordle = 'prowl' #Need to change this to whatever the word of the day is 
wrong_letters = '' #empty string to add letters to
green_letters = [0,0,0,0,0] #which letters have correct guesses. Initiate with all 0's
incorrect_spots = [[],[],[],[],[]] #this is representing the 'yellow' guesses, or letters that are in the word but incorrect spot.
def find_best_letters(word_list = wordle_list):
    # the letter list is like this instead of alphabetical because it is by popularity.
    # having the list like this decreased the average guess count by .02, so slightly better?
    letter_list = ['s', 'e', 'a', 'o', 'r', 'i', 'l', 't', 'n', 'u', 'd', 'y', 'c', 'p',
                   'm', 'h', 'g', 'b', 'k', 'f', 'w', 'v', 'z', 'j', 'x', 'q']
    letter_count = [0]*26
    sorted_letters = []
    sorted_letter_count = []
    for word in word_list:
        # adding 1 to the letter count for each letter that shows up
        for char in word:
            letter_count[letter_list.index(char)] += 1
    for i in range(26):
        #finding the index of letter with the lowest count
        low_count_index  = letter_count.index(min(letter_count))
        #appending that letter to sorted letters
        sorted_letters.append(letter_list.pop(low_count_index))
        sorted_letter_count.append(letter_count.pop(low_count_index))
    return(sorted_letters)
#################################################################################
#                        Finding the best word                                  #
#################################################################################
def find_best_word_1(w_l = wrong_letters, i_s = incorrect_spots, word_list=wordle_list):
    # base_i_s = list(i_s)
    # base_w_l = w_l[:]
    current_best_word = "qqqqq"
    current_best_word_score = 50000
    for i in range(len(word_list)):
        words_after_guess = []
        # for each word in our list, we...
        for possible_answer in word_list:
            # mock guess the word against the possible answer
            num_words_left = mock_guess(word_list[i], possible_answer, word_list = word_list)
            # Adds that number of words left to the list of possible word counts
            words_after_guess.append(num_words_left)
        # once we have the list of possible word counts, we take the average and append that do the word_score
        temp = sum(words_after_guess)/len(words_after_guess)
        if temp < current_best_word_score:
            current_best_word_score = temp
            current_best_word = word_list[i]
        if (len(word_list)//100)!=0:#this will only be printed when less than 100 words are left to guess
            if (i % (len(word_list)//10))==0: #will print every 10% way through
                print("tested word %i of %i. Best word so far is %s with score %f"%(i, len(word_list),
                                                                                    current_best_word,
                                                                                    current_best_word_score))
    # once all words have an average word result, find the minimum average, and find the matching word
    return(current_best_word)
#################################################################################
#                        Finding the best word                                  #
#################################################################################
# this method is used once there are at least 3 green letters, as it hopefully prevents
# the possibility of guessing wrong 4 times in a row on similar words
# think of sight, might, night, tight, light, fight, right, or wight
def find_best_word_2(w_l = wrong_letters, i_s = incorrect_spots, word_list=wordle_list):
    # base_i_s = list(i_s)
    # base_w_l = w_l[:]
    current_best_word_1 = "qqqqq"
    current_best_word_score_1 = 50000
    current_best_word_2 = "qqqqq"
    current_best_word_score_2 = 50000
    # First check possible answers like before
    for i in range(len(word_list)):
        words_after_guess = []
        # for each word in our list, we...
        for possible_answer in word_list:
            # mock guess the word against the possible answer
            num_words_left = mock_guess(word_list[i], possible_answer, word_list = word_list)
            # Adds that number of words left to the list of possible word counts
            words_after_guess.append(num_words_left)
        # once we have the list of possible word counts, we take the average and compare to best guess
        temp = sum(words_after_guess)/float(len(words_after_guess))
        if temp < current_best_word_score_1:
            current_best_word_score_1 = temp
            current_best_word_1 = word_list[i]
    # keep track of this guess to compare to the other

    # then we check through the whole WORDLE list instead of just possible answers
    # this can give us a better word that eliminates more answers
    # if we get to a _ight guess, throwing away a guess on mints to get rid of m/n/t/s makes the win more guaranteed.
    for i in range(len(wordle_list)):
        words_after_guess = []
        # for each word in our list, we...
        for possible_answer in word_list:
            # mock guess the word against the possible answer
            num_words_left = mock_guess(wordle_list[i], possible_answer, word_list = word_list)
            # Adds that number of words left to the list of possible word counts
            words_after_guess.append(num_words_left)
        # once we have the list of possible word counts, we take the average and compare to best guess
        temp = statistics.fmean(words_after_guess)
        if temp < current_best_word_score_2:
            current_best_word_score_2 = temp
            current_best_word_2 = wordle_list[i]
##        if i%1000 == 0:
##            print("tested word %i of %i. Best word so far is %s with score %5f"%(i, len(word_list),
##                                                                                current_best_word_2,
##                                                                                current_best_word_score_2))
    # choose the next guess by which average score is lower
    if current_best_word_score_2 < current_best_word_score_1:
        next_guess = current_best_word_2
    else:
        next_guess = current_best_word_1
    print("Possible Guesses: %s with score %f, %s with score %f"
          %(current_best_word_1, current_best_word_score_1, current_best_word_2,current_best_word_score_2))
    # once all words have an average word result, find the minimum average, and find the matching word
    return(next_guess)

#################################################################################
#                       Making a mock guess                                     #
#################################################################################
def mock_guess(guess_word, pos_cor_word,
               word_list = wordle_list):
    mock_gre_lett = [0,0,0,0,0]
    mock_inc_spots = [[],[],[],[],[]]
    mock_cor_lett = ""
    mock_inc_lett = ""
    #1. getting green letters
    for i in range(5):
        if guess_word[i] == pos_cor_word[i]:
            mock_gre_lett[i] = pos_cor_word[i]
    #2. make list of correct letters and wrong letters
    for letter in guess_word:
        if letter in pos_cor_word:
            mock_cor_lett += letter
        else:
            mock_inc_lett += letter
    #3. for each correct letter, check if in right spot. If not, add to incorrect spot
    for letter in mock_cor_lett:
        #check each spot for that letter
        for j in range(5):
            if guess_word[j] == letter:
                #if the correct letter we are looking at isn't the correct word spot,
                if guess_word[j] != pos_cor_word[j]:
                    mock_inc_spots[j].append(letter)
    # now that we have info on a mock guess for a possible answer, make a temp word list using that info
    possible_words = 0
    for word in word_list:
        possible = True
        # check if we have all letters we need
        for letter in mock_cor_lett:
            if letter not in word:
                possible = False
        if not possible:
            continue
        # check if any incorrect spots are repeated
        for i in range(5):
            if word[i] in mock_inc_spots[i]:
                possible = False
        if not possible:
            continue
        # check if we have any wrong letters
        for letter in mock_inc_lett:
            if letter in word:
                possible = False
        if not possible:
            continue
        # check if green letters are in the right spot
        for i in range(5):
            if mock_gre_lett[i] == 0:
                continue
            if word[i] != mock_gre_lett[i]:
                possible = False
        # if the word passes all checks, the count of possible words goes up by 1.
        if possible:
            possible_words += 1
    return(possible_words)

#################################################################################
#                        Shrinking possible words list                          #
#################################################################################
def wordle_help(correct_letters, wrong_letters,
                green_letters = [0,0,0,0,0], incorrect_spots = incorrect_spots,
                word_list=wordle_list):
    possible_words = []
    for word in word_list:
        possible = True
        # check if we have all letters we need
        for letter in correct_letters:
            if letter not in word:
                possible = False
        if not possible:
            continue
        # check if any incorrect spots are repeated
        for i in range(5):
            if word[i] in incorrect_spots[i]:
                possible = False
        if not possible:
            continue
        # check if we have any wrong letters
        for letter in wrong_letters:
            if letter in word:
                possible = False
        if not possible:
            continue
        # check if green letters are in the right spot
        for i in range(5):
            if green_letters[i] == 0:
                continue
            if green_letters[i] != word[i]:
                possible = False
        if possible:
            possible_words.append(word)
    return possible_words

#################################################################################
#                        Scoring a wordle guess                                 #
#################################################################################
def wordle_guess_score(guess_word, correct_word, green_letters,
                       wrong_letters=wrong_letters, incorrect_spots = incorrect_spots):
    correct_letters = ""
    for i in range(5):
        if guess_word[i] == correct_word[i]:
            green_letters[i] = correct_word[i]
    #2. make list of correct letters, or add to wrong letter
    for letter in guess_word:
        if letter in correct_word:
            correct_letters += letter
        else:
            wrong_letters += letter
    #3. for each correct letter, check if in right spot. If not, add to incorrect spot
    for letter in correct_letters:
        #check each spot for that letter
        for j in range(5):
            if guess_word[j] == letter:
                #if the correct letter we are looking at isn't the correct word spot,
                if guess_word[j] != correct_word[j]:
                    #add that letter to that index of incorrect_spots if not already there
                    if letter not in incorrect_spots[j]:
                        incorrect_spots[j].append(letter)
    #4. return new strings/list of correct/green/wrong letters and wrong spots.
    return(correct_letters, wrong_letters, green_letters, incorrect_spots)
#################################################################################
#                                The actual AI                                  #
#################################################################################
def wordle_ai(guess_word, correct_word, correct_letters = '', wrong_letters = '',
              green_letters = [0,0,0,0,0], incorrect_spots = [[],[],[],[],[]], word_list = wordle_list, guess_count = 0):
    #1. guess word: tares is first word.
    print("New guess: "+guess_word)
    guess_count +=1
    #2. check the word for correctness
    new_correct_letters, new_wrong_letters, new_green_letters, new_incorrect_spots = wordle_guess_score(guess_word, correct_word, green_letters,
                                                                                    incorrect_spots = incorrect_spots, wrong_letters = wrong_letters)
    # if the word is correct, return that word!
    if guess_word==correct_word or guess_count==7:
        return guess_count, guess_word
    #3. use wordle_help to find list of possible words
    new_word_list = wordle_help(new_correct_letters, new_wrong_letters,
                                green_letters=new_green_letters, incorrect_spots = new_incorrect_spots,
                                word_list=word_list)
    #4. use find_best_letters to find most common letters from possible words.
##    best_letters = find_best_letters(word_list = new_word_list)
##    print("DEBUG - best letters list:" +str(best_letters))
    #5. find a word from possible words using find_best_word
    if new_green_letters.count(0)<3:
        # if there are 3 green letters, we check all words in the wordle list
        next_guess = find_best_word_2(w_l = new_wrong_letters, i_s = new_incorrect_spots, word_list = new_word_list)
    else:
        # if not, we just check possible answers. Checking all words probably would be better, but a lot slower
        # with only a little gain
        next_guess = find_best_word_1(w_l = new_wrong_letters, i_s = new_incorrect_spots, word_list = new_word_list)
    #6. guess that word in wordle_ai

##    print("DEBUG - Green letters: " +str(new_green_letters))
##    print("DEBUG - correct letters: " +str(new_correct_letters))
##    print("DEBUG - word list: " +str(new_word_list))
##    print("DEBUG - incorrect_spots: "+str(incorrect_spots))
    
    return wordle_ai(next_guess, correct_word, correct_letters = new_correct_letters,
                     wrong_letters = new_wrong_letters, green_letters = new_green_letters,
                     incorrect_spots = new_incorrect_spots, word_list = new_word_list, guess_count = guess_count)



##sum_ai_scores = []
##count = 0
##sorted_wordles = sorted(wordle_list)
##print(sorted_wordles[720:750])
##for i in range(7,10):
##    ai_scores = []
##    for j in range(100):
##        count +=1
##        wordle = sorted_wordles[i*100+j]
##        if count%10 == 0:
##            print("current word: %s, count %i"%(wordle, count))
##        wrong_letters = ''
##        incorrect_spots = [[],[],[],[],[]]
##        guess_count = 0
##        green_letters= [0,0,0,0,0]
##        correct_letters = ''
##        ai_scores.append(wordle_ai('arose',wordle,wrong_letters = '',
##                         incorrect_spots = [[],[],[],[],[]],guess_count = 0))
##    avg_score = sum(ai_scores)/len(ai_scores)
##    print("Average score from %i00 to %i00: %f"%(i,i+1,avg_score))
##    sum_ai_scores.append(avg_score)
##ai_scores = []
##for i in range(74):
##    count +=1
##    wordle = sorted_wordles[i+12000]
##    wrong_letters = ''
##    incorrect_spots = [[],[],[],[],[]]
##    guess_count = 0
##    ai_scores.append(wordle_ai('arose',wordle))

##avg_score = sum(ai_scores)/len(ai_scores)
##print("Average score: %f"%(avg_score))
##sum_ai_scores.append(avg_score)



##
start_time = time.time()
print(wordle_ai(first_guess,correct_wordle))
end_time = time.time()
print((end_time - start_time)/60)



#This was used to find the "best" starting word.
#Very unoptomized, takes a long time to run.
#print(find_best_word_2())
#rales with score 292.160321
#salet with score 333.779559
#tested word 12279 of 12974. Best word so far is lares with score 288.718668

print(wordle_help("so","",
                  green_letters = ['s',0,'o',0,0],
                  incorrect_spots=[[],
                                   ['d','e','f','g','h','i','j','k','l','q','r','s','t','u','v'],
                                   [],
                                   ['d','e','f','h','i','j','n','o','p','s','t','u','v','w','x'],
                                   ['d','e','f','j','k','l','m','n','o','q','r','s','t','u']]))







