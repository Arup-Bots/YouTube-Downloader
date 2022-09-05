from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/arupbots")],
        [InlineKeyboardButton("Arup Bots", url="https://t.me/arupbots/")]


    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b> Welcome To Youtube Downloader </b> This Bot Created By @tech_arup </b> \n help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
    
    
