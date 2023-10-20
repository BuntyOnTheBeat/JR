name = input("What is your name, please enter your name: ").casefold()

if name == "JR".casefold():
    print("Oh, I know you. Your name is Just Retarded right? You seem to not want anyone to know that. It's ok no body"
          "will find out.")
    ans = input(str("Is this true?: "))

    if ans == "yes".casefold():
        print("gug")

    elif ans == "no".casefold():
        print("liar liar pant on fire!!!! ohhhhhhh")
    else:
        print("I dont understand what did you type?")

elif name == "aaron".casefold():
    print("hi stupid")
    ans = input(str("If this is not true, type yes.: "))

    if ans == "yes".casefold():
        print("HAHAHHAHAHA you said you stupid.")

    if ans == "no":
        print("liar liar pant on fire !!!!!!! ohhhhhhh.")


elif name == "Aariz".casefold():
    print("Bro your sooooo bad at aiming that you aimed at Bugha and killed yourself, and you aren't playing in "
          "FNCS, Bugha joined your lobbies for the bots")
    ans = input(str("Answer, wether or not this is correct?: "))

    if ans == "no".casefold():
        print("that's cap")

    if ans == "yes".casefold():
        print("fax bro")

elif name == "mason".casefold():
    print("Hi, " + name + " you suck.")

    ans = input("Tell, me, is this true?: ")

    if ans == "no".casefold():
        print("cap")

    if ans == "yes" .casefold():
        print("gj")

    if ans == "".casefold():
        print("Bro you got to answer with yes or no.")

elif name == "dennis".casefold():
    print("Hi, " + name + " you are 很聪明.")

    ans = input("Tell, me, is this true?: ")

    if ans == "no".casefold():
        print("thats cap")

    if ans == "yes" .casefold():
        print("gj")

    if ans == "".casefold():
        print("Bro you got to answer with yes or no.")

else:
    print("Oh hi {}, nice to meet you".format(name))
