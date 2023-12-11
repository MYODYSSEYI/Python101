
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(plain_text, shift_amount, chosen_direction):
    result = ''
    if chosen_direction == 'encode':
        for letter in plain_text:
            letterIndex = alphabet.index(letter)
            if len(alphabet) - (letterIndex + shift_amount)   < 0:
                # print (letterIndex)
                zandfurther = letterIndex + shift_amount - len(alphabet)  
                result += alphabet[zandfurther]
            else:
                result += alphabet[letterIndex + shift_amount]
    elif chosen_direction == 'decode':
        for letter in plain_text:
            letterIndex = alphabet.index(letter)
            newLetter = letterIndex - shift_amount
            result += alphabet[newLetter]
    print(f"Here's the {chosen_direction}d result: {result}")
    
ceaser(plain_text=text, shift_amount=shift, chosen_direction=direction)

