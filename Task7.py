#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 08:41:54 2018

@author: varshath
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
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






def generatePrivateKey(size):
    start=timer()
    private_key = dsa.generate_private_key(key_size=size,backend=default_backend())
    end=timer()
    print("Time Taken to generate key is ",(end-start))
    return private_key



def sign(private_key,fileName):
    data=getData(fileName)
    data=data.encode("utf-8")
    start=timer()
    signature = private_key.sign(data,hashes.SHA256())
    end=timer()
    print("Time Taken to generate signature is ",(end-start))
    print("Time Taken per byte to sign is ",((end-start)/len(data)))
    return signature

def verify(signature,private_key,fileName):
    data=getData(fileName)
    data=data.encode("utf-8")
    start=timer()
    public_key = private_key.public_key()
    public_key.verify(
        signature,
        data,
        hashes.SHA256()
    )
    end=timer()
    print("Time Taken to verify the signature is ",(end-start))
    print("Time Taken per byte to verify is ",((end-start)/len(data)))

generateFiles()
private_key=generatePrivateKey(2048)
signature=sign(private_key,"kbfile.txt")
verify(signature,private_key,"kbfile.txt")
signature=sign(private_key,"mbfile.txt")
verify(signature,private_key,"mbfile.txt")