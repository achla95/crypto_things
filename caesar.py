############################################################################################################
#            This programm will encrypt & decrypt in caesar code but also brute-force it enjoy !           #
############################################################################################################
def caesar_encrypt(cypher_plaintext:str, key:int) -> str: ### work fine
    assert type(cypher_plaintext) == str and type(key) == int   ### cypher_plaintext must be str : <class 'str'> and key must be <class 'int'>
    return ''.join(chr((ord(cypher_plaintext[i].upper()) + key-65)%26+97) for i in range(len(cypher_plaintext))).upper()

def caesar_decrypt(cypher:str, key:int) -> str: ## work fine
    assert type(cypher) == str and type(key) == int 
    return ''.join(chr((ord(cypher[i].upper()) - key-65)%26+97) for i in range(len(cypher))).upper()

def caesar_brute_force(cypher:str) -> str: ### work fine
    assert type(cypher) == str ### cypher type must be str : <class 'str'>
    return print('\n'.join(caesar_decrypt(cypher,i).upper() for i in range(1,27)))

if __name__ == "__main__":
    try:
        print("Choose one of the numbers :")
        print("[+] 1 Encrypt\n[+] 2 Decrypt\n[+] 3 Brute-force")
        user_input = int(input("Your choice : "))
        if user_input > 3 or user_input < 1:
            print("[+] Enter only number between 1 & 3.")
        elif user_input == 1:
            cypher =  str(input("[+] Enter your text : "))
            key = int(input("[+] Now enter the key : "))
            print(f"[+] Result : {caesar_encrypt(cypher,key)}")
        elif user_input == 2:
            encrypted_cypher =  str(input("[+] Enter your text : "))
            key = int(input("[+] Now enter the key : "))
            print(f"[+] Result : {caesar_decrypt(encrypted_cypher,key)}")
        elif user_input == 3:
            encrypted_cypher =  str(input("[+] Enter your text : "))
            print(caesar_brute_force(encrypted_cypher))
    except ValueError:
        print("[+] Enter only number between 1 & 3.")



