#1
def sum(a,b):
    ad = a+b
    return ad


#2
def sub(a,b):
    su = a-b
    return su


#3
def mul(a,b):
    mu = a*b
    return mu


#4
def div(a,b):
    di = a/b
    return di


#5
def distance(x1,x2,y1,y2):
    dis = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return dis


#6
def title():
    lylics = "Switch sides and I'm beside you."
    t = lylics[21:31]
    return t


#7
def reverseStr(string):
    rev = string[::-1]
    return rev


#8
def introduce():
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    school = input("재학중인 학교를 입력하세요 : ")
    birthday = input("생일을 입력하세요 : ")

    month = int(birthday[2:4])
    date = int(birthday[4:6])

    intro = "제 이름은 {}입니다. 취미는 {}입니다. 저는 {}를 다니고 있습니다. 제 생일은 {}월 {}일 입니다.".format(name, hobby, school, month, date)
    print(intro)


#9
def calc():
    a = input("첫 번째 수를 입력하세요 : ")
    b = input("두 번째 수를 입력하세요 : ")

    a = int(a)
    b = int(b)

    print("두 수의 합 : ",a+b)
    print("두 수의 차 : ",a-b)
    print("두 수의 곱 : ",a*b)
    print("두 수의 몫 : ",a//b)