# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    sum = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]*2 == lst[j]:
                sum+=1
    return sum



# 2번
def pascal(n):
    l = [1]
    for i in range(n-1):
        for j in range(len(l)-1, 0, -1):
            l[j] += l[j-1]
        l.append(1)
    return l



# 3번
def beerRefrigerator(n):
    
    li=[]
    for i in range(1,n//2):
        temp = n//i
        if n%i == 0:
            for j in range(i,temp):
                if temp%j == 0:
                    li.append([temp//j,j,i])

    surface = (lambda l: l[0]*l[1] + l[1]*l[2] + l[2]*l[0])
    best = min(li, key=surface)
    best.sort()
    best.reverse()

    return f"{best[0]} X {best[1]} X {best[2]}"



# 4번
def matrixMul(mat1, mat2):
    li=[]
    for n in range(len(mat1)):
        small = []
        for k in range(len(mat2[0])):
            temp=0
            for m in range(len(mat2)):
                temp += mat1[n][m] * mat2[m][k]
            small.append(temp)
        li.append(small)
    return li