alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift,code):
    output = ""
    if code == "decode":
        shift *= -1
    for i in original_text:
        if i not in alphabet:
            output += i
        else:
            shift_pos = alphabet.index(i) + shift
            shift_pos %= len(alphabet)
            output += alphabet[shift_pos]
    print(f"Here is the {code}d result: {output}")


game_continue = True

while game_continue:
    print("Welcome to encrypt and decrypt the code!!")
    code = input("Enter encode/decode: ")
    original_text = input("Enter the original word: ")
    shift = int(input("Enter shift position: "))
    caesar(original_text,shift,code)
    
    restart = input("If you want to continue, type 'yes' or else 'no'. \n").lower()
    if restart == "no":
        game_continue = False
        print("Good Bye!!")

