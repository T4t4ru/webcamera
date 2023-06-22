import os, cv2, time, telebot
bot_token = 'ВАШ_ТОКЕН_БОТА'
bot = telebot.TeleBot(bot_token)
def get_webcam_image():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Используется CAP_V4L2 для подключения веб-камеры
    if not cap.isOpened(): raise IOError("Ошибка подключения к веб-камере")
    ret, frame = cap.read()
    cap.release()
    img_name = "webcam_" + str(time.time()) + ".jpg"
    cv2.imwrite(img_name, frame)
    return img_name
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Как я могу помочь вам?")
@bot.message_handler(commands=['webcam'])
def send_webcam_image(message):
    try:
        img_name = get_webcam_image()
        photo = open(img_name, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        os.remove(img_name)
    except Exception as e:
        bot.reply_to(message, str(e))
bot.polling()
