import inspect
import shlex
import math
import asyncio
import time
import aiofiles
import aiohttp
import wget
import os
import datetime
from json import JSONDecodeError
import requests
import ffmpeg
from info import Config, CMD_LIST
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch
import yt_dlp
from youtube_search import YoutubeSearch
import requests
from typing import Tuple
from pyrogram import filters
from pyrogram import Client
from plugins.CrazyBoss.friday import humanbytes, edit_or_reply, fetch_audio

help_message = []

async def _sudo(f, client, message):
    if not message:
        return bool(False)
    if not message.from_user:
        return bool(False)
    if not message.from_user.id:
        return bool(False)
    if message.from_user.id in sudo_list_.result():
        return bool(True)
    return bool(False)

_sudo = filters.create(func=_sudo, name="_sudo")


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

def friday_on_cmd(
    cmd: list,
    group: int = 0,
    pm_only: bool = False,
    group_only: bool = False,
    chnnl_only: bool = False,
    only_if_admin: bool = False,
    ignore_errors: bool = False,
    propagate_to_next_handler: bool = True,
    disable_sudo: bool = False,
    file_name: str = None,
    is_official: bool = True,
    cmd_help: dict = {"help": "No One One Gonna Help You", "example": "{ch}what"},
):
    """- Main Decorator To Register Commands. -"""
    if disable_sudo:
        filterm = (
        filters.me
        & filters.command(cmd, Config.COMMAND_HAND_LER)
        & ~filters.via_bot
        & ~filters.forwarded
    )
    else:
        filterm = (
            (filters.me | _sudo)
            & filters.command(cmd, Config.COMMAND_HAND_LER)
            & ~filters.via_bot
            & ~filters.forwarded)
    cmd = list(cmd)
    add_help_menu(
        cmd=cmd[0],
        stack=inspect.stack(),
        is_official=is_official,
        cmd_help=cmd_help["help"],
        example=cmd_help["example"],
    )

def add_help_menu(
    cmd,
    stack,
    is_official=True,
    cmd_help="No One Gonna Help You",
    example="{ch}what",
    file_name=None,
):
    if not file_name:
        previous_stack_frame = stack[1]
        if "xtraplugins" in previous_stack_frame.filename:
            is_official = False
        file_name = os.path.basename(previous_stack_frame.filename.replace(".py", ""))
    cmd_helpz = example.format(ch=Config.COMMAND_HAND_LER)
    cmd_helper = f"**Module Name :** `{file_name.replace('_', ' ').title()}` \n\n**Command :** `{Config.COMMAND_HAND_LER}{cmd}` \n**Help :** `{cmd_help}` \n**Example :** `{cmd_helpz}`"
    if is_official:
        if file_name not in CMD_LIST.keys():
            CMD_LIST[file_name] = cmd_helper
        else:
            CMD_LIST[
                file_name
            ] += f"\n\n**Command :** `{Config.COMMAND_HAND_LER}{cmd}` \n**Help :** `{cmd_help}` \n**Example :** `{cmd_helpz}`"
    elif file_name not in XTRA_CMD_LIST.keys():
        XTRA_CMD_LIST[file_name] = cmd_helper
    else:
        XTRA_CMD_LIST[
            file_name
        ] += f"\n\n**Command :** `{Config.COMMAND_HAND_LER}{cmd}` \n**Help :** `{cmd_help}` \n**Example :** `{cmd_helpz}`"
            

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
    except Exception:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms

n = "\n"
w = " "


bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "

mono = lambda x: f"`{x}`{n}"


def section(
    title: str,
    body: dict,
    indent: int = 2,
    underline: bool = False,
) -> str:

    text = (bold_ul(title) + n) if underline else bold(title) + n

    for key, value in body.items():
        text += (
            indent * w
            + bold(key)
            + ((value[0] + n) if isinstance(value, list) else mono(value))
        )
    return text
