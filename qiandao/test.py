from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from base64 import b64encode
import requests 


def get():
    response = requests.get("https://saying.api.azwcl.com/saying/get") 
    response.encoding = response.apparent_encoding 
    null = None 
    a = eval(str(response.text)) 
    msg = eval(str(a['data']))['content']
    a = ""
    if len(msg) <= 15:
        a=msg
    else:
        while(True):
            a+= (msg[:15]+"\n")
            if len(msg)<15:
                break
            msg = msg[15:]
    return a


def createrr(user_name,gid,number,uid) -> str:
    # 图像的参数是凭感觉来的
    # TODO: we have a lot of byte copies. we have to optimise them.
    bg_dir = f'.\\qiandao\\chaotian2.png'
    font_dir = f'.\\qiandao\\VonwaonBitmap-16px.ttf'

    image = Image.open(bg_dir)
    draw = ImageDraw.ImageDraw(image)
    font_title = ImageFont.truetype(font_dir, 33 if len(user_name) < 8 else 28)
    font_detail = ImageFont.truetype(font_dir, 22)

    txt_user = f'{user_name}({uid})'
    draw.text((370, 65), txt_user, fill=(255, 255, 255), font=font_title, stroke_width=1, stroke_fill='#7042ad')

    txt_detail = (
        '小天使请安！\n'
        f'群: {gid}\n'
        f'签到数: {number}\n'
        f'{get()}'
    )
    draw.text((370, 115), txt_detail, fill=(255, 255, 255), font=font_detail, stroke_width=1, stroke_fill='#75559e')
    image=image.convert('RGB')
    image.save(fp = f".\\qiandao\\{uid}.png",format='JPEG',quality = 95)
    return 



