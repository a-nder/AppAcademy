#While loops | used when you don't kno when a task will end

#A count using a while loop

# count = 4

# while count > 0 :
#     print(count)
#     count = count - 1

# print("Blast off!")

# #for loop | when you know hoe moany times you want to repeat something. use it in conjuction with range() function#

# for rep in range(1,4):
#     print(f"This is rep no. {rep}")


#A guessing game

secret_word = "python"


while True:
    guess = input("Enter the programming language we are using: ").lower()

    if guess == secret_word:
        print("You guessed the correct language!!!")
        break
    else:
        print("Incorrect guess try again!!!")
