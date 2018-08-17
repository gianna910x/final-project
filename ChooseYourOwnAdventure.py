#shoutout to Tania for not giving up on her code
start = '''
"You just woke up, its 7:30am, you you want to get up or sleep"
'''
print(start)
answer = input("Enter 'get up' or 'sleep': ")
if answer == "get up":
    print("You decided to get up, you make your way to the bathroom when suddenly you're overthrown by anxiety, you feel weaker than ever before. Do you fight your way thruogh the pain or get back into bed?")
    answer = input("Enter 'fight' or 'sleep':")
    if answer == "fight":
        print("You fight your way to the bathroom feeling light headed. You get dressed and start to head out the door. Do you take your car or the bus?")
        answer = input("Enter 'car' or 'bus':")
        if answer == "car":
            print("You get into the car, the sky gets dark quicky and soon it's beating down on you, taunting you. You know you can still go back to bed if you wanted to, what do you do?")
            answer = input("Enter 'go to work'or'go to bed':")
        elif answer == "bus":
           print ("You quickly run to the bus, you have to cross a busy road. One minute you're finally feeling fine and suddenly you stop thinking. You see all the cars in front of you and you think about how easy it would be for you to just jump in front of one of them, how easily it would end all your pain.")
           answer = input("Enter 'jump'or 'deep breath':")
           if answer == "jump":
                print("Without even looking back you walk into the traffic, hoping one will hit you in a way to end all your pain for once and for all.")
           elif answer == "deep breath":
                print("You take a deep breath and throw yourself into the incoming truck the world becomes dark and you smile for the first time in years.")
    elif answer =="sleep":
        print("you give up easily now-a-days, you retreat back to the comfort of you home. you think of an excuse to tell you boss, what do you tell him?")
        answer = input("Enter 'im sick'or'dont call':")
        if answer== "im sick":
            print ("You leave a message with your coworker, and tell her that you're feeling too sick to come in, your coworker knows why and asks if you'd like her to come over after work.")
            answer = input("Enter 'sure'or'be alone':")
            if answer =="sure":
                print("You say sure, and immediately regret it but a deals a deal. You hang up the phone and wait for 6:30pm, where you have to pretend you're fine.")
            elif answer=="be alone":
                print("You stumble into the bathroom and look around, soon you find exactly what your looking for, you go get some water and pulling out your laptop. You turn on your favorite music and blast it on full. You close your eyes and slip a pill in your mouth. Slowly letting it dissolve on your tongue. When you open your eyes, your vision seems to be blinking in and out, you let the now empty bottle of pills slip out of your hands and you clutch the photo of your mom and you laughing, and you make one last wish. To be happy. Everything goes black and you smile because the pain is finally fading away. Away it goes. Suddenly you see a bright light but your eyes arent open yet, you hear people rushing around. You try to slowly open your eyes but find that you can't.")
                answer=input("Enter 'panic' or 'remain calm':")
                if answer == "panic":
                    print("You start to panic and try to lift your arms and discover that you can't. Your whole body feels numb. Suddenly from your right side you hear your coworker crying, explaining to the nurses that she found you like this when she decided to check on you last minute. The nurses tell her that youre in a coma and no one can be sure for how long.")
                elif answer == "remain calm":
                    print("You calm your breath and try to listen for what happening around you, from your right side you hear your coworker crying, explaining to the nurses that she found you like this when she decided to check on you last minute. The nurses tell her that youre in a coma and no one can be sure for how long.")
        elif answer == "dont call":
            print("You stumble into the bathroom and look around, soon you find exactly what your looking for, you go get some water and pulling out your laptop. you turn on your favorite music and blast it on full. you close your eyes and slip a pill in your mouth. slowly letting it dissolve on your tongue. when you open your eyes youre vision seems to be blinking in and out you let the now empty bottl of pills slip out of your hands and you clutch the photo of your mom and you laughing, and you make one last wish. to be happy. everything goes black and you smile because the pain is finally fading away. away it goes.")
elif answer == "sleep":
    print ("You decided to go back to sleep, about an hour later you wake up to your cellphone ringing, its your boss. Do you answer the phone or pretend to miss it?")
    answer = input("Enter 'answer' or 'miss it':")
    if answer == "answer":
        print("He yells at you, calling you a few ungraceful words. and aburtly hangs up after telling you to get into the office! do you really care about your job?")
        answer = input("Enter 'who cares'or'get going':")
        if answer == "who cares":
            print("Who cares about work anway? We're all gonna die right? Some sooner than others. You pass out huddled in a corner trying to escape your own thoughts when you wake up you have a headache and genuinely feel like ending it all")
            answer = input("Enter 'close eyes' or 'call friends':")
            if answer == "close eyes":
                print("You close your eyes and listen to the birds singing their songs outside of your window. soon you pass out again, another day wasted.")
            elif answer == "call friends":
<<<<<<< HEAD
                print("you dial your best friends number it rings twice before she picks up, she asks if you're ok, and you reply saying you felt a bit lonely and were feeling sad. she immediately invites herself over and brings wine to have fun. you're happy you called her because she can make your day better more than anyone")
        elif answer == "get going":
            print ("you decide to get going to work, you arrive to work ad theres only 10 other people there, you find out they all called in sick, but luckily for you the boss is paying overtime for all the people who decided to come in. The days goes by fairly quickly, you spend most of it daydreaming, finally its time to go bed and youre a bit better than that morning. Your coworkers invite you out to drink.")
            answer = input("Enter 'go out'or 'go home':")
            if answer == "go out":
                print ("you decide to go out and have a blast with your coworkers, its past midnight when you stumble home, you find your way to the bed and pass out. ready for the next day.")
            elif answer == "go home":
                print("you politely reject the offer, you dont want to bother your coworkerswith your problems, and youd rather keep a distance from people who could potentially hurt you. you go home and watch some old movies in the dark and chomp out some popcorn. you feel satisfeid but part of you wishes you were bold enough to go drinking with your coworkers.")
=======
                print("You dial your best friends number it rings twice before she picks up, she asks if you're ok, and you reply saying you felt a bit lonely and were feeling sad. she immediately invites herself over and brings wine to have fun. you're happy you called her because she can make your day better more than anyone")
>>>>>>> 4dd26a152380b578e01a8c0b2d453872ca2fbb7a
    elif answer == "miss it":
        print("You roll over, and close our eyes trying to keep the tears from drowning you again. your stomach rumbles but you have no energy, you dont care about your own health. do you go eat or starve yourself")
        answer = input("Enter 'eat'or'starve':")
        if answer =="eat":
            print("You decide to go eat, but your head feels to heavy to be walking around. you bump into the corner of your table a picture hits the floor. its of your mother hugging you and smiling. you start crying, wondering why you could never find that type of happiness.")
            answer = input("Enter 'remincise'or'forget it':")
            if answer == "remincise":
                print("You hold the photo close cry, you let the tears fly out of you. When you finish crying you feel lighter than before, almosst as if a weight was taken off your shoulders. you find yourself talking to the photo, teling it how youve been, how youve been coping, and how much you wish you could hear your moms laugh again")
            elif answer == "forget it":
                print("You put the photo back down, face down, some how its already 5:30pm and it feels like the seconds are dragging by. you fall on to the floor and cry yourself to sleep for the 5th time that week.")
        elif answer == "starve":
            print("You stay in bed, whast the point of eating, food smells revolting lately, you can barely drink water. you close your eyes and just wait for night to fall.")
