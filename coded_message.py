alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

isContinue = True

def codeTheMessage(starting_text, origin_shift, direction_code):
    end_text = "" 
    if direction_code == "decode":
        origin_shift *= -1
    for letter in starting_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = position + origin_shift
            end_text += alphabet[newPosition]
        else:
            end_text += letter
    print(f"The {direction_code}d text is {end_text}")

while isContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    codeTheMessage(text, shift, direction)

    isContinue = input("If you want to keep going type 'yes' otherwise type 'no'.\n").lower()
    if isContinue == "no":
        isContinue = False
print("Goodbye")