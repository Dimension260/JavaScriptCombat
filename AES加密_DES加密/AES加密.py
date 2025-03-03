from Crypto.Cipher import AES,DES,DES3
from Crypto.Util.Padding import pad, unpad
import base64

# aes = AES.new(key=b'1234556789123454',IV=b'5989452345789126',mode=AES.MODE_CBC)
# #
# ming = '帅死了简单'
# ming = ming.encode('utf-8')
# ming = pad(ming,16)
# # print(ming)
# mi = aes.encrypt(ming)
# # b'\x81a7S\x04G\x96]\xdd\x9dBtPDt%'
# # print(mi)
# #
# s = base64.b64encode(mi).decode()
# # # gWE3UwRHll3dnUJ0UER0JQ==
# print(s)

# mi = 'gWE3UwRHll3dnUJ0UER0JQ=='
# aes = AES.new(key=b'1234556789123454',IV=b'5989452345789126',mode=AES.MODE_CBC)
# mi=base64.b64decode(mi)
# ming = aes.decrypt(mi)
# ming = unpad(ming,16)
# print(ming.decode('utf-8'))