n = input("")

def remove_substring():
    output = []
    while index < len(string):
        if sting[index:index + n] == 'n':
            index += n
        else:
            output.append(string[index])
            index += 1
        print("".join(output))
