from PIL import Image
from image_commodity_searcher.image_caption import ImageCaptionHandler
from image_commodity_searcher.keyword_generator import KeywordGenerator
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import configparser
from util.keyword_parser import parse

secrets = configparser.ConfigParser()
secrets.read('secret.ini')
CHANNEL_SECRET = secrets['DEFAULT']['CHANNEL_SECRET']
CHANNEL_ACCESS_TOKEN = secrets['DEFAULT']['CHANNEL_ACCESS_TOKEN']
OPENAI_API_KEY = secrets['DEFAULT']['OPENAI_API_KEY']



line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


def handler(event, context):
    signature = event.headers['X-Line-Signature']
    body = event["body"]
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        {
            "statusCode": 400,
            "body": "InvalidSignatureError"
        }
    return {
        "statusCode": 200,
        "body": "ok"    
    }

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    filename = f'{event.message.id}.jpg'
    with open(filename, 'wb') as fd:
        fd.write(message_content.content)
    
    image = Image.open(filename)
    image_caption_handler = ImageCaptionHandler()

    caption = image_caption_handler.generate_caption(image)

    keyword_generator =  KeywordGenerator(key=OPENAI_API_KEY)
    result = parse(keyword_generator.generate(caption))

    shopee_link = "https://shopee.tw/search?keyword=" + result
            
    os.remove(filename)    
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=shopee_link))