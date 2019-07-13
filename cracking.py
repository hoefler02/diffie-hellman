"""
Secure communication established between A and B!

p = 207080661200384833303080496562605487473
g = 178610548800843800639486516995488564788

B -> A ~ 78259913733803025092539024300534194541
A -> B ~ 31222482936005213821562053897313002272

Shared secret established!

B -> A ~ 64445692639996584659112689530505997073
A -> B ~ 60371285466096798840170942333708221940493753111492365229078081035978838893670

Secure communication ended.
"""

from Crypto.Cipher import AES
import time

p = 207080661200384833303080496562605487473
g = 178610548800843800639486516995488564788

pk1 = 78259913733803025092539024300534194541
pk2 = 31222482936005213821562053897313002272

pr1 = 0
pr2 = 0

m1 = bytes.fromhex(hex(64445692639996584659112689530505997073)[2:])
m2 = bytes.fromhex(hex(60371285466096798840170942333708221940493753111492365229078081035978838893670)[2:])

e = 1

b = 0

t = time.time()

while True:
	if pow(g, e, p) == pk1:
		print('\n[*] PRIVATE KEY ONE RECOVERED : %d\n' % (e))
		pr1 = e
		b += 1
		if b == 2:
			break
	if pow(g, e, p) == pk2:
		print('\n[*] PRIVATE KEY TWO RECOVERED : %d\n' % (e))
		pr2 = e
		b += 1
		if b == 2:
			break
	if e % 1000000 == 0:
		print('[-] %d seconds elapsed...' % (time.time() - t))
	e += 1


print('\n[-] starting decryption\n\n')

s = str(hex(pow(g, (pr1 * pr2), p))[2:])

if len(s) % 2 != 0: s = '0' + s

cipher = AES.new(bytes.fromhex(s))

p1 = cipher.decrypt(m1)
p2 = cipher.decrypt(m2)

p1 = p1.decode('utf-8').replace('\x00', '')
p2 = p2.decode('utf-8').replace('\x00', '')

print('[*] PLAINTEXT ONE RECOVERED...\n\n%s\n\n[*] PLAINTEXT TWO RECOVERED...\n\n%s\n' % (p1, p2))
