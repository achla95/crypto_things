############################################################################################################
#            This programm will encrypt & decrypt in caesar code but also brute-force it enjoy !           #
############################################################################################################
##################################################################
#   How to use it :                                              #
#   On Windows's terminal -> python3 \path\to\your\file.py -h    #
#   On Linux's terminal   -> python3 path/to/your/file.py  -h    #
##################################################################
import argparse

def caesar_encrypt(cypher_plaintext:str, key:int) -> str:
    assert type(cypher_plaintext) == str and type(key) == int   ### cypher_plaintext must be str : <class 'str'> and key must be <class 'int'>
    return ''.join(chr((ord(cypher_plaintext[i].upper()) + key-65)%26+97) for i in range(len(cypher_plaintext))).upper()

def caesar_decrypt(cypher:str, key:int) -> str: 
    assert type(cypher) == str and type(key) == int  ### cypher must be str : <class 'str'> and key must be <class 'int'>
    return ''.join(chr((ord(cypher[i].upper()) - key-65)%26+97) for i in range(len(cypher))).upper()

def caesar_brute_force(cypher:str) -> str:
    assert type(cypher) == str ### cypher type must be str : <class 'str'>
    return print('\n'.join(caesar_decrypt(cypher,i).upper() for i in range(1,27)))

if __name__ == "__main__":
# Get command line arguments
    parser = argparse.ArgumentParser(description="This programm will encrypt, decrypt or brute-force some encrypted cypher with caesar encryption ")
    parser.add_argument("--encrypt","-e",type=str,help="Encrypt your text with caesar encryption.")
    parser.add_argument("--decrypt","-d",type=str,help="Decrypt your text with using caesar decryption.")
    parser.add_argument("--brute-force","-b",type=str,help="Brute-force caesar encrypted cypher.")
    parser.add_argument("--key","-k",type=int,help="The key is required for encryption/decryption.")
    args= parser.parse_args()
    error_msg = "[+] Error -> please use -h or --help options for more informations."
    
    if args.encrypt:
        if args.key:
            if (args.decrypt or args.brute_force) or (args.decrypt and args.brute_force):
                quit(error_msg)
            print(caesar_encrypt(args.encrypt,args.key))
        else:
            quit("[+] Key is missing.")
    elif args.decrypt:
        if args.key:
            if (args.encrypt or args.brute_force) or (args.encrypt and args.brute_force):
                quit(error_msg)
            print(caesar_decrypt(args.decrypt,args.key))
        else:
            quit("[+] Key is missing.")
    elif args.brute_force:
        if (args.encrypt or args.decrypt or args.key) or (args.encrypt and args.key and args.decrypt):
            quit(error_msg)
        print(caesar_brute_force(args.brute_force))
    elif args.key:
        quit(error_msg)





























































