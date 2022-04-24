define c = Character("Chloe")

label start:
    play sound "audio/city.mp3"
    scene bg templeintro
    with fade

    show chloehappy

    c "Welcome to Temple University!"

    c "My name is Chloe, and I will help you experience Temple today!"

    c "On your journey, you will be making decisions, exploring new places, and discovering what it is like to be a Temple Student!"

    c "I hope you enjoy your time today!"

    stop sound


    play sound "audio/belltower.mp3"
    scene bg belltower
    with fade
    show chloehappy

    c "Do you hear that ringing?"
    c "That's the sound of our Bell Tower, which chimes every hour!"
    c "Also, the surrounding areas of the Bell Tower is the Beury Beach!"
    c "Although it is not a REAL beach, it is a nice area for students to hang out when it is nice outside!"

    menu:
        c "It is a nice day out today. What would you like to do?"
        "Stop and relax. You want to sit down and enjoy the sun!":
            jump sit
        "Keep exploring. You want to explore what Temple what's to offer!":
            jump explore

label sit:
    play sound "audio/football.mp3"
    scene bg beach
    with fade
    show chloehappy
    "You decide to sit down and enjoy the weather"
    c "Isn't this beautiful? I love studying outside when the weather is nice!"
    "You love sitting on Beury Beach. It is nice outside. Almost too nice."
    "You start to become sleepy, and you pass outside right in front of your tour guide!"
    stop sound
    scene bg sleep
    with dissolve
    c "Hey! Wake up! We have so much more to explore!"
    "You don't wake up. You nap on Beury Beach for 2 hours. Chloe leaves you, and you are not able to explore Temple."
    "{b}Bad Ending{/b}."
    return

label explore:
    scene bg belltower
    show chloehappy
    "I want to see what Temple has to offer, but I will come back and relax later!"
    c "Good idea! Let's go!"
    play sound "audio/city.mp3"
    show bg library
    with fade
    show chloehappy
    c "Welcome to our Charles Library!"
    c "This building is open to all students to study and get homework done!"
    c "We also have a small cafe on the first floor of the library for your studying needs!"
    stop sound
    menu:
        c "Do you want to get coffee and explore the library, or do you want to move on?"
        "I want coffee, lets go inside!":
            jump coffee
        "I'm not a big coffee drinker. Let's continue the tour.":
            jump continuetour
    label coffee:
        "Actually, I'd really like coffee right now."
        c "Sounds good! Let's go inside"
        stop sound
        play sound "audio/coffee.wav"
        show bg charles
        with fade
        show chloehappy
        "You and Chloe drink coffee together."
        "The two of you get so caught up in your coffee that Chloe forgets that she is on a time limit for her tour."
        "Chloe went over the time limit, and has to take another tour with someone else."
        c "I am so sorry. I lost track of time. I have to go on another tour.Come back again to see the things you weren't able to see."
        "{b}Bad Ending{/b}."
        return
    label continuetour:
        "I don't want coffee. I'd like to see what else is around."
        c "That's great! I actually don't like coffee myself. Let's go explore!"
        show bg serc
        play sound "audio/city.mp3"
        with fade
        show chloehappy
        c "Welcome to the SERC, also known as our Science Education and Research Center!"
        c "This building is home to our science and technology majors!"
        c "If you're not a science or technology major, you may have an elective class in this building!"
        stop sound
        show bg morganhall
        play sound "audio/city.mp3"
        with fade
        show chloehappy
        c "Welcome to our Morgan Residence Hall and dining Hall!"
        c "Our Morgan residence halls, both north and south, have apartment style dorms for students to live in!"
        c "Morgan dining Hall is one of two of our on campus dining halls!"
        stop sound
        menu:
            c "Would you like to grab food?"
            "Food sounds lovely!":
                jump food
            "I'm not hungry right now":
                jump full
        label full:
            "I'm actually not hungry right now."
            c "How will you experience Temple without trying something from the dining hall?"
            c "Clearly you're not someone who really WANTS to go to Temple!"
            "{b}Bad Ending{/b}."
            return
        label food:
            "I want to try something from the dining hall."
            c "Sounds good! Let's go"
            play sound "audio/cafeteria.mp3"
            show bg foodmorgan
            with fade
            show chloehappy
            c "Welcome to our dining hall!"
            c "We have many food options available for all students!"
            c "This is our lower morgan food court, which had restaraunts such as Chick Fil A, Panda Express, Bento Sushi, and Starbucks!"
            c "I hope you enjoyed the food here!"
            stop sound
            play sound "audio/city.mp3"
            show bg 1300
            with fade
            show chloehappy
            c "Welcome to our 1300 Residence Hall!"
            c "This is another residents hall open to all students, both new and returning!"
            c "There are 5 floors, and the third floor is for 1st year honors students!"
            c "Maybe you will live here some day!"
            stop sound
            play sound "audio/city.mp3"
            show bg studentcenter
            with fade
            show chloehappy
            c "Welcome to our Student Center!"
            c "If you're tired of the dining hall, you can grab food such as SaladWorks, Which Wich, Twisted Taco, Burger Fi, and Pitachip!"
            c "We also have a gaming lounge, where you can play both video games and board games!"
            c "Many clubs also host meetings here!"
            stop sound
            menu:
                c "So, are you up to game? I could use a break from the tour."
                "I love to play games! Game on!":
                    jump game
                "Gaming is not my thing. What else is around?":
                    jump nextplease
            label game:
                c "yay! Let's go!"
                play sound "audio/ping.mp3"
                show bg gaming
                show chloehappy
                c "Let's play ping pong! I love that game!"
                "Sounds good!"
                "You and Chloe play ping pong together. You are having a lot of fun!"
                "You end up beating Chloe by a fairly large amount"
                c "Wow! You're really good at this game!"
                c "You definitely have the right skills to be a Temple Student!"
                c "You don't need me! Go explore! Have fun!"
                "{b}Good Ending. Try again for a better ending!{/b}."
                return
            label nextplease:
                "Gaming is not my thing. Maybe I'll have a club meeting there in the future!"
                c "Totally understandable! I could always game after the tour. Let's move on!"
                play sound "audio/city.mp3"
                show bg fox
                with fade
                show chloehappy
                c "Welcome to our Fox School Of Business!"
                c "This is a very popular building for all of our business majors!"
                stop sound
                play sound "audio/concert.mp3"
                show bg performing
                with fade
                show chloehappy
                c "Welcome to our Temple Performing Arts Center!"
                c "Many concerts from our choirs and orchestras perform here!"
                c "Looks like a concert from the Temple University Diamond Marching Band is about to start"
                stop sound
                menu:
                    c "Do you want to watch the concert? It looks really good!"
                    "Absolutely I do!":
                        jump templeband
                    "Watching a concert does not interest me":
                        jump nextplace
                label nextplace:
                    "I don't really like concerts. What else is here?"
                    c "You don't want to support the Temple Marching Band? What kind of perspective Temple Student are you?"
                    "{b}Bad Ending{/b}."
                    return
                label templeband:
                    "Is that even a question? Yes I want to watch!"
                    play sound "audio/bandplaying.mp3"
                    "And with that, the concert begins, and you and Chloe sit back and watch the concert."
                    stop sound
                    play sound "audio/basketball.mp3"
                    show bg basketball
                    with fade
                    show chloehappy
                    c "Wasn't that concert great!"
                    c "Now we are inside our Liacouras Center!"
                    c "This is home to our basketball games and concerts!"
                    stop sound
                    play sound "audio/applause.wav"
                    show bg connor
                    with fade
                    show chloehappy
                    c "You did it!"
                    c "You successfully completed the tour!"
                    c "While there are other places of the tour I did not feature, feel free to go off on your own and explore!"
                    c "Best of luck, and enjoy your time at Temple!"
                    "{b}Good ending. Thanks for playing! Replay the game for more endings!{/b}."
                

    return
