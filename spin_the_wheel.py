import random
import time


# implementing the method
def spin_the_wheel(ans, option_list):

    # for writing results in the file as a history log
    f = open("game_history.txt", "a")

    # user wants to play the game
    if ans == "Y" or ans == "y":
        flag = True
        selected_option = random.choice(option_list)
        print("Waiting for the wheel to stop....")
        f.write("\n\nWaiting for the wheel to stop....")
        time.sleep(2)
        print("You got", selected_option)
        f.write("You got " + repr(selected_option))
        f.close()
        return flag
    # user doesn't want to play the game
    elif ans == "N" or ans == "n":
        flag = False
        print("\nThanks for playing. BYE")
        return flag
    # illegal character
    else:
        flag = True
        print("Invalid answer. Please try again")
        return flag


# Getting the number of options from the user
print("\n\tWelcome to the \"Spin the Wheel\" game\n")
no_of_options = int(input("Enter the number of options: "))
options = []

# saving the options for the game
for i in range(no_of_options):
    options.append(input("Option {i}: ".format(i=i + 1)))

print("We have", no_of_options, "options in the game. They are:", options)

# spinning the wheel
play_again = True
while play_again:
    answer = input("Spin the wheel??? [y/n] --- ")
    play_again = spin_the_wheel(answer, options)
