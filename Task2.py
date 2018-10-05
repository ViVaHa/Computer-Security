#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:48:10 2018

@author: varshath
"""
import base64
import time
from timeit import default_timer as timer
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode,b64decode

from Crypto.Util.Padding import pad,unpad




def writeFile(data,fileName):
    with open(fileName, 'w+') as f:
        f.write(data)



def writeFileInBytes(data,fileName):
    with open(fileName, 'wb+') as f:
        f.write(data)



def generateFiles():
    with open('kbfile.txt', 'w+') as f:
        num_chars = 256
        f.write("abcd" * num_chars)
        #f.write("\n"*1)
    
        
     
    with open('mbfile.txt', 'w+') as f:
        num_chars = 256 * 1024
        f.write("abcd" * num_chars)
        f.write("\n"*1)
        

def getData(fileName):      
        
    x="" 
    with open(fileName,'r') as file:
        x=file.read()
    return x

def getDataInBytes(fileName):      
        
    x="" 
    with open(fileName,'rb') as file:
        x=file.read()

    return x



def generateKey(size):
    start = timer()
    key = get_random_bytes(size)
    end= timer()
    print("Time Taken to generate Key is ",(end-start))
    return key
    

def encryptInCTR(key,data,fileNameToEncrypt):
    data=bytes(data, 'utf-8')
    cipher = AES.new(key, AES.MODE_CTR)
    start = timer()
    ct_bytes = cipher.encrypt(data)
    end= timer()
    print("Time Taken to Encrypt is ",(end-start))
    print("Time Taken to Decrypt per byte is ",(end-start)/len(data))
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    writeFileInBytes(bytes(ct,"utf-8"),fileNameToEncrypt)
    return nonce

def decryptInCTR(key,fileNameToDecrypt,nonce,fileNameToSavePT):
    ct = b64decode(getDataInBytes(fileNameToDecrypt))
    nonce = b64decode(nonce)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start=timer()
    pt = cipher.decrypt(ct)
    end=timer()
    print("Time Taken to Decrypt is ",(end-start))
    print("Time Taken to Decrypt per byte is ",((end-start)/len(pt)))
    pt=pt.decode("utf-8")
    writeFile(pt,fileNameToSavePT)
    return pt

generateFiles()
key=generateKey(16)
kbData=getData("kbfile.txt")
mbData=getData("mbfile.txt")

nonce=encryptInCTR(key,kbData,"Encrypted_kbfile.txt")
ptKb=decryptInCTR(key,"Encrypted_kbfile.txt",nonce,"Decypted_kbfile.txt")

nonce=encryptInCTR(key,mbData,"Encrypted_mbfile.txt")
ptMb=decryptInCTR(key,"Encrypted_mbfile.txt",nonce,"Decypted_mbfile.txt")

if ptKb==kbData and ptMb==mbData:
    print("Encryption and decryption done successfully")
else:
    print("Error in Encryption and Decryption")


