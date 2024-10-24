import aiogram
from src.database.models import *
from src.tools.settings_manager import SettingsManager
from os import makedirs

router: aiogram.Router = aiogram.Router()

async def save_media(media: aiogram.types.Message) -> None:
    media_dir: str = SettingsManager().get_settings_for_field('media_dir')
    makedirs(f'{media_dir}/{media.chat.id}/photo', exist_ok=True)
    makedirs(f'{media_dir}/{media.chat.id}/voicemessages', exist_ok=True)
    makedirs(f'{media_dir}/{media.chat.id}/videomessages', exist_ok=True)

    if media.photo:
        photo: aiogram.types.PhotoSize = media.photo[-1]
        await media.bot.download(photo.file_id, f'{media_dir}/{media.chat.id}/photo/{photo.file_id}.png')
    if media.voice:
        await media.bot.download(media.voice.file_id, f'{media_dir}/{media.chat.id}/voicemessages/{media.voice.file_id}.ogg')
    if media.video_note:
        await media.bot.download(media.video_note.file_id,f'{media_dir}/{media.chat.id}/videomessages/{media.video_note.file_id}.mp4')


@router.message()
async def on_message(message: aiogram.types.Message):
    Message().dump_message(message)
    await save_media(message)

@router.edited_message()
async def on_edited_message(message: aiogram.types.Message):
    await message.reply(str(message))