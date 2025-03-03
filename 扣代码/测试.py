import execjs

with open("用js实现RSA加密.js", "r", encoding='utf-8') as f:  # 关键修复点
    js_code = f.read()

ctx = execjs.compile(js_code)

# 调用js文件获得加密的结果
mi_result = ctx.call("encryptMessage", "Hello, World!")
# print(mi_result)