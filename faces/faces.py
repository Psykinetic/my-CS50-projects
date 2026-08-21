def main():
    emoji = convert(input())
    print(emoji)

def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoticon


main()
