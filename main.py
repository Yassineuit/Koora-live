import logging
import telegram
import time
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# تهيئة سجل السجلات لتسجيل الأحداث والأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# استبدال "TOKEN" بتوكن البوت الخاص بك الذي حصلت عليه من BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# إنشاء كائن Updater وتمرير توكن البوت الخاص بك
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# تعريف وظيفة للتعامل مع الأمر /start
def start(update, context):
    keyboard = [[telegram.KeyboardButton("Star")]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('هذا البوت يمكنك الربح منه عن طريق القيام بالمهمات و يتم دفع 5$ لكل مهمة هل أنت مستعد للعمل ؟',
                              reply_markup=reply_markup)

# تعريف وظيفة للتعامل مع الاستجابة على الزر "star"
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='قمت بالضغط على الزر "Star"')

# تعريف وظيفة للتعامل مع أي رسالة تم استلامها
def echo(update, context):
    user_response = update.message.text
    update.message.reply_text('مرحبًا بالجميع، اسمي ميشا وأنا مساعد موارد بشرية في Moniagame. تشرفت بلقائكم!')
    time.sleep(1)  # تأخير لمدة ثانية واحدة
    update.message.reply_text('مهمتنا المحددة هي الترويج التعاوني لـ "Moniagame" وإكمال إنشاء أحجام تداول حقيقية للعملات المشفرة. إذا كنت تعمل بجد، يمكنك كسب ما بين 200 و 5000 درهم مغربي في اليوم حيث يتم تسوية الأجور في الوقت الحقيقي!')
    if user_response:
        update.message.reply_text('ممتاز، المهمة هي كالتالي :
1: اضغط على الإستبيان عبر الرابط التالي : https://locked4.com/sl/4kw12

2: اجب على 6 أسئلة كاملة

3: ارسل لي لقطة شاشة عند الانتهاء من المهمة

من افضلك بعد الاجابة على الأسئلة ابقى في الموقع لمدة 30 ثانية لكي نتحقق من اكتمال المهمة')

# تمرير الأمر /start للتعامل معه باستخدام الدالة start()
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# تمرير الاستجابة للزر "star" للتعامل معها باستخدام الدالة button()
button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

# تمرير أي رسالة للتعامل معها باستخدام الدالة echo()
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# بدء التشغيل
updater.start_polling()</html>
