
NAME = "AutoCaption"
API_ID = None
API_HASH =  ""
BOT_TOKEN = ""
DB_URL = ""


START_TEXT = """
**Hello {},**
**I am Channel Auto Caption bot.**

**I can automatically add pre-setted caption and button to the files.**
**You can also use Markdown styles, supported Dynamic variables in seting caption (Details in below buttons).**

**Commands:**
    - /get_info: To get caption and button
    - /set_cap: To set caption
    - /set_btn: To set button
    - /rmv_cap: To remove caption
    - /rmv_btn: To remove button

⚠️ **Before seting, ensure that bot is admin in your channel with editing permission.**
"""

DYNAMIC_TEXT = """
--**About Dynamic**--

- **You can add** `{variable_name}` **in caption, bot will replace these variables by its value according to message.**

**Supported variables:**
    - `{file_id}` -> (video, audio, document, photo)
    - `{mime_type}` -> (video, audio, document)
    - `{file_name}` -> (audio, document)
    - `{duration}` -> (video, audio)
    - `{height}` -> (video, photo)
    - `{width}` -> (video, photo)
    - `{performer}` -> (audio)
    - `{title}` -> (audio)
    - `{ext}` -> (document)

**Example:**
    - `/set_cap -1001234567890 Artist: {performer} Song: {title}
    
    - Your is caption -> Artist: Taylor Swift Song: Shake it Off
"""

MARKDOWN_TEXT = """
<b><u>ABOUT MARKDOWN</u></b>

<b>Bold text:</b>
    <code>**text**</code>

<b>Italic text:</b>
    <code>__text__</code>

<b>Underline text:</b>
    <code>--text--</code>

<b>Strike text:</b>
    <code>~~text~~</code>

<b>Code text:</b>
    <code>`text`</code>

<b>Hyperlink text</b>
    <code>[text](https://t.me/durov)</code>
"""
