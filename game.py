

#Game setup
inventory=[]
def start_game():
# Game intro
    print("Welcome to Quest for Knowledge!")
    print("You are a student trapped in a mysterious school.")
    print("To graduate, you must explore and escape all five subject-based rooms:")
    print("- Math Room")
    print("- English Room")
    print("- History Hall")
    print("- Science Hall")
    print("- Graduation chamber")
    print("Each room has a challenge and gives you an important item.")
    print("When you collect all items, you can enter the Graduation Chamber and graduate.")
    print("\nUse the following commands to play:")
    print("- Movement: go north, go south, go east, go west")
    print("- Collect items: collect key, collect master key, collect hall pass, collect graduation cap, collect passcode")
    print("- Other:  check inventory, quit")
    print("\nLet us begin your quest!")
    print("You have 10 minutes to complete all tasks and escape!")


    #lobby description
    print("\nYou are in the school lobby.")
    print("The Math Room is to the north.")
    print("All other doors are locked.")

    # to  Get input and respond
    while True:
        command = input("\nWhat do you want to do? ").strip().lower()
        if command == "go north":
         return math_room()
        else:
          print("Invalid command. please type 'go north'.")
          
    
def graduation_chamber():
    print("\n--- GRADUATION CHAMBER ---")
    print("You have made it to the final room of your journey—the Graduation Chamber.")
    print("This is the last step before you can graduate, and it feels like an exam room.")
    print("The air is tense, and the walls are lined with whiteboards and desks. You can hear a faint ticking of a clock, reminding you of the time running out.")
    print("The Graduation Chamber is where your knowledge and skills will be tested one last time. It feels like the culmination of your entire journey.")
    print("\nThis is it—the final lap of your adventure. To graduate and escape, you must answer three questions correctly.")
    print("These questions will test your knowledge in three subjects: Math, Science, and History.")
    print("You will have two attempts for each question. If you fail to answer correctly, you will have to restart the game.")
    print("Good luck! The fate of your graduation rests in your hands...\n")
    print("If you successfully complete these three questions, you will gain access to your graduation cap and officially complete your journey.")

    # Puzzle 1: Math Question
    attempts = 0
    while attempts < 2:
        answer1 = input("\nPuzzle 1: What is the square root of 81?\n"
                   "a) 7\nb) 9\nc) 11\nYour answer: ").strip().lower()
        if answer1 == "b" or answer1 == "9":
            print("Correct!")
            break
        else:
            attempts += 1
            if attempts < 2:
                print("Wrong answer. Try again.")
            else:
              print("Wrong answer. You lose! You have failed to complete the task.")
              print("You are now sent back to the lobby to start over.")
              input("Press enter to restart the game....")
              start_game()
              return
    # Puzzle 2: Science Question
    attempts = 0
    while attempts < 2:
         answer2 = input("\nPuzzle 2: Which of these is a gas at room temperature?\n"
                   "a) Iron\nb) Water\nc) Oxygen\nYour answer: ").strip().lower()
         if answer2 == "c" or answer2 == "oxygen":
             print("Correct!")
             break
         else:
            attempts += 1
            if attempts < 2:
               print("Wrong answer. Try again.")
            else:
              print("Wrong answer. You lose! You have failed to complete the task.")
              print("You are now sent back to the lobby to start over.")
              input("Press enter to restart the game....")
              start_game()
              return
    # Puzzle 3: History Question
    attempts = 0
    while attempts < 2:
          answer3 = input("\nPuzzle 3: Who was the first president of the United States?\n"
                   "a) Thomas Jefferson\nb) George Washington\nc) Abraham Lincoln\nYour answer: ").strip().lower()
          if answer3 == "b" or answer3 == "george washington":
             print("Correct!")
             break
          else:
            attempts += 1
          if attempts < 2:
               print("Wrong answer. Try again.")
          else:
             print("Wrong answer. You lose! You have failed to complete the task.")
             print("You are now sent back to the lobby to start over.")
             input("Press enter to restart the game....")
             start_game()
             return
    print("\nWell done! You've completed the Graduation Chamber challenge.")
    print("You’ve passed the final exam!")

    print("Use the command 'collect graduation cap' to finally graduate and complete your journey.")
    # Wait for the player to collect their graduation cap
    while True:
        command = input("\nWhat do you want to do? ").strip().lower()
        if command == "collect graduation cap":
             print("Graduation cap collected and added to inventory.")
             inventory.append("graduation cap")
             print("Congratulations! You have completed your journey and officially graduated and escaped the school!")
             break
        else:
           print("Invalid command. To continue, type 'collect graduation cap'.")




    
def science_lab():
    print("\n--- SCIENCE LAB ---")
    print("You are now in the Science Lab.")
    print("The air is dense with the smell of chemicals and the faint humming of machines.")
    print("Beakers bubble on the counters, and complex formulas are scribbled across the walls.")
    print("This room feels more intense, as if it's designed to push your brain to the limit.")
    print("\nCondition:")
    print("You must answer 4 challenging science-based puzzles.")
    print("You have ONLY 2 attempts per question.")
    print("If you fail any of the questions after two attempts, you will be sent back to the beginning of the game to start over.")
    print("\nReward:")
    print("If you successfully complete all 4 puzzles, you will receive the Master Key.")
    print("The Master Key will grant you access to the Graduation Chamber — the final step in your journey.")
    print("\nGood luck!")
    print("Remember, no shortcuts this time. All questions must be answered to earn the Master Key.")
    print("")

    # Puzzle 1
    attempts = 0
    correct = False
    while attempts < 2:
        print("\nPuzzle 1: What is the chemical symbol for water?")
        print("a) H2O")
        print("b) CO2")
        print("c) NaCl")
        answer = input("Your answer: ").lower()
        if answer == "a" or answer == "h2o":
            print("Correct!")
            correct = True
            break
        else:
            attempts += 1
            print("Incorrect.")
    if not correct:
        print("\nYou have failed to answer correctly. You are being sent back to the start of the game.")
        input("Press Enter to restart...")
        start_game()
        return

    # Puzzle 2
    attempts = 0
    correct = False
    while attempts < 2:
        print("\nPuzzle 2: Which gas do plants absorb from the atmosphere during photosynthesis?")
        print("a) Oxygen")
        print("b) Carbon Dioxide")
        print("c) Nitrogen")
        answer = input("Your answer: ").lower()
        if answer == "b" or answer == "carbon dioxide":
            print("Correct!")
            correct = True
            break
        else:
            attempts += 1
            print("Incorrect.")
    if not correct:
        print("\nYou have failed to answer correctly. You are being sent back to the start of the game.")
        input("Press Enter to restart...")
        start_game()
        return

    # Puzzle 3
    attempts = 0
    correct = False
    while attempts < 2:
        print("\nPuzzle 3: What part of the cell contains the genetic material?")
        print("a) Cytoplasm")
        print("b) Mitochondria")
        print("c) Nucleus")
        answer = input("Your answer: ").lower()
        if answer == "c" or answer == "nucleus":
            print("Correct!")
            correct = True
            break
        else:
            attempts += 1
            print("Incorrect.")
    if not correct:
        print("\nYou have failed to answer correctly. You are being sent back to the start of the game.")
        input("Press Enter to restart...")
        start_game()
        return

    # Puzzle 4
    attempts = 0
    correct = False
    while attempts < 2:
        print("\nPuzzle 4: What force pulls objects toward the Earth's center?")
        print("a) Magnetism")
        print("b) Gravity")
        print("c) Friction")
        answer = input("Your answer: ").lower()
        if answer == "b" or answer == "gravity":
            print("Correct!")
            correct = True
            break
        else:
            attempts += 1
            print("Incorrect.")
    if not correct:
        print("\nYou have failed to answer correctly. You are being sent back to the start of the game.")
        input("Press Enter to restart...")
        start_game()
        return

    print("\nCongratulations! You have successfully completed all the Science Lab challenges.")
    print("You have obtained the Master Key.")
    while True:
        collect = input("Enter 'collect master key' to collect it and add it to your inventory: ").strip().lower()
        if collect == "collect master key":
           inventory.append("Master Key")
           print("Master Key collected and added to your inventory.")
           print("Now that you have the Master Key, you can access the Graduation Chamber- the final room.")
        else:
          print("Invalid command. Please enter 'collect master key' to collect the key.")
      # go to the Graduation Chamber
        print("\nThe Graduation Chamber is to the north.")
        direction = input("What do you want to do? ").lower()
        if "go north" in direction:
            print("You are heading to the Graduation Chamber...")
            graduation_chamber()
        else:
            print("Invalid choice. Please enter 'go north' to continue.")

 
    
def history_hall():
    print("---HISTORY HALL---")
    print("\nWelcome to the History Hall.")
    print("As you step into the room, the atmosphere shifts.")
    print("Ancient scrolls line the walls, dusty portraits of legendary figures stare down at you,")
    print("and a giant timeline stretches across the room like a mural of forgotten times.")
    print("In this room, your knowledge of history will be tested.")
    print("You will be asked three questions, but since you chose the History Hall, you are allowed to skip one question of your choice.")
    print("You will have two attempts for each question you choose to answer.")
    print("Answer wisely.")
    print("\nOnce you successfully complete the challenges in this room, a hidden compartment will open,")
    print("revealing a Hall Pass — your only way forward into the Graduation chamber- the final step in your journey.")
    print("But remember, the Hall Pass is only granted if you complete the puzzles. Good luck!")
    print("")

    #puzzle 1
    skip_choice = input("Which puzzle would you like to skip? (Enter 1, 2, or 3): ")
    def ask_puzzle(puzzle_num, question, options, correct_option):
       print(f"\nPuzzle {puzzle_num}:")
       print(question)
       for option in options:
           print(option)
       attempts = 0
       while attempts < 2:
           answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
           if answer == correct_option:
               print("Correct!")
               return True
           else:
               attempts += 1
               if attempts < 2:
                   print("Incorrect. Try again.")
       print("Wrong answer.you lose ! You have failed to complete the task.")
       input("Press Enter to restart the game....")
       start_game()  
       return False
    # Puzzle 1
    if skip_choice != "1":
       ask_puzzle(
           1,
           "Who was the first President of the United States?",
           ["A. Abraham Lincoln", "B. George Washington", "C. Thomas Jefferson", "D. John Adams"],
           "B"
       )
    else:
       print("\nYou chose to skip Puzzle 1.")

   # Puzzle 2
    if skip_choice != "2":
       ask_puzzle(
           2,
           "In which year did World War II end?",
           ["A. 1939", "B. 1942", "C. 1945", "D. 1950"],
           "C"
       )
    else:
       print("\nYou chose to skip Puzzle 2.")

   # Puzzle 3
    if skip_choice != "3":
       ask_puzzle(
           3,
           "What ancient civilization built the pyramids?",
           ["A. Romans", "B. Greeks", "C. Mesopotamians", "D. Egyptians"],
           "D"
       )
    else:
       print("\nYou chose to skip Puzzle 3.")
    print("\nCongratulations! You have completed the History Hall challenges.")
    print("The hidden compartment is now opened")
    print("You have obtained the Hall Pass.")
    while True:
        collect = input("Use the command 'collect hall pass' to collect the Hall Pass: ").strip().lower()
        if collect == "collect hall pass":
            inventory.append("Hall Pass")
            print("Hall Pass collected and added to your inventory.")
        else:
            print("Invalid command. you must type the correct command to collect Hall Pass")
        print("\nNow that you have your Hall Pass, you have gained access to the Graduation Chamber.") #* correct -add some code
        print("The graduation chamber is to the north")
        direction = input("What do you want to do? ").lower()
        if direction == "go north":
              graduation_chamber() 
        else:
            print("Invalid command. the graduation chamber is to the north")
        
       



    
def english_room():
    print("---ENGLISH ROOM---")
    print("\nYou are now in the English Room.")
    print("\nYou step into the English Room.")
    print("The room feels calm and quiet, with bookshelves lining the walls, filled with classic novels and grammar guides.")
    print("The faint smell of paper and ink fills the air.")
    print("In front of you, there is a desk with a notebook open.")
    print("As you flip through the pages, you find a passcode hidden between the notes.")
    print("But you can’t take it yet—it’s locked behind a puzzle that you must solve first.")
    print("\nYou must answer the English puzzle to earn the passcode. You have two attempts to get it right.")
    print("If you fail, you will be sent back to the lobby to start over.")

    # puzzle 1
    attempts= 0
    while attempts < 2:
       answer1 = input("\nPuzzle 1: Choose the correct word:\n'The student ___ going to the library.'\n"
                       "a) is\nb) are\nc) were\nYour answer: ").strip().lower()
       if answer1 == "a" or answer1 == "is":
           print("Correct!")
           break
       else:
           attempts += 1
           if attempts < 2:
               print("Wrong answer. Try again.")
           else:
               print("Wrong answer. you lose! You have failed to complete the task.")
               print("You are now sent back to the start of the game.")
               input("press enter to restart the game....")
               start_game()
               return
    # puzzle 2
    attempts = 0
    while attempts < 2:
       answer2 = input("\nPuzzle 2: Which sentence is grammatically correct?\n"
                       "a) Their going to the park.\n"
                       "b) They're going to the park.\n"
                       "c) There going to the park.\nYour answer: ").strip().lower()
       if answer2 == "b" or answer2 == "they're going to the park" or answer2 == "they're":
           print("Correct!")
           break
       else:
           attempts += 1
           if attempts < 2:
               print("Wrong answer. Try again.")
           else:
               print("Wrong answer. you lose! You have failed to complete the task.")
               print("You are now sent back to the start of the game.")
               input("press enter to restart the game....")
               start_game()
               return
    
    # puzzle 3
    attempts = 0
    while attempts < 2:
       answer3 = input("\nPuzzle 3: What is the synonym of the word 'happy'?\n"
                       "a) sad\nb) joyful\nc) angry\nYour answer: ").strip().lower()
       if answer3 == "b" or answer3 == "joyful":
           print("Correct!")
           break
       else:
           attempts += 1
           if attempts < 2:
               print("Wrong answer. Try again.")
           else:
               print("Wrong answer. you lose! You have failed to complete the task.")
               print("You are now sent back to the lobby to thestart of the game.")
               input("press enter to restart the game....")
               start_game()
               return
    print("\nWell done! You've completed the English Room challenge.")
    print("You’ve found the passcode!")
    print("Use the command 'collect passcode' to collect your reward.")
    # Wait for player to collect the passcode
    while True:
       command = input("\nWhat do you want to do? ").strip().lower()
       if command == "collect passcode":
           print("Passcode collected and added to inventory.")
           inventory.append("passcode")
           break
       else:
           print("Invalid command. To continue, type 'collect passcode'.")
    # transition to other rooms
    print("You have completed the English Room puzzle and now have the passcode.")
    print("You are at a crossroad. You can use the passcode to unlock one of two rooms, so choose wisely:")
    print("1. History Hall")
    print("2. Science Lab")
    while True:
        choice = input("Which room would you like to enter? (Enter '1' for History Hall or '2' for Science Lab): ")
        if choice == '1':
           print("\nYou've chosen History Hall!")
           print("Congratulations! You will now have the option to skip one of the three questions in the History Hall.")
           print("The history hall is to the west")

           direction = input("What do you want to do? ").lower()
           if direction == "go west":
                history_hall()  
           else:
              print("Invalid command. the history hall is to the west.")
    
        elif choice == '2':
            print("\nYou've chosen Science Lab!")
            print("Unlucky you! You won't have access to the bonus feature that lets you skip a question.")
            print("However, there will be an extra question in the Science Lab, making it a bit more challenging!")
            print("The science lab is to the east")

            direction = input("What do you want to do? ").lower()
            if direction == "go east":
                science_lab()
        else:
           print("\nInvalid choice! Please enter either '1' for History Hall or '2' for Science Lab.")

   
    
def math_room():
   print("\n You have entered the math room")
   print("There is a puzzle on the board.")
   print("you only have two attempts. after the second attempt, " \
   "you will lose the game which means you will be sent back to start the game from the beginning")
   # Puzzle 1
   attempts=0
   while attempts<2:
       answer1 = input("Puzzle 1: What is 7 + 5? ")
       if answer1.strip() == "12":
           print("Correct!")
           break
       else:
           attempts +=1
           if attempts < 2:
                print("Wrong answer. Try again.")
           else:
               print("wrong answer. you lose! you have failed to complete the task")
               print("you are now sent back to restart the game")
               input("press enter to restart the game....")
               start_game()
               return 
   # Puzzle 2
   attempts=0
   while attempts<2:
       answer2 = input("Puzzle 2: What is the square root of 49? ")
       if answer2.strip() == "7":
           print("Correct!")
           break
       else:
           attempts +=1
           if attempts<2:
              print("Wrong answer. Try again.")
           else:
               print("wrong answer. you lose! you have failed to complete the task")
               print("you are now sent back to restart the game")
               input("press enter to restart the game....")
               start_game()
               return 
               
   # Puzzle 3
   attempts=0
   while attempts<2:
       answer3 = input("Puzzle 3: What is 8 * 6? ")
       if answer3.strip() == "48":
           print("Correct!")
           break
       else:
           attempts +=1
           if attempts<2:
                print("Wrong answer. Try again.")
           else:
               print("wrong answer. you lose! you have failed to complete the task")
               print("you are now sent back to restart the game")
               input("press enter to restart the game....")
               start_game()
               return 
               
   print("\nCongratulations! You've successfully completed the challenge in the Math Room.")
   print("You've earned the key to unlock the English Room.")
   print("Use the command 'collect key' to collect your key.")
   # Wait for player to collect the key
   while True:
       collect_command = input("\nWhat do you want to do? ").strip().lower()
       if collect_command == "collect key":
           print("Key collected and added to inventory.")
           inventory.append("key")
           break
       else:
           print("Invalid command. To continue, type 'collect key'.")

    # transitiion to the english room
   print("\nYou now have the key to the English Room.")
   print("The English Room is to the south.")
   print("What do you want to do?")
   # to get input for going south
   while True:
       command = input().strip().lower()
       if command == "go south" and "key" in inventory:
           print("\nYou have used the key to unlock the English Room.")
           english_room()
           break
       else:
           print("Invalid command. To continue, type 'go south' to go to the English Room.")



#calling the function
start_game()
