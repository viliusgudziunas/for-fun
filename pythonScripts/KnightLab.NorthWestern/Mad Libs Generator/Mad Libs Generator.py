# 3. Mad Libs Generator

# The Goal:
# Inspired by Summer Son’s Mad Libs project with Javascript.
# The program will first prompt the user for a series of inputs a la Mad Libs.
# For example, a singular noun, an adjective, etc.
# Then, once all the information has been inputted,
# the program will take that data and place them into a premade story template.
# You’ll need prompts for user input, and to then print out the full story at the end with the input included.

# Concepts to keep in mind:

# Strings
# Variables
# Concatenation
# Print


# A pretty fun beginning project that gets you thinking about how to manipulate userinputted data.
# Compared to the prior projects, this project focuses far more on strings and concatenating.
# Have some fun coming up with some wacky stories for this!

print("Welcome to a Mad Libs Generator!")
print("In this mini-game you will be asked to enter words, names and places.")
print("The game will use them to create the worst bed time story ever!")
print("Once the story is finished you will be able to read it in full and hopefully have a giggle.")
print("Thus, let us begin! This is 'The World's Worst Bedtime Story'!")
a_place = input("Please enter a place ")
an_adjective = input("Please enter an adjective ")
a_female_celebrity = input("Please enter a name of a female celebrity ")
a_body_part = input("Please enter a body part ")
a_body_part1 = input("Please enter another body part ")
a_human_organ = input("Please enter a human organ ")
an_adjective1 = input("Please enter another adjective ")
a_male_celebrity = input("Please enter a name of a male celebrity ")
an_adjective2 = input("Please enter another adjective ")
a_body_part2 = input("Please enter another body part ")
a_body_part3 = input("Please enter one more body part ")
a_place1 = input("Please enter another place ")
a_celebrity = input("Please enter another name of a celebrity ")
an_animal = input("Please enter an animal ")
a_verb = input("Please enter a verb ")
a_number = input("Please enter a number ")
a_body_part4 = input("Please enter a body part - this will be the last one, I promise :) ")
an_adjective3 = input("Please enter one last adjective ")
an_adjective4 = input("Please enter an adjective - this is the last one for real ")
for i in range(1, 10000):
    print("LAST REQUEST")
a_verb_past_tense = input("Please enter a verb in past tense ")
for element in range(1, 100000):
    print("Creating Your Bedtime Story")
print("Thank you for playing, enjoy your story!")
print("The World's Worst Bedtime Story")
print("Once upon a time")
print("in a place called " + a_place + ", there was a " + an_adjective + " princess named " + a_female_celebrity + ".")
print("Her kingdom was huge, but her " + a_body_part + " was bigger.")
print("She was beautiful from her " + a_body_part1 + " to her " + a_human_organ + ".")
print("One day she saw a " + an_adjective1 + " prince named " + a_male_celebrity + ".")
print("He had a " + an_adjective2 + " face.")
print("As soon as his " + a_body_part2 + " touched her " + a_body_part3 + " they fell in love.")
print("They got married at " + a_place1 + " the following day")
print("")
print("Not long after, they had a baby.")
print("They decided to call him/her " + a_celebrity + ".")
print("He/She looked like a " + an_animal + ".")
print("He/She used to " + a_verb + " " + a_number + " times a day")
print("so that his/her " + a_body_part4 + " would be " + an_adjective3 + " and " + an_adjective4 + ".")
print("And they " + a_verb_past_tense + " happily ever after!")
print("Hope you enjoyed your bedtime story. See you next time! :)")