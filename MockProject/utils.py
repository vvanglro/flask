from pypinyin import lazy_pinyin,  Style
import random, string

# 中文转拼音
def pinyin(character):
    style = Style.NORMAL
    return ''.join(lazy_pinyin(character, style=style))

# 随机生成大写字母+数字
def train_orderNO(num):
    numberalphabet = string.ascii_letters[-26:] + string.digits
    return 'WH' + "".join(random.sample(numberalphabet, num))