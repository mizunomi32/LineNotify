#!/usr/bin/env python
# coding: utf-8

import requests
class LineNotify:
    '''
    LINE Notifyのマイページ(https://access.line.me/dialog/oauth/weblogin?response_type=code&client_id=1476232700&redirect_uri=https%3A%2F%2Fnotify-bot.line.me%2Flogin%2Fcallback&state=cVUqnqvNYgJzq2EPMLqCVy&response_mode=form_post)
    にログインし,アクセストークンを取得してご使用ください．

    # 使い方
    from line_notify import LineNotify as Line
    token = 'xxxxxxxxxxxxxx' # 取得したトークン
    myLine = Line(token)
    myLine.send("text") # 文字だけを送る場合
    myLine.send("image","/path/to/image.jpeg") # 画像を送る場合
    '''
    
    def __init__(self,token):
        self.token = token
        self.line_notify_api = 'https://notify-api.line.me/api/notify'

    def send(self,message,file_path=None):
        '''
        message : 送信するメッセージ
        file_path : 送信する画像(png/jpeg)
        '''
        message = '\n' + message
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + self.token}
        if file_path!=None :
            try:
                files = {"imageFile": open(file_path, "rb")}
                r = requests.post(self.line_notify_api, headers = headers, params=payload, files=files)
                return r
            except FileNotFoundError:
                print("FileNotFoundError")
                return
        r = requests.post(self.line_notify_api, headers=headers, data=payload)
        return r
