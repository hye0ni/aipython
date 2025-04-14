import random

def play_random_choice_game():
    choices = ["가위", "바위", "보"]

    while True:
        computer_choice = random.choice(choices)
        print("다음 중 하나를 선택하세요:")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

        user_input = input("당신의 선택 (1-3 또는 '종료'): ")

        if user_input.lower() == '종료':
            print("게임을 종료합니다.")
            break

        try:
            user_choice_index = int(user_input) - 1
            if 0 <= user_choice_index < len(choices):
                user_choice = choices[user_choice_index]
                print(f"당신의 선택: {user_choice}")
                print(f"컴퓨터의 선택: {computer_choice}")

                if user_choice == computer_choice:
                    print("무승부입니다!")
                elif (user_choice == "가위" and computer_choice == "보") or \
                     (user_choice == "바위" and computer_choice == "가위") or \
                     (user_choice == "보" and computer_choice == "바위"):
                    print("당신이 이겼습니다!")
                else:
                    print("컴퓨터가 이겼습니다!")
                print("-" * 20)
            else:
                print("잘못된 선택입니다. 1에서 3 사이의 숫자를 입력하거나 '종료'를 입력하세요.")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하거나 '종료'를 입력하세요.")

if __name__ == "__main__":
    print("3가지 선택 랜덤 게임")
    print("=" * 20)
    play_random_choice_game()