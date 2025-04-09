print("그림 출력 프로그램")
print("============================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("============================")
n = int(input("선택: "))
# 만약에 1을 입력하면 1번 캐릭터 출력
if n == 1: 
    print("고양이 그림")
# 만약에 2를 입력하면 2번 캐릭터 출력
elif n == 2: 
    print("강아지 그림")
# 3을 입력하면 3번 캐릭터 출력
elif n == 3: 
    print("토끼 그림")
# 잘못 입력하면 잘못 입력했다고 출력
else:
    print("잘못 입력")

def print_ascii_art(option):
    if option == 1:
        print("""
         /\_/\  
        ( o.o ) 
         > ^ <  
        """)
    elif option == 2:
        print("""
          / \__
         (    @\___
         /         O
        /   (_____ /
       /_____/   U
       |    |    |
       |    |    |
        """)
    elif option == 3:
        print("""
         (\_/)
        ( •_•)
        ( >🍪 ) 
        """)
    else:
        print("잘못 입력했습니다")

# 사용자로부터 입력 받기
try:
    user_input = int(input("1, 2, 3 중 번호를 입력하세요: "))
    print_ascii_art(user_input)
except ValueError:
    print("잘못 입력했습니다")
    user_input = 0  # 오류가 나면 기본값 0으로 설정

def play(option):
    print("선택한 그림 반복 출력")
    print_ascii_art(option)

print("5번 출력 프로그램 시작")
for i in range(5):
    play(user_input)
print("5번 출력 프로그램 종료")

print("0을 입력하면 종료 프로그램 시작 ")
while True:
    try:
        command = int(input("숫자를 입력하세요 (0 입력 시 종료): "))
        if command == 0:
            break
    except ValueError:
        print("숫자를 입력해주세요.")
print("0을 입력하면 종료 프로그램 종료 ")