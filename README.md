# Safe Keyboard Logger

This is a demo project that safely logs keyboard events using Python for personal use or automation testing. Press `ESC` to exit.

We’ll use the pynput library to detect specific key events and write them to a file only when explicitly intended, like pressing a hotkey or for personal logging on your own system:

## Setup

```bash
pip install -r requirements.txt
python logger.py
```


## What this does:

Logs each key you press (when running this script with your knowledge).

Exits safely when you press ESC.

Stores output in key_log.txt in the same folder.

## ⚠️ Notes:

Only use this on your own machine for learning or automation.

Never deploy scripts like this on someone else's computer or network.

Inform users clearly if you are capturing any input — transparency is key.
