#--------------------Variables Shorts-------------------
def main():
    guess = get_guess();
    if guess == 50:
        print('Correct!');
    else:
        print('Incorrect!')
    # greeting = greet("Hello, there! Is anyone home?");
    # print(greeting);
    # global emoticon;
    # emote("Hi there,")
    # emoticon = ":D"
    # emote("How are you doing?")
    name = "randy smith"
    print(name.capitalize());


def get_guess():
    guess = 50;
    return guess;


#-------------------Return Values Short-----------------
def greet(input):
    if "Hello" in input:
        return "Hello, there!"
    else:
        return "I'm not sure what you mean."


#--------------------Side Effects Short-----------------
emoticon = "v.v";
def emote(input):
    print(input, emoticon);

#---------------------String Methods------------------

main();

