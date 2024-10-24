import logging

from peewee import *
from src.tools.settings_manager import SettingsManager
from typing import Any

database_settings: dict[str, Any] = SettingsManager().get_settings_for_field("database")

db = MySQLDatabase(
    database=database_settings["name"],
    user=database_settings["user"],
    password=database_settings["password"],
    host=database_settings["host"],
    port=database_settings["port"],
)


class BaseModel(Model):
    class Meta:
        database = db


class Message(BaseModel):
    message_id = IntegerField(primary_key=True)
    date = DateTimeField()

    # Поля из Chat
    chat_id = BigIntegerField()
    chat_type = CharField()
    chat_title = CharField(null=True)
    chat_username = CharField(null=True)
    chat_first_name = CharField(null=True)
    chat_last_name = CharField(null=True)
    chat_is_forum = BooleanField(null=True)
    chat_accent_color_id = IntegerField(null=True)
    chat_active_usernames = TextField(null=True)  # Преобразуем список в строку
    chat_available_reactions = TextField(null=True)  # Преобразуем список в строку
    chat_background_custom_emoji_id = CharField(null=True)
    chat_bio = TextField(null=True)
    chat_birthdate = DateTimeField(null=True)
    chat_business_intro = TextField(null=True)
    chat_business_location = TextField(null=True)  # Преобразуем структуру в строку
    chat_business_opening_hours = TextField(null=True)  # Преобразуем структуру в строку
    chat_can_set_sticker_set = BooleanField(null=True)
    chat_custom_emoji_sticker_set_name = CharField(null=True)
    chat_description = TextField(null=True)
    chat_emoji_status_custom_emoji_id = CharField(null=True)
    chat_emoji_status_expiration_date = DateTimeField(null=True)
    chat_has_aggressive_anti_spam_enabled = BooleanField(null=True)
    chat_has_hidden_members = BooleanField(null=True)
    chat_has_private_forwards = BooleanField(null=True)
    chat_has_protected_content = BooleanField(null=True)
    chat_has_restricted_voice_and_video_messages = BooleanField(null=True)
    chat_has_visible_history = BooleanField(null=True)
    chat_invite_link = CharField(null=True)
    chat_join_by_request = BooleanField(null=True)
    chat_join_to_send_messages = BooleanField(null=True)
    chat_linked_chat_id = BigIntegerField(null=True)
    chat_location = TextField(null=True)  # Преобразуем структуру в строку
    chat_message_auto_delete_time = IntegerField(null=True)
    chat_permissions = TextField(null=True)  # Преобразуем структуру в строку
    chat_personal_chat = BooleanField(null=True)
    chat_photo = TextField(null=True)  # Преобразуем структуру в строку
    chat_pinned_message = IntegerField(null=True)
    chat_profile_accent_color_id = IntegerField(null=True)
    chat_profile_background_custom_emoji_id = CharField(null=True)
    chat_slow_mode_delay = IntegerField(null=True)
    chat_sticker_set_name = CharField(null=True)
    chat_unrestrict_boost_count = IntegerField(null=True)

    # Поля из FromUser
    from_user_id = BigIntegerField()
    from_user_is_bot = BooleanField(default=False)
    from_user_first_name = CharField(null=True)
    from_user_last_name = CharField(null=True)
    from_user_username = CharField(null=True)
    from_user_language_code = CharField(null=True)
    from_user_is_premium = BooleanField(null=True)
    from_user_added_to_attachment_menu = BooleanField(null=True)
    from_user_can_join_groups = BooleanField(null=True)
    from_user_can_read_all_group_messages = BooleanField(null=True)
    from_user_supports_inline_queries = BooleanField(null=True)
    from_user_can_connect_to_business = BooleanField(null=True)
    from_user_has_main_web_app = BooleanField(null=True)

    # Поля из сообщения
    text = TextField(null=True)
    entities = TextField(null=True)  # Преобразуем структуру в строку
    is_topic_message = BooleanField(null=True)
    message_thread_id = IntegerField(null=True)
    via_bot_id = IntegerField(null=True)
    edit_date = DateTimeField(null=True)
    has_protected_content = BooleanField(null=True)
    media_group_id = CharField(null=True)

    # Поля пересылки (forward)
    forward_date = DateTimeField(null=True)
    forward_from_user_id = BigIntegerField(null=True)
    forward_from_chat_id = BigIntegerField(null=True)
    forward_from_message_id = IntegerField(null=True)
    forward_sender_name = CharField(null=True)
    forward_signature = CharField(null=True)

    # Поля reply (ответ)
    reply_to_message_id = IntegerField(null=True)

    # Прочие медиа поля
    animation = TextField(null=True)  # Преобразуем структуру в строку
    audio = TextField(null=True)  # Преобразуем структуру в строку
    document = TextField(null=True)  # Преобразуем структуру в строку
    photo = TextField(null=True)  # Преобразуем структуру в строку
    sticker = TextField(null=True)  # Преобразуем структуру в строку
    video = TextField(null=True)  # Преобразуем структуру в строку
    voice = TextField(null=True)  # Преобразуем структуру в строку
    video_note = TextField(null=True)  # Преобразуем структуру в строку

    # Прочие поля
    contact = TextField(null=True)  # Преобразуем структуру в строку
    dice = TextField(null=True)  # Преобразуем структуру в строку
    game = TextField(null=True)  # Преобразуем структуру в строку
    poll = TextField(null=True)  # Преобразуем структуру в строку
    venue = TextField(null=True)  # Преобразуем структуру в строку
    location = TextField(null=True)  # Преобразуем структуру в строку

    # Поля изменений в чате
    new_chat_members = TextField(null=True)  # Преобразуем список в строку
    left_chat_member = TextField(null=True)  # Преобразуем структуру в строку
    new_chat_title = CharField(null=True)
    new_chat_photo = TextField(null=True)  # Преобразуем структуру в строку
    delete_chat_photo = BooleanField(null=True)
    group_chat_created = BooleanField(null=True)
    supergroup_chat_created = BooleanField(null=True)
    channel_chat_created = BooleanField(null=True)

    # Прочие события
    migrate_to_chat_id = BigIntegerField(null=True)
    migrate_from_chat_id = BigIntegerField(null=True)
    pinned_message_id = IntegerField(null=True)

    # Специфичные поля
    business_connection_id = IntegerField(null=True)
    sender_boost_count = IntegerField(null=True)
    sender_business_bot = IntegerField(null=True)
    giveaway_created = BooleanField(null=True)
    giveaway_winners = TextField(null=True)  # Преобразуем список в строку
    giveaway_completed = BooleanField(null=True)
    video_chat_scheduled = BooleanField(null=True)
    video_chat_started = BooleanField(null=True)
    video_chat_ended = BooleanField(null=True)
    video_chat_participants_invited = TextField(null=True)

    def dump_message(self, message: dict | Any):
        if not isinstance(message, dict):
            message = dict(message)

        message['chat'] = dict(message['chat'])
        message['from_user'] = dict(message['from_user'])
        message['forward_from'] = dict(message['forward_from']) if message['forward_from'] else message['forward_from']

        def stringify(value):
            return str(value) if isinstance(value, (list, dict)) else value

        self.create(
            message_id=message['message_id'],
            date=message['date'],

            # Поля Chat
            chat_id=message['chat']['id'],
            chat_type=message['chat']['type'],
            chat_title=message['chat']['title'],
            chat_username=message['chat']['username'],
            chat_first_name=message['chat']['first_name'],
            chat_last_name=message['chat']['last_name'],
            chat_is_forum=message['chat']['is_forum'],
            chat_accent_color_id=message['chat']['accent_color_id'],
            chat_active_usernames=stringify(message['chat']['active_usernames']),
            chat_available_reactions=stringify(message['chat']['available_reactions']),
            chat_background_custom_emoji_id=message['chat']['background_custom_emoji_id'],
            chat_bio=message['chat']['bio'],
            chat_birthdate=message['chat']['birthdate'],
            chat_business_intro=message['chat']['business_intro'],
            chat_business_location=stringify(message['chat']['business_location']),
            chat_business_opening_hours=stringify(message['chat']['business_opening_hours']),
            chat_can_set_sticker_set=message['chat']['can_set_sticker_set'],
            chat_custom_emoji_sticker_set_name=message['chat']['custom_emoji_sticker_set_name'],
            chat_description=message['chat']['description'],
            chat_emoji_status_custom_emoji_id=message['chat']['emoji_status_custom_emoji_id'],
            chat_emoji_status_expiration_date=message['chat']['emoji_status_expiration_date'],
            chat_has_aggressive_anti_spam_enabled=message['chat']['has_aggressive_anti_spam_enabled'],
            chat_has_hidden_members=message['chat']['has_hidden_members'],
            chat_has_private_forwards=message['chat']['has_private_forwards'],
            chat_has_protected_content=message['chat']['has_protected_content'],
            chat_has_restricted_voice_and_video_messages=message['chat']['has_restricted_voice_and_video_messages'],
            chat_has_visible_history=message['chat']['has_visible_history'],
            chat_invite_link=message['chat']['invite_link'],
            chat_join_by_request=message['chat']['join_by_request'],
            chat_join_to_send_messages=message['chat']['join_to_send_messages'],
            chat_linked_chat_id=message['chat']['linked_chat_id'],
            chat_location=stringify(message['chat']['location']),
            chat_message_auto_delete_time=message['chat']['message_auto_delete_time'],
            chat_permissions=stringify(message['chat']['permissions']),
            chat_personal_chat=message['chat']['personal_chat'],
            chat_photo=stringify(message['chat']['photo']),
            chat_pinned_message=message['chat']['pinned_message'],
            chat_profile_accent_color_id=message['chat']['profile_accent_color_id'],
            chat_profile_background_custom_emoji_id=message['chat']['profile_background_custom_emoji_id'],
            chat_slow_mode_delay=message['chat']['slow_mode_delay'],
            chat_sticker_set_name=message['chat']['sticker_set_name'],
            chat_unrestrict_boost_count=message['chat']['unrestrict_boost_count'],

            # Поля FromUser
            from_user_id=message['from_user']['id'],
            from_user_is_bot=message['from_user']['is_bot'],
            from_user_first_name=message['from_user']['first_name'],
            from_user_last_name=message['from_user']['last_name'],
            from_user_username=message['from_user']['username'],
            from_user_language_code=message['from_user']['language_code'],
            from_user_is_premium=message['from_user']['is_premium'],
            from_user_added_to_attachment_menu=message['from_user']['added_to_attachment_menu'],
            from_user_can_join_groups=message['from_user']['can_join_groups'],
            from_user_can_read_all_group_messages=message['from_user']['can_read_all_group_messages'],
            from_user_supports_inline_queries=message['from_user']['supports_inline_queries'],
            from_user_can_connect_to_business=message['from_user']['can_connect_to_business'],
            from_user_has_main_web_app=message['from_user']['has_main_web_app'],

            # Поля сообщения
            text=message['text'],
            entities=stringify(message['entities']),
            is_topic_message=message['is_topic_message'],
            message_thread_id=message['message_thread_id'],
            via_bot_id=message['via_bot'],
            edit_date=message['edit_date'],
            has_protected_content=message['has_protected_content'],
            media_group_id=message['media_group_id'],

            # Поля пересылки (forward)
            forward_date=message['forward_date'],
            forward_from_user_id=message['forward_from']['id'] if message.get('forward_from') is not None else None,
            forward_from_chat_id=message['forward_from_chat']['id'] if message.get(
                'forward_from_chat') is not None else None,
            forward_from_message_id=message['forward_from_message_id'],
            forward_sender_name=message['forward_sender_name'],
            forward_signature=message['forward_signature'],

            # Поля ответа
            reply_to_message_id=message['reply_to_message']['message_id'] if message.get(
                'reply_to_message') is not None else None,

            # Прочие поля
            animation=stringify(message['animation']),
            audio=stringify(message['audio']),
            document=stringify(message['document']),
            photo=stringify(message['photo']),
            sticker=stringify(message['sticker']),
            video=stringify(message['video']),
            voice=stringify(message['voice']),
            video_note=stringify(message['video_note']),
            contact=stringify(message['contact']),
            dice=stringify(message['dice']),
            game=stringify(message['game']),
            poll=stringify(message['poll']),
            venue=stringify(message['venue']),
            location=stringify(message['location']),

            # Изменения чата
            new_chat_members=stringify(message['new_chat_members']),
            left_chat_member=stringify(message['left_chat_member']),
            new_chat_title=message['new_chat_title'],
            new_chat_photo=stringify(message['new_chat_photo']),
            delete_chat_photo=message['delete_chat_photo'],
            group_chat_created=message['group_chat_created'],
            supergroup_chat_created=message['supergroup_chat_created'],
            channel_chat_created=message['channel_chat_created'],

            # Прочие события
            migrate_to_chat_id=message['migrate_to_chat_id'],
            migrate_from_chat_id=message['migrate_from_chat_id'],
            pinned_message_id=message['pinned_message'],

            # Специфичные поля
            business_connection_id=message['business_connection_id'],
            sender_boost_count=message['sender_boost_count'],
            sender_business_bot=message['sender_business_bot'],
            giveaway_created=message['giveaway_created'],
            giveaway_winners=stringify(message['giveaway_winners']),
            giveaway_completed=message['giveaway_completed'],
            video_chat_scheduled=message['video_chat_scheduled'],
            video_chat_started=message['video_chat_started'],
            video_chat_ended=message['video_chat_ended'],
            video_chat_participants_invited=stringify(message['video_chat_participants_invited'])
        )

    class Meta:
        database = db
        table_name = 'messages'

try:
    logging.info('Попытка подключения к базе данных')
    db.connect()
    logging.info('Соединение установлено')
except OperationalError:
    logging.error('Подключение к базе данных не удалось установить')
    exit()

db.create_tables([Message])
