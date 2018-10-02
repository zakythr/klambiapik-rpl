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


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
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
    if text=="adit":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Hello, world'))
    if text=="mama":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://cdn.sindonews.net/dyn/620/content/2015/04/15/40/989729/ini-kapal-perang-china-yang-jadi-momok-bagi-as-gCA.jpg',preview_image_url='https://cdn.sindonews.net/dyn/620/content/2015/04/15/40/989729/ini-kapal-perang-china-yang-jadi-momok-bagi-as-gCA.jpg'))
    if text=="papa":
        line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://www.youtube.com/watch?v=ezWCLhZhDkw',preview_image_url='https://ecs7.tokopedia.net/img/cache/700/product-1/2017/7/29/600547/600547_9c950a89-e32b-4ec5-bd90-8ccedb2effe8.jpg'))
    if text=='tuan':
        line_bot_api.get_profile('U77ece03c792be8a0b931471cd636ba7a')
            print(profile.display_name)
            print(profile.user_id)
            print(profile.picture_url)
            print(profile.status_message)

    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Halo '+profile.display_name+'\nKata Kunci Tidak Diketahui :) \nKetik "menu" untuk mengetahui menu yang tersedia'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)