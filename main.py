import sys

def exitShell(status):
    status = "".join(status)
    if status == '0':
        return True
    else:
        return False
def echo(input):
    inputJoined = " ".join(input)
    print(inputJoined)

def shellInput(input):
    function = {'exit': exitShell, 'echo': echo}
    separated_input = input.split()
    if separated_input[0] in function:
        return function[separated_input[0]](separated_input[1:])
    else:
        print(f"{input}: command not found")
def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        userInput = input()
        returned_input = shellInput(userInput)

        if returned_input:
            break



if __name__ == "__main__":
    main()
