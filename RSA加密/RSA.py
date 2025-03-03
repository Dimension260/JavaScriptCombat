import base64

from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.PublicKey import RSA # 这个RSA我们看到的样子是 帮我们生成和管理公钥和私钥的

# 如何生成公钥和私钥
# key = RSA.generate(bits=1024,e=65537)
# with open('private.pem', 'wb') as f:
#     f.write(key.exportKey())
#
# with open('public.pem', 'wb') as f:
#     f.write(key.publickey().exportKey())


# rsa = PKCS1_v1_5.new(key=)

# 如何加密

# # 处理成字节
# s = '我喜欢吴迪简单'
# ming_bs = s.encode('utf-8')
#
# # 加载公钥
# f = open('public.pem',mode='rb')
# pub_key = RSA.importKey(f.read())
# f.close()
#
# # 创建加密器
# rsa = PKCS1_OAEP.new(pub_key)
# mi_bs = rsa.encrypt(ming_bs)
# mi_bs = base64.b64encode(mi_bs)
# print(mi_bs)

# 解密
mi_str = b'HHp4PNfktvRweA5MDOtoN6PrEnJNK6b1WEGaxqEH+U4q79iuWkL/c9sD4HJTK4H+YOkd6g1qkCYt0DA3MvTKfhErPCV7pOBXw0rrNF5UCrHqeHsU1xlpSwfbgqc6BYHA8M+B5qJmwiqUiHVTrbRYCKLtgIr+LEh/GlVFGAmiSpo='

f = open('private.pem', 'rb')
pri_key =RSA.importKey(f.read())
rsa = PKCS1_OAEP.new(pri_key)
ming_bs =rsa.decrypt(base64.b64decode(mi_str))
print(ming_bs.decode('utf-8'))