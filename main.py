
import random
from art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## drawing function
def draw(person):
  """adds one card to the person's list"""
  card = random.choice(cards)
  person.append(card)
  return card

def ace_check(person):
  """checks if there's an ace and replaces it with a 1 if the score is too high."""
  score = sum(person)
  if 11 in person and score > 21:
    person.remove(11)
    person.append(1)
    score = sum(person)


##let's start

play = input("Do you want to play a game of Blackjack? Y/N   ").lower()
while play == "y":
  print(logo)
  ## empty hands
  user = []
  pc = []

  ## drawing the first 2 cards cards and calculating scores
  draw(user)
  draw(user)
  draw(pc)
  draw(pc)

  user_score = sum(user)
  pc_score = sum(pc)
  


##output
  print(f"    Your cards {user}, your score: {user_score}")
  print(f"    Computer's card {pc[0]}")
  
## Blackjack check
  if user_score == 21:
    print("You have a blackjack. You won")
    play = input("Do you want to play another game of Blackjack? Y/N   ")
    clear()
  if pc_score == 21:
    print(f"Computer has a blackjack. {pc} Computer won")
    play = input("Do you want to play another game of Blackjack? Y/N   ")
    clear()

  
  else:
## new card
    new_card = input("""Type "y" to get another card, "n" to pass   """ ).lower()
  
    while new_card =="y":
      draw(user)
      ace_check(user)
      user_score = sum(user)
      if user_score >= 21:
        print(f"    Your cards are {user}, your score is {user_score}.")
        new_card = "n"
      else: 
        new_card = input(f"    Your cards are {user}, your score is {user_score}. Do you want another card or do you pass? Y/N   ").lower()
  
    ## PC draws
    while pc_score < user_score:
      ace_check(pc)
      pc_score = sum(pc)
      if pc_score < 17 or (user_score <= 21 and pc_score < user_score):
        draw(pc)
        print(f"Computer draws a card. {pc}")
      else:
        break
    ## final scores
    print(f"    Your final hand: {user}, your final score {user_score}")
    print(f"    Computer's final hand: {pc}, computer's final score {pc_score}")
  
  
    ## Victory conditions
  
    if pc_score > 21 and user_score <= 21:
      print("GG! You win!")
    elif pc_score <= 21 and user_score <= 21 and pc_score < user_score:
      print("GG! You win!")
  
    elif pc_score <= 21 and user_score <= 21 and user_score < pc_score:
      print("You lose!")
  
    elif user_score > 21 and pc_score <= 21:
      print("You went over. You lose.")
    elif pc_score > 21 and user_score > 21:
      print("You both went over.")
  
    elif pc_score == user_score:
      print("Tie.")
  
    play = input("Do you want to play another game of Blackjack? Y/N   ").lower()
    clear()
  