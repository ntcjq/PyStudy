from text_blind_watermark import TextBlindWatermark2


def encrypt(text, watermark, password):
    text_blind_wm = TextBlindWatermark2(password=password)

    text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
    print('加密内容：', text_with_wm)
    return text_with_wm


def decrypt(text_with_wm, password):
    text_blind_wm2 = TextBlindWatermark2(password=password)
    wm_extract = text_blind_wm2.extract(text_with_wm)
    print('提取内容：', wm_extract)


if __name__ == '__main__':
    text = '这句话中有盲水印，你能提取出来吗？'
    watermark = 'sea'
    password = '1993'
    text_with_wm = encrypt(text, watermark, password)
    wm = decrypt(text_with_wm, password)
