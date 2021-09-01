import random
import easygui
count = 0

def rule():
    print()
    print("카드를 뽑아서 카드 숫자들의 합이 21에 가까우면 이깁니다.")
    print("숫자의 합이 21이면 블랙잭으로 승리하고,")
    print("21을 넘으면 버스트로 패배하게 됩니다.")
    print("카드 A는 1과 11중 숫자를 선택할 수 있습니다.")
    print()
############################################
def card(hand):
    a =cardNum.pop()
    hand.append(a)
####################################
def plus(hand):
    result = 0
    for a in hand :
          if a == 'J' or a == 'Q' or a == 'K':
              sc = 10
          elif a == 'A':
              if hand == comhand:
                  if len(hand) == 2:
                      sc = 11
                  else :  #컴퓨터가 카드를 한장더 뽑았을 경우(3장)
                      if result <= 10:
                          sc = 11
                      else :
                          sc =1
              else:   
                  answer = easygui.buttonbox("A를 1과 11중 어떤 카드로 사용할 것인가요?",choices=['1','11'])
                

                  if answer == '1':
                      sc = 1
                  else:
                      sc = 11
          else :  #문자가 없는 경우 
              sc = a
          result = result + sc
    return result
###################################
def showC(hand):
    print("----------뽑은 카드---------- ")
    j = 0 
    for i in hand:
       print(" : "+str(hand[j]))
       j = j + 1
#####################################33
def BB(res):
    if res > 21 :
        print("&&& 버스트! &&&")
    elif res == 21 :
        print("&&& 블랙잭! &&&")
#########################################
def WL(resC, resP, mo, betmo):
    if resP == 21 :          #플레이어가 블랙잭
        if resC == 21:            #플레이어, 컴퓨터 블랙잭
            print("무승부!")
            mo = mymo
        else :                          #플레이어만 블랙잭              
            print("*^^* 플레이어 승리! *^^*")
            print(str(betmo)+"원을 획득하셨습니다.")
            mo = mo + betmo
            return mo
    else :                  #플레이어가 블랙잭이 아닌경우
        if reP > 21:        #플레이어가 버스트
            if reC > 21 :       #플레이어, 컴퓨터 버스트
                print("*-_-* 무승부! *-_-*")
            else :              #플레이어만 버스트
                print("*T.T* 플레이어 패배! *T.T*")
                print(str(betmo)+"원을 잃었습니다.")
                mo = mo - betmo
                return mo
        else :          #플레이어가 버스트가 아닌경우
            if reP > reC or reC > 21:
                print("*^^* 플레이어 승리! *^^*")
                print(str(betmo)+"원을 획득하셨습니다.")
                mo = mo + betmo
                return mo
            elif reP == reC :
                print("*-_-* 무승부! *-_-*")
                return mo
            else :
                print("*T.T* 플레이어의 패배! *T.T*")
                print(str(betmo)+"원을 잃었습니다.")
                mo = mo - betmo
                return mo
###########################################
def clean(hand):
    del hand[0::]
###########################################
def CA(hand):  #컴퓨터가 뽑은 2장의 합
    result = 0
    for a in hand:
        if a == 'K' or a == 'J' or a == 'Q':
            sc = 10
        elif a == 'A':
            sc = 11
        else :
            sc = a
        result = result + sc
    return result
###########################################
###########################################

comhand = []
playhand = []

print()
print("*~***~*BLACK JACK GAME*~***~*")
print()

ruleans = easygui.buttonbox("룰을 보시겠습니까? (yes / no) ",choices=['yes','no'])
if ruleans == 'yes' :
    rule()

print()
print("돈을 베팅하세요.")
print()
mymo = easygui.integerbox("당신이 가지고있는 금액을 입력하세요. ")
print()
#############################################
while(count == 0):
    print ("현재 당신이 가지고 있는 돈 : " + str(mymo))
    print()
    bet = easygui.integerbox("돈을 얼마거시겠습니까? ")
           
    while(mymo < bet) :
           print("현재 가지고 있는 돈이 부족합니다.")
           print()
           bet = int(input("돈을 얼마거시겠습니까? "))
           
    print ("현재 당신이 가지고 있는 돈 : " + str(mymo))

    print()
    print("==========GAME START==========")
    print()

    clean(comhand)
    clean(playhand)
    
    cardNum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K'] *4

    random.shuffle(cardNum)


    print("컴퓨터가 카드를 두 장 뽑습니다.")
    card(comhand)
    showC(comhand) # 카드 한장만 공개
    card(comhand)
    print()

    print("플레이어가 카드를 두 장 뽑습니다.")
    card(playhand) 
    card(playhand)
    showC(playhand) #카드 두장 공개
    print()

    ans = easygui.buttonbox("카드를 더 뽑으시겠습니까? (y / n) ",choices=['yes','no'])
    if ans == 'yes' :
        card(playhand)
        showC(playhand)

    print()
    if CA(comhand) >= 18 :
        print("컴퓨터는 카드를 뽑지않습니다.")
    elif CA(comhand) <= 13 :
        card(comhand)
        print("컴퓨터가 카드를 뽑습니다.")
    else :
        num = random.randint(1,2)  #컴퓨터 카드뽑기 랜덤으로
        if num == 1 :
            card(comhand)
            print("컴퓨터가 카드를 뽑습니다.")
        else :
            print("컴퓨터가 카드를 뽑지않습니다.")
    print()
    
    reP = plus(playhand) #플레이어 카드 점수 총합
    reC = plus(comhand) #컴퓨터 카드 점수 총합

    print()
    print("@@@@@@@@@@@@@@@@@@@@@@@")
    print()
    print("## 컴퓨터 결과 : ")
    showC(comhand) #전체카드 공개
    print("[[합 : "+str(reC)+"]]")
    BB(reC)

    print()
    print("## 플레이어 결과 : ")
    showC(playhand) #전체카드 공개
    print("[[합 : "+str(reP)+"]]")
    BB(reP)

    print()
    mymo = WL(reC, reP, mymo, bet)
    print()

    if mymo == 0 :
        print("남은 돈이 없습니다. 다음에 다시 도전하세요.")
        break
    else:
        conti = easygui.buttonbox("게임을 계속 하실건가요?",choices=['yes','no'])
        print()
        if conti == 'no' :
            print("GAME OVER")
            count = 1