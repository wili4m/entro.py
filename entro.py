import random, string, math

size = 50
numbers = True
uppercase = True
symbols = True
autoGen = 5
inputData = "<<<"
outputData = ">>>"
high_entropy = 800
median_entropy = 500

def bar():
    print("-" * 50)

def error():
    print("[Error] You must answer 'Y or N'\n")
    exit(1)

def gen_passwd(size, numbers, uppercase, symbols):
    chars = string.ascii_lowercase
    if numbers:
        chars += string.ascii_uppercase
    if uppercase:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    passwd = ''.join(random.choice(chars) for a in range(size))
    return passwd

def check_entropy(passwd):
    countSymbols = string.punctuation
    sumSymbols = sum(1 for char in passwd if char in countSymbols)
    length = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    N = len(length)
    L = len(passwd)
    entropy = math.log2(N ** L)
    entropy = entropy * sumSymbols
    return entropy

bar()
print("Automagically generated passwords:")
bar()
counter = 1

while True:
    if counter <= autoGen:
        passwd = gen_passwd(size, numbers, uppercase, symbols)
        print(f"{counter}: {passwd}")
        counter = counter + 1
    else:
        print()
        userParams = input(f"{inputData} Would you like to specify the password format? [y/N]:").strip().lower()

        if userParams == "y":

            userSize = input(f"\n{inputData} Amount of characters: ")

            if not userSize.isdigit():
                print("[Error] Value not accepted")
                exit(1)

            else:
                userSize = int(userSize)

            userNumbers = input(f"{inputData} Include numbers? [Y/n]: ").strip().lower()
            if not userNumbers or userNumbers == "y" or userNumbers == "yes":
                userNumbers = "y"
                if userNumbers.isalpha():
                    userNumbers = True
                else:
                    userNumbers = False
            else:
                error()

            userUpper = input(f"{inputData} Include uppercase characters? [Y/n]: " ).strip().lower()
            if not userUpper or userUpper == "y" or userUpper == "yes":
                userUpper = "y"
                if userUpper.isalpha():
                    userUpper = True
                else:
                    userUpper = False
            else:
                error()

            userSymbols = input(f"{inputData} Include symbols? [Y/n]: ").strip().lower()
            if not userSymbols or userSymbols == "y" or userSymbols == "yes":
                userSymbols = "y"
                if userSymbols.isalpha():
                    userSymbols = True
                else:
                    userSymbols = False
                print()
            else:
                error()

            passwd = gen_passwd(size=userSize, numbers=userNumbers, uppercase=userUpper, symbols=userSymbols)
            entropy = check_entropy(passwd)

            bar()
            print(f"{outputData} Password: {passwd}")

            if entropy >= high_entropy:
                print(f"{outputData} Strength: Strong")
            elif entropy >= median_entropy and high_entropy:
                print(f"{outputData} Strength: Medium")
            else:
                print(f"{outputData} Strength: Weak")
            bar()
            print(entropy)
            print()
            exit(0)

        else:
            exit(0)