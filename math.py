import random
import tkinter as tk
def get_limits():
    ok=1
    while ok==1:
        inf_limit = input("Enter inferior limit:")
        sup_limit=input("Enter superior limit:")
        # print("low limit",inf_limit)
        # print("high limit",sup_limit)
        try:
            inf_limit=int(inf_limit)
            sup_limit=int(sup_limit)
        except:
            
            print("Limits have to be numbers")
            exit()
        if inf_limit > sup_limit:
            print("Inferior limit has to be smaller than superior limit")
            ok=1
        elif inf_limit == sup_limit:
            print("Limits have to be different")
            ok=1
        else:
            ok=0
    return int(inf_limit),int(sup_limit)
def get_random_number(num1,num2):
    return  random.randint(num1,num2)
def get_random_sign(signs):
    return random.choice(signs)
def do_math(a,b,sign):
    if sign == "+":
        a=a+b
        return a 
    elif sign == "-":
        a=a-b
        return a
    elif sign == "*":
        a=a*b
        return a
    else:
        a=a//b
        return a

def snow_ball_mode(signs_list):
    score=0
    low_limit,high_limit=get_limits()
    number1=get_random_number(low_limit,high_limit)
    number2=get_random_number(low_limit,high_limit)
    while number1 < number2:
            number1=get_random_number(low_limit,high_limit)
            number2=get_random_number(low_limit,high_limit)
    sign=get_random_sign(signs_list)
    print(number1,sign,number2,"= ")
            
    result=input()
    try:
        result=int(result)
    except:
        result=str(result)
    if isinstance(result,str):
        if result =="stop":
            print("Exiting game")
            return score
        else:
            print("Unknown answer")
            return score
    
    elif isinstance(result,int) and  result == do_math(number1,number2,sign):
        while 1 : 
            number2=get_random_number(low_limit,high_limit)
            sign=get_random_sign(signs_list)
            print(sign,number2,"?")
            user_result=input()
            try:
                user_result=int(user_result)
            except:
                user_result=str(user_result)
            if isinstance(user_result,str):
                if  user_result =="stop":
                    print("Exiting game")
                    return score
                else:
                    print("Unknown answer")
                    return score
            if isinstance(user_result,int) and  user_result == do_math(result,number2,sign):
                result=do_math(result,number2,sign)
                print("Correct")
                score=score+1
                # number1=get_random_number(a,b)
            else:
                print("Incorrect")
                print("Correct answer was:",do_math(result,number2,sign))
                # print(result)
                # print(do_math)
                return score

def normal_mode(signes_list):
        score=0
        low_limit,high_limit=get_limits()
        while 1 :
            number1=get_random_number(low_limit,high_limit) 
            number2=get_random_number(low_limit,high_limit)
            while number1 < number2:
                    number1=get_random_number(low_limit,high_limit)
                    number2=get_random_number(low_limit,high_limit)
            sign=get_random_sign(signes_list)
            print(number1,sign,number2,"=")
            user_result=input()
            try:
                user_result=int(user_result)
            except:
                user_result=str(user_result)
            if isinstance(user_result,str):
                if user_result =="stop":
                    print("Exiting game")
                    return score
                else:
                    print("Unknown answer")
                    return score
            if isinstance(user_result,int) and user_result == do_math(number1,number2,sign):
                # result=do_math(result,number2,sign)
                print("Correct")
                score=score+1
                # number1=get_random_number(a,b)
            else:
                print("Incorrect")
                print("Correct answer was",do_math(number1,number2,sign))
                # print(result)
                # print(do_math)
                return score


if  __name__ == "__main__":
    easy_signes_list=["+","-"]
    difficult_signes_list=["+","-","*","//"]
    print("Choose play style: 1.Normal 2.Snow-ball")
    mod=str(input("Style number "))
    score=-1
    if mod.strip() == "1":
        score=normal_mode(easy_signes_list)
    elif mod.strip() == "2":
        score=snow_ball_mode(easy_signes_list)
    else:
        print("Invalid Style ")
    
    if score != -1:
        print("You solved ",score," calculations")