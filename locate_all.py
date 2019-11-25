def locate_all(string, sub):
    matches = [] #creates empty list to append to for all matches of the substring
    index = 0 #sets index starting position
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index) #appends the index location of the matches
            index += len(sub) #checks the length of the substring to make sure
        else:
            index += 1 #moves the index position forward 1 to continue looking for matches
    return matches
