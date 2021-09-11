import random
"""
*** All boards in func***
"""
def hangman_boards(incorrect_ans):

  board0 = [
      "","","","","","","","","",      #0-8
      "",""," "," "," "," ","","","",         #9-17
      "",""," "," "," "," ","","","",         #18-26
      " "," "," ","",""," ","","","",       #27-35
      "",""," "," "," "," ","","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board1 = [
      "","","","","","","","","",      #0-8
      "",""," "," "," "," ","|","","",         #9-17
      "",""," "," "," "," ","|","","",         #18-26
      " "," "," ","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board2 = [
      "","","+","-","-","-","+","","",      #0-8
      "",""," "," "," "," ","|","","",         #9-17
      "",""," "," "," "," ","|","","",         #18-26
      " "," "," ","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board3 = [
      "","","+","-","-","-","+","","",      #0-8
      "","","|"," "," "," ","|","","",         #9-17
      "",""," "," "," "," ","|","","",         #18-26
      " "," "," ","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board4 = [
      "","","+","-","-","-","+","","",      #0-8
      "","","|"," "," "," ","|","","",         #9-17
      "","","O"," "," "," ","|","","",         #18-26
      " "," "," ","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board5 = [
      "","","+","-","-","-","+","","",      #0-8
      "","","|"," "," "," ","|","","",         #9-17
      "","","O"," "," "," ","|","","",         #18-26
      " ","|"," ","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board6 = [
      "","","+","-","-","-","+","","",      #0-8
      "","","|"," "," "," ","|","","",         #9-17
      "","","O"," "," "," ","|","","",         #18-26
      " ","|","-","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]
  board7 = [
      "","","+","-","-","-","+","","",      #0-8
      "","","|"," "," "," ","|","","",         #9-17
      "","","O"," "," "," ","|","","",         #18-26
      "-","|","-","",""," ","|","","",       #27-35
      "",""," "," "," "," ","|","","",          #36-44
      "=","=","=","=","=","=","=","=","=",  #45-53
    ]


  if incorrect_ans == 0:
    return board0
  elif incorrect_ans == 1:
    return board1
  elif incorrect_ans == 2:
    return board2
  elif incorrect_ans == 3:
    return board3
  elif incorrect_ans == 4:
    return board4
  elif incorrect_ans == 5:
    return board5
  elif incorrect_ans == 6:
    return board6
  elif incorrect_ans == 7:
    return board7




"""
***This will display the board***
"""
def display_board(board):
  print(board[0]+'',board[1]+'',board[2]+'',board[3]+'',board[4]+'',board[5]+'',board[6]+'',board[7]+'',board[8])
  print(board[9]+'',board[10]+'',board[11]+'',board[12]+'',board[13]+'',board[14]+'',board[15]+'',board[16]+'',board[17])
  print(board[18]+'',board[19]+'',board[20]+'',board[21]+'',board[22]+'',board[23]+'',board[24]+'',board[25]+'',board[26])
  print(board[27]+'',board[28]+'',board[29]+'',board[30]+'',board[31]+'',board[32]+'',board[33]+'',board[34]+'',board[35])
  print(board[36]+'',board[37]+'',board[38]+'',board[39]+'',board[40]+'',board[41]+'',board[42]+'',board[43]+'',board[44])
  print(board[45]+'',board[46]+'',board[47]+'',board[48]+'',board[49]+'',board[50]+'',board[51]+'',board[52]+'',board[53])
  

def get_random_word():
  words = [
    'apple', 'orange', 'banana', 'computer', 'sunday', 'programming', 'html is not a programming language'
  ]

  return random.choice(words)

def convert_word_to_letters(word):
  word_letters = list(word)
  return word_letters

def play_again():
  ask = input("do want paly again y/n: ")
  if ask == 'y':
    return True
  else:
    return False
  

#Show the board and blanks for letters


    
  #print("_ "*len(secret_word))



#display_blanks(solved_letters)


# Python program to find the common elements 
# in two lists 



  

#main
def main():
  #variables
  secret_word = convert_word_to_letters(get_random_word())
  solved_letters = []
  max_incorrect_ans = 10
  incorrect_ans = 0
  bad_ans = False
  game_is_running = True
  play_again_var = False
  blanks = "_"*len(secret_word)
  
  while game_is_running:
    #tu sa zobrazuju veci na terminaly
    display_board(hangman_boards(incorrect_ans=incorrect_ans))
    print(blanks)
    print(f"your incorrect answers: {incorrect_ans}")
    aksed_letter = input('write one letter: ')    #pyta sa hraca na pismeno

    if aksed_letter in solved_letters:  #ak som uz pismeno uhadol nemozem ho znovu napisat
      print('repeat')
    else:
      
      for i in range(len(secret_word)):   # ak je tam viac rovnakych tak sa vyplnia
        if aksed_letter in secret_word[i]:
          solved_letters.append(aksed_letter)
          bad_ans = False
          
          blanks_list = list(blanks)
          if secret_word[i] in aksed_letter:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
        
        else:         #ak odpoviem zle pismeno nastavy sa na True a pripocita mi to zlu odpoved
          bad_ans = True



      if bad_ans:   #ak je bad_ans true prida zlu odpoved
        if aksed_letter not in secret_word:
          incorrect_ans += 1
      
    #print(f'solved: {solved_letters}')
    #common_member(secret_word, solved_letters) 
    


    if "_" not in blanks:   #ak v blanks nieje uz ziadna medzera hra skonci
      print("********************************")
      print(f'you won!!!  \nYour count of incorrect ansewrs is: {incorrect_ans} \nThe word was: {blanks}')
      print('')
      print("********************************")

      game_is_running = False
      play_again_var = play_again()
    elif incorrect_ans == max_incorrect_ans:
      print('you loose')
      game_is_running = False
      play_again_var = play_again()
    
    if play_again_var :
      secret_word = convert_word_to_letters(get_random_word())
      solved_letters = []
      max_incorrect_ans = 10
      incorrect_ans = 0
      bad_ans = False
      game_is_running = True
      blanks = "_"*len(secret_word)
      play_again_var = False


main()
