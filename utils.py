
import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_button():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "About Markdown",
                    callback_data="markdown_data"), 
                InlineKeyboardButton(
                    "About Dynamic",
                    callback_data="dynamic_data")
            ],
            [
                InlineKeyboardButton(
                    "Source Code",
                    url="https://github.com/suphiozturk8"),
                InlineKeyboardButton(
                    "Close",
                    callback_data="close_data")
            ]
        ]
    )

def close_and_back_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Back",
                    callback_data="back_data"
                ),
                InlineKeyboardButton(
                    "Close",
                    callback_data="close_data"
                )
            ]
        ]
    )

def create_button(button):
    Url = button.rsplit(" ", 1)[1]
    Name = button.split(" | ")[0]
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    Name,
                    url=f"{Url}"
                )
            ]
        ]
    )

def generate_caption(message, cap):
    m = message.photo or message.audio or message.video or message.document
    if m:
        former_cap = str(message.caption) if hasattr(message, "caption") else ""
        file_id = str(m.file_id) if hasattr(m, "file_id") else ""
        file_name = str(m.file_name) if hasattr(m, "file_name") else ""
        mime_type = str(m.mime_type) if hasattr(m, "mime_type") else ""
        width = str(m.width) if hasattr(m, "width") else ""
        height = str(m.height) if hasattr(m, "height") else ""
        performer = str(m.performer) if hasattr(m, "performer") else ""
        title = str(m.title) if hasattr(m, "title") else ""
        duration = str(datetime.timedelta(seconds=m.duration)) if hasattr(m, "duration") else ""

        if file_name and "." in file_name:
            file_extension = "." + file_name.rsplit(".", 1)[1]
        else:
            file_extension = ""

        caption = cap\
            .replace("{file_id}", file_id)\
            .replace("{file_name}", file_name)\
            .replace("{mime_type}", mime_type)\
            .replace("{width}", width)\
            .replace("{height}", height)\
            .replace("{performer}", performer)\
            .replace("{title}", title)\
            .replace("{duration}", duration)\
            .replace("{ext}", file_extension)\
            .replace("{former_cap}", former_cap)

    return caption
