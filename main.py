import requests
from bs4 import BeautifulSoup
import telebot
import time
import json

TOKEN = 'TELEGRAM_BOT_TOKEN'
CHAT_ID = 'TELEGRAM_GRUP/KANAL_ID' # Paylaşım yapılacak grup veya kanal username'ini @ ile yazın. (Örn: @bihaberimvar)

# Telegram botunu oluşturun
bot = telebot.TeleBot(TOKEN)

# Daha önce gönderilen mesajların takibi için kullanılacak sözlük
# Her kanal için ayrı bir liste kullanılacak
sent_messages = {}

# İçerik kopyalanacak kanal ve grupların bulunduğu json dosya yolunu yazın
json_url = 'https://siteadiniz.com/kanallar.json'

channels = {}

def update_channels():
    global channels
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            channels = response.json()
            for channel_name in channels:
                if channel_name not in sent_messages:
                    sent_messages[channel_name] = []
            print("Channels updated.")
        else:
            print(f"Failed to fetch JSON: {response.status_code}")
    except Exception as e:
        print(f"Error fetching JSON: {str(e)}")

def check_channel_and_send_messages(channel_url, channel_name):
    global sent_messages
    
    try:
        response = requests.get(channel_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        message_wraps = soup.find_all('div', class_='tgme_widget_message_wrap')

        for message_wrap in message_wraps:
            message_text_element = message_wrap.find('div', class_='tgme_widget_message_text')
            message_text = message_text_element.text.strip() if message_text_element else None

            video_link_element = message_wrap.find('a', class_='tgme_widget_message_video_player')

            if video_link_element:
                video_url = video_link_element['href']
                if video_url not in sent_messages[channel_name]:
                    bot.send_video(chat_id=CHAT_ID, video=video_url, caption=message_text)
                    sent_messages[channel_name].append(video_url)
            else:
                photo_link_element = message_wrap.find('a', class_='tgme_widget_message_photo_wrap')

                if photo_link_element:
                    photo_url = photo_link_element['href']
                    if photo_url not in sent_messages[channel_name]:
                        bot.send_photo(chat_id=CHAT_ID, photo=photo_url, caption=message_text)
                        sent_messages[channel_name].append(photo_url)
                else:
                    # Eğer Fotoğraf yada video yoksa sadece metin mesajını gönder
                    if message_text and message_text not in sent_messages[channel_name]:
                        bot.send_message(chat_id=CHAT_ID, text=message_text)
                        sent_messages[channel_name].append(message_text)

        print(f"{channel_name}: {len(sent_messages[channel_name])} messages sent.")

    except Exception as e:
        print(f"Error processing channel {channel_url}: {str(e)}")

update_channels()

start_time = time.time()
while True:
    current_time = time.time()
    
    if current_time - start_time >= 3 * 3600:
        update_channels()
        start_time = current_time
      
    for channel_name, channel_url in channels.items():
        check_channel_and_send_messages(channel_url, channel_name)
    
    time.sleep(30)  # Her 30 saniyede bir kontrol eder
