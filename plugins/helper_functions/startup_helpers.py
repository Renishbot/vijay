import asyncio
import glob
import importlib
import logging
from info import Config
import ntpath
import shlex
from typing import Tuple
import sys
from datetime import datetime
from os import environ, execle, path, remove
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError


def load_plugin(plugin_name, assistant=False):
    """Load PLugins - Assitant & User Using ImportLib"""
    if (
        not plugin_name.endswith("__")
        and plugin_name not in Config.MAIN_NO_LOAD
    ):
        if assistant:
            plugin_path = "assistant." + plugin_name
        else:
            plugin_path = "plugins." + plugin_name
        loader_type = "[Assistant]" if assistant else "[User]"
        importlib.import_module(plugin_path)
        logging.info(f"{loader_type} - Loaded : " + str(plugin_name))
