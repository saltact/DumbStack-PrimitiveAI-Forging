def main():
    emoticon = input("Enter your emoticon: ");
    emoji = convert(emoticon);
    print(emoji);
    

def convert(text):
    text = text.replace(":)","🙂");
    text = text.replace(":()","🙁");
    text = text.replace("T-T","😭");
    return text;


main()