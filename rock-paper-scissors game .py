import random
GameRunning = True
user_point = 0
pc_point = 0

print ("'p' means paper\n'r' means rock \n's' means scissors \n'q' means quit " )

def winner ():
    global user_point
    global pc_point
    if user_move == pc_move :
        print("it's a tie.")
    elif user_move == 's':
        if pc_move == 'r':
            pc_point += 1 
        else:
            user_point += 1
    elif user_move == 'p':
        if pc_move == 'r':
            user_point += 1 
        else :
            pc_point += 1 
    elif user_move == 'r':
        if pc_move == 'p':
            pc_point += 1 
        else :
            user_point += 1
    print(f'you\'r point :{user_point} \t 🤖\'s point :{pc_point} ')

while GameRunning :
    user_move = input("your move : ").lower()
    if user_move  not in ['q','s','r','p']:
        print("invalid move")
        continue 
    if user_move == 'q':
        print("Thanks for plying.")
        break
    pc_move = random . choice(['s','r','p'])
    print(f"🤖's move : {pc_move}")
    winner()
    if user_point == 3 :
        print("🤖 said 'Cheers to you'.")
        GameRunning = False
    elif pc_point ==3:
        print("🤖 wins this game.")
        GameRunning = False