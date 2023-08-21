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
result = [rock, paper, scissors]
entered_input = input("What do you choose: type 0 for rock, 1 for paper and 2 for scissors\n")
if entered_input == "0":
  print(f"What you chose is \n {rock}")
elif entered_input == "1":
  print(f"What you chose is \n {paper}")
elif entered_input == "2":
  print(f"What you chose is \n {scissors}")
else: 
  print("Invalid input")

print("What computer chose is ")
print(random.choice(result))
  



