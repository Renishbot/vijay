# codes added by @lallu_tg
# use with  proper credits

"""Get info about the replied user
Syntax: .whois"""

import os
import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from info import COMMAND_HAND_LER
from plugins.helper_functions.extract_user import extract_user
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from plugins.helper_functions.last_online_hlpr import last_online


