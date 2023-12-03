import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import User, Message
from details import api_id, api_hash, bot_token, auth_users, sudo_user, log_channel, txt_channel
from subprocess import getstatusoutput
import logging
import os
import sys
import re

import requests
bot = Client(
    "bot",
    api_id= 22779671,
    api_hash= "125d8d88b77309dc3b154cbbfc2dacb2",    
    bot_token= "6152562853:AAGimPmtvHjqcE8em9iDMH-QAjkM8133P0c"
)

logger = logging.getLogger()
@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **Classplus txt Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/cp** to continue..\n\n")
@bot.on_message(filters.command(["cp"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    s = requests.Session()
    editable = await m.reply_text("**Send Token from ClassPlus App**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    headers = {
    'authority': 'api.classplusapp.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'api-version': '28',
    'cache-control': 'no-cache',
    'device-id': '516',
    'origin': 'https://web.classplusapp.com',
    'pragma': 'no-cache',
    'referer': 'https://web.classplusapp.com/',
    'region': 'IN',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-access-token':f'{raw_text0}'
}
    
    resp = s.get('https://api.classplusapp.com/v2/batches/details?limit=20&offset=0&sortBy=createdAt', headers=headers)
    if resp.status_code==200:
        pass
    else:
        editable = await m.reply_text("Login Failed Check Response")
    b_data = resp.json()["data"]["totalBatches"]
    print(b_data)
    await input1.delete(True)
    cool = ""
    for data in b_data:
        t_name =data['batchName']
        t_id =data['batchId']
        FFF = "**BATCH-ID - BATCH NAME**"
        aa = f" ```{t_id}```  - **{t_name}**\n\n"
        # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    cr = input2.text
    resp = s.get(f'https://api.classplusapp.com/v2/course/content/get?courseId={cr}', headers=headers)
    print(resp.content)
    b_data = resp.json()['data']['courseContent']
    cool = ""
    for data in b_data:
        id1 = data['id']
        nam2 =  data["name"]
        content =  data["contentType"]
        FFF = "**FOLDER-ID - FOLDER NAME**"
        aa = f" ```{id1}```      - **{nam2}**\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these Folders :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await editable1.delete(True)
    resp = s.get(f'https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text2}', headers=headers)
    bdata = resp.json()['data']['courseContent']
    cool = ""
    for data in bdata:
        id1 = data['id']
        nam2 =  data["name"]
        vid =  data["resources"]["videos"]
        fid =  data["resources"]["files"]
        content =  data["contentType"]
        FFF = "**FOLDER-ID -FOLDER NAME -TOTAL VIDEOS/PDFS**"
        aa = f" ```{id1}``` - **{nam2}  -{vid} -{fid}**\n\n"
        if len(f'{cool}{aa}') > 4096:
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these Folders :-**"}\n\n{FFF}\n\n{cool}')
    await input2.delete(True)
    editable1 = await m.reply_text("**Now send the Folder ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await editable1.delete(True)
    respc = s.get(f'https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text3}', headers=headers).json()
    ddata = respc['data']['courseContent']
    
    if (respc["data"]["courseContent"][0]["contentType"]) ==1:
        bdata = resp.json()['data']['courseContent']
        cool = ""
        for datas in ddata:
            id2 = datas['id']
            nam2 =  datas["name"]
            vid2 =  datas["resources"]["videos"]
            fid =  datas["resources"]["files"]
            content =  datas["contentType"]
            print(id2,nam2,vid)
            FFF = "**FOLDER-ID -FOLDER NAME -TOTAL VIDEOS/PDFS**"
            aa = f" ```{id2}``` - **{nam2} -{vid2}**\n\n"
            if len(f'{cool}{aa}') > 4096:
                cool = ""
            cool += aa
        await editable.edit(f'{"**You have these Folders :-**"}\n\n{FFF}\n\n{cool}')
        await input2.delete(True)
        editable1 = await m.reply_text("**Now send the Folder ID to Download**")
        input4 = message = await bot.listen(editable.chat.id)
        raw_text4 = input4.text
        await editable1.delete(True)
        resp = s.get(f'https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text4}', headers=headers)
        #print(resp)
        bdat = resp.json()['data']['courseContent']
        bdat.reverse()
        #print(bdat)
        cool = ""
        vj1 = ""
        for data in bdat:
            id1 = data['id']
            nam2 =  data["name"]
            dis2 = data["description"]
            url2 = data["url"]
            content =  data["contentType"]
            FFF = "**Topic-ID -Topic NAME **"
            aa = f" ```{id2}``` - **{nam2}  -{dis2}**\n\n"
            if len(f'{vj1}{aa}') > 4096:
                #print(aa)
                cool = ""
            cool += aa
            mm = "careerplus1"
            with open(f'{mm}.txt', 'a') as f:
                    f.write(f"{nam2}-{dis2}:{url2}\n")
        await m.reply_document(f"{mm}.txt")
        await input4.delete(True)
        await editable.edit(f'{"**You have these Videos :-**"}\n\n{FFF}\n\n{cool}')
    else:
        ddata.reverse()
        cool = ""
        vj = ""
        
        for data in ddata:
            id2 = str(data['id'])
            #idid = f"{data['id']}&"
            nam2 =  data["name"]
            url2=  data["url"]
            des2=  data["description"]
            
            #respc = s.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers).json()
            #urli = respc["url"]
            FFF = "**Topic-ID -Topic NAME **"
            aa = f" ```{id2}``` - **{nam2}  -{des2}**\n\n"
            if len(f'{vj}{aa}') > 4096:
                #print(aa)
                cool = ""
            cool += aa
            
            mm = "classplus"
            with open(f'{mm}.txt', 'a') as f:
                    f.write(f"{nam2}-{des2}:{url2}\n")
        await m.reply_document(f"{mm}.txt")           
        await editable.edit(f'{"**You have these Videos :-**"}\n\n{FFF}\n\n{cool}')
        #await m.reply_document(f"{nam2}.txt")
        await input3.delete(True)
        await m.reply_text("**Now Press /cpd to Download **")
