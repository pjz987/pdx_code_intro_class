'''
filename: magic8ball.py
Make a Magic Eight Ball program
'''

# 1.Print a welcome screen to the user.
print("\nCome one and all...\n\nStep in to this den of curiosities and learn the innermost truths of the Magic 8 Ball!\n")

# 2.Use the random module's random.choice() to choose a prediction.
import random

eight_ball_answer = ["Reply hazy, try again", "Signs point to yes.", "Don't shake me so hard", "As I see it, yes.", "Don't count on it.", "My sources say no.", "It is decidedly so!", "What was your question again?", "Wait, what?", "That's a dumb question.", "It will be so?", "No way!"]

eight_ball_prompt = ["What dare you glean from the unkown?", "What would you ask of the knowers of stuff?", "What is your query, o innocent one?"]

giddy_eight_ball = ["Oh ho ho back into the mysteries we delve...", "Then the secrets will become less secret once more."]

# 3.Prompt the user to ask the 8-ball a question [of their choice]
eight_ball_question = input("What darkest truth would you unbind from the black pool of the unknown?...  ")

# 4.Display the result of the 8 ball.
selection = random.choice(eight_ball_answer)
print(f"\nThe answer to your query: {eight_ball_question} is {selection}")

while True:

    '''
    Advanced version 1
        - Let the user choose if they want to ask a second question.
    '''
    go_again = random.choice(giddy_eight_ball)
    # Ask to ask a second question.
    ask_again = input("\nAre your darkest curiousities satisfied?...\n\nOr would you delve further into the mysteries?... ").lower()
    if ask_again in ['yes', 'yes, please', 'y', 'si', 'oui', 'ja', 'yeah', 'oh yeah', 'mos def']:
        print(f"\n{go_again}\n")
    else:
        print("\nWhat a pity...")
        break

    prompt = random.choice(eight_ball_prompt)
    loop_question = input(f"{prompt}  ")

    # had to make a second selection thing here
    selection = random.choice(eight_ball_answer)

    print(f"\nThe answer to your, deeper, darker query: {loop_question} is {selection}\n\nAha what a revelation...")
