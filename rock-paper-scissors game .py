import random
GameRunning = True

print ("'p' means paper\n'r' means rock \n's' means scissors \n'q' means quit " )

while GameRunning :
    user_move = input("your move : ").lower()
    if user_move  not in ['q','s','r','p']:
        print("invalid move")
        continue 
    if user_move == 'q':
        print("Thanks for plying.")
        break
    pc_move = random . choice(['s','r','p'])
    print(f"pc's move : {pc_move}")