
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys


HOME_TEXT = "<b>🤞 Pɪᴋᴀ Pɪᴋᴀ, [{}](tg://user?id={}).\n\n• I'ᴀᴍ Pɪᴋᴀᴄʜᴜ • Mᴜsɪᴄ.\n• I Cᴀɴ Mᴀɴᴀɢᴇ Gʀᴏᴜᴘ Vᴄ's.\n\n• Hɪᴛ /help Tᴏ Kɴᴏᴡ Aʙᴏᴜᴛ Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs.</b>"
HELP = """
🎧 <b>I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄs Oɴ Vᴏɪᴄᴇᴄʜᴀᴛs 🤘.</b>

🎧 **Cᴏᴍᴍᴏɴ Cᴏᴍᴍᴀɴᴅs**:
• `/song` __Dᴏᴡɴʟᴏᴀᴅ Sᴏɴɢ Fʀᴏᴍ Yᴏᴜᴛᴜʙᴇ__
• `/play`  __Pʟᴀʏ Sᴏɴɢ Yᴏᴜ Rᴇǫᴜᴇsᴛᴇᴅ__
• `/help` __Sʜᴏᴡ Hᴇʟᴘ Fᴏʀ Cᴏᴍᴍᴀɴᴅs__
• `/dplay` __Pʟᴀʏ Sᴏɴɢ Yᴏᴜ Rᴇǫᴜᴇsᴛᴇᴅ Vɪᴀ Dᴇᴇᴢᴇʀ__
• `splay` __Pʟᴀʏ Sᴏɴɢ Yᴏᴜ Rᴇǫᴜᴇsᴛᴇᴅ Vɪᴀ Jɪᴏ Sᴀᴀᴠɴ__
• `/ytplay` __Pʟᴀʏ Sᴏɴɢ Dɪʀᴇᴄᴛʟʏ Fʀᴏᴍ Yᴏᴜᴛᴜʙᴇ Sᴇʀᴠᴇʀ__
• `/search` __Sᴇᴀʀᴄʜ Vɪᴅᴇᴏ Sᴏɴɢs Lɪɴᴋs__
• `/current` __Sʜᴏᴡ Nᴏᴡ Pʟᴀʏɪɴɢ__
• `/playlist` __Sʜᴏᴡ Nᴏᴡ Pʟᴀʏɪɴɢ Lɪsᴛ__
• `/video` __Dᴏᴡɴʟᴏᴀᴅs Vɪᴅᴇᴏ Sᴏɴɢ Qᴜɪᴄᴋʟʏ__
🎧 **Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs**:
• `/player`  __Oᴘᴇɴ Mᴜsɪᴄ Pʟᴀʏᴇʀ Sᴇᴛᴛɪɴɢs Pᴀɴᴇʟ__
• `/pause` __Pᴀᴜsᴇ Sᴏɴɢ Pʟᴀʏ__
• `/skip` __Sᴋɪᴘ Nᴇxᴛ Sᴏɴɢ__
• `/resume`  __Rᴇsᴜᴍᴇ Sᴏɴɢ Pʟᴀʏ__
• `/userbotjoin`  __Iɴᴠɪᴛᴇs Assɪsᴛᴀɴᴛ Tᴏ Yᴏᴜʀ Cʜᴀᴛ__
• `/end` __Sᴛᴏᴘs Mᴜsɪᴄ Pʟᴀʏ__
• `/admincache` __Rᴇғʀᴇsʜ Lɪsᴛ Oғ Aᴅᴍɪɴs Wɪᴛʜ Vᴄ Pᴏᴡᴇʀ__
© Pᴏᴡᴇʀᴇᴅ Bʏ 
[ __@Sanki_BOTs__ ].
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/Sanki_BOTs'),
                InlineKeyboardButton('💬 Sᴜᴘᴘᴏʀᴛ', url='https://t.me/Sanki_Bots_Support')
                ],[
                InlineKeyboardButton('🤖 Dᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/iTs_Nitric'),
                InlineKeyboardButton('🎧 Cʜᴀᴛ', url='https://t.me/Dramaa_Club')
                ],[
                InlineKeyboardButton('📜 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 📜', url='https://t.me/iTs_Nitric'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/707fda22ee5dc349b50ab.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/Sanki_BOTs'),
                InlineKeyboardButton('💬 Sᴜᴘᴘᴏʀᴛ', url='https://t.me/Sanki_Bots_Support')
                ],[
                InlineKeyboardButton('🤖 Dᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/iTs_Nitric'),
                InlineKeyboardButton('🎧 Cʜᴀᴛ', url='https://t.me/Dramaa_Club')
                ],[
                InlineKeyboardButton('📜 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 📜', url='https://t.me/iTs_Nitric'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/707fda22ee5dc349b50ab.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
