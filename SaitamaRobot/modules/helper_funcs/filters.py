from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS
from telegram import Message
from telegram.ext import BaseFilter


class CustomFilters(object):

    class _Supporters(BaseFilter):
        def __call__(self, message: Message) -> bool:
            return bool(message.from_user and message.from_user.id in DEMONS)

    support_filter = _Supporters()

    class _Sudoers(BaseFilter):
        def __call__(self, message: Message) -> bool:
            return bool(message.from_user and message.from_user.id in DRAGONS)

    sudo_filter = _Sudoers()

    class _Developers(BaseFilter):
        def __call__(self, message: Message) -> bool:
            return bool(message.from_user and message.from_user.id in DEV_USERS)

    dev_filter = _Developers()

    class _MimeType(BaseFilter):
        def __init__(self, mimetype: str):
            self.mime_type = mimetype
            self.name = f"CustomFilters.mime_type({self.mime_type})"

        def __call__(self, message: Message) -> bool:
            return bool(message.document and
                        message.document.mime_type == self.mime_type)

    mime_type = _MimeType

    class _HasText(BaseFilter):
        def __call__(self, message: Message) -> bool:
            return bool(
                message.text or message.sticker or message.photo or
                message.document or message.video
            )

    has_text = _HasText()
