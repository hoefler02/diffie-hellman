#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Title: Diffie Hellman Example
# @Author: Michael Hoefler
# @Date:   2019-07-12 22:49:42

from Crypto.Util.number import getStrongPrime, getPrime
from dh_client import DH_Client
from random import randint
from faker import Faker

# The information printed out is what the man in the middle is able to see

p = getStrongPrime(512)
g = randint(2, p - 2)


a = DH_Client('Alice', g, p)
b = DH_Client('Bob', g, p)

print('Secure communication established between %s and %s!\n' % (a.name, b.name))

print('p = %d\ng = %d\n' % (p, g))

print('%s -> %s ~ %d' % (b.name, a.name, b.public_key))

a.establish_shared_secret(b.public_key)


print('%s -> %s ~ %d\n' % (a.name, b.name, a.public_key))

b.establish_shared_secret(a.public_key)



print('Shared secret established!\n')


msg_two = 'the weathers nice today'

print('%s -> %s ~ %d' % (b.name, a.name, b.aes_ecb_encrypt(msg_two)))


msg_one = 'it is indeed'

print('%s -> %s ~ %d\n' % (a.name, b.name, a.aes_ecb_encrypt(msg_one)))


print('Secure communication ended.')
