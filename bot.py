print('       start bot...\n\n')
from io import BufferedReader
from os import remove
import urllib3,random,base64,datetime,math,wget
from os.path import dirname,abspath,join
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from json import loads,dumps
from requests import get,post
from rich.console import Console
from rich.traceback import install
from requests import get
from re import findall
from rubika.client import Bot
from requests import post
import time
from time import time
import io
from random import choice
import threading 

tink="@upload_elias"
#در قسمت بالا لینک چنل آپلود را وارد کنید

authtwo="atkiflsgqchnvqyaohgnjuogsvjzsage"
#در قسمت بالا شناسه اکانت (auth)خود را وارد کنید

bot = Bot("AppName", auth=authtwo)

target="c0BLm9F0439957a9c0dea73d9b71f8cf"
#در قسمت بالا جی یو ایدی(guid) چنل آپلود را وارد کنید


get="g0BwuKA039192c4a454a9822f82b04b8"

#در قسمت بالا جی یو ایدی (guid) جایی که میخواید لینک فایل رو ارسال کنید  وارد کنید


cakl=open("cc.txt","r",encoding='utf-8').read()


nname="@upload_elias"
#در قسمت بالا نام فایل را انتخاب کنید


console = Console()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
install()

class Encryption:
    def __init__(self, auth) -> int:
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('utf-8'),AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result
    
class Server:
    def rubika(self):
        return {
            "link":"https://messengerg2c13.iranlms.ir",
            "package": "web.rubika.ir"
        }
        
    def shad(self):
        return {
            "link":"https://shadmessenger15.iranlms.ir/",
            "package": "web.shad.ir"
        }   
    
class Methods:
    
    def __init__(self,auth,server:Server):
        self.auth = auth
        self.enc = Encryption(self.auth)
        self.server = server
        
    def request(self,data:dict) -> dict:
        while True:
            try:

                response = post(self.server["link"],json=data).json()
                return loads(self.enc.decrypt(response["data_enc"]))
            except Exception as error:
                ...
        
    def requestDataResult(self,inputData:dict,method:str) -> dict:
        data_enc = {
            "method": method,
            "input": inputData,
            "client": {
                "app_name": "Main",
                "app_version": "3.2.2",
                "platform": "Web",
                "package": self.server["package"],
                "lang_code": "fa"
            }
        }
        return {
            "api_version": "5",
            "auth": self.auth,
            "data_enc": self.enc.encrypt(dumps(data_enc)),
        }
        
    def requestSendFile(self,file_name:str,mime:str,size:int) -> dict:
        return self.request(self.requestDataResult({
            "file_name": file_name,
            "size": size,
            "mime": mime,
        },"requestSendFile"))
        
    def uploadFile(self,file:BufferedReader,id:int,access_hash_send:str,upload_url:str) -> dict:
        readFile = file.read()
        if len(readFile) <= 131072:
            headerOption = {
                "access-hash-send": access_hash_send,
                "auth": self.auth,
                "chunk-size": str(len(readFile)),
                "file-id": id,
                "part-number": str(1),
                "total-part": str(1)
            }
            while True:
                try:
                    return post(url=upload_url,headers=headerOption,data=readFile).json()["data"]
                except Exception as error:console.log(error)
        else:
            total_part = random._floor(len(readFile) / 131072 +1)
            for part_number in range(1,total_part+1):
                if part_number != total_part:
                    k = part_number - 1
                    k = k * 131072
                    t2 = True
                    while t2:
                        try:
                            headerOption = {
                                "access-hash-send": access_hash_send,
                                "auth": self.auth,
                                "chunk-size": str(131072),
                                "file-id": id,
                                "part-number": str(part_number),
                                "total-part": str(total_part)
                            }
                            response = post(upload_url,headers=headerOption,data=readFile[k:k + 131072]).json();t2=False
                        except Exception as error:...;t2 = True
                else:
                    k = part_number - 1
                    k = k * 131072
                    t2 = True
                    while t2:
                        try:
                            headerOption = {
                                "access-hash-send": access_hash_send,
                                "auth": self.auth,
                                "chunk-size": str(len(readFile[k:])),
                                "file-id": id,
                                "part-number": str(part_number),
                                "total-part": str(total_part)
                            }
                            response = post(upload_url,headers=headerOption,data=readFile[k:]).json()["data"];t2=False
                        except Exception as error:...;t2 = True
                        
                    return response
                
    def sendFile(self,directory:str,object_guid:str,file_name:str,size:int,mime:str,text:str) -> dict:
        infouploadvideo = self.requestSendFile(file_name,mime,size)["data"]

        captin=cakl
        accesshashrec = self.uploadFile(open(directory,"rb"),infouploadvideo["id"],infouploadvideo["access_hash_send"],infouploadvideo["upload_url"])
        return self.request(self.requestDataResult({
            "object_guid": object_guid,
            "text": captin,
            "rnd": random.randint(10000,99999),
            "file_inline": {
                "dc_id": infouploadvideo["dc_id"],
                "file_id": infouploadvideo["id"],
                "type": "File",
                "file_name": nname +'                '+ file_name,
                "size": size,
                "mime": mime,
                "access_hash_rec": accesshashrec['access_hash_rec']
            }
        },"sendMessage"))                    
        
    def getChatsUpdates(self) -> None:
        time_stamp = str(math.floor(datetime.datetime.today().timestamp()) - 200)
        return self.request(self.requestDataResult({
            "state": time_stamp,
        },"getChatsUpdates"))["data"]["chats"]
        
    def sendMessage(self,object_guid:str,text:str):
        return self.request(self.requestDataResult({
            "object_guid": object_guid,
            "rnd": random.randint(10000,99999),
            "text": text,
        },"sendMessage"))     
        
class Main:
    
    def __init__(self,auth:str,guid:str,server:dict) -> None:
        self.path = dirname(abspath(__file__))
        self.myGuid = guid
        self.method = Methods(auth,server)
        self.answered = [] 
        self.server = server
        
    def decrypt(self):
        ...   
        
    def upload(self,directory,object_guid):
        try:
            with open(directory,"rb+") as file:
                self.method.sendFile(file.name,object_guid,str(file.name).split("\\")[-1],len(file.read()),str(file.name).split(".")[-1],str(file.name).split("\\")[-1])
        except Exception as error:self.method.sendMessage(self.myGuid,str(error));console.log(error)
        
    def download(self,link:str) -> None:
        try:
            self.method.sendMessage(self.myGuid,"در حال دانلود...")
            return wget.download(link,join(self.path,"",link.split('/')[-1]))
        except Exception as error:self.method.sendMessage(self.myGuid,str(error));console.log(error)
        
    def handlerLink(self) -> bool:
        try:
            update = self.method.getChatsUpdates()
            for msg in update:
                if msg['abs_object']['object_guid'] == self.myGuid and msg["last_message"]["type"] == "Text" and not msg["last_message"]['message_id'] in self.answered and (str(msg['last_message']['text']).startswith("http://") or str(msg['last_message']['text']).startswith("https://")):
                    return {
                        "status": True,
                        "link": str(msg['last_message']['text'])
                    }
                            
                self.answered.append(msg["last_message"]["message_id"])        
                        
        except Exception as error:self.method.sendMessage(self.myGuid,str(error));self.answered.append(msg["last_message"]["message_id"]);console.log(error)
        
    def debuging(self):
        self.handlerLink()
        location = self.download(self.handlerLink()["link"])
        ...
        
    def bot(self):
        while True:
            try:
                linkBool = self.handlerLink()
                if linkBool == None:
                    continue
                elif linkBool["status"]:
                    startTime = time()
                    location = self.download(linkBool["link"])
                    self.upload(location,target)
                    executionTime = (time() - startTime)
                    mip=str(int(executionTime))
                    ticf=location[20:100]
                    self.method.sendMessage(self.myGuid,'فایل با نام :\n'+ticf+'\n\nدر زمان '+mip+' ثانیه در چنل\n'+tink+'\n آپلود شد')

                    remove(location)
            except Exception as error:self.method.sendMessage(self.myGuid,str(error));console.log(error)
        
if __name__ == "__main__":
    bot = Main(authtwo,get,Server().rubika()).bot()
