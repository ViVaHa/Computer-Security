#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 08:27:11 2018

@author: varshath
"""

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from timeit import default_timer as timer

def generateFiles():
    with open('kbfile.txt', 'w+') as f:
        num_chars = 256
        f.write("abcd" * num_chars)
    
        
     
    with open('mbfile.txt', 'w+') as f:
        num_chars = 256 * 1024
        f.write("abcd" * num_chars)
        

def getData(fileName):      
        
    x="" 
    with open(fileName,'r') as file:
        x=file.read()
    return x


def rsa(message,size):
   start = timer()
   key = RSA.generate(size)
   key_gen_time=  timer() - start
   
   cipher = PKCS1_OAEP.new(key.publickey())
   buffer=""
   chunks=[]
   size=342
   parts=int(len(message)/size)
   x=0
   for i in range(parts):
       chunks.append(message[size*i:size*(i+1)])
       x=i
       
   chunks.append(message[(x+1)*size:])
   ciphers=[]
   start = timer() 
   for chunk in chunks:
       chunk_bytes=chunk.encode("utf-8")
       ciphertext = cipher.encrypt(chunk_bytes)
       ciphers.append(ciphertext)
   encrypt_time=timer() - start
   #decryption
   cipher = PKCS1_OAEP.new(key)
   start = timer()  
   for ciphertext in ciphers:
       pt = cipher.decrypt(ciphertext)
       buffer+=pt.decode("utf-8")
   decrypt_time = timer() - start
   if buffer==message:
       print("successfull encryption and decryption")
   else:
       print("Incorrect encryption/decryption")
   print("time taken for key gen ",(key_gen_time))
   print("time taken to encrypt ",(encrypt_time))
   print("Time Taken to Encrypt per byte is ",((encrypt_time)/len(message)))
   print("time taken to Decrypt ",(decrypt_time))
   print("Time Taken to Decrypt per byte is ",((decrypt_time)/len(message)))
   
generateFiles()
kbData=getData("kbfile.txt")
mbData=getData("mbfile.txt")
rsa(kbData,3072)
rsa(mbData,3072)