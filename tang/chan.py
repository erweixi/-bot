import random
from aiocqhttp import MessageSegment
import aiocqhttp
from nonebot import on_command, CommandSession


sex = 1 #涩涩的开关，设为0则不能涩涩

@on_command("桌面",only_to_me=False)
async def zhuomian(session:CommandSession):
    message =  MessageSegment.image(f'file:///C://Users//Administrator//Desktop//nonebot//tang//桌面.png')
    await session.send(message)


@on_command("陪玩",only_to_me=False)
async def peiwan(session:CommandSession):
    await session.send("今天我们要来干点什么呢，阿P\n" + '[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//陪玩.png]')

@on_command("交流",only_to_me=False)
async def communication(session:CommandSession):
    await session.send("来摸摸我的头吧！")

@on_command("游戏",aliases=("打游戏","玩游戏"),only_to_me=False)
async def game(session:CommandSession):
    message = MessageSegment.image(f'file:///C://Users//Administrator//Desktop//nonebot//tang//打游戏.gif')
    await session.send(message)

@on_command("涩涩的事情",aliases=("色色的事情"),only_to_me=False)
async def sese(session:CommandSession):
    global sex
    if sex == 0:
        await session.send("不可以涩涩！")
        return
    reply = ['''好舒服啊~
没想到我们的肉体跟心灵一样的合拍。
否则就是糖糖已经被打上阿P的标记了吧~''',
'''阿P的一切我都喜欢
这么爽的事情一旦上瘾了
脑子就会变成水从耳朵里流出去的
明天还想被搞~（直接）''',
'''感觉除了啪以外，其他的一切都无所谓了。
还买了不少小玩具，感觉怎么都做不腻。
如果我以后不爱阿P只爱啪了可怎么办……''',
'''啊~昨晚也跟阿P友谊（隐语）了
中途阿P还胡闹玩了我后面
………………………感觉还不坏''',
'''呜呜。我再也不会丢下直播去啪了。再也不了。
我绝对绝对要忍住。
我发誓……我对天发誓我要节制。
所以大家（虽然你们看不到这个号）要原谅我哦~''']
    replyment = random.choice(reply)
    await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//涩涩.gif]''' + replyment)

@on_command("出门",only_to_me=False)
async def chumen(session:CommandSession):
    place = str(session.ctx['message']).split()
    #await session.send(str(place))
    if place[-1] == "医院":
        await session.send('''今天去看医生了！！！
本来还担心早上会睡过头，不过阿P叫我起床了，看病大成功。
成功起床，我好棒！''')
    elif place[-1] == "下北泽":
        await session.send(
            '''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//下北泽.png]
满屋子都是乐队杀马特超级要命的好吗？？
不过我也没有资格说别人。。。'''
        )
    elif place[-1] == '市谷':
        await session.send(
            '''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//市谷.png]
建筑就是艺术品啊。
我还买过一本《精美阶梯影集》呢。
我特别喜欢那种像漩涡一样的螺旋楼梯。
希望有一天我能和阿P手牵着手，慢慢地一起沿着楼梯走下去。'''
        )
    elif place[-1] == "原宿":
        await session.send(
            '''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//原宿.png]
在原宿吃了好多甜点！甜品天堂永远的神！
回头想想，为了吃个甜品天堂有必要特地跑到人这么多的地方吗
失策；；'''
        )
    elif place[-1] == '涩谷':
        await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//涩谷.png]\n去道玄坂约会，主要就是去挑家好的酒店开房吧？''')
    elif place [-1 ] == "秋叶原":
        await session.send('[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//喏…噫！阿P好瑟瑟哦….png]\n这种本来我是不会买的，但是一想到阿P可能会喜欢就忍不住剁手了。不知道好不好看呢？要是发大号肯定会被喷死')
    elif place[-1] == "池袋":
        await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//池袋.png]
在池袋看到那辆大到变态的卡车了
如今他们也懂得要把音量调小了''')
    elif place[-1] == '中野':
        await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//中野.png]
哇真的在4楼打了一天的格斗。
让我打一辈子饿x偶都行。''')
    elif place[-1]== "神保町":
        await session.send("""[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//神保町.png]
神保町真的像R.O.D.里演的一样好厉害
跟阿P一起逛了好几家旧书店
这里居然还能买到萝莉写真集
这种现在都不能卖了""")
    elif place[-1] == "吉祥寺":
        await session.send("""[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//吉祥寺.png]
跟阿P去吉祥寺喝了很好的茶
我一直以为茶都一个味道，原来好茶真的不一样~~
现在我能理解刘备为了母亲喝好茶而卖刀的心情了
        """)
    else:
        await session.send("阿P今天我们去哪里呀\n[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//出门.png]")



@on_command("吃药",only_to_me=False)
async def yao(session:CommandSession):
    drug = str(session.ctx['message']).split()[-1]
    if drug == "安神片":
        await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//安神片.gif]
j见面接吗救命啊救命救
mng上么都不zhd头痛tttt头ttttttt通
wwsm要出生 想死 相似相似想死''')
    elif drug =="止咳药":
        await session.send('''[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//止咳药.gif]
啊 啊 啊 啊 啊都跟自己说过多少次了，服药过量后绝对不能出门！
如果没有阿P在，我可能真的就摔死在哪个角落里了。
不行，绝对不行！''')
    elif drug == "海波隆cp":
        await session.send("""[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//海波隆cp.gif]
啊啊啊 脑阔里好舒服啊
好像有凉凉的东西包裹住了脑子
要融化了融化了融化了
啊~~……脑浆喷发~~~""")
    elif drug == "魔法香烟":
        await session.send("""[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//魔法香烟.gif]
难搞的事情就全部忘了吧~
只有这个瞬间我才是幸福的
镜头前的我只是在逢场作戏""")
    elif drug == "魔法邮票":
        await session.send("""[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//魔法邮票.gif]
天使。我是散发着七彩祥光的如假包换的天使""")
    else :
        await session.send("压力好大...今天吃点什么呢")

@on_command("睡觉",only_to_me=False)
async def sleeep(session:CommandSession):
    await session.send("想要睡到什么时候呢")

@on_command("睡到傍晚",only_to_me=False)
async def bangwan(session:CommandSession):
    await session.send("[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//傍晚.png]ZZZ~\n压力↓\n阴暗度↓")

@on_command("睡到晚上",only_to_me=False)
async def wsss(session:CommandSession):
    await session.send("[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//晚上.png]呼呼~\n压力↓↓\n阴暗度↓↓")

@on_command("睡到明天",only_to_me=False)
async def mt(session:CommandSession):
    await session.send("[CQ:image,file=file:///C://Users//Administrator//Desktop//nonebot//tang//明天.png]ZZZ~\n压力↓↓↓↓\n阴暗度↓↓↓↓")


@on_command("因特网",only_to_me=False)
async def netnet(session:CommandSession):
    await session.send("因特网仍在开发中，请耐心等待哦~")