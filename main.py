import os
import telebot


bot = telebot.TeleBot("1986932872:AAGgsXeeiLmP4hVeUJzuOe854591B542wBk")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I Am User Id Bot.. Send Me Any /id commands In See A Your Info...👍")


@bot.message_handler(commands=["id"])
def send_message(message):
  bot.send_message(message.chat.id, "Your Name Is<firstname></firstname>")



bot.polling()
