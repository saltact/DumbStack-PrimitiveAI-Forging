def main():
    sentence = input("Please enter your sentence: ");
    playback = playbackSpeed(sentence);
    print(playback);

def playbackSpeed(string):
    return string.replace(" ", "...");

main()