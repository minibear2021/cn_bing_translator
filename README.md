# 微软bing翻译器python sdk

[![PyPI version](https://badge.fury.io/py/cn_bing_translator.svg)](https://badge.fury.io/py/cn_bing_translator)
[![Download count](https://img.shields.io/pypi/dm/cn_bing_translator)](https://img.shields.io/pypi/dm/cn_bing_translator)

## 介绍

微软bing翻译器，支持cn.bing.com和www.bing.com，建议轻量使用，欢迎star、follow、fork。

## 适用对象

无法或者不便使用微软Azaue Text Translation服务的用户轻量级用户可以使用bing提供的翻译能力。

## 源码

[github](https://github.com/minibear2021/cn_bing_translator)

[gitee](https://gitee.com/minibear2021/cn_bing_translator)

## 安装

```
pip install cn_bing_translator
```

## 使用方法

```python
from cn_bing_translator import Translator

if __name__ == "__main__":
    translator = Translator()
    source = "翻译器"
    result = translator.process(source)
    print(result)
```

默认情况下将自动检测源语言语种，并翻译为英语，如果需要指定其他语种，可以在初始化的时候传入对应的语言代码：

```python
# 传入以下参数初始化一个从英语到日语的翻译器
translator = Translator(fromLang='en', toLang='ja')
```

具体支持的语言类型和代码请参考[微软网站](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)。

翻译器初始化的时候，也可以定制user agent：

```python
agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 Edg/99.0.4844.51'
translator = Translator(agent=agent)
```

如果有使用代理的需求，可以指定proxy：

```python
proxy = {'https':'http://localhost:8080'}
translator = Translator(proxy=proxy)
```

默认调用cn.bing.com，如需使用www.bing.com，可以在初始化的时候指定：

```python
translator = Translator(cnBing=False)
```

需要注意的是，根据bing.com的跳转规则，如果服务器判断是中国区用户访问，即使指定cnBing为False，仍然会自动跳转到cn.bing.com。

## 注意事项

建议轻量级使用，控制调用量和频率，微软bing翻译器默认带有防滥用措施，频繁发起大量请求可能会触发拦截。
