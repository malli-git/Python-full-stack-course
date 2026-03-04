#while

'''i=1
while i<=10:
    print(i)
    i=i+1'''

'''moves = 15
winning_point = int(input("Tell me how me moves is required to finish the game: "))
while moves >=1:
    if 15-winning_point == moves:
        print("You won the Game")
        break
    print(f'{moves} are left')
    moves-=1

else:
    print("game over")'''
                    
                
bullets = 10

while bullets>0:
    print(f'You Have {bullets} bullets,shoot them!')
    bullets-=1
else:
    print("game over")


