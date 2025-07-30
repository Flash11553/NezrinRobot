from telegram import Update, Message
from telegram.ext import MessageFilter
from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS

class CustomFilters:

    class _Supporters(MessageFilter):
        def filter(self, update: Update) -> bool:
            message: Message = update.effective_message
            return bool(message.from_user and message.from_user.id in DEMONS)

    support_filter = _Supporters()

    class _Sudoers(MessageFilter):
        def filter(self, update: Update) -> bool:
            message: Message = update.effective_message
            return bool(message.from_user and message.from_user.id in DRAGONS)

    sudo_filter = _Sudoers()

    class _Developers(MessageFilter):
        def filter(self, update: Update) -> bool:
            message: Message = update.effective_message
            return bool(message.from_user and message.from_user.id in DEV_USERS)

    dev_filter = _Developers()

    class _MimeType(MessageFilter):
        def __init__(self, mimetype: str):
            self.mime_type = mimetype
            self.name = f"CustomFilters.mime_type({self.mime_type})"

        def filter(self, update: Update) -> bool:
            message: Message = update.effective_message
            return bool(message.document and message.document.mime_type == self.mime_type)

    mime_type = _MimeType

    class _HasText(MessageFilter):
        def filter(self, update: Update) -> bool:
            message: Message = update.effective_message
            return bool(
                message.text or message.sticker or message.photo or
                message.document or message.video
            )

    has_text = _HasText()
