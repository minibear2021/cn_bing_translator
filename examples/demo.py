import logging
import os

from cn_bing_translator import Translator

if __name__ == "__main__":
    logging.basicConfig(
        filename=os.path.join(os.getcwd(), 'demo.log'),
        level=logging.DEBUG,
        filemode='a',
        format='%(asctime)s - %(process)s - %(levelname)s: %(message)s')

    translator = Translator(logger=logging.getLogger("demo"))

    while 1:
        text = input("请输入待翻译文本：")
        if text == '0':
            break
        result = translator.process(text)
        print(result)
