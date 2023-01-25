from pyrogram import Client, filters 
from config import ADMIN, temp

@Client.on_message(filters.command("set") & filters.user(ADMIN))                            
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    Tumb = msg.reply_to_message.photo.file_id
    temp.THUMBNAIL = Tumb
    return await msg.reply(f"Temporary Thumbnail saved✅️ \nDo You want permanent thumbnail. \n\n`{Tumb}` \n\n👆👆 please add this id to your server enviro with key=`THUMBNAIL`")            


@Client.on_message(filters.command("view") & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    if temp.THUMBNAIL:
        await msg.reply_photo(photo=temp.THUMBNAIL, caption="this is your current thumbnail")
