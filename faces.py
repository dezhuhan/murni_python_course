def main():
    text = input("Enter text: ")
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()