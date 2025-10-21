import discord
import random
from gen_pass import gen_pass

# Botun ayrıcalıkları (intents) tanımlanıyor
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturuluyor
client = discord.Client(intents=intents)

# Emoji oluşturucu fonksiyonu
def emoji_olusturucu():
    return random.choice(["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"])

# Yazı tura fonksiyonu
def yazi_tura():
    para = random.randint(1, 2)
    if para == 1:
        return "$Yazı"
    else:
        return "$Tura"

# Yardım fonksiyonu
def yardim():
    return "$yazı_tura, $merhaba, $bye, $password, $emoji, $yardım"

# Bot hazır olduğunda çalışan olay
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

# Mesaj alındığında çalışan olay
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$yazı_tura'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$yardım'):
        await message.channel.send(yardim())
    else:
        await message.channel.send(message.content)

# BURADA TOKEN'İ GÜNCELLE!
client.run("TOKENİNİ_BURAYA_YENİDEN_KOY")
