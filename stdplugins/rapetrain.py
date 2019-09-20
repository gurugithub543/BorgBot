"""Emoji

Available Commands:

.repe

build by legend @r4v4n4 , if u edit it then u r gay..."""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "repe":

        await event.edit(input_str)

        animation_chars = [
        
            "**R**",
            "**RA**",
            "**RAP**",
            "**RAPE**",
            "**RAPE_**",    
            "**RAPE_T**",
            "**RAPE_TR**",
            "**RAPE_TRA**",
            "**RAPE_TRAI**",
            "**RAPE_TRAIN**",
            "**APE_TRAIN🚅**",
            "**PE_TRAIN🚅🚃🚃**",
            "**E_TRAIN🚅🚃🚃🚃**",
            "**_TRAIN🚅🚃🚃🚃🚃**",
            "**TRAIN🚅🚃🚃🚃🚃🚃**",
            "**RAIN🚅🚃🚃🚃🚃🚃🚃**",
            "**AIN🚅🚃🚃🚃🚃🚃🚃🚃**",
            "**IN🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
            "**N🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
            "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃",
            "🚃🚃🚃",
            "🚃🚃",
            "🚃",
            "**RAPED**"
 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
