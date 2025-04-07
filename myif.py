# 아스키 코드 그림 출력하기

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
if n == 2: 
    print("강아지 그림")
# 3을 입력하면 3번 캐릭터 출력
if n == 3: 
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

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한)반복하게 하고
# 만약에 0을 입력하면 종료되는 프로그램을 만드시오.