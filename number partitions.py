#################################################################################
#                               Number Partiitions                              #
#                                                                               #
# PROGRAMMER:       Maxwell Solko                                               #
# Date:             1/23/2021                                                   #
#                                                                               #
# DESCRIPTION:                                                                  #
# This program find how many ways to partition any number, skipping repeats     #
# For example, 4 has 4 partitions, 1+1+1+1, 2+1+1, 2+2, 3+1.  1+2+1 isn't       #
# counted because it is essentially the same as 2+1+1.  This pattern is         #
# intertwined in a lot of math topics and has been well researched.             #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is (c) 2020 Maxwell Solko. This is original work, without use    #
# of outside sources.                                                           #
#################################################################################
import time

class  Partitions():

    def __init__(self):
        self.partition = [1]
        self.plus_minus = [1,2,5]
        self.pm_diff = [1,3]

# These get functions are mainly here for debugging or seeing the pattern
    def get_pm_diff(self):
        return self.pm_diff
    def get_partition(self):
        return self.partition
    def get_plus_minus(self):
        return self.plus_minus

    def get_final_partition(self):
        return self.partition[-1]

    def next_partition(self):
        next_num = 0
        count = 0
        while len(self.partition)>=self.plus_minus[count]:
            if count%4==0 or count%4==1:
                next_num += self.partition[-self.plus_minus[count]]
            else:
                next_num -= self.partition[-self.plus_minus[count]]
            count += 1
        self.partition.append(next_num)
        if len(self.partition)>=self.plus_minus[-1]:
            self.next_plus_minus()
        return

    def next_plus_minus(self):
        temp = self.next_pm_diff()+self.plus_minus[-1]
        self.plus_minus.append(temp)
        return temp

    def next_pm_diff(self):
        temp1 = len(self.pm_diff)%2
        if temp1==0:
            temp2 = self.pm_diff[-2]+1
            self.pm_diff.append(temp2)
        else:
            temp2 = self.pm_diff[-2]+2
            self.pm_diff.append(temp2)
        return temp2

#Testing the whole thing
euler = Partitions()
start = time.time()
for i in range(666):
    euler.next_partition()
end = time.time()
print(euler.get_final_partition())
print(end-start)
