from PyQt5 import QtWidgets
from AES_By_ECB.ECB_Window import Ui_MainWindow
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        # 第一组P1
        self.E1Button.clicked.connect(self.encrypt1)  # 槽函数不用加括号
        self.D1Button_6.clicked.connect(self.decrypt1)
        # 第二组P2
        self.E2Button_2.clicked.connect(self.encrypt2)
        self.D2Button_5.clicked.connect(self.decrypt2)
        # 第三组P3
        self.E3Button_3.clicked.connect(self.encrypt3)  # 槽函数不用加括号
        self.D3Button_4.clicked.connect(self.decrypt3)
        # 第四组P4
        self.E4Button_7.clicked.connect(self.encrypt4)
        self.D4Button_8.clicked.connect(self.decrypt4)


    def encrypt1(self):

        key = self.Ekey.text() # 获取秘钥
        text = self.P1.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        text = text.encode("utf-8")
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        # 计算秘钥长度
        add = length - (count % length)
        # 在字符串末尾加0
        text = text + (b'\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return self.C1.setText(b2a_hex(ciphertext).decode("ASCII"))

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt1(self):
        key = self.Dkey.text()
        text = self.C1.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return self.AP1.setText(plain_text.rstrip(b'\0').decode("utf-8"))

    def encrypt2(self):
        key = self.Ekey.text()  # 获取秘钥
        text = self.P2.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        text = text.encode("utf-8")
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return self.C2.setText(b2a_hex(ciphertext).decode("ASCII"))

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt2(self):
        key = self.Dkey.text()
        text = self.C2.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return self.AP2.setText(plain_text.rstrip(b'\0').decode("utf-8"))

    def encrypt3(self):
        key = self.Ekey.text()  # 获取秘钥
        text = self.P3.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        text = text.encode("utf-8")
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return self.C3.setText(b2a_hex(ciphertext).decode("ASCII"))

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt3(self):
        key = self.Dkey.text()
        text = self.C3.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return self.AP3.setText(plain_text.rstrip(b'\0').decode("utf-8"))

    def encrypt4(self):
        key = self.Ekey.text()  # 获取秘钥
        text = self.P4.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        text = text.encode("utf-8")
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return self.C4.setText(b2a_hex(ciphertext).decode("ASCII"))

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt4(self):
        key = self.Dkey.text()
        text = self.C4.text()
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return self.AP4.setText(plain_text.rstrip(b'\0').decode("utf-8"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())