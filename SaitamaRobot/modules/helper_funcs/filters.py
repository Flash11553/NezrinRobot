from telegram import Update
from telegram.ext import BaseFilter  # Dəyişiklik budur

from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS

class CustomFilters:

    class _Supporters(BaseFilter):
        def filter(self, update: Update) -> bool:
            msg = getattr(update, "effective_message", None)
            return bool(msg and msg.from_user and msg.from_user.id in DEMONS)

    support_filter = _Supporters()

    class _Sudoers(BaseFilter):
        def filter(self, update: Update) -> bool:
            msg = getattr(update, "effective_message", None)
            return bool(msg and msg.from_user and msg.from_user.id in DRAGONS)

    sudo_filter = _Sudoers()

    class _Developers(BaseFilter):
        def filter(self, update: Update) -> bool:
            msg = getattr(update, "effective_message", None)
            return bool(msg and msg.from_user and msg.from_user.id in DEV_USERS)

    dev_filter = _Developers()

    class _MimeType(BaseFilter):
        def __init__(self, mimetype: str):
            self.mime_type = mimetype
            self.name = f"CustomFilters.mime_type({self.mime_type})"

        def filter(self, update: Update) -> bool:
            msg = getattr(update, "effective_message", None)
            return bool(msg and msg.document and msg.document.mime_type == self.mime_type)

    mime_type = _MimeType

    class _HasText(BaseFilter):
        def filter(self, update: Update) -> bool:
            msg = getattr(update, "effective_message", None)
            return bool(
                msg and (
                    getattr(msg, "text", None) or
                    getattr(msg, "sticker", None) or
                    getattr(msg, "photo", None) or
                    getattr(msg, "document", None) or
                    getattr(msg, "video", None)
                )
            )

    has_text = _HasText()
