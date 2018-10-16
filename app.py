from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from random import randint
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests, json
import re

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('In++hTLWDsGi8712BFxRaC9Qkr/Lbn8fQe6dhkBm+8Fxl6zH19I97WzYRsKEJlX9ZgCJb9DAWSTuEFedqenfMHdQuDraavqIjrGVNibdCS8idf2QmCNpmQqqd9flJQyxNgX4tjBdncjkyTYKA3N4ogdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1aa040aad1ecfbcf33d3a5916b4a1439')
#===========[ NOTE SAVER ]=======================
notes = {}

#INPUT DATA MHS buat di app.py
def inputmhs(nrpku, namaku, daeasal, jurusanku):
    r = requests.post("http://www.aditmasih.tk/zaky-api/insert.php", data={'nrpku': nrpku, 'namaku': namaku, 'daeasal': daeasal, 'jurusanku': jurusanku})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Data '+' berhasil dimasukkan\n'
    elif(flag == "0"):
        return 'Data gagal dimasukkan\n'

def carimhs(nrpku):
    URL = "http://www.aditmasih.tk/zaky-api/show.php?nrpku=" + nrpku
    r = requests.get(URL)
    data = r.json()
    err = "data tidak ditemukan"
    
    flag = data['flag']
    if(flag == "1"):
        nrpku = data['data_mhs'][0]['nrpku']
        namaku = data['data_mhs'][0]['namaku']
        daeasal = data['data_mhs'][0]['daeasal']
        jurusanku = data['data_mhs'][0]['jurusanku']

        # munculin semua, ga rapi, ada 'u' nya
        # all_data = data['data_angkatan'][0]
        data= "Nama Mahasiswa : "+namaku+"\nNRP : "+nrpku+"\nDaerah Asal : "+daeasal+"\nJurusan : "+jurusanku
        return data
        # return all_data

    elif(flag == "0"):
        return err

def allmhs():
    r = requests.post("http://www.aditmasih.tk/zaky-api/all.php")
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        hasil = ""
        for i in range(0,len(data['data_mhs'])):
            id_buku = data['data_mhs'][int(i)][0]
            judul_buku = data['data_mhs'][int(i)][2]
            pengarang = data['data_mhs'][int(i)][4]
            tahun = data['data_mhs'][int(i)][6]
            hasil=hasil+str(i+1)
            hasil=hasil+".\nNRP : "
            hasil=hasil+nrpku
            hasil=hasil+"\nNama Mahasiswa : "
            hasil=hasil+namaku
            hasil=hasil+"\nDaerah Asal : "
            hasil=hasil+daeasal
            hasil=hasil+"\nJurusan :"
            hasil=hasil+jurusanku
            hasil=hasil+"\n"
        return hasil
    elif(flag == "0"):
        return 'Mahasiswa kosong\n'

def hapusmhs(nrpku):
    r = requests.post("http://www.aditmasih.tk/zaky-api/delete.php", data={'nrpku': nrpku})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Data '+nrpku+' berhasil dihapus\n'
    elif(flag == "0"):
        return 'Data gagal dihapus\n'

def updatemhs(nrpLama,nrpku,namaku,daeasal,jurusanku):
    URL = "http://www.aditmasih.tk/zaky-api/show.php?nrpku=" + nrpLama
    r = requests.get(URL)
    data = r.json()
    err = "data tidak ditemukan"
    nrpLama=nrplama
    flag = data['flag']
    if(flag == "1"):
        r = requests.post("http://www.aditmasih.tk/zaky-api/update.php", data={'nrplama':nrplama, 'nrpku': nrpku, 'namaku': namaku,
         'daeasal': daeasal, 'jurusanku': jurusanku})
        data = r.json()
        flag = data['flag']

        if(flag == "1"):
            return 'Data '+id_lama+' berhasil diupdate\n'
        elif(flag == "0"):
            return 'Data gagal diupdate\n'

    elif(flag == "0"):
        return err


# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    
    data=text.split('-')
    if(data[0]=='lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=carimhs(data[1])))
    elif(data[0]=='tambah'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=inputmhs(data[1],data[2],data[3],data[4])))
    elif(data[0]=='hapus'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=hapusmhs(data[1])))
    elif(data[0]=='ganti'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=updatemhs(data[1],data[2],data[3],data[4],data[5])))
    elif(data[0]=='semua'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=allmhs()))
    elif(data[0]=='menu'):
        menu = "1. lihat-[nrpku]\n2. tambah-[nrpku]-[namaku]-[daeasal]-[jurusanku]\n3. hapus-[nrpku]\n4. ganti-[id lama]-[id baru]-[namaku baru]-[daeasal baru]-[jurusanku baru]\n5. semua"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=menu))


    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)