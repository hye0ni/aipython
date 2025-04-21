from rich import print
from rich.panel import Panel
from rich.text import Text

# 🐰 토끼 아스키 아트
rabbit_art = r"""
 (\(\ 
 ( -.-)  
 o_(")(")
"""

# 🐿️ 다람쥐 아스키 아트
squirrel_art = r"""
  (\__/)
 ( •ㅅ•)
 / 　 づ
"""

# 🌰 도토리 아스키 아트
acorn_art = r"""
  __
 / o\_
 \__/
"""

# 🐱 고양이 아스키 아트
cat_art = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

def main():
    print("[bold cyan]🌟 Rich 스타일 & 아스키 아트 실험실[/bold cyan]")
    print("[green]입력해보세요: '토끼', '다람쥐', '고양이' 또는 스타일 마크업 문장[/green]")
    print("종료하려면 'exit'을 입력하세요.\n")

    while True:
        user_input = input("🎨 입력 > ").strip().lower()

        if user_input in ["exit", "quit"]:
            print("\n[bold yellow]프로그램을 종료합니다. 안녕히 가세요! 👋[/bold yellow]")
            break

        elif user_input == "토끼":
            text = Text.from_markup("[bold magenta]깡총![/bold magenta]")
            art_panel = Panel.fit(rabbit_art + "\n" + str(text), title="🐰 토끼", border_style="magenta")
            print(art_panel)

        elif user_input == "다람쥐":
            message = "[bold sandy_brown]다람쥐와 도토리![/bold sandy_brown]"
            art = squirrel_art + "\n" + acorn_art
            print(Panel.fit(art + "\n" + message, title="🐿️ 다람쥐", border_style="sandy_brown"))

        elif user_input == "고양이":
            message = Text.from_markup("[bold yellow]냥[/bold yellow]")
            art_panel = Panel.fit(cat_art + "\n" + str(message), title="🐱 고양이", border_style="yellow")
            print(art_panel)

        else:
            try:
                styled_text = Text.from_markup(user_input)
                print(Panel(styled_text, border_style="bright_blue", title="[bold magenta]미리보기[/bold magenta]", padding=(1, 2)))
            except Exception as e:
                print(f"[red]❌ 오류가 발생했습니다: {e}[/red]")
                print("[dim]형식 예시: [bold white on red]강조된 텍스트[/bold white on red][/dim]\n")

if __name__ == "__main__":
    main()

