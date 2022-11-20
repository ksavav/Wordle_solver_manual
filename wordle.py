from words import words

yellow_list = []
yellow = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": []
}
green = ['-', '-', '-', '-', '-']
used_letters = []

def word_creator():
    for item in words:
        i = 0
        counter = 0

        for letter in item[0]:
            if letter in used_letters:
                if (letter in yellow_list and counter == 0) or (letter in green and counter == 0): counter = 1
                else: break

            if green[i] != '-' and letter != green[i]: break
            
            if letter in yellow[str(i+1)]: break
            i += 1

        if i == 5:
            temp_y = yellow_list.copy()

            for l in yellow_list:
                for x in item[0]:
                    if x == l: 
                        try:
                            temp_y.remove(l)
                        except:
                            True
            
            if len(temp_y) == 0:
                print(f"Try this: {item}")
                break

def main():
    print("RULES:\n Use only lower cases or numbers,\n If a letter is green you will not be asked for that letter in the next iteration\n This program is not user-friendly so if you make mistake, restart program\n")

    while 1:
        current_word = input("What word you typed?\n")
        j = 0


        for letter in current_word:
            if(green[j] == '-'):
                print(f"Letter '{letter}' on position {j+1} is:")
                temp_color = int(input("Green (type '1'), yellow (type '2') or gray (type '3')?\n"))
                
                if temp_color == 1: green[j] = letter

                elif temp_color == 2:
                    yellow_list.append(letter)
                    yellow[str(j+1)].append(letter)

                else: used_letters.append(letter)
                
            j += 1

        word_creator()

    


if __name__ == "__main__":
    main()

