n = input("")

def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
        if sting[index:index + len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)
