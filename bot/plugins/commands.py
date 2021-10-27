#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command("start"))
async def start(bot, update):
    update_channel = "@mcnewmovies"
        if update_channel:
            try:
                user = await bot.get_chat_member(int(update_channel), update.chat.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=update.chat.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=update.chat.id,
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url={update_channel})
                            ],
                            [
                                InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=update.chat.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption =f"<b>FILM NAME📽️</b>: <code><b> {file_name}</b> </code>\n\n<b>❤️<u> 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜❤️</b></u>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('★彡[ꜱʜᴀʀᴇ]彡★', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('★ꜱᴜᴘᴘᴏʀᴛ★', url="https://t.me/joinchat/Qdw9ffZKXMxmMTg1"),
                    InlineKeyboardButton('★ꜱᴇʀɪᴇꜱ★', url="https://t.me/MoviesClubSeriesonly")
                ]
            ]
        )
    )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('★ᴄʀᴇᴀᴛᴏʀ★', url='https://t.me/AlbertEinstein_TG'),
        InlineKeyboardButton('★ʜᴇʟᴘ★', callback_data="help")
    ],[
        InlineKeyboardButton('★彡[ʙʟɪɴᴅᴇʀ ᴛɢ]彡★', url='https://t.me/Myfreak123')
    ],[
        InlineKeyboardButton('★ɢʀᴏᴜᴘ★', url='https://t.me/Movies_Club_2019'),
        InlineKeyboardButton('★ᴏᴛᴛ ᴜᴘᴅᴀᴛᴇꜱ★', url='https://t.me/mcnewmovies')
    ],[
        InlineKeyboardButton('★彡[ꜰᴏʟʟᴏᴡ ᴍᴇ ᴏɴ ɢɪᴛʜᴜʙ]彡★', url='https://github.com/Sreejithmadmax')
   ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
                chat_id = update.chat.id,
                sticker= "CAACAgIAAxkBAAEBIkthdn0aVyTONxI9gAvIOyG-1cD6NAAC1AwAAnqLoEieLyIklDO8mx4E",
                reply_markup=reply_markup,  
                reply_to_message_id=update.message_id
            )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('★ʜᴏᴍᴇ★', callback_data='start'),
        InlineKeyboardButton('★ᴀʙᴏᴜᴛ★', callback_data='about')
    ],[
        InlineKeyboardButton('★ᴄʟᴏꜱᴇ★', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('★ᴄʀᴇᴀᴛᴏʀ★', url='https://t.me/AlbertEinstein_TG')
    ],[
        InlineKeyboardButton('★彡[ꜰᴏʟʟᴏᴡ ᴍᴇ ᴏɴ ɢɪᴛʜᴜʙ]彡★', url='https://github.com/Sreejithmadmax')
    ],[
        InlineKeyboardButton('★ʜᴏᴍᴇ★', callback_data='start'),
        InlineKeyboardButton('★ᴄʟᴏꜱᴇ★', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
