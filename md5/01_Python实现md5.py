from hashlib import md5

def fun(s):
    obj = md5()

    obj.update(s.encode('utf-8'))

    md5_value = obj.hexdigest()
    print(md5_value) # d517acb68fbed2331b57d1a11ca21dcc

sign = fun("简单")