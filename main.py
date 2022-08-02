import telegram.ext
import os
from os import environ
import re
import base64
import requests
from urllib.parse import urlparse, parse_qs

TOKEN = environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("Hello! THis bot will bypass the shortlinks and Generate Direct GDrive Link\nBot Developed by :- @DextiN_xD\nSupport @NetflixTudum")
    
def support(update, context):
   update.message.reply_text("""
   Only following sites' links are supported by me:
| `gplinks` | `droplink.co` | `mdisk` |
| adf.ly / fumacrom.com |
| appdrive | sharer.pw | hubdrive |
| rocklinks | ouo.press / ouo.io |
| linkvertise.com |
| sub2unlock.net / sub2unlock.com |
| letsboost.net | ph.apps2app.com |
| mboost.me | goo.gl | rekonise.com |
| shortconnect.com | sub4unlock.com |
| bit.ly | social-unlock.com |
| shrto.ml | t.co | tinyurl.com |
| ytsubme.com | boost.ink |""")

def adf(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ ADFLY LINK BYPASSING ⚡️⚡️")
        os.system('python adf.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"Done")
        update.message.reply_text(f"{zkm}")
        
def mdisk(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ MDISK LINK BYPASSING ⚡️⚡️")
        os.system('python mdisk.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def generic(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GENERIC LINK BYPASSING (UNSTABLE FAILS FREQUENTLY) ⚡️⚡️")
        os.system('python generic.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def gp(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GPLINKS LINK BYPASSING ⚡️⚡️")
        os.system('python gp.py')
        update.message.reply_text(f"Done")
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def droplink(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ DROPLINK LINK BYPASSING ⚡️⚡️")
        os.system('python droplink.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def gdtot(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GDTOT LINK BYPASSING ⚡️⚡️")
        os.system('python gdtot.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def hubdrive(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ HUBDRIVE LINK BYPASSING ⚡️⚡️")
        os.system('python hubdrive.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def katdrive(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GDTOT LINK BYPASSING ⚡️⚡️")
        os.system('python katdrive.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def kolop(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GDTOT LINK BYPASSING ⚡️⚡️")
        os.system('python kolop.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def drivefire(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GDTOT LINK BYPASSING ⚡️⚡️")
        os.system('python drivefire.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def magic(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ UNIFIED LINK BYPASSING ⚡️⚡️")
        os.system('python magic.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

        
def rocklinks(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ ROCKLINKS LINK BYPASSING ⚡️⚡️")
        os.system('python rocklinks.py')
        update.message.reply_text(f"Done")
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
@Bot.on_message(filters.command("bin"))
async def bin(_, m: Message):
    if len(m.command) < 2:
        msg = await m.reply_text("Please Provide a Bin!\nEx:- `/bin 401658`")
        await sleep(15)
        await msg.delete()

    else:
        try:
            mafia = await m.reply_text("processing...")
            inputm = m.text.split(None, 1)[1]
            bincode = 6
            ask = inputm[:bincode]
            req = requests.get(f"https://bins-su-api.vercel.app/api/{ask}").json()
            res = req["result"]

            if res == False:
                return await mafia.edit("❌ #INVALID_BIN ❌\n\nPlease provide a valid bin.")
            da = req["data"]
            bi = da["bin"]
            ve = da["vendor"]
            ty = da["type"]
            le = da["level"]
            ban = da["bank"]
            co = da["country"]
            cc = da["countryInfo"]
            nm = cc["name"]
            em = cc["emoji"]
            cod = cc["code"]
            dial = cc["dialCode"]

            mfrom = m.from_user.mention
            caption = f"""
    ╔ Valid :- `{res} ✅`\n╚ Bin :- `{bi}`\n\n╔ Brand :- `{ve}`\n╠ Type :- `{ty}`\n╚ Level :- `{le}`\n\n╔ Bank :- `{ban} ({co})`\n╠ Country :- `{nm} {em}`\n╠ Alpha2 :- `{cod}`\n╚ DialCode :- `{dial}`\n\n**↠ Checked By :-** {mfrom}\n**↠ __Bot By :-** [Denuwan](https://github.com/ImDenuwan/Bin-Checker-Bot)__
    """
            await mafia.edit(caption, disable_web_page_preview=True)

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("support", support))
disp.add_handler(telegram.ext.CommandHandler("adf", adf))
disp.add_handler(telegram.ext.CommandHandler("mdisk", mdisk))
disp.add_handler(telegram.ext.CommandHandler("droplink", droplink))
disp.add_handler(telegram.ext.CommandHandler("gdtot", gdtot))
disp.add_handler(telegram.ext.CommandHandler("hubdrive", hubdrive))
disp.add_handler(telegram.ext.CommandHandler("katdrive", katdrive))
disp.add_handler(telegram.ext.CommandHandler("kolop", kolop))
disp.add_handler(telegram.ext.CommandHandler("drivefire", drivefire))
disp.add_handler(telegram.ext.CommandHandler("magic", magic))
disp.add_handler(telegram.ext.CommandHandler("gp", gp))
disp.add_handler(telegram.ext.CommandHandler("generick", generic))
disp.add_handler(telegram.ext.CommandHandler("rocklinks", rocklinks))
#disp.add_handler(telegram.ext.CommandHandler("bincheck", bincheck))
updater.start_polling()
updater.idle()
