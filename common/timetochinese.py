import time


def tochinese(data):
    chinese_data_dict = {
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九',
        '0': '零'
    }
    chinese_data2_dict={
        '一': '十',
        '二': '二十',
        '三': '三十'
    }
    for c in data:
        if c in chinese_data_dict:
            data = data.replace(c, chinese_data_dict[c])
    return data


def get_time():
    try:
        ft = time.strftime('%Y年%m月%d日%H时%M分%S秒')
    except UnicodeEncodeError as e:
        print(e)
    finally:
        ft = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分',s='秒')
    return tochinese(ft)


if __name__ == '__main__':
    a = get_time()
    print('a',a)
