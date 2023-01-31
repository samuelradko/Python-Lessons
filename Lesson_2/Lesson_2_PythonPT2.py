### :: "timeit" shows us how much runtime took to the code from when it started until it finished 
### :: for to see in seconds and not miliseconds we have to setup two valubales 
### :: Example down below 

# import timeit # - imports the timeit module from the buildin Python library

# t1 = timeit.default_timer() # - First we set up the first timer so the timer will know when to start the time test

########################### - code goes betwen t1 and t2
# sum = 0
# for i in range(1000425):
#     sum += 1
# print(sum)
###########################

# t2 = timeit.default_timer() # - here in t2 we will see how much time has passed from t1 

# print("The time that was passed is:", t2-t1, "seconds") # - to see in second how much time has passed we first will put t2 and after him we will put t1 


#[Q1 + Q2] What is the loop that drawing the next triangle? + make it so each new loop the stars will print one more then the last star before
## Example ##
#####
# * #
# ** #
# *** #
# **** #
# ***** #
##########
for i in range(1, 6): # first we loop in the range from 1 - 6 >> outer loop 
    for j in range(i): # then we use a nested loop which print the first index and then continue to the next index so if I started from 1 star >>> inner loop  
        # on the next loop it will print 2 stars and so on until first loop will reach to the end of the index which will be number 5(range(1,6))
        print("*", end="")
    print("")