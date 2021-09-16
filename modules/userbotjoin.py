
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from services.callsmusic.callsmusic import client as USER
from config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Pɪᴋᴀ Pɪᴋᴀ, Aᴅᴅ Mᴇ As Aᴅᴍɪɴ Oғ Yᴏᴜʀ Gʀᴏᴜᴘ Fɪʀsᴛ.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "PikachuXMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Pɪᴋᴀ Pɪᴋᴀ, I Jᴏɪɴᴇᴅ Tʜɪs Gʀᴏᴜᴘ Fᴏʀ Pʟᴀʏɪɴɢ Mᴜsɪᴄs Iɴ Vᴄ.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Pɪᴋᴀ Pɪᴋᴀ, Hᴇʟᴘᴇʀ Aʟʀᴇᴀᴅʏ Iɴ Yᴏᴜʀ Cʜᴀᴛ.</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Pɪᴋᴀ Pɪᴋᴀ, 🔴 Fʟᴏᴏᴅ Wᴀɪᴛ Eʀʀᴏʀ 🔴 \nUsᴇʀ @PikachuXdAssistant Cᴏᴜʟᴅɴ'ᴛ Jᴏɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ Dᴜᴇ Tᴏ Hᴇᴀᴠʏ Rᴇǫᴜᴇsᴛᴇᴅ Fᴏʀ Usᴇʀʙᴏᴛ! Mᴀᴋᴇ Sᴜʀᴇ Usᴇʀ Is Nᴏᴛ Bᴀɴɴᴇᴅ Iɴ Gʀᴏᴜᴘ."
            "\n\nOʀ Mᴀɴᴜᴀʟʟʏ Aᴅᴅ @PikachuXdAssistant Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Tʀʏ Aɢᴀɪɴ.</b>",
        )
        return
    await message.reply_text(
        "<b>Pɪᴋᴀ Pɪᴋᴀ, Hᴇʟᴘᴇʀ Usᴇʀʙᴏᴛ Jᴏɪɴᴇᴅ Yᴏᴜʀ Cʜᴀᴛ.</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Pɪᴋᴀ Pɪᴋᴀ, Usᴇʀ Cᴏᴜʟᴅɴ'ᴛ Lᴇᴀᴠᴇ Yᴏᴜʀ Gʀᴏᴜᴘ! Mᴀʏ Bᴇ Fʟᴏᴏᴅᴡᴀɪᴛs."
            "\n\nOʀ Mᴀɴᴜᴀʟʟʏ Kɪᴄᴋ Mᴇ Fʀᴏᴍ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ.</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Pɪᴋᴀ Pɪᴋᴀ, Assɪsᴛᴀɴᴛ Lᴇᴀᴠɪɴɢ Aʟʟ Cʜᴀᴛs.")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assɪsᴛᴀɴᴛ Lᴇᴀᴠɪɴɢ... Lᴇғᴛ : {left} Cʜᴀᴛs. Fᴀɪʟᴇᴅ : {failed} Cʜᴀᴛs.")
            except:
                failed=failed+1
                await lol.edit(f"Assɪsᴛᴀɴᴛ Lᴇᴀᴠɪɴɢ... Lᴇғᴛ : {left} Cʜᴀᴛs. Fᴀɪʟᴇᴅ : {failed} Cʜᴀᴛs.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Lᴇғᴛ : {left} Cʜᴀᴛs. Fᴀɪʟᴇᴅ : {failed} Cʜᴀᴛs.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Pɪᴋᴀ Pɪᴋᴀ, Aᴅᴅ Mᴇ As Aᴅᴍɪɴ Oғ Yᴏᴜʀ Gʀᴏᴜᴘ Fɪʀsᴛ.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "PikachuXMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Pɪᴋᴀ Pɪᴋᴀ, I Jᴏɪɴᴇᴅ Tʜɪs Gʀᴏᴜᴘ Fᴏʀ Pʟᴀʏɪɴɢ Mᴜsɪᴄs Iɴ Vᴄ.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Pɪᴋᴀ Pɪᴋᴀ, Hᴇʟᴘᴇʀ Aʟʀᴇᴀᴅʏ Iɴ Yᴏᴜʀ Cʜᴀᴛ.</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Pɪᴋᴀ Pɪᴋᴀ, 🔴 Fʟᴏᴏᴅ Wᴀɪᴛ Eʀʀᴏʀ 🔴 \nUsᴇʀ @PikachuXdAssistant Cᴏᴜʟᴅɴ'ᴛ Jᴏɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ Dᴜᴇ Tᴏ Hᴇᴀᴠʏ Rᴇǫᴜᴇsᴛᴇᴅ Fᴏʀ Usᴇʀʙᴏᴛ! Mᴀᴋᴇ Sᴜʀᴇ Usᴇʀ Is Nᴏᴛ Bᴀɴɴᴇᴅ Iɴ Gʀᴏᴜᴘ."
            "\n\nOʀ Mᴀɴᴜᴀʟʟʏ Aᴅᴅ @PikachuXdAssistant Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Tʀʏ Aɢᴀɪɴ.</b>",
        )
        return
    await message.reply_text(
        "<b>Pɪᴋᴀ Pɪᴋᴀ, Hᴇʟᴘᴇʀ Usᴇʀʙᴏᴛ Jᴏɪɴᴇᴅ Yᴏᴜʀ Cʜᴀᴛ.</b>",
    )
    
