from telegram import Update
from telegram.ext import MessageFilter
from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS


class SupportFilter(MessageFilter):
    def filter(self, update: Update) -> bool:
        return update.effective_user and update.effective_user.id in DEMONS

    def __call__(self, update: Update) -> bool:
        return self.filter(update)


class SudoFilter(MessageFilter):
    def filter(self, update: Update) -> bool:
        return update.effective_user and update.effective_user.id in DRAGONS

    def __call__(self, update: Update) -> bool:
        return self.filter(update)


class DevFilter(MessageFilter):
    def filter(self, update: Update) -> bool:
        return update.effective_user and update.effective_user.id in DEV_USERS

    def __call__(self, update: Update) -> bool:
        return self.filter(update)


class MimeTypeFilter(MessageFilter):
    def __init__(self, mimetype: str):
        self.mime_type = mimetype
        super().__init__()

    def filter(self, update: Update) -> bool:
        msg = update.effective_message
        return (
            msg and msg.document and msg.document.mime_type == self.mime_type
        )

    def __call__(self, update: Update) -> bool:
        return self.filter(update)


class HasTextFilter(MessageFilter):
    def filter(self, update: Update) -> bool:
        msg = update.effective_message
        return bool(
            msg and (
                msg.text or msg.sticker or msg.photo or msg.document or msg.video
            )
        )

    def __call__(self, update: Update) -> bool:
        return self.filter(update)


# Tək yerdən istifadə etmək üçün:
support_filter = SupportFilter()
sudo_filter = SudoFilter()
dev_filter = DevFilter()
mime_type = MimeTypeFilter  # instansiatə ehtiyac olanda istifadə et
has_text = HasTextFilter()
