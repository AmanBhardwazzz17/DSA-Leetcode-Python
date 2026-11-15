class Codec:
    def __init__(self):
        # Ek diary (dictionary) banayi jisme short aur long URL ka hisab rakhenge
        self.diary = {}

    def encode(self, longUrl: str) -> str:
        # Diary mein jitne URLs hain, uske hisab se naya short link banao
        short = f"http://tinyurl.com{len(self.diary)}"
        self.diary[short] = longUrl  # Diary mein note kar liya
        return short

    def decode(self, shortUrl: str) -> str:
        # Diary mein short link dhoondh kar asli URL wapas de diya
        return self.diary[shortUrl]
