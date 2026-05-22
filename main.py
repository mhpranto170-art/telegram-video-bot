
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8789213846:AAF4sq5z8Dbj33C1L1DxuC-nfitZYxRSfao"

VIDEO_LINK = "https://t.me/yourchannel/1"

SHORTLINK = "https://loot-link.com/s?example"

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔓 Unlock Video", callback_data="unlock")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 Premium Video Locked!\n\nClick below to unlock.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "unlock":
        users[user_id] = True

        keyboard = [
            [InlineKeyboardButton("📢 Watch Ads & Unlock", url=SHORTLINK)],
            [InlineKeyboardButton("✅ I Completed", callback_data="done")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "Watch ads then click completed.",
            reply_markup=reply_markup
        )

    elif query.data == "done":
        if user_id in users:
            await query.message.reply_text(
                f"🎉 Video Unlocked!\n\n{VIDEO_LINK}"
            )
        else:
            await query.message.reply_text("❌ Complete ads first.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
