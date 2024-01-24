# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


#Nikita Harčenkovs, 10.B, 24/01/2024


print("Spēlēsim Cirku!")
print("Jūsu galvenais mērķis tikt laukuma pēdējā laukumiņā!(kopā 100 laukumiņi)")


import random
computer = int(1)
red = int(-11)
red2 = int(-21)
blue = int(9)
blue2 = int(19)
g = 0
loopcounter = g



while(loopcounter <= 26):
 loopcounter += 1
 if loopcounter == 26:
     print("Neviens nevinēja!")
     break



 #Datora gājiens:
 print(loopcounter, "gājiens")
 answer = input("Esat gatavi?")
 print("Sākam!")
 (random.randint(1, 6))
 computer_move = int(random.randint(1, 6))

 print("Dators kūstas par:", computer_move )

 computer = 1 + computer_move


 #sarkanās kapnītes:

 if computer == 18:
     def new_func(computer, red):
      computer = computer + red 
     print("Neveiksme dators tika uz sarkano kāpni!")


 if computer == 67:
     def new_func(computer, red2):
      computer = computer + red2 
     print("Neveiksme dators tika uz sarkano kāpni!")


 if computer == 80:
     def new_func(computer, red):
      computer = computer + red 
     print("Neveiksme dators tika uz sarkano kāpni!")


 if computer == 74:
     def new_func(computer, red):
      computer = computer + red 
     print("Neveiksme dators tika uz sarkano kāpni!")


 #zilas kapnītes:

 if computer == 15:
     def new_func(computer, blue):
      computer = computer + blue 
     print("Paveicas! Dators tika uz zilu kapnīti!")


 if computer == 33:
     def new_func(computer, blue2):
      computer = computer + blue2 
     print("Paveicas! Dators tika uz zilu kapnīti!")


 if computer == 39:
     def new_func(computer, blue):
      computer = computer + blue
     print("Paveicas! Dators tika uz zilu kapnīti!")


 if computer == 87:
     def new_func(computer, blue):
      computer = computer + blue
     print("Paveicas! Dators tika uz zilu kapnīti!")

 print("Jūsu opponents atrodas uz:", computer)



 print("Jūsu gajiens!")
 answer = input("Esat gatavi?")
 #Jūsu gājiens:



 (random.randint(1, 6))
 player_move = int(random.randint(1, 6))

 print("Jūs kūstāties par:", player_move )

 player = 1 + player_move


 #sarkanas kapnītes:

 if player == 18:
   def new_func(player, red):
    player = player + red 
   print("Neveiksme! Jūs tikat uz sarkano kāpni!")

 if player == 67:
     def new_func(player, red2):
      player = player + red2 
     print("Neveiksme! Jūs tikat uz sarkano kāpni!")

 if player == 80:
     def new_func(player, red):
      player = player + red 
     print("Neveiksme! Jūs tikat uz sarkano kāpni!")

 if player == 74:
     def new_func(player, red):
      player = player + red 
     print("Neveiksme! Jūs tikat uz sarkano kāpni!")


 #zilas kapnītes:

 if player == 15:
     def new_func(player, blue):
      player = player + blue 
     print("Paveicas! Dators tika uz zilu kapnīti!")

 if computer == 33:
     def new_func(player, blue2):
      player = player + blue2 
     print("Paveicas! Dators tika uz zilu kapnīti!")

 if player == 39:
     def new_func(player, blue):
      player = player + blue 
     print("Paveicas! Dators tika uz zilu kapnīti!")

 if player == 87:
     def new_func(player, blue):
      player = player + blue 
     print("Paveicas! Dators tika uz zilu kapnīti!")


 print("Jūsu pozīcija:", player)


 if player == 100:
     print("Jūs vinējat!")

 if computer == 100:
     print("Dators vinēja!")
