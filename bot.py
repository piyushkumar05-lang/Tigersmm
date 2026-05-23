# ================== CLEAN (IMPROVED UI) ==================

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "8897480826:AAGOV84ofjBfsyaCu5Q0ybhRKA88lnNsNH0"
ADMIN_ID = 6719411631

user_state = {}
VIP_USERS = [123456789]

# ================== MENUS ==================

def main_menu():
    keyboard = [
        ["👥 『𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦』", "❤️ 『𝗟𝗜𝗞𝗘𝗦』"],
        ["💬 『𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦』", "🎬 『𝗩𝗜𝗘𝗪𝗦』"],
        ["📞 『𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥』"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def package_menu(service):
    menus = {
        "👥 『𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦』": [
            ["🔥 𝟭𝟬𝟬 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 — ₹6 💸", "⚡ 𝟯𝟬𝟬 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 — ₹17 💸"],
            ["🚀 𝟱𝟬𝟬 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 — ₹29 💸"]
        ],
        "❤️ 『𝗟𝗜𝗞𝗘𝗦』": [
            ["🔥 𝟱𝟬 𝗟𝗜𝗞𝗘𝗦 — ₹4 💸", "⚡ 𝟭𝟬𝟬 𝗟𝗜𝗞𝗘𝗦 — ₹7 💸"],
            ["💎 𝟮𝟬𝟬 𝗟𝗜𝗞𝗘𝗦 — ₹14 💸", "🚀 𝟱𝟬𝟬 𝗟𝗜𝗞𝗘𝗦 — ₹32 💸"]
        ],
        "💬 『𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦』": [
            ["🔥 𝟱𝟬 𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 — ₹7 💸", "⚡ 𝟭𝟬𝟬 𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 — ₹13 💸"],
            ["💎 𝟮𝟬𝟬 𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 — ₹25 💸", "🚀 𝟱𝟬 𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 — ₹40 💸"]
        ],
        "🎬 『𝗩𝗜𝗘𝗪𝗦』": [
            ["🔥 20𝟬𝟬 𝗩𝗜𝗘𝗪𝗦 — ₹4 💸", "⚡ 5𝟬𝟬𝟬 𝗩𝗜𝗘𝗪𝗦 — ₹10 💸"],
            ["💎 10𝟬𝟬𝟬 𝗩𝗜𝗘𝗪𝗦 — ₹15 💸", "🚀 15𝟬𝟬𝟬 𝗩𝗜𝗘𝗪𝗦 — ₹20 💸"]
        ],
    }

    keyboard = menus.get(service, [])
    keyboard.append(["🔙 𝗕𝗔𝗖𝗞"])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def is_vip(user_id):
    return user_id in VIP_USERS

# ================== START ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_state[user_id] = {}

    vip_text = "👑 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥 👑\n\n" if is_vip(user_id) else ""

    await update.message.reply_text(
        vip_text +
        "💀 𝗗𝗔𝗥𝗞 𝗣𝗔𝗡𝗘𝗟 𝗔𝗖𝗧𝗜𝗩𝗘 💀\n\n"
        "⚡ INSTANT DELIVERY\n"
        "🔥 REAL RESULTS\n"
        "🚀 ULTRA FAST\n\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "💎 SELECT YOUR POWER 💎",
        reply_markup=main_menu()
    )

# ================== HANDLE ==================

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_state:
        user_state[user_id] = {}

    state = user_state[user_id]

    if text == "🔙 𝗕𝗔𝗖𝗞":
        user_state[user_id] = {}
        await update.message.reply_text("🏠 MAIN MENU", reply_markup=main_menu())
        return

    if text in ["👥 『𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦』", "❤️ 『𝗟𝗜𝗞𝗘𝗦』", "💬 『𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦』", "👀 『𝗩𝗜𝗘𝗪𝗦』"]:
        state["service"] = text

        await update.message.reply_text(
            f"⚡ {text} SELECTED\n\n💰 CHOOSE PACKAGE:",
            reply_markup=package_menu(text)
        )
        return

    if "₹" in text:
        try:
            price = int(text.split("₹")[1].split()[0])
        except:
            await update.message.reply_text("❌ INVALID PACKAGE")
            return

        state["package"] = text
        state["price"] = price

        stock = random.randint(3, 15)

        await update.message.reply_text(
            f"🚨 LIMITED STOCK 🚨\n"
            f"⚠️ ONLY {stock} SLOTS LEFT ⚠️\n\n"
            f"📦 {text}\n"
            f"💰 ₹{price}\n\n"
            f"💳 UPI:\n`tigerkumar@fam`\n\n"
            "━━━━━━━━━━━━━━━\n"
            "➊ Payment karo\n"
            "➋ UID bhejo\n"
            "➌ Screenshot bhejo 🚀"
        )
        return

    if "package" in state and "uid" not in state:
        state["uid"] = text
        await update.message.reply_text("📸 SCREENSHOT BHEJO")
        return

    if text == "📞 『𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥』":
        await update.message.reply_text("📞 OWNER: @YOUR_USERNAME")
        return

    await update.message.reply_text("❌ INVALID OPTION", reply_markup=main_menu())

# ================== PAYMENT ==================

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if user_id not in user_state:
        return

    state = user_state[user_id]

    if "uid" not in state:
        await update.message.reply_text("❌ PEHLE UID BHEJO")
        return

    photo = update.message.photo[-1].file_id

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "🚨 NEW ORDER 🚨\n\n"
            f"👤 @{user.username}\n"
            f"🆔 {user_id}\n\n"
            f"🎯 {state.get('service')}\n"
            f"📦 {state.get('package')}\n"
            f"💰 ₹{state.get('price')}\n"
            f"🔗 UID: {state.get('uid')}"
        )
    )

    await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo)

    await update.message.reply_text(
        "✅ PAYMENT SUCCESS 💸\n\n"
        "⏳ VERIFYING...\n"
        "🚀 START SOON\n\n"
        "💀 NO WAY BACK 😈"
    )

    user_state[user_id] = {}

# ================== MAIN ==================

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.add_handler(MessageHandler(filters.PHOTO, handle_payment))

    print("💀 BOT RUNNING (IMPROVED UI)...")
    app.run_polling()