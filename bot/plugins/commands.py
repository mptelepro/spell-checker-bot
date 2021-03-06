#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
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
                caption =f"<b>FILM NAMEπ½οΈ</b>: <code><b> {file_name}</b> </code>\n\n<b>β€οΈ<u> ππππππ’ππ π΅ππ πππππ πΎππ πππππππ πΏπππππ πππππππ ππ π±π’ πππππππ πΎππ π²ππππππ/πΆππππ π»πππ ππ ππππ π΅ππππππβ€οΈ</b></u>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('βε½‘[κ±Κα΄Κα΄]ε½‘β', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('βκ±α΄α΄α΄α΄Κα΄β', url="https://t.me/joinchat/Qdw9ffZKXMxmMTg1"),
                    InlineKeyboardButton('βκ±α΄ΚΙͺα΄κ±β', url="https://t.me/MoviesClubSeriesonly")
                ]
            ]
        )
    )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('βα΄Κα΄α΄α΄α΄Κβ', url='https://t.me/AlbertEinstein_TG'),
        InlineKeyboardButton('βΚα΄Κα΄β', callback_data="help")
    ],[
        InlineKeyboardButton('βε½‘[ΚΚΙͺΙ΄α΄α΄Κ α΄Ι’]ε½‘β', url='https://t.me/Myfreak123')
    ],[
        InlineKeyboardButton('βΙ’Κα΄α΄α΄β', url='https://t.me/Movies_Club_2019'),
        InlineKeyboardButton('βα΄α΄α΄ α΄α΄α΄α΄α΄α΄κ±β', url='https://t.me/mcnewmovies')
    ],[
        InlineKeyboardButton('βε½‘[κ°α΄ΚΚα΄α΄‘ α΄α΄ α΄Ι΄ Ι’Ιͺα΄Κα΄Κ]ε½‘β', url='https://github.com/Sreejithmadmax')
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
        InlineKeyboardButton('βΚα΄α΄α΄β', callback_data='start'),
        InlineKeyboardButton('βα΄Κα΄α΄α΄β', callback_data='about')
    ],[
        InlineKeyboardButton('βα΄Κα΄κ±α΄β', callback_data='close')
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
        InlineKeyboardButton('βα΄Κα΄α΄α΄α΄Κβ', url='https://t.me/AlbertEinstein_TG')
    ],[
        InlineKeyboardButton('βε½‘[κ°α΄ΚΚα΄α΄‘ α΄α΄ α΄Ι΄ Ι’Ιͺα΄Κα΄Κ]ε½‘β', url='https://github.com/Sreejithmadmax')
    ],[
        InlineKeyboardButton('βΚα΄α΄α΄β', callback_data='start'),
        InlineKeyboardButton('βα΄Κα΄κ±α΄β', callback_data='close')
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
