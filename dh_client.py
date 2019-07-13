from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint


class DH_Client:
	
	def __init__(self, name, generator, prime):
		
		self.name = name
		
		self.g = generator
		self.p = prime

		self.private_key = randint(1, prime)
		self.public_key = pow(self.g, self.private_key, self.p)
		
		
	def establish_shared_secret(self, received_public_key):
		
		self.shared_secret = hex(pow(received_public_key, self.private_key, self.p))[2:]
		
		while True:
			if (len(self.shared_secret) == 32 or len(self.shared_secret) == 48 or len(self.shared_secret) == 64):
				break
			elif (len(self.shared_secret) > 32):
				self.shared_secret = self.shared_secret[1:]
			else:
				self.shared_secret = '0' + self.shared_secret
		
		self.shared_secret = bytes.fromhex(self.shared_secret)
		
		return int(self.shared_secret.hex(), 16)


	def aes_ecb_encrypt(self, msg):
		
		cipher = AES.new(self.shared_secret)
		
		msg = ''.join([hex(ord(c))[2:] for c in msg])
		
		while(len(msg) % 32 != 0):
			msg = '0' + msg
		
		msg = bytes.fromhex(msg)
		
		ciphertext = cipher.encrypt(msg)
		
		return int(ciphertext.hex(), 16)

