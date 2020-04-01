import requests  # 导入requests包
import json

url = 'http://meowmeow.com.cn/'


def get_translate_date(word=None):
    print(url)
    From_data = {
        name: 'wangkj'
    }
    # 请求表单数据
    response = requests.post(url, data=From_data)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)


    # 打印翻译后的数据
    # print(content['translateResult'][0][0]['tgt'])
if __name__ == '__main__':
    get_translate_date('我爱中国')
