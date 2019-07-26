import random
print("歡迎來訓練拍國古拳法：猜拳！")
human_name = str(input("請輸入名號："))
print("拍國古拳法 Beta Come 大師對上 " + human_name + " 選手！")
human_score = computer_score = 0
round_x = wb = 0
human_boxing = computer_boxing = ["scissors","paper","rock"]

def round_fight(r):
    global wb
    if human_score < 3 and computer_score < 3:
        r = r + 1
        print("第 "+ str(r) +" 回合。")
        wb = 0
        human_go(human_name)
    else:
        whoIsWinner(human_score,computer_score,r)

def boxing (temp):
    global wb
    if temp.isdecimal(): 
        if int(temp) >= 1 and int(temp) <= 3:
            hb = human_boxing[int(temp) - 1]
            return hb
        else:
            wb = wb + 1
            human_go(human_name)
        
    else:
        if temp.upper() == "S":
            temp = 1
            hb = human_boxing[int(temp) - 1]
            return hb
        elif temp.upper() == "P":
            temp = 2
            hb = human_boxing[int(temp) - 1]
            return hb
        elif temp.upper() == "R":
            temp = 3
            hb = human_boxing[int(temp) - 1]
            return hb
        else:
            wb = wb + 1
            human_go(human_name)
            
def battle (hb,cb):
    global human_score
    global computer_score
    global round_x
    if hb == "scissors" and cb == "paper" or hb == "paper" and cb == "rock" or hb == "rock" and cb == "scissors":
        human_score = human_score + 1
        print(human_name + " 選手的 " + hb + " 擊中 Beta Come 大師！\n比數 " + str(human_score) + "：" + str(computer_score) + "\n")
        round_x = round_x + 1
    elif cb == "scissors" and hb == "paper" or cb == "paper" and hb == "rock" or cb == "rock" and hb == "scissors":
        computer_score = computer_score + 1
        print(human_name + " 選手中了 Beta Come 大師一招 " + cb + "！\n比數 " + str(human_score) + "：" + str(computer_score) + "\n")
        round_x = round_x + 1
    else:
        print(human_name + " 選手和 Beta Come 大師都用了 " + hb + " 擋下了對方攻擊！\n比數維持 " + str(human_score) + "：" + str(computer_score) + "\n")
        round_x = round_x + 1
    round_fight(round_x)
        
def human_go(n):
    temp = input("還請 " + str(n) + " 選手請出拳：\n1. (S)cissors; \n2. (P)aper; \n3. (R)ock \n") if wb >= 1 else input(str(n) + " 選手請出拳：\n1. (S)cissors; \n2. (P)aper; \n3. (R)ock \n")
    hb = boxing(temp)
    if hb != "":
        battle(hb,computer_go())
    else:
        return

def computer_go():
    cb = computer_boxing[random.randint(1,3) - 1]
    return cb

def whoIsWinner(hs,cs,rx):
    if hs > cs :
        print("恭喜 " + human_name + " 練成拍國古拳法！\n以 "+ str(hs) +" 比 "+ str(cs) + " 在 " + str(rx) + " 回合擊敗 Beta Come 大師！")
        continue_game = input("是否結束？ 1. 是； 2. 否。")
    else:
        print("恭喜 Beta Come 大師以 "+ str(hs) +" 比 "+ str(cs) + " 在 " + str(rx) + " 回合擊敗 " + human_name + "！\nBeta Come 大師對 " + human_name + "說：「回家耕田吧！」")
        continue_game = input("是否雪恥？ 1. 否； 2. 是。")
    playAgain (int(continue_game))
    
def playAgain (continue_game):
    global human_score
    global computer_score
    global round_x
    if continue_game == 1:
        print("有空再來！")
        round_x = 0
        human_score = 0
        computer_score = 0
        return
    elif continue_game == 2:
        round_x = 0
        human_score = 0
        computer_score = 0
        round_fight(round_x)
    else:
        print("來亂的，掰掰")
        round_x = 0
        human_score = 0
        computer_score = 0
        return

round_fight(round_x)
