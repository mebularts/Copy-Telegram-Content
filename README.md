# Telegram Kanal/Grup İçerik Kopyalama Botu

[![Boyut](https://img.shields.io/github/repo-size/mebularts/Copy-Telegram-Content?logo=git&logoColor=white&label=Boyut)](#)
[![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/mebularts/Copy-Telegram-Content&title=Görüntülenme)](#)
<a href="https://t.me/mebularts" target="_blank"><img src="https://img.shields.io/badge/☕️-İletişime Geç-ffdd00" title="İletişime Geç" style="padding-left:5px;"></a>

[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://t.me/mebularts/)

Bu Python scripti, belirli Telegram kanallarından içerik kopyalayıp otomatik olarak başka bir Telegram grubuna veya kanalına göndermek için tasarlanmıştır. Bot, metin mesajları, fotoğraflar ve videolar gibi çeşitli medya türlerini işleyebilir. Belirtilen kanalları periyodik olarak kontrol eder ve daha önce gönderilmemiş yeni içerikleri hedef gruba veya kanala iletir.

[@mebularts](https://t.me/mebularts) tarafından <img href="https://t.me/mebularts" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/17fa94fb-0ae5-45a2-8313-2d3eedaf69db/d8fohut-eb4f893c-d1ad-4111-8e05-29993454b082.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE3ZmE5NGZiLTBhZTUtNDVhMi04MzEzLTJkM2VlZGFmNjlkYlwvZDhmb2h1dC1lYjRmODkzYy1kMWFkLTQxMTEtOGUwNS0yOTk5MzQ1NGIwODIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.J7M952F5dOS4-H45vJfTWA1yYE0ePYbTwamSfZHEQPY" width="30" height="30" /> ile yazılmıştır.


## Özellikler

- Belirtilen Telegram kanallarından mesajları, fotoğrafları ve videoları otomatik olarak alır ve iletir.
- Daha önce gönderilen içerikleri takip ederek yinelenmeleri önler.
- Uzaktaki bir JSON dosyasından kanal listesini periyodik olarak günceller.
- Basit bir JSON yapılandırmasıyla özelleştirilebilir.

## Gereksinimler

- Python 3.x
- Gerekli Python paketleri: `requests`, `beautifulsoup4`, `pyTelegramBotAPI`

## Kurulum

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/mebularts/Copy-Telegram-Content.git
   cd Copy-Telegram-Content
   ```

2. **Gerekli Python paketlerini yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ortamınızı yapılandırın:**

   - `TELEGRAM_BOT_TOKEN` ile kendi Telegram botunuzun token'ını değiştirin.
   - `TELEGRAM_GRUP/KANAL_ID` ile mesajların gönderileceği hedef grup veya kanalın kullanıcı adını değiştirin (örn. `@bihaberimvar`).

4. **JSON yapılandırmanızı hazırlayın:**
   - İçeriğin kopyalanacağı kanalları içeren bir JSON dosyası (`kanallar.json`) oluşturun. Dosya bir URL'de barındırılmalı (veya yerel bir dosya yolu kullanabilirsiniz). İşte bir örnek:
   
     ```json
     {
         "HaberKanali": "https://t.me/s/HaberKanaliUsername",
         "Guncellemeler": "https://t.me/s/GuncellemelerUsername",
         "MedyaKanali": "https://t.me/s/MedyaKanaliUsername"
     }
     ```
   - Scriptteki `json_url` değişkenini, JSON dosyanızın konumunu gösterecek şekilde ayarlayın.

## Kullanım

1. **Botu çalıştırın:**
   ```bash
   python main.py
   ```

   Bot çalışmaya başlayacak ve JSON yapılandırmasında belirtilen kanalları yeni içerik için periyodik olarak kontrol edecektir. Yeni içerik bulunduğunda, belirtilen grup veya kanala iletecektir.

2. **Yapılandırma detayları:**

   - Bot, her 30 saniyede bir yeni içerik için kontrol yapar.
   - Kanal listesi içeren JSON dosyası, her 3 saatte bir güncellenir.

3. **Günlükler:**
   - Script, iletimlerin başarılı olup olmadığını ve karşılaşılan hataları içeren güncellemeleri konsola yazdırır.

## Örnek

Diyelim ki `kanallar.json` dosyanız şöyle görünüyor:

```json
{
    "TeknolojiHaberleri": "https://t.me/s/TeknolojiHaberleri",
    "GünlükGüncellemeler": "https://t.me/s/GunlukGuncellemeler"
}
```

Bot, `TeknolojiHaberleri` ve `GünlükGüncellemeler` kanallarını izleyerek, bulduğu yeni mesajları, fotoğrafları veya videoları hedef grup veya kanala iletecektir.

## Sorun Giderme

- **JSON dosyası alınamadı hatası:** JSON dosyanızın URL'sinin doğru olduğundan ve erişilebilir olduğundan emin olun.
- **JSON alınamadı:** İnternet bağlantınızı kontrol edin veya JSON dosyanızı barındıran sunucunun çevrimiçi olduğundan emin olun.
- **Mesajlar gönderilmedi:** Kanalların herkese açık olduğundan ve botunuzun bu kanalları görebileceğinden emin olun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
