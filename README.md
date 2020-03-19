# Diffie Hellman Key Exchange in Python
A means of securely exchanging cryptographic keys over a public channel. Script for cracking the communication is also included.

# Example
```python
from Crypto.Util.number import getStrongPrime
from dh_client import DH_Client

p = getStrongPrime(512)
g = randint(2, p - 2)

a = DH_Client('Alice', g, p)
b = DH_Client('Bob', g, p)

a.establish_shared_secret(b.public_key)
b.establish_shared_secret(a.public_key)

b.aes_ecb_encrypt(msg_two)
a.aes_ecb_encrypt(msg_one)
```
