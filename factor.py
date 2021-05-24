####################################################################################################
#                                                                                                  #
#       This programm will factorize N into 2 prime numbers & decrypt your message                 #
#                                                                                                  #
####################################################################################################

from binascii import hexlify,unhexlify #convertir en hexadécimal ou l'inverse !
import base64 # pour decoder le message qui est en base64
import rsa #afin de déchiffrer le message && pip install rsa   
import requests
from factordb.factordb import FactorDB ## pip install factordb-python && pip install factordb-pycli


cypher = str(input("[+] Enter your message encoded in base64 : "))
cypher_decoded = base64.b64decode(cypher)

n = int(input("[+] Enter N : "))
N = FactorDB(n)
N.connect()
lst = N.get_factor_from_api()
e = int(input("[+] Then enter e (mostly e = 65537) : "))
print("[+] Trying to Factorize N into two primes numbers p & q")
p = int(lst[0][0])
q = int(lst[1][0])
print("[+] Now calculating phi(n)...")
phi_n = (p-1)*(q-1)
print(f"[+] Phi(n) = {phi_n}")
print("[+] Restoring d (private key) using e and phi(n)")
d = pow(e,-1,phi_n) ## or e**-1 % phi_n
print(f"[+] Found d = {d}")
print("[+] Decrypting your message...")
solve = rsa.PrivateKey(n,e,d,p,q)
plaintext = rsa.decrypt(cypher_decoded,solve)
print(f"[+] Decrypted cypher : {plaintext}")
