rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice =input('What do you choose? Type: \n0 for 🪨 \n1 for 📃 \n2 for ✂️ \nAnswer: ')
props =[rock, paper, scissors]

#player
player = int(choice)
print(props[player])
  
# Computer
computer = random.randint(0,2)
print('Computer Chose:\n' + props[computer])

#validation
if player >= 3 or player < 0: 
  print("You typed an invalid number, you lose!") 
elif player == 0 and computer == 2:
  print("You win!")
elif computer == 0 and player == 2:
  print("You lose")
elif computer > player:
  print("You lose")
elif player > computer:
  print("You win!")
elif computer == player:
  print("It's a draw")