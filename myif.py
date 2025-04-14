# 아스키 코드 그림 출력 하기
def print_cat():
    cat_lines = [
        "\033[94m /\_/\  \033[0m",
        "\033[94m( o.o ) \033[0m",
        "\033[94m > ^ <  \033[0m"
    ]
    for line in cat_lines:
        print(line)

def print_dog():
    dog_lines = [
        "\033[33m / \\__\033[0m",
        "\033[33m(    @\\___\033[0m",
        "\033[33m /      O\033[0m",
        "\033[33m/  (_____/ \033[0m",
        "\033[33m/_____/  U\033[0m"
    ]
    for line in dog_lines:
        print(line)

def print_rabbit():
    rabbit_lines = [
        "\033[95m (\\_/)\033[0m",         # 문자열로 변경 + 역슬래시 이스케이프
        "\033[95m ( •_•)\033[0m",
        "\033[95m ( >🍪 )\033[0m"
    ]
    for line in rabbit_lines:
        print(line)

# 여기 함수를 잘 수정해서 두개의 프로그램이 될 수 있게 만들어 보기기
def play(n):
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토 끼")
    print("=====================")
    # n = 3
    # n = int(input("선택: "))

    # 만약에 1을 입력하면 1번 캐릭터 출력
    if n == 1:
        print("고양이")
        print_cat()
    # 만약에 2를 입력하면 2번 캐릭터 출력
    elif n == 2:
        print("강아지")
        print_dog()
    # 3을 입력하면 3번 캐릭터 출력
    elif n == 3:
        print("토끼")
        print_rabbit()
    # 잘못입력하면 잘못 입력했다고 출력
    else:
        print("잘못입력")

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.
print("\n5번 출력 프로그램 시작")
for i in range(5):
    play(i % 3 + 1) # 1, 2, 3 순서대로 출력

print("5번 출력 프로그램 종료\n")

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한)반복하게 하고
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오.
print("0을 입력하면 종료 프로그램 시작 ")
while True: # 무한 반복 (계속 참)
    # 만약에 0이면  break
    try:
        print("\033[46m선택(1-3) 종료(0): \033[0m", end="") # 배경색 적용 및 줄바꿈 방지
        n_str = input()
        n = int(n_str) # 여기서 ValueError 발생 가능
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue # 다시 입력 받기 위해 반복문 처음으로 돌아감

    if n == 0:
        break
    play(n) # play 함수는 1, 2, 3 외의 숫자를 받으면 "잘못입력" 처리
# 여기까지 하면 되겠네
print("\033[31m\033[4m0을 입력하면 종료 프로그램 종료 \033[0m")