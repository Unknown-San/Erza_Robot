#import re

# import emoji

# url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
# import re

# import aiohttp

# # from google_trans_new import google_translator
# from googletrans import Translator as google_translator
# from pyrogram import filters

# from AsunaRobot import BOT_ID, pbot as erza
# from AsunaRobot.helper_extra.aichat import add_chat, get_session, remove_chat
# from AsunaRobot.pyrogramee.pluginshelper import admins_only, edit_or_reply

# translator = google_translator()


# async def lunaQuery(query: str, user_id: int):
#     luna = await arq.luna(query, user_id)
#     return luna.result


# def extract_emojis(s):
#     return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


# async def fetch(url):
#     try:
#         async with aiohttp.Timeout(10.0):
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(url) as resp:
#                     try:
#                         data = await resp.json()
#                     except:
#                         data = await resp.text()
#             return data
#     except:
#         print("AI response Timeout")
#         return


# erza_chats = []
# en_chats = []
# # AI Chat (C) 2020-2021 by @InukaAsith

# from Python_ARQ import ARQ   
# from aiohttp import ClientSession
# ARQ_API_URL = "https://thearq.tech"
# ARQ_API_KEY = "EHUWCI-NULYWW-NMOKVY-SIDRJL-ARQ"

# aiohttpsession = ClientSession()
# arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)


# @erza.on_message(
#     filters.command("chatbot") & ~filters.edited & ~filters.bot & ~filters.private
# )
# @admins_only
# async def hmm(_, message):
#     global erza_chats
#     if len(message.command) != 2:
#         await message.reply_text(
#             "I only recognize `/chatbot on` and /chatbot `off only`"
#         )
#         message.continue_propagation()
#     status = message.text.split(None, 1)[1]
#     chat_id = message.chat.id
#     if status == "ON" or status == "on" or status == "On":
#         lel = await edit_or_reply(message, "`Processing...`")
#         lol = add_chat(int(message.chat.id))
#         if not lol:
#             await lel.edit("Erza AI Already Activated In This Chat")
#             return
#         await lel.edit(
#             f"Erza AI Successfully Added For Users In The Chat {message.chat.id}"
#         )

#     elif status == "OFF" or status == "off" or status == "Off":
#         lel = await edit_or_reply(message, "`Processing...`")
#         Escobar = remove_chat(int(message.chat.id))
#         if not Escobar:
#             await lel.edit("Erza AI Was Not Activated In This Chat")
#             return
#         await lel.edit(
#             f"Erza AI Successfully Deactivated For Users In The Chat {message.chat.id}"
#         )

#     elif status == "EN" or status == "en" or status == "english":
#         if not chat_id in en_chats:
#             en_chats.append(chat_id)
#             await message.reply_text("English AI chat Enabled!")
#             return
#         await message.reply_text("AI Chat Is Already Disabled.")
#         message.continue_propagation()
#     else:
#         await message.reply_text(
#             "I only recognize `/chatbot on` and /chatbot `off only`"
#         )


# @erza.on_message(
#     filters.text
#     & filters.reply
#     & ~filters.bot
#     & ~filters.edited
#     & ~filters.via_bot
#     & ~filters.forwarded,
#     group=2,
# )
# async def hmm(client, message):
#     if not get_session(int(message.chat.id)):
#         return
#     if not message.reply_to_message:
#         return
#     try:
#         senderr = message.reply_to_message.from_user.id
#     except:
#         return
#     if senderr != BOT_ID:
#         return
#     msg = message.text
#     chat_id = message.chat.id
#     if msg.startswith("/") or msg.startswith("@"):
#         message.continue_propagation()
#     if chat_id in en_chats:
#         test = msg
#         test = test.replace("erza", "Aco")
#         test = test.replace("Erza", "Aco")
#         response = await lunaQuery(
#             test, message.from_user.id if message.from_user else 0
#         )
#         response = response.replace("Aco", "erza")
#         response = response.replace("aco", "erza")

#         pro = response
#         try:
#             await erza.send_chat_action(message.chat.id, "typing")
#             await message.reply_text(pro)
#         except CFError:
#             return

#     else:
#         u = msg.split()
#         emj = extract_emojis(msg)
#         msg = msg.replace(emj, "")
#         if (
#             [(k) for k in u if k.startswith("@")]
#             and [(k) for k in u if k.startswith("#")]
#             and [(k) for k in u if k.startswith("/")]
#             and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
#         ):

#             h = " ".join(filter(lambda x: x[0] != "@", u))
#             km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
#             tm = km.split()
#             jm = " ".join(filter(lambda x: x[0] != "#", tm))
#             hm = jm.split()
#             rm = " ".join(filter(lambda x: x[0] != "/", hm))
#         elif [(k) for k in u if k.startswith("@")]:

#             rm = " ".join(filter(lambda x: x[0] != "@", u))
#         elif [(k) for k in u if k.startswith("#")]:
#             rm = " ".join(filter(lambda x: x[0] != "#", u))
#         elif [(k) for k in u if k.startswith("/")]:
#             rm = " ".join(filter(lambda x: x[0] != "/", u))
#         elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
#             rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
#         else:
#             rm = msg
#             # print (rm)
#         try:
#             lan = translator.detect(rm)
#             lan = lan.lang
#         except:
#             return
#         test = rm
#         if not "en" in lan and not lan == "":
#             try:
#                 test = translator.translate(test, dest="en")
#                 test = test.text
#             except:
#                 return
#         # test = emoji.demojize(test.strip())

#         test = test.replace("erza", "Aco")
#         test = test.replace("Erza", "Aco")
#         response = await lunaQuery(
#             test, message.from_user.id if message.from_user else 0
#         )
#         response = response.replace("Aco", "Erza")
#         response = response.replace("aco", "Erza")
#         response = response.replace("Luna", "Erza")
#         response = response.replace("luna", "Erza")
#         pro = response
#         if not "en" in lan and not lan == "":
#             try:
#                 pro = translator.translate(pro, dest=lan)
#                 pro = pro.text
#             except:
#                 return
#         try:
#             await erza.send_chat_action(message.chat.id, "typing")
#             await message.reply_text(pro)
#         except CFError:
#             return


# @erza.on_message(
#     filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot
# )
# async def inuka(client, message):
#     msg = message.text
#     if msg.startswith("/") or msg.startswith("@"):
#         message.continue_propagation()
#     u = msg.split()
#     emj = extract_emojis(msg)
#     msg = msg.replace(emj, "")
#     if (
#         [(k) for k in u if k.startswith("@")]
#         and [(k) for k in u if k.startswith("#")]
#         and [(k) for k in u if k.startswith("/")]
#         and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
#     ):

#         h = " ".join(filter(lambda x: x[0] != "@", u))
#         km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
#         tm = km.split()
#         jm = " ".join(filter(lambda x: x[0] != "#", tm))
#         hm = jm.split()
#         rm = " ".join(filter(lambda x: x[0] != "/", hm))
#     elif [(k) for k in u if k.startswith("@")]:

#         rm = " ".join(filter(lambda x: x[0] != "@", u))
#     elif [(k) for k in u if k.startswith("#")]:
#         rm = " ".join(filter(lambda x: x[0] != "#", u))
#     elif [(k) for k in u if k.startswith("/")]:
#         rm = " ".join(filter(lambda x: x[0] != "/", u))
#     elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
#         rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
#     else:
#         rm = msg
#         # print (rm)
#     try:
#         lan = translator.detect(rm)
#         lan = lan.lang
#     except:
#         return
#     test = rm
#     if not "en" in lan and not lan == "":
#         try:
#             test = translator.translate(test, dest="en")
#             test = test.text
#         except:
#             return

#     # test = emoji.demojize(test.strip())

#     # Kang with the credits bitches @InukaASiTH
#     test = test.replace("erza", "Aco")
#     test = test.replace("Erza", "Aco")

#     response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
#     response = response.replace("Aco", "Erza")
#     response = response.replace("aco", "Erza")

#     pro = response
#     if not "en" in lan and not lan == "":
#         pro = translator.translate(pro, dest=lan)
#         pro = pro.text
#     try:
#         await erza.send_chat_action(message.chat.id, "typing")
#         await message.reply_text(pro)
#     except CFError:
#         return


# @erza.on_message(
#     filters.regex("Erza|erza|erza|ERZA|Erza")
#     & ~filters.bot
#     & ~filters.via_bot
#     & ~filters.forwarded
#     & ~filters.reply
#     & ~filters.channel
#     & ~filters.edited
# )
# async def inuka(client, message):
#     msg = message.text
#     if msg.startswith("/") or msg.startswith("@"):
#         message.continue_propagation()
#     u = msg.split()
#     emj = extract_emojis(msg)
#     msg = msg.replace(emj, "")
#     if (
#         [(k) for k in u if k.startswith("@")]
#         and [(k) for k in u if k.startswith("#")]
#         and [(k) for k in u if k.startswith("/")]
#         and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
#     ):

#         h = " ".join(filter(lambda x: x[0] != "@", u))
#         km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
#         tm = km.split()
#         jm = " ".join(filter(lambda x: x[0] != "#", tm))
#         hm = jm.split()
#         rm = " ".join(filter(lambda x: x[0] != "/", hm))
#     elif [(k) for k in u if k.startswith("@")]:

#         rm = " ".join(filter(lambda x: x[0] != "@", u))
#     elif [(k) for k in u if k.startswith("#")]:
#         rm = " ".join(filter(lambda x: x[0] != "#", u))
#     elif [(k) for k in u if k.startswith("/")]:
#         rm = " ".join(filter(lambda x: x[0] != "/", u))
#     elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
#         rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
#     else:
#         rm = msg
#         # print (rm)
#     try:
#         lan = translator.detect(rm)
#         lan = lan.lang
#     except:
#         return
#     test = rm
#     if not "en" in lan and not lan == "":
#         try:
#             test = translator.translate(test, dest="en")
#             test = test.text
#         except:
#             return

#     # test = emoji.demojize(test.strip())

#     test = test.replace("erza", "Aco")
#     test = test.replace("Erza", "Aco")
#     response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
#     response = response.replace("Aco", "Erza")
#     response = response.replace("aco", "Erza")

#     pro = response
#     if not "en" in lan and not lan == "":
#         try:
#             pro = translator.translate(pro, dest=lan)
#             pro = pro.text
#         except Exception:
#             return
#     try:
#         await erza.send_chat_action(message.chat.id, "typing")
#         await message.reply_text(pro)
#     except CFError:
#         return


# __help__ = """
# <b> AI Chatbot </b>
# Erza AI 3.0 IS THE ONLY AI SYSTEM WHICH CAN DETECT & REPLY UPTO 200 LANGUAGES

#  - /chatbot [ON/OFF]: Enables and disables AI Chat mode (EXCLUSIVE)
#  - /chatbot EN : Enables English only chatbot
 
 
# <b> Chatbot </b>
#  - /ask [question]: Ask question from Erza
#  - /ask [reply to voice note]: Get voice reply
 
# """

# __mod_name__ = "Chatbot"
