import asyncio
from googletrans import Translator


@Hikka.on_message(hikka.on_cmd_prefix('trn'))
async def translate_message(event):
    text_to_translate = event.text.split()

    if len(text_to_translate) < 3:
        await event.reply("Неправильный формат команды. Используйте .trn Текст Язык, например: .trn Hello English")
        return

    text = ' '.join(text_to_translate[1:-1])
    target_lang = text_to_translate[-1]

    translator = Translator()
    translated_text = await hikka.run_blocking(translator.translate, text, dest=target_lang)

    await event.reply(f'Перевод на язык {target_lang}: {translated_text.text}')
