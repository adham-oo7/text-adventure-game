import time    #importing time module to use print puase
import random  #import random to randomise monesters

def play_again() :
    #asking user if he would like to play again y= restart game   .  n= break the loop
    while True:
        play_again =input("Do you want to play again? (y/n)? : ").lower() 
        if play_again =="y":
            start_game()
            break
    
        elif play_again == "n" :
            print("See you soon!")
            break
    
        else:
            print("enter valid option (y/n)") 

def game_intro(random_enemy) :
    
    #introduction to the story of the game  
    print("On a dark rainy day")
    time.sleep(1.7)
    print("You found yourself lost in the creepy jungle alone")
    time.sleep(1.6)
    print("Your goal is to stay away from monsters and collet equipment that will help you in your journey ")
    time.sleep(1.8)
    print("Be careful there are many monesters there! .. good luck Wariorr." )
    time.sleep(1.8)
    print("Choose wisely! to get out of here safely.")

def rand_enemy () :
    enemies = ["Witch", "Evil wizard", "Boogyman", "Forest monster", "Godzilla","King Kong"]
 
    #randomise enemies
    return(random.choice(enemies))
    
    
    
                   
def start_game(): 
    #the main content of the game 
    # Generate the random enemy name once per game session
    enemy = rand_enemy()
    game_intro(enemy)


    
    while True :    
        ready = input("Are you ready for the adventure? (y/n) :  ").lower()

        if ready == "y":
            score = 0
            time.sleep(1.5)
            choice1 = input("(1) Hide in the cave / (2) Go to the house: ")
             
            if choice1 == "1":
                print ("you found the Legendary Sword! ")
                time.sleep(1)
                print("It can be useful in fighting monsters")
                time.sleep(1.8)
                score += 10
                print("Score = " + str(score))
                while True:
                    choice2 = input("(1) enter house / (2) stay at the cave: ")
                    if choice2 =="1":
                        print("you enterd "+ enemy +"'s house !")
                        time.sleep(1.8)
                        score += 5
                        print("Score = "+ str(score))
                        time.sleep(1.8)
                        while True:
                            choice3 = input("(1) attack/ (2) defence: ")
                            if choice3 == "1":
                                print("you attacked the "+ enemy +" with the Legendary Sword , you killed the "+ enemy +". Good job!")
                                time.sleep(1.8)
                                print("hurray ! you beat the "+ enemy )#####play again
                                score += 50
                                time.sleep(1)
                                print("Score = "+ str(score))
                                play_again() 
                                break
                            
                            elif choice3 == "2" : 
                                print("the "+enemy +" attack and you tried to defend but he is much stronger than you, you died immediatly")  
                                score -= 40
                                time.sleep(1.8)
                                print("Score = "+ str(score))
                                print("You won . Game Over")
                                time.sleep(1)
                                play_again()
                                break
                            else:
                                print("enter valid option (1/2)")
                            
                    elif choice2 == "2":
                        print("you died from hunger.")
                        score -= 40
                        time.sleep(1) 
                        print("Score = "+ str(score))
                        play_again() 
                        break
                          
            elif choice1 == "2":                           #Wrong Choice#
                print ("you enterd the "+enemy + " house you can't fight  with out an equipment ")
                score =- 40
                time.sleep(1.8)
                print("Score = "+ str(score))
                play_again() 
                break
              ##########you lost message /do you want to play again option#########       

            else:
                print("Enter vaild option")

        elif ready == "n":
            print("You missed a special adventure")
            break

        else:
            print("Please enter vaild option (y/n)") #checking user input
    
   

        
   

start_game () 
        
    
            



    






