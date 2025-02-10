# 163KeyDecrypter
解密网易云音乐文件的163key  
  
在网易云下载的音乐文件都会带有以“163 key(Don't modify):”开头的注释，后面是经过加密的json代码。  
只需要输入“163 key(Don't modify):”后面的一串代码，本程序即可解密出对应的json文本。  
解码流程：163key→Base64解码→AES-128-ECB解密→json代码  

本代码依赖pycryptodome运行，可在操作系统终端输入以下命令安装pycryptodome：  
```
pip3 insatll pycryptodome
```
