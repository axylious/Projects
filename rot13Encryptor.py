# Encryptor/Decryptor with hash function

import codecs

# inititialize rpt so program runs initially
rpt = 'y'

# Capture user input
while rpt != 'n':
    plaintxt = input("Enter text to be encrypted: ")

    cyphertxt = codecs.encode(plaintxt, 'rot_13')
    print("\nCyphertext: " + str(cyphertxt))

    hashtxt = hash(plaintxt)
    hashOP = print("\nHash: " + str(hashtxt))

    while rpt != 'n' or rpt != 'y':
        rpt = input("\nWould you like to decrypt your input? [y/n]: ")

        if rpt == 'n':
            break
        elif rpt == 'y':
            clrtxt = codecs.encode(cyphertxt, 'rot_13')
            print("\nCleartext: " + str(clrtxt))
            break

    while rpt != 'n' or rpt != 'y':
        rpt = input("\nWould you like to encrypt again? [y/n]: ")

        if rpt == 'y':
            break
        elif rpt == 'n':
            break
