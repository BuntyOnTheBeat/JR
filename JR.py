name = input("What is your name, please enter your name: ")

if name == "JR".casefold():
    print("Oh, I know you. Your name is Just Retarded right. You seem to not want anyone to know that. It's ok no "
          "will find out.")
    ans = input(str("Is this true: "))
    if ans == "yes".casefold():
        print("gug")


else:
    print("Oh hi {}, nice to meet you".format(name))
