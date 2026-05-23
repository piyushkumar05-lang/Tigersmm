# ================== ULTRA PREMIUM + FORCE JOIN ==================

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "8897480826:AAGOV84ofjBfsyaCu5Q0ybhRKA88lnNsNH0"
ADMIN_ID = 6719411631
CHANNEL_USERNAME = "@your_channel" # <-- Apna channel daal
CHANNEL_LINK = "https://t.me/your_channel" # <-- Link daal

user_state = {}
VIP_USERS = [123456789]

# ================== CHECK CHANNEL JOIN ==================

async def check_joined(user_id, context):
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# ================== MENUS ==================

def main_menu():
    keyboard = [
        ["👥 𝗙𝗢𝗟𝗢𝗪𝗘𝗥𝗦 🔥", "❤️ 𝗟𝗜𝗞𝗘𝗦 💎"],
        ["💬 𝗖𝗢𝗠𝗘𝗡𝗧𝗦 ⚡", "🎬 𝗩𝗜𝗘𝗪𝗦 🚀"],
        ["📊 𝗠𝗬 𝗢𝗥𝗗𝗘𝗥𝗦", "📞 𝗦𝗨𝗣𝗢𝗥𝗧 𝟮𝟰/𝟳"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def package_menu(service):
    menus = {
        "👥 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 🔥": [
            ["🔥 𝟭𝟬𝟬 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 • ₹𝟲 💸", "⚡ 𝟯𝟬𝟬 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 • ₹𝟭𝟳 💸"],
            ["🚀 𝟱𝟬𝟬 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 • ₹𝟮𝟵 💸", "👑 𝟭𝗞 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 • ₹𝟱 💸"]
        ],
        "❤️ 𝗟𝗜𝗞𝗘𝗦 💎": [
            ["🔥 𝟱𝟬 𝗟𝗶𝗸𝗲𝘀 • ₹𝟰 💸", "⚡ 𝟭𝟬𝟬 𝗟𝗶𝗸𝗲𝘀 • ₹𝟳 💸"],
            ["💎 𝟮𝟬𝟬 𝗟𝗶𝗸𝗲𝘀 • ₹𝟭𝟰 💸", "🚀 𝟱𝟬𝟬 𝗟𝗶𝗸𝗲𝘀 • ₹𝟯𝟮 💸"]
        ],
        "💬 𝗖𝗢𝗠𝗘𝗡𝗧𝗦 ⚡": [
            ["🔥 𝟱𝟬 𝗖𝗼𝗺𝗲𝗻𝘁𝘀 • ₹𝟳 💸", "⚡ 𝟭𝟬𝟬 𝗖𝗼𝗺𝗲𝗻𝘁𝘀 • ₹𝟭𝟯 💸"],
            ["💎 𝟮𝟬𝟬 𝗖𝗼𝗺𝗲𝗻𝘁𝘀 • ₹𝟮𝟱 💸", "🚀 𝟱𝟬𝟬 𝗖𝗼𝗺𝗲𝗻𝘁𝘀 • ₹𝟰𝟬 💸"]
        ],
        "🎬 𝗩𝗜𝗘𝗪𝗦 🚀": [
            ["🔥 𝟮𝗞 𝗩𝗶𝗲𝘄𝘀 • ₹𝟰 💸", "⚡ 𝟱𝗞 𝗩𝗶𝗲𝘄𝘀 • ₹𝟭𝟬 💸"],
            ["💎 𝟭𝟬𝗞 𝗩𝗶𝗲𝘄𝘀 • ₹𝟭𝟱 💸", "🚀 𝟱𝟬𝗞 𝗩𝗶𝗲𝘄𝘀 • ₹𝟲𝟵 💸"]
        ],
    }
    keyboard = menus.get(service, [])
    keyboard.append(["🔙 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨 🏠"])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def is_vip(user_id):
    return user_id in VIP_USERS

# ================== START WITH FORCE JOIN ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    
    # Force Join Check
    if not await check_joined(user_id, context):
        join_btn = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔔 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗘𝗟 🔔", url=CHANNEL_LINK)],
            [InlineKeyboardButton("✅ 𝗜 𝗝𝗢𝗜𝗡𝗘𝗗", callback_data="check_join")]
        ])
        await update.message.reply_text(
            f"⚠️ 𝗛𝗘𝗬 {user_name.upper()} ⚠️\n\n"
            f"🚫 𝗔𝗖𝗘𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 🚫\n\n"
            f"👇 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗙𝗜𝗥𝗦𝗧 👇\n"
            f"💎 𝗚𝗲𝘁 𝗙𝗿𝗲 𝗢𝗳𝗲𝗿𝘀 & 𝗨𝗽𝗱𝗮𝘁𝗲𝘀\n\n"
            f"𝗧𝗵𝗲𝗻 𝗰𝗹𝗶𝗰𝗸 '𝗜 𝗝𝗢𝗜𝗡𝗘𝗗' ✅",
            reply_markup=join_btn
        )
        return

    user_state[user_id] = {}
    vip_badge = "👑 𝗩𝗜𝗣 𝗠𝗘𝗠𝗕𝗘𝗥 👑\n▰▰▰▰▰▰▰▰\n" if is_vip(user_id) else ""
    
    await update.message.reply_text(
        f"{vip_badge}"
        f"🌟 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 {user_name.upper()} 🌟\n\n"
        f"💀 𝗗𝗔𝗥𝗞 𝗣𝗔𝗡𝗘𝗟 𝗩𝟯.𝟬 💀\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"⚡ 𝗜𝗡𝗦𝗧𝗔𝗡𝗧 𝗗𝗘𝗟𝗜𝗩𝗘𝗥𝗬 ⚡\n"
        f"🔥 𝟭𝟬𝟬% 𝗥𝗘𝗔𝗟 & 𝗦𝗔𝗙𝗘 🔥\n"
        f"💎 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗤𝗨𝗔𝗟𝗜𝗧𝗬 💎\n"
        f"🚀 𝗦𝗨𝗣𝗘𝗥𝗙𝗔𝗦𝗧 𝟬-𝟯𝟬𝗠𝗜𝗡 🚀\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"🎯 𝗦𝗘𝗟𝗘𝗖𝗧 𝗦𝗘𝗥𝗩𝗜𝗖𝗘 𝗕𝗘𝗟𝗢𝗪 👇",
        reply_markup=main_menu()
    )

# ================== CALLBACK FOR JOIN CHECK ==================

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    
    if query.data == "check_join":
        if await check_joined(user_id, context):
            await query.answer("✅ Verified! Welcome")
            await start(update, context)
        else:
            await query.answer("❌ Pehle channel join karo!", show_alert=True)

# ================== HANDLE ==================

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Har message pe join check
    if not await check_joined(user_id, context):
        await start(update, context)
        return
        
    text = update.message.text

    if user_id not in user_state:
        user_state[user_id] = {}

    state = user_state[user_id]

    if text == "🔙 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨 🏠":
        user_state[user_id] = {}
        await update.message.reply_text("🏠 𝗠𝗔𝗜𝗡 𝗠𝗘𝗡𝗨", reply_markup=main_menu())
        return

    if text in ["👥 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 🔥", "❤️ 𝗟𝗜𝗞𝗘𝗦 💎", "💬 𝗖𝗢𝗠𝗘𝗡𝗧𝗦 ⚡", "🎬 𝗩𝗜𝗘𝗪𝗦 🚀"]:
        state["service"] = text
        stock = random.randint(2, 8)
        await update.message.reply_text(
            f"🎯 {text} 𝗦𝗘𝗟𝗘𝗖𝗧𝗘𝗗 ✅\n\n"
            f"⚠️ 𝗛𝗨𝗥𝗥𝗬! 𝗢𝗡𝗟𝗬 {stock} 𝗦𝗟𝗢𝗧𝗦 𝗟𝗘𝗙𝗧 ⚠️\n"
            f"⏰ 𝗢𝗙𝗘𝗥 𝗘𝗡𝗗𝗦 𝗧𝗢𝗡𝗜𝗚𝗛𝗧 𝟭𝟮𝗔𝗠\n\n"
            f"💰 𝗖𝗛𝗢𝗢𝗦𝗘 𝗣𝗔𝗖𝗞𝗔𝗚𝗘 👇",
            reply_markup=package_menu(text)
        )
        return

    if "₹" in text:
        try:
            price = int(text.split("₹")[1].split()[0])
            package_name = text.split("•")[0].strip()
        except:
            await update.message.reply_text("❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗣𝗔𝗖𝗞𝗔𝗚𝗘")
            return

        state["package"] = text
        state["price"] = price
        state["order_id"] = f"#DL{random.randint(10000,99999)}"

        await update.message.reply_text(
            f"🧾 𝗢𝗥𝗗𝗘𝗥 {state['order_id']}\n"
            f"▰▰▰▰▰▰▰▰▰▰▰\n"
            f"📦 𝗣𝗮𝗰𝗸𝗮𝗴𝗲: {package_name}\n"
            f"💰 𝗔𝗺𝗼𝘂𝗻𝘁: ₹{price}\n"
            f"⚡ 𝗗𝗲𝗹𝗶𝘃𝗲𝗿𝘆: 𝟬-𝟯𝟬 𝗠𝗶𝗻𝘂𝘁𝗲𝘀\n"
            f"🔒 𝗚𝘂𝗮𝗿𝗮𝗻𝘁𝗲: 𝟯𝟬 𝗗𝗮𝘆𝘀\n\n"
            f"💳 𝗣𝗔𝗬 𝗧𝗢 𝗨𝗣𝗜:\n"
            f"`tigerkumar@fam`\n\n"
            f"▰▰▰▰▰\n"
            f"📝 𝗦𝗧𝗘𝗣𝗦:\n"
            f"𝟭️⃣ 𝗣𝗮𝘆 ₹{price} 𝗼𝗻 𝗨𝗣𝗜 𝗮𝗯𝗼𝘃𝗲\n"
            f"𝟮️⃣ 𝗦𝗲𝗻𝗱 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸/𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲\n"
            f"𝟯️⃣ 𝗦𝗲𝗻𝗱 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗦𝗰𝗿𝗲𝗻𝘀𝗵𝗼𝘁\n\n"
            f"⚠️ 𝗡𝗘𝗩𝗘𝗥 𝗦𝗘𝗡𝗗 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ⚠️",
            parse_mode="Markdown"
        )
        return

    if text == "📊 𝗠𝗬 𝗢𝗥𝗗𝗘𝗥𝗦":
        await update.message.reply_text(
            "📊 𝗬𝗢𝗨𝗥 𝗢𝗥𝗗𝗘𝗥 𝗛𝗜𝗦𝗧𝗢𝗥𝗬\n"
            "▰▰▰▰▰▰▰\n\n"
            "❌ 𝗡𝗼 𝗼𝗿𝗱𝗲𝗿𝘀 𝗳𝗼𝘂𝗻𝗱\n\n"
            "🚀 𝗣𝗹𝗮𝗰𝗲 𝘆𝗼𝘂𝗿 𝗳𝗶𝗿𝘀𝘁 𝗼𝗿𝗱𝗲𝗿 𝗻𝗼𝘄!"
        )
        return

    if "package" in state and "uid" not in state:
        state["uid"] = text
        await update.message.reply_text(
            "📸 𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗦𝗖𝗥𝗘𝗡𝗦𝗛𝗢𝗧\n\n"
            "✅ 𝗠𝘂𝘀𝘁 𝗯𝗲 𝗰𝗹𝗲𝗮𝗿\n"
            "✅ 𝗙𝘂𝗹𝗹 𝘀𝗰𝗿𝗲𝗲𝗻 𝗽𝗶𝗰\n"
            "❌ 𝗡𝗼 𝗰𝗿𝗼𝗽/𝗲𝗱𝗶𝘁"
        )
        return

    if text == "📞 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝟮𝟰/𝟳":
        await update.message.reply_text(
            "📞 𝟮𝟰/𝟳 𝗦𝗨𝗣𝗣𝗢𝗥𝗧\n"
            "▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
            "👨‍💻 𝗔𝗱𝗺𝗶𝗻: @YOUR_USERNAME\n"
            "⚡ 𝗥𝗲𝗽𝗹𝘆 𝗧𝗶𝗺𝗲: 𝟱-𝟭𝟬 𝗠𝗶𝗻\n"
            "💬 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: 𝗛𝗶𝗻𝗱𝗶/𝗘𝗻𝗴𝗹𝗶𝘀𝗵"
        )
        return

    await update.message.reply_text("❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗢𝗣𝗧𝗜𝗢𝗡\n👇 𝗨𝘀𝗲 𝗺𝗲𝗻𝘂 𝗯𝘂𝘁𝗼𝗻𝘀", reply_markup=main_menu())

# ================== PAYMENT ==================

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if not await check_joined(user_id, context):
        await start(update, context)
        return

    if user_id not in user_state:
        return

    state = user_state[user_id]

    if "uid" not in state:
        await update.message.reply_text("❌ 𝗙𝗜𝗥𝗦𝗧 𝗦𝗘𝗡𝗗 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗟𝗜𝗡𝗞/𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘")
        return

    photo = update.message.photo[-1].file_id

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            f"🚨 𝗡𝗘𝗪 𝗢𝗥𝗗𝗘𝗥 {state.get('order_id')} 🚨\n"
            f"▰▰▰▰▰\n"
            f"👤 𝗨𝘀𝗲𝗿: @{user.username or 'None'}\n"
            f"🆔 𝗨𝘀𝗲𝗿 𝗜𝗗: `{user_id}`\n"
            f"📛 𝗡𝗮𝗺𝗲: {user.first_name}\n\n"
            f"🎯 𝗦𝗲𝗿𝘃𝗶𝗰𝗲: {state.get('service')}\n"
            f"📦 𝗣𝗮𝗰𝗸𝗮𝗴𝗲: {state.get('package')}\n"
            f"💰 𝗔𝗺𝗼𝘂𝗻𝘁: ₹{state.get('price')}\n"
            f"🔗 𝗟𝗶𝗻𝗸/𝗨𝗜𝗗: `{state.get('uid')}`"
        ),
        parse_mode="Markdown"
    )

    await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo)

    await update.message.reply_text(
        f"✅ 𝗢𝗥𝗗𝗘𝗥 {state.get('order_id')} 𝗣𝗟𝗔𝗖𝗘𝗗\n"
        f"▰▰▰▰▰▰▰\n"
        f"⏳ 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗩𝗲𝗿𝗶𝗳𝘆𝗶𝗻𝗴...\n"
        f"🚀 𝗗𝗲𝗹𝗶𝘃𝗲𝗿𝘆 𝘀𝘁𝗮𝗿𝘁𝘀 𝗶𝗻 𝟱-𝟯𝟬 𝗺𝗶𝗻\n"
        f"🔔 𝗬𝗼𝘂'𝗹 𝗴𝗲𝘁 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝘁𝗶𝗼𝗻\n\n"
        f"📊 𝗧𝗿𝗮𝗰𝗸: 𝗠𝘆 𝗢𝗿𝗱𝗲𝗿𝘀\n"
        f"💬 𝗛𝗲𝗹𝗽: @YOUR_USERNAME\n\n"
        f"💀 𝗧𝗛𝗔𝗡𝗞𝗦 𝗙𝗢𝗥 𝗢𝗥𝗗𝗘𝗥𝗜𝗡𝗚 💀",
        reply_markup=main_menu()
    )

    user_state[user_id] = {}

# ================== MAIN ==================

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.add_handler(MessageHandler(filters.PHOTO, handle_payment))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle))
    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(button_callback))

    print("💀 PREMIUM BOT + FORCE JOIN RUNNING...")
    app.run_polling()        "🎬 『𝗩𝗜𝗘𝗪𝗦』": [
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
