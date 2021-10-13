#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from .funcn import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await e.client.send_message(e.chat_id, "👋")
    await event.reply(
        f"ℍ𝕚 `{event.sender.first_name}`, \n𝕀 𝕒𝕞 𝕂𝕒𝕚84'𝕤 𝔹𝕠𝕥 𝕎𝕙𝕚𝕔𝕙 ℂ𝕒𝕟 𝔼𝕟𝕔𝕠𝕕𝕖 𝕍𝕚𝕕𝕖𝕠𝕤 𝕌𝕤𝕚𝕟𝕘 𝔽𝔽𝕄ℙ𝔼𝔾 𝔸𝕟𝕕 𝕆𝕥𝕙𝕖𝕣𝕤.𝕀 𝕒𝕞 𝕦𝕤𝕚𝕟𝕘 𝕒𝕟 𝕠𝕗𝕗𝕚𝕔𝕚𝕒𝕝 𝕗𝕗𝕞𝕡𝕖𝕘 𝕔𝕠𝕕𝕖 𝕦𝕤𝕖𝕕 𝕓𝕪 [𝕂𝕒𝕚84](https://t.me/Kai_8_4), ℙ𝕝𝕤 𝔻𝕠𝕟'𝕥 𝕥𝕣𝕪 𝕥𝕠 𝔼𝕟𝕔𝕠𝕕𝕖 𝔸𝕟𝕪 𝔸𝕟𝕚𝕞𝕖 𝔼𝕡𝕚𝕤𝕠𝕕𝕖𝕤 𝕆𝕥𝕙𝕖𝕣𝕨𝕚𝕤𝕖 𝕀 𝕎𝕚𝕝𝕝 𝕂𝕟𝕠𝕨 𝔸𝕟𝕕 𝔹𝕒𝕟 𝕌.",
        buttons=[
            [Button.inline("ℍ𝕖𝕝𝕡", data="ihelp")],
            [
                Button.url("👥ᘜ尺ㄖㄩ卩", url="t.me/anime_hub_group"),
                Button.url("👨‍💻ᗪ乇ᐯㄥㄖ卩乇尺", url="t.me/Kai_8_4"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"ℍ𝕚 `{event.sender.first_name}`, \n𝕀 𝕒𝕞 𝕂𝕒𝕚84'𝕤 𝔹𝕠𝕥 𝕎𝕙𝕚𝕔𝕙 ℂ𝕒𝕟 𝔼𝕟𝕔𝕠𝕕𝕖 𝕍𝕚𝕕𝕖𝕠𝕤 𝕌𝕤𝕚𝕟𝕘 𝔽𝔽𝕄ℙ𝔼𝔾 𝔸𝕟𝕕 𝕆𝕥𝕙𝕖𝕣𝕤.𝕀 𝕒𝕞 𝕦𝕤𝕚𝕟𝕘 𝕒𝕟 𝕠𝕗𝕗𝕚𝕔𝕚𝕒𝕝 𝕗𝕗𝕞𝕡𝕖𝕘 𝕔𝕠𝕕𝕖 𝕦𝕤𝕖𝕕 𝕓𝕪 [𝕂𝕒𝕚84](https://t.me/Kai_8_4), ℙ𝕝𝕤 𝔻𝕠𝕟'𝕥 𝕥𝕣𝕪 𝕥𝕠 𝔼𝕟𝕔𝕠𝕕𝕖 𝔸𝕟𝕪 𝔸𝕟𝕚𝕞𝕖 𝔼𝕡𝕚𝕤𝕠𝕕𝕖𝕤 𝕆𝕥𝕙𝕖𝕣𝕨𝕚𝕤𝕖 𝕀 𝕎𝕚𝕝𝕝 𝕂𝕟𝕠𝕨 𝔸𝕟𝕕 𝔹𝕒𝕟 𝕌.",
        buttons=[
            [Button.inline("ℍ𝕖𝕝𝕡", data="ihelp")],
            [
                Button.url("👥ᘜ尺ㄖㄩ卩", url="t.me/anime_hub_group"),
                Button.url("👨‍💻ᗪ乇ᐯㄥㄖ卩乇尺", url="t.me/Kai_8_4"),
            ],
        ],
    )
