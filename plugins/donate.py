from pyrogram import Client, Filters


@Client.on_message(Filters.command(["donate"]))
async def start(client, message):
    donatetxt = f"helloarup@paytm"
    await message.reply_text(donatetxt)

    
