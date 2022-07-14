import asyncio
import re

from time import time
from pyrogram import Client as app
from pyrogram.errors import FloodWait
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    ChatPermissions,
    Message,
)

from info import BOT_ID, SUDO_USERS
from wbb.core.decorators.errors import capture_err
from wbb.core.keyboard import ikb
