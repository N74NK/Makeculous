from telethon import TelegramClient, events, sync
import time
import datetime
import os

os.system("rm -rf .session")
os.system("clear")

print("\n\n\n\n\033[1;35m ╔╦╗╔═╗╦╔═╔═╗╔═╗╦ ╦╦  ╔═╗╦ ╦╔═╗")
print(" ║║║╠═╣╠╩╗║╣ ║  ║ ║║  ║ ║║ ║╚═╗")
print(" ╩ ╩╩ ╩╩ ╩╚═╝╚═╝╚═╝╩═╝╚═╝╚═╝╚═╝")
print("   \033[1;36m[\033[0;31m+\033[1;36m] \033[0;36mAuthor: \033[0;37mNjank Soekamti")
print("   \033[1;36m[\033[0;31m+\033[1;36m] \033[0;36mYoutube: \033[0;37mNjank Soekamti")
print("   \033[1;36m[\033[0;31m+\033[1;36m] \033[0;36mFacebook:\033[0;37m Njank Soekamti")
print("   \033[1;36m[\033[0;31m+\033[1;36m] \033[0;36mTelegram:\033[0;37m @HDRXDROID")
print("   \033[1;36m[\033[0;31m+\033[1;36m] \033[0;36mGithub: \033[0;37mN74NK\n\033[0;36m")

api_id = 491787
api_hash = '58839ada91de89607ec39b86c3f85247'
client = TelegramClient(".session", api_id, api_hash)
client.start()
BCbot = client.get_entity('Makeculous_bot')
print("\n")
count=0
while 1:
    client.send_message(BCbot, "/Ads")
    currentDT = datetime.datetime.now()
    print (currentDT.strftime("   \033[1;36m[\033[1;90m%H:%M:%S\033[1;36m] \033[0;32mCongratulation! Claim reward success!"))
    time.sleep(33)
end