def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def convert(string):
    if (2 >= len(string) >= 1) and (string[0].upper() in 'ABCDEFH') and (1<=string[1]<=8) :
        return [ord(string[0].upper())-65, int(string[1])-1]
    else:
        print('Pas bon')

