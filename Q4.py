for candies in range(200):
    if candies % 5 != 2:
        continue
    if candies % 6 != 3:
        continue
    if candies % 7 != 2:
        continue

    x = int(input("Guess the number of candies:"))
    if x % 5 == 2 and x % 6 == 3 and x % 7 == 2:
        print("You guessed the right number of candies")
    else:
        print("You guessed the wrong number of candies" + "--" + str(candies) + " is the answer!")