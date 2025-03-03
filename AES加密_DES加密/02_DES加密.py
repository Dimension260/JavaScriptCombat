
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad  # 填充
import base64

# s = "我爱吃鱼"
#
# ming = s.encode("utf-8")
#
# des = DES.new(key=b'12345678', iv=b'12345678', mode=DES.MODE_CBC)
# ming = pad(ming, 8)  # 填充到8位
# mi = des.encrypt(ming)
# mi_s = base64.b64encode(mi).decode()
# print(mi_s)


mi_s = "bXZ8WcOzh/SW0yuFPTTZog=="

des = DES.new(key=b'12345678', iv=b'12345678', mode=DES.MODE_CBC)

ming = des.decrypt(base64.b64decode(mi_s))
ming = unpad(ming, 8)
print(ming.decode("utf-8"))
