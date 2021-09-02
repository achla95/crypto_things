from binascii import hexlify,unhexlify #convertir en hexadécimal ou l'inverse !
import base64 # pour decoder le message qui est en base64
import rsa #afin de déchiffrer le message

msg = base64.b64decode("e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA")
msg_decoded = int(hexlify(msg),16) #decodage du message en base64



e = 65537 #exposant de chiffrement

n = 188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059
p = 398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
q = 472772146107435302536223071973048224632914695302097116459852171130520711256363590397527
phi_n = (p-1)*(q-1) # indicatrice d'Euler

d = pow(e,-1,phi_n) #clé privée
solve = rsa.PrivateKey(n,e,d,p,q)

plaintext = rsa.decrypt(msg,solve)
print(plaintext)
