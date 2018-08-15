#shoutout to Tania for not giving up on her code
start = '''
"You just woke up, its 7:30am, you you want to get up or sleep"
'''
print(start)
answer = input("Enter 'get up' or 'sleep': ")
if answer == "get up":
    print("you decided to get up, you make your way to the bathroom when suddenly you're overthrown by anxiety, you feel weaker than ever before. do you fight your way thruogh the pain or get back into bed?")
    answer = input("Enter 'fight' or 'sleep':")
    if answer == "fight":
        print("you fight your way to the bathroom feeling light headed. you get dressed and start to head out the dor. do you take your car or the bus?")
        answer = input("Enter 'car' or 'bus':")
        if answer == "car":
            print("you get into the car, the sky gets dark quicky and soon it beating down on you, taunting you. you know you can still go back to bed if you want to, what do you do?")
            answer = input("Enter 'go to work'or'go to bed':")
#        elif answer == "bus":
#     elif answer =="sleep":
#         print("you give up easily now-a-days, you retreat back to the comfort of you home. you think of an excuse to tell you boss, what do you tell him?")
#         answer = input("Enter 'im sick'or'dont call':")
#             if answer= "im sick":
#             elif answer = "dont call":
elif answer == "sleep":
    print ("You decided to go back to sleep, about an hour later you wake up to your cellphone ringing, its your boss. Do you answer the phone or pretend to miss it?")
    answer = input("Enter 'answer' or 'miss it':")
    if answer == "answer":
        print("He yells at you, calling you a few ungraceful words. and aburtly hangs up afeter telling you to get into the office! do you really care about your job?")
        answer = input("Enter 'who cares'or'get going'")
    elif answer == "miss it":
        print("you roll over, and close our eyes trying to keep the tears from drowning you again. your stomach rumbles but you have no energy, you dont care about your own health. do you go eat or starve yourself")
        answer = input("Enter 'eat'or'starve'")
        if answer =="eat":
            print("")
