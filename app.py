from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    teks = event.message.text
    text = teks.lower().strip()
    data=text.split('-')
    data2=text.split(' ')
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

#MENAMPILKAN MENU
    if text=="/menu":
        menu="1. '/sangar' gawe ndelok kesangaran wong-wong\n2. '/spam-[kalimat]-[jumlah spam]' gawe nyepam wong sing mbok sayang\n3. '/spamkata [kalimat]' gawe nyepam tiap kata sebanyak kalimat sing diketik\n4. '/bye' gawe ngetokno bot teko grup opo room\n5. '/rev-[kalimat]' gawe ngewalik tulisan\n6. '/dev' ndelok pengembang bot line iki\n7. tiap ngetik ng grup opo room isok munculo terjemahan boso jowo\n\nawakmu bebas isok ngetik keyword nggawe huruf gede opo cilik"  
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=menu))

#PENGEMBANGAN
    if text=="rey":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJnBoXCQfR16ILIYBCrxyovSI86b32DblCcnrT8mFn5QDsyXv9EA',preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJnBoXCQfR16ILIYBCrxyovSI86b32DblCcnrT8mFn5QDsyXv9EA'))
    if text=="Google Center":
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='Mountain View, California', address='United State of America',latitude=37.4225195,longitude=-122.0847433))
    if text=="/dev":
        dev="Dikembangkan oleh Andhika Yoga Perdana, mahasiswa Informatika ITS, dengan menggunakan bahasa Python, PHP, dan mySQL"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=dev))
#MENU SANGAR
    elif(data[0]=='/sangar'):
        pro = "Wong suroboyo terkenal karo kesangarane. Sak piro sangarmu cak?\n1. lihat-[id]\n2. tambah-[id]-[kesangaran]\n3. hapus-[id]\n4. ganti-[id lama]-[id baru]-[kesangaran baru]\n5. kabeh"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=pro))

#TINGGALKAN GROUP/ROOM
    elif text=="/bye":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Pingin ngekick aku?:(\nketik "/start" gawe ngekick!'))
    elif text=="/start":
        if isinstance(event.source, SourceGroup):
            line_bot_api.push_message(event.source.group_id, TextSendMessage(text='Woy '+profile.display_name+', kurang ajar banget kon wani ngekick aku teko grup iki!'))
            line_bot_api.push_message(event.source.room_id, TextSendMessage(text='Sepurane rek aku tinggal disek, aku bosen ng kene! GAK MENARIK blass cuk'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.push_message(event.source.room_id, TextSendMessage(text='Woy '+profile.display_name+', kurang ajar banget kon wani ngekick aku teko grup iki!'))
            line_bot_api.push_message(event.source.room_id, TextSendMessage(text='Sepurane rek aku tinggal disek, aku bosen ng kene! GAK MENARIK blass cuk'))
            line_bot_api.leave_room(event.source.room_id)
        else: 
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Mending blokiren aku daripada ngekick aku"))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)