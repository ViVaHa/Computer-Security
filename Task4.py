#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:42:54 2018

@author: varshath
"""

import base64
from timeit import default_timer as timer
from Crypto.Hash import SHA256,SHA512
from Crypto.Hash import SHA3_256



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



def generateHashUsingSHA256(fileName):
    print("SHA_256")
    data=getData(fileName)
    data=bytes(data,"utf-8")
    start = timer()
    h = SHA256.new()
    h.update(data)
    #Because this looks better when viewed instead of h.digest()
    digest=h.hexdigest()
    end = timer()
    #print(digest)
    print("Time Taken to generate Hash is ",(end-start))
    print("Time Taken to Hash per byte is ",(end-start)/len(data))
    
    
def generateHashUsingSHA512(fileName):
    print("SHA_512")
    data=getData(fileName)
    data=bytes(data,"utf-8")
    start = timer()
    h = SHA512.new()
    h.update(data)
    #Because this looks better when viewed instead of h.digest()
    digest=h.hexdigest()
    end = timer()
    #print(digest)
    print("Time Taken to generate Hash is ",(end-start))
    print("Time Taken to Hash per byte is ",(end-start)/len(data))
    
def generateHashUsingSHA3_256(fileName):
    print("SHA3_256")
    data=getData(fileName)
    data=bytes(data,"utf-8")
    start = timer()
    h = SHA3_256.new()
    h.update(data)
    #Because this looks better when viewed instead of h.digest()
    digest=h.hexdigest()
    end = timer()
    #print(digest)
    print("Time Taken to generate Hash is ",(end-start))
    print("Time Taken to Hash per byte is ",(end-start)/len(data))
    

generateFiles()
generateHashUsingSHA256("kbfile.txt")
generateHashUsingSHA256("mbfile.txt")
generateHashUsingSHA512("kbfile.txt")
generateHashUsingSHA512("mbfile.txt")
generateHashUsingSHA3_256("kbfile.txt")
generateHashUsingSHA3_256("mbfile.txt")



