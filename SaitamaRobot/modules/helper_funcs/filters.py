from telegram import Update
from telegram.ext import MessageFilter

from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS


class CustomFilters:

    class _Supporters(MessageFilter):
        def __init__(self):
            super().__init__()

        def filter(self, update: Update) -> bool:
            msg = update.effective_message
            return bool(msg and msg.from_user and msg.from_user.id in DEMONS)

    support_filter = _Supporters()

    class _Sudoers(MessageFilter):
        def __init__(self):
            super().__init__()

        def filter(self, update: Update) -> bool:
            msg = update.effective_message
            return bool(msg and msg.from_user and msg.from_user.id in DRAGONS)

    sudo_filter = _Sudoers()

    class _Developers(MessageFilter):
        def __init__(self):
            super().__init__()

        def filter(self, update: Update) -> bool:
            msg = update.effective_message
            return bool(msg and msg.from_user and msg.from_user.id in DEV_USERS)

    dev_filter = _Developers()

    class _MimeType(MessageFilter):
        def __init__(self, mimetype: str):
            super().__init__()
            self.mime_type = mimetype
            self.name = f"CustomFilters.mime_type({self.mime_type})"

        def filter(self, update: Update) -> bool:
            msg = update.effective_message
            return bool(msg and msg.document and msg.document.mime_type == self.mime_type)

    mime_type = _MimeType

    class _HasText(MessageFilter):
        def __init__(self):
            super().__init__()

        def filter(self, update: Update) -> bool:
            msg = update.effective_message
            return bool(
                msg and (
                    msg.text or
                    msg.sticker or
                    msg.photo or
                    msg.document or
                    msg.video
                )
            )

    has_text = _HasText()
