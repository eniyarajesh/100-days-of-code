print("Welcome to The Secret Auction Program!!\n")
 
def find_highest_bitter():
    bits = {}
    bit_continue = True
    while bit_continue:
        name = input("What is your name?: ")
        bit_amount = int(input("What is your bid?: $"))
        bits[name] = bit_amount
        auc_continue = input("If any other bidder? Type 'yes' or 'no': \n").lower()
        print("\n" * 60)
        if auc_continue == "no":
            bit_continue = False

    highest = 0
    winner = ""
    for i in bits:
        if bits[i] > highest:
            highest = bits[i]
            winner = i
    print(f"The winner of the auction is '{winner}'")
find_highest_bitter()

        


