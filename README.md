
# My Channel Auto Caption Bot

## Overview
This bot automatically add caption and button to any media/document/video sent to a channel.

## Features
- **Automatic Title and Button Insert:** Predetermined titles and buttons can be automatically added to files.
- **Markdown Styles and Dynamic Variables:** You can make caption settings using Markdown styles and dynamic variables.
- **User Commands:** You can extend the functionality of the bot through user commands such as `/get_info`, `/set_cap`, `/set_btn`, `/rmv_cap`, `/rmv_btn`.
- **Helpful Messages:** The bot offers helpful messages related to specific commands that users can use.

## Usage
You can perform different functions using the bot's commands. Here is the use of some commands:
1. **/get_info**
This command allows you to retrieve the current title and button information for a specific channel.

Example Usage:
```
/get_info -1001234567890
```
2. **/set_cap**
This command allows you to set a custom title for a specific channel.

Example Usage:
```
/set_cap -1001234567890 Artist: {performer} Song: {title}
```
3. **/set_btn**
This command allows you to set a custom button for a specific channel.

Example Usage:
```
/set_btn -1001234567890 Channel | https://t.me/channel
```
4. **/rmv_cap**
This command allows you to remove the current title of a specific channel.

Example Usage:
```
/rmv_cap -1001234567890
```
5. **/rmv_btn**
This command allows you to remove the current button of a specific channel.

Example Usage:
```
/rmv_btn -1001234567890
```

## Getting Started
1. Clone the repository: `git clone https://github.com/suphiozturk8/AutoCaption.git && cd AutoCaption`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Telegram bot token in the `config.py` file.
4. Run the bot: `python main.py`

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).