import sys
import os
import shutil
import subprocess
from sys import executable



def find_function(function):
    path = os.environ.get('PATH')
    pathList = path.split(os.pathsep)
    searched_path = set()
    foundPath = []
    for path in pathList:
        for root, dirnames, filenames in os.walk(path, followlinks=False):
            if root in searched_path:
                pass
            else:
                if function in filenames:
                    if os.access(os.path.join(root, function), os.X_OK):
                        foundPath.append(os.path.join(root, function))
                        return foundPath[0]
                #searched_path.add(root)
    return False
    
def present_directory():
    print(os.getcwd())
    
def typeShell(userInput):
    typeInput = "".join(userInput)
    if typeInput in shellFunction:
        print(f"{typeInput} is a shell built in")
    else:
        foundPath = find_function(typeInput)
        if foundPath:
            print(f"{typeInput} is {foundPath}")
        else:
            print(f"{typeInput}: not found")

def exit_shell(status = 0):
        sys.exit(status)
        
def echo(input):
    inputJoined = " ".join(input)
    print(inputJoined)
    

def shellInput(userInput):
    if not userInput:
        return None
    separated_input = userInput.split()

    function_name = separated_input[0]
    args = separated_input[1:]
    if separated_input[0] in shellFunction:
        if not args:
            return shellFunction[function_name]()
        else:
            return shellFunction[function_name](args)

    foundExecutablePath = find_function(function_name)
    if foundExecutablePath and len(args) > 0:
        run_function_with_args(foundExecutablePath, args)
        return None
    elif foundExecutablePath and len(args) == 0:
       run_function_no_args(foundExecutablePath)
       return None
    else:
        print(f"{userInput}: command not found")
        return None
        
def run_function_with_args(path, args):
    head, tail = os.path.split(path)
    local_function = [tail]
    local_function.extend(args)
    subprocess.run(local_function)
    
def run_function_no_args(path):
    head, tail = os.path.split(path)
    local_function = [tail]
    subprocess.run(local_function)
    
def change_prompt(new_prompt):
    p_s_1 = new_prompt
    return None
def change_directory(path):
    path = "".join(path)
    if path == '~':
        try:
            os.chdir(os.getenv('HOME'))
        except FileNotFoundError:
            print("How do you not have a home??")
    else:
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"{path} is not a valid file or directory. ")
p_s_1 = "$ "
    
shellFunction = {'exit': exit_shell, 'echo': echo, 'type': typeShell, 'pwd': present_directory, 'cd': change_directory}
    
def main():
    while True:
        sys.stdout.write(p_s_1)
        userInput = input()
        returned_input = shellInput(userInput)




if __name__ == "__main__":
    main()
