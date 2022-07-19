import sys
from datetime import datetime
from os import environ, execle, path, remove
from pyrogram import Client, filters

import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from info import Config
from plugins import listen
from plugins import run_cmd
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text
from plugins.helper_functions.logger_s import LogIt

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = Config.U_BRANCH


@Client.on_message(filters.command('update'))
async def update_it(client, message):
    msg_ = await message.reply_text("Updating Vijay please Wait")
    try:
        repo = Repo()
    except GitCommandError:
        return await msg_.edit(
            engine.get_string("Invalid git Command")
        )
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(Config.U_BRANCH, origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    if repo.active_branch.name != Config.U_BRANCH:
        return await msg_.edit(
            engine.get_sring("CUSTOM_BRANCH").format(repo.active_branch.name, Config.U_BRANCH)
        )
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(Config.U_BRANCH)
    if not Config.HEROKU_URL:
        try:
            ups_rem.pull(Config.U_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
        await msg_.edit(engine.get_string("UPDATED"))
        args = [sys.executable, "-m", "main_startup"]
        execle(sys.executable, *args, environ)
        exit()
        return
    else:
        await msg_.edit(engine.get_string("HEROKU_DETECTED"))
        ups_rem.fetch(Config.U_BRANCH)
        repo.git.reset("--hard", "FETCH_HEAD")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(Config.HEROKU_URL)
        else:
            remote = repo.create_remote("heroku", Config.HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except BaseException as error:
            await msg_.edit(f"**Updater Error** \nTraceBack : `{error}`")
            return repo.__del__()
