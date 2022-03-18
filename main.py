
from os import path
import nonebot
import config
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("糖糖")

if __name__ == '__main__':
    
    nonebot.init(config)

    ######################
    #导入本插件

    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'tang'),
        'tang'
)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'qiandao'),
        'qiandao'
)
    ######################
    
    nonebot.run()

