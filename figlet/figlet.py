from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    f = random.choice(figlet.getFonts())

    if len(sys.argv) == 1:
        s = input("Input: ")
        figlet.setFont(font=f)
        print("Output:")
        print(figlet.renderText(s))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:")
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
