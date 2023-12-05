import logging, asyncio

from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery, Message

from config import NAME, API_ID, API_HASH, BOT_TOKEN, START_TEXT, DYNAMIC_TEXT, MARKDOWN_TEXT
from database import update_caption, update_button, get_button, get_caption, del_caption, del_button
from utils import start_button, close_and_back_buttons, create_button, generate_caption

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

app = Client(NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command(["start", "help"]) & filters.private)
async def start(app, message: Message):
    await message.reply_text(
        START_TEXT.format(
            message.from_user.first_name
        ),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=start_button(),
        quote=True
    )

@app.on_callback_query()
async def button(app, message: CallbackQuery):
    cb_data = message.data
    if "back_data" in cb_data:
        await message.message.edit(
            text=START_TEXT.format(
                message.from_user.first_name
            ),
            parse_mode=ParseMode.MARKDOWN, 
            disable_web_page_preview=True,
            reply_markup=start_button()
        )
    elif "close_data" in cb_data:
        await message.message.delete()
        # await message.message.reply_to_message.delete()
    elif "markdown_data" in cb_data:
        await message.message.edit(
            text=MARKDOWN_TEXT,
            parse_mode=ParseMode.HTML, 
            disable_web_page_preview=True, 
            reply_markup=close_and_back_buttons()
        )
    elif "dynamic_data" in cb_data:
        await message.message.edit(
            text=DYNAMIC_TEXT,
            parse_mode=ParseMode.MARKDOWN, 
            disable_web_page_preview=True, 
            reply_markup=close_and_back_buttons()
        )

@app.on_message(filters.private)
async def set(app, message: Message):
    if ("/set_cap" in message.text) and ((len(message.text.split(" ")) == 2) or (len(message.text.split(" ")) == 1)):
        await message.reply_text(
            """**SET CAPTION**

Use this command to set custom caption for any of your channels.

- `/set_cap -1001234567890 My Caption`
            """,
            quote = True)
    elif ("/set_cap" in message.text) and (len(message.text.split(" ")) != 2) and (len(message.text.split(" ")) != 1):
        caption = message.text.markdown.split(" ", 2)[2]
        channel = message.text.split(" ", 2)[1].replace("-100", "")
        try:
            a = await get_caption(channel)
            b = a.caption
        except:
            await update_caption(channel, caption)
            return await message.reply_text(
                f"**Your Caption:**\n\n{caption}",
                quote=True)
        await message.reply_text(
            """⚠️
A caption already seted for this channel.
You should first use /rmv_cap command to remove the current caption and then try seting new.
            """,
            quote=True)
    if ("/set_btn" in message.text) and ((len(message.text.split(" ")) == 2) or (len(message.text.split(" ")) == 1)):
        await message.reply_text(
            """**SET BUTTON**

Use this command to set button for any of your channels.
Send a Button name and URL(separated by ' | ').

- `/set_btn -1001234567890 Channel | https://t.me/channel`
            """
            , quote = True)
    elif ("/set_btn" in message.text) and (len(message.text.split(" ")) != 2) and (len(message.text.split(" ")) != 1):
        button = message.text.split(" ", 2)[2]
        channel = message.text.split(" ", 2)[1].replace("-100", "")
        try:
            a = await get_button(channel)
            b = a.button
        except:
            await update_button(channel, button)
            return await message.reply_text(
                f"**Your Button:**\n\n{button}",
                reply_markup=create_button(button),
                disable_web_page_preview=True,
                quote=True,
            )

        await message.reply_text(
            """⚠️
A button already seted for this channel.
You should first use /rmv_btn command to remove the current button and then try seting new.
            """,
            quote=True)
    if (message.text == "/rmv_cap"):
        await message.reply_text(
            """**REMOVE CAPTION**

Use this command to remove the current caption of any of your channels.

- `/rmv_cap -1001234567890`
            """,
            quote = True)
    elif ("/rmv_cap" in message.text) and (len(message.text.split(" ")) != 1):
        channel = message.text.split(" ", 1)[1].replace("-100", "")
        try:
            a = await get_caption(channel)
            b = a.caption
        except:
            return await message.reply_text(
                "Caption not setted yet!",
                quote=True)     
        await del_caption(channel)
        await message.reply_text(
            "The Caption Removed Successfully.",
            quote=True)

    if (message.text == "/rmv_btn"):
        await message.reply_text(
            """**REMOVE BUTTON**

Use this command to remove the current button of any of your channels.

- `/rmv_btn -1001234567890`
            """,
            quote=True)
    elif ("/rmv_btn" in message.text) and (len(message.text.split(" ")) != 1):
        channel = message.text.split(" ", 1)[1].replace("-100", "")
        try:
            a = await get_button(channel)
            b = a.button
        except:
            return await message.reply_text(
                "Button not setted yet!",
                quote=True)
        await del_button(channel)
        await message.reply_text(
            "The Button Removed Successfully.",
            quote=True)

    if (message.text == "/get_info"):
        await message.reply_text(
            """**GET BUTTON AND CAPTION**

Use this command to get the current button and caption of any of your channels.

- `/get_info -1001234567890`
            """,
            quote=True)
    elif ("/get_info" in message.text) and (len(message.text.split(" ")) != 1):
        channel = message.text.split(" ", 1)[1].replace("-100", "")

        try:
            b = await get_button(channel)
            button = b.button
            reply_markup = create_button(button)
        except:
            button = "`None`"
            reply_markup = None

        caption = (await get_caption(channel)).caption if await get_caption(channel) else "`None`"

        await message.reply_text(
            f"""
**Your Caption:**
{caption}

**Your Button:**
{button}
            """,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True,
        )


@app.on_message(
    filters.channel & (
        filters.photo |
        filters.audio |
        filters.video |
        filters.document
    ),
    group=-1
)
async def edit(app: Client, message: Message):
    channel = str(message.chat.id).replace("-100", "")
    try:
        btn = await get_button(int(channel))
        button = btn.button
    except:
        button = None
        pass

    try:
        c = await get_caption(int(channel))
        cap = c.caption
        caption = generate_caption(message, cap)
    except:
        caption = None
        pass

    if (caption and button) is None:
        return

    if button is not None:
        if caption is not None:
            _caption = caption
            reply_markup_ = create_button(button)
        elif caption is None:
            reply_markup_ = create_button(button)
            if message.caption:
                _caption = message.caption
            else:
                _caption = None
    elif (button is None) and (caption is not None):
        _caption = caption
        reply_markup_ = None

    try:
        await app.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message.id,
            caption=_caption,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_markup_
        )
    except FloodWait as e:
        print(f"Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
    except Exception as e:
        print(e)

print("Bot is runing...")
app.run()