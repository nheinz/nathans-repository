import random

# For this program I used the random.randint function to give myself a random integer in from 0 to 4 for my base and exponent.
# I then set my answer to equal the random base number raised to the random exponent number/

# I intend to demonstrate the ability to use comments in this homework assignment.

# A sequence of assignments to generate a random problem:
base = random.randint(0,4) # For the base, I used the module random.randint because this module will generate a random integer for us depending on the range we give it.
# In this instance, I used the range (0,4). I will elaborate on this in a later comment.

exponent = random.randint(0,4) # Once again, I used the random.randint module to generate a single digit integer from 0 to 4. This range will be explained later.

answer = base ** exponent # For answer, I took the randomly generated single digit integer for base and raised that number to a randomly generated single digit number for exponent.
# The reason for choosing the ranges that I did is that our answer cannot be four digits or larger. In this case, if we had our two largest options, 4 and 4, we would get an answer of 256. 
# So, we are assured that our answer will be less than four digits.

print('Problem: {base} ^ {exponent} = ?' .format(base = base, exponent = exponent)) # Although this step will print more, it allows us to see more of the process. 
# It shows that we have a problem and we have two numbers, but we do not know what the answer is.
print('Answer: {answer}' .format(answer = answer)) # This final step will print out the answer to the problem presented above. Although it requires more code, it makes the end result much more pleasant. 