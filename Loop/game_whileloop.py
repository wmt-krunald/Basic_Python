secret_word = "zebra"
gusse = ""
gusse_count = 0
gusse_limit = 5
out_of_gusse = False
i = 1

print("\nEnter Any Animal Name and Check Your Luck:)\n")
print("You have Only Five chance\n")

while gusse != secret_word and not(out_of_gusse):
    if gusse_count < gusse_limit:
        gusse = input("Enter Your Gusse :")
        gusse_count += 1
        print("\nYou have only " + str(gusse_limit -i) + " chance left\n")
        i += 1
    else:
        out_of_gusse = True

if out_of_gusse:
    print("\nBetter Luck For Next Time\n")
else:
    print("\nYou Win\n")
