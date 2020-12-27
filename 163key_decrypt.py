'''
163key解码器
在网易云下载的音乐文件都会带有以“163 key(Don't modify):”开头的注释，后面是经过加密的json代码。
只需要输入“163 key(Don't modify):”后面的一串代码，本程序即可解密出对应的json文本。
解码流程：163key→Base64解码→AES-128-ECB解密→json代码
'''
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
import os
'''
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')
'''
'''
# 加密函数
def encrypt(data):
    key = '#14ljk_!\]&0U<\'('.encode('utf-8')
    mode = AES.MODE_ECB
    #text = add_to_16(text)
    cryptos = AES.new(key, mode)

    ecdata = cryptos.encrypt(data)
    return ecdata
'''


# 解密
def decrypt(data):
    key = '#14ljk_!\]&0U<\'('.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    dcdata = cryptor.decrypt(data)
    return dcdata


if __name__ == '__main__':
    key = input('163 key(Don\'t modify):')
    encdata = base64.b64decode(key.encode('utf-8'))
    decstr = decrypt(encdata).decode('utf-8')
    os.system('cls')
    print(decstr)
    input('按任意键退出。')