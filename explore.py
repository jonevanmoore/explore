from sys import exit
import random

print("\nWelcome to Explore!\n")
name = input("What is your name, adventerous one? ").capitalize()

def start():
    state = input(f"\nHowdy {name}! Do you enjoy the great state of Utah? ").lower().strip()
    while state not in ("yes", "yessir", "yep", "yeppers", "absolutley", "of course", "yes!", "no", "not really", "nah", "nope", "quit", "exit", "sure"):
        print(f"Sorry, {name}, that's not an option.")
        state = input("> ").lower().strip()
    if state in ("yes", "yessir", "yep", "yeppers", "absolutley", "of course", "yes!", "sure"):
        print("\nFantastic! You're in for a treat!")
        utah()
    elif state in ("no", "not really", "nah", "nope"):
        print("\nWell that's too bad, because that's where we're headed :)")
        utah()
    elif state in ("quit", "exit"):
        exit(0)

def utah():
    print("\nWelcome to Utah! An adventurer's playground.")
    print("Today you will be exploring the one and only Angel's Landing, located at Zion National Park")
    angels_landing()

def angels_landing():
    score = 100
    print("\nAngel's Landing is one of the defacto classic hikes in Zion,")
    print("and one of the most stunning viewpoints you will ever experience!")
    print("""
Let's begin.



    """)
    print("Now in order to hike Angel's Landing, we must first find the Grotto Trailhead.\n")
    print("I hope you have your compass, because you're gonna have to lead us.")
    direction = input("> ").lower().strip()
    while direction not in ("west", "go west", "head west"):
        if direction in ("south", "go south", "head south"):
            wrong_south = ["No, that's the Pa'rus Trail. It's adjacent to our campground.", "I'm pretty sure that's the Pa'rus Trail.", "I don't think the Grotto Trail is this way."]
            print(random.choice(wrong_south))
            score -= 15
            direction = input("> ").strip().lower()
        elif direction in ("north", "go north", "head north"):
            wrong_north = ["That's the Watchman Trail. We need start at the Grotto Trail.", "We did the Watchman Trail yesterday!", "I know for a fact the Grotto Tail is not north."]
            print(random.choice(wrong_north))
            score -= 20
            direction = input("> ").strip().lower()
        elif direction in ("east", "go east", "head east"):
            wrong_east = ["That's the Hidden Canyon Trail. It's lovely, but it's closed due to rockfall.", "No, we're not doing the Hidden Canyon again.", "When has the Grotto Trail ever been east?"]
            print(random.choice(wrong_east))
            score -= 10
            direction = input("> ").strip().lower()
        else:
            wrong_else = ["Ummm, what?", "Excuse me?", "Huh?", "I don't understand.", f"Are you ok, {name}?"]
            print(random.choice(wrong_else))
            score -= 35
            direction = input("> ").strip().lower()
    if direction in ("west", "go west", "head west"):
        right_west = ["Yes! I think that's right!", "The map says this is the right way!", "I think you're right! Let's go!"]
        print(random.choice(right_west))
        score += 25
        print("\nWe continue west.")
        print("""
We proceed along the Grotto Trail, then reach a spot called Refrigerator Canyon.
It's a wonderful spot to get away from the blistering heat before we continue our hike.

            While we rest in the shade in for a bit, let's have a little quiz about the great canyons of Zion.
            Are you able to guess how old the rock layers in Zion Canyon are?
            Is it:
            a. 90 million
            b. 300 thousand
            c. 270 million
            d. 800 thousand
        """)
        wrong_layer = ["Sorry, that's incorrect.", "Keep trying.", "Close, but no.", "Sorry, try again"]
        rock_age = input("> ").lower().strip()
        while rock_age not in ("c", "270 million"):
            if rock_age in ("a", "90 million"):
                print(random.choice(wrong_layer))
                score -= 10
                rock_age = input("> ").lower().strip()
            elif rock_age in ("b", "300 thousand"):
                print(random.choice(wrong_layer))
                score -= 10
                rock_age = input("> ").lower().strip()
            elif rock_age in ("d", "800 thousand"):
                print(random.choice(wrong_layer))
                score -= 10
                rock_age = input("> ").lower().strip()
            else:
                print("What? That's not even an option")
                score -=20
                rock_age = input("> ").lower().strip()
        if rock_age in ("c", "270 million"):
            print("Correct! moving on!\n")
            score += 25
        print(f"""\n
    Oh boy! Now we have reached the infamous Walter's Wiggles.
    This is often the point where people who deem this hike too difficult tend to turn around.
    The reason they turn around is because the amount of back-to-back switchbacks it has.

    How many switchbacks do you think there are?
    (Hint: it's less than 30 but more than 15)
        """)
        while True:
            try:
                switchbacks = int(input("> "))
                o30u15 = ["Are you even paying attention? -.-", "Points deducted for not paying attention.", "You're not paying attention, are you?", "Gonna have to take away points if you're not focusing."]
                while switchbacks >= 30:
                    score -= 15
                    print(random.choice(o30u15))
                    switchbacks = int(input("> "))
                while switchbacks <= 15:
                    score -= 15
                    print(random.choice(o30u15))
                    switchbacks = int(input("> "))
                while switchbacks in (16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29):
                    not_21 = ["Not quite! Keep guessing.", f"Almost, {name}. Keep trying.", "Almost got it!"]
                    print(random.choice(not_21))
                    switchbacks = int(input("> "))
                if switchbacks == 21:
                    print("Yes! It's crazy how endless they feel. Anyways let's push through it\n")
                    score += 30
                    break
            except ValueError:
                print("Numbers only please")
                score -= 5
                continue
        print(f"""\n
        Okay, {name}, we finally conquered Walter's Wiggles, but we're not out of the woods yet.
        We're almost to the summit, but now we must deal with Hogsback, otherwise known as "The Spine."
        This is the part where this hike gets a little spooky.
        It has a very narrow path, and has chains bolted into the stone to keep people from falling hundreds of feet to their death.
        This is a very popular hike nonetheless, so we must deal with fellow passerbyers that need to get around us.""")
        print("""
        A young woman just got to the top and is now ready to head down.
        You are currently using the chains to keep you from falling, but she needs to get around you.
        What should you do so both of you safely pass each other.
        """)
        solution = input("> ").lower().strip()
        while "duck" not in solution:
            if solution in ("move left", "left", "go left"):
                print("You moved left and fell 800 feet to your death.")
                print("Let's try that again.\n")
                score -= 15
                print("""
        A young woman just got to the top and is now ready to head down.
        You are currently using the chains to keep you from falling, but she needs to get around you.
        What should you do so both of you safely pass each other.
                """)
                solution = input("> ").lower().strip()
            elif solution in ("right", "move right", "go right"):
                print("You moved right and the young woman fell 800 feet to her death.")
                print("Let's try that again")
                score -= 15
                print("""
        A young woman just got to the top and is now ready to head down.
        You are currently using the chains to keep you from falling, but she needs to get around you.
        What should you do so both of you safely pass each other.
                """)
                solution = input("> ").lower().strip()
            else:
                print("Sorry, that's not an option.")
                solution = input("> ").lower().strip()
        if "duck" in solution:
            score += 35
            print("""
    You ducked and went under her arm while the young woman was still able
    to hang on to the chain and get passed you. Good job!
                """)
        print(f"""
        Alright, {name}, we made it to the TOP!
        One last trivia question, and I'm done pesturing you.

        How many feet in the air are we currently standing at right now?
        a. 2,173
        b. 8,167
        c. 4,124
        d. 5,790
        """)
        feet = input("> ").lower().strip()
        while feet not in ("d", "5,790", "5790"):
            if feet in ("a", "2,173", "2173", "b", "8,167", "8167", "c", "4,124", "4124"):
                feet_no = ["Sorry, keep trying", "Not quite. Try again.", "Incorrect. Try again."]
                print(random.choice(feet_no))
                feet = input("> ").lower().strip()
            else:
                print("That's not even an option")
                feet = input("> ")
        if feet in ("d", "5,790", "5790"):
            score += 15
            print("Correct!\n")
            print(f"Congradulations, {name}, you hiked Angel's Landing.")
            print("Now all there is left to do is take a picture")
            picture = input("> ").lower().strip()
            while picture not in ("take picture", "take photo","take a photo", "take a picture" "picture", "photo"):
                print("Just take a photo. Very simple.")
                picture = input("> ").lower().strip()
            if picture in ("take picture", "take photo","take a photo", "take a picture" "picture", "photo"):
                print(f"""

        ──▒▒▒▒▒▒▒▒───▒▒▒▒▒▒▒▒
        ─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒
        ──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒
        ─────██─────────██
        ░░░▄▄██▄░░░░░░░▄██▄░░░

                """)
                print("So beautiful!")
                print(f"\nYou ended up with a score of {score}!")
                print("Thanks for playing!")

start()
