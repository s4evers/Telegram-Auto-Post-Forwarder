from telethon import TelegramClient, events

# Ваши данные для авторизации в Telegram API
api_id = 'ВАШ_API_ID'
api_hash = 'ВАШ_API_HASH'
phone = 'ВАШ_НОМЕР_ТЕЛЕФОНА'

# ID или ссылка на исходный и целевой каналы
source_channel = 'ID_ИЛИ_ССЫЛКА_ИСТОЧНИКА'
target_channel = 'ID_ИЛИ_ССЫЛКА_ЦЕЛЕВОГО'

# Настройка клиента Telethon
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Вход в аккаунт Telegram
    await client.start(phone)

    # Получаем объекты каналов
    source = await client.get_entity(source_channel)
    target = await client.get_entity(target_channel)

    # Подписка на новые сообщения в исходном канале
    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        # Пересылаем сообщение в целевой канал
        await client.forward_messages(target, event.message)
        print(f"Сообщение переслано из {source_channel} в {target_channel}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
