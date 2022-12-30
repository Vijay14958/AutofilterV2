# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 27639102))
    API_HASH = os.environ.get("API_HASH", "35142c1407be6264e68fb6bec5dcabd9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5950527826:AAFmfHIP5l7Aoqa84S3ONVQK8-gRcG7N6hM")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOMIBu7JGF2Z1wW7mJ4n-IYGhcxNiJp8FCq1YqsnZGVJrnTvXiFIUMFFZzDe8l2wQFqCmBaB82PhuaVSyckYWl7_o11OZGbOOk4xNBPHvpwpbzAZ1ZNtJHbAFkB0fJ-_vr22X_LNfsg52MOLAebxcm6tdx0Fnsunqu8-y0VzHHi1xd2Qd0vVlAvZPiivStrDLQSCsfLHouF-pIWoIAcpjEohvo1TTIh9hxjiDLso8xFmguWw2egzNuWztgAcUsJCVoHc7b8jl7e-t-5QB-m4QNv5VE2fd8EN6o6T1FmOPTtth-HTtyYvbrpRoEQvYkpXcXU1Q437erC4pulFjfNiESQ2Y2-I=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001855754121))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "BetterFilter_VJBot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5606411877))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Demo123:Demo123@cluster0.qans7w0.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/vj_bots'>Update Channel</a> is an open source project.

    Devs: 
        <a href='https://t.me/anjel_neha'>❤️ Developer ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/VJ_Bots'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/vj_bots'>Developer</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/anjel_neha'>Developer</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/anjel_neha'>Developer</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

