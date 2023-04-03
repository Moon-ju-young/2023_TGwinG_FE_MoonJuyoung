# 1번
def grade(score):
    if score>100 or score<0:
        return "error"
    elif score<60 :
        return 'F'
    elif score<70 :
        return 'D'
    elif score<80 :
        return 'C'
    elif score<90 :
        return 'B'
    else :
        return 'A'

    

# 2번
def quadrant(x, y):
    if x>0 :
        if y>0:
            return "제 1사분면"
        else:
            return "제 2사분면"
    else:
        if y>0:
            return "제 4사분면"
        else:
            return "제 3사분면"



# 3번
def leapYear(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0 :
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."



# 4번
def dice(a, b, c):
    if a==b and b==c :
        prize = 10000 + a*1000
    elif a==b or b==c or c==a:
        if a==b:
            prize = 1000 + a*100
        else:
            prize = 1000 + c*100
    else:
        prize = max(a,b,c)*100
    return prize


        
# 5번
def alarm(time):
    hour = time // 100
    minute = time % 100
    minute -= 45

    if minute < 0:
        minute += 60
        hour -= 1

    if hour < 0 :
        hour += 24
    
    return f"{hour}시 {minute}분"