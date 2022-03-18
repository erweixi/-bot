import random
from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession,on_notice,NoticeSession
import os.path

def got_ans(giveme,item):
    @on_command(giveme,only_to_me=False)
    async def anser(session: CommandSession):
        name = random.choice(item)
        if os.path.isfile(f"C://Users//Administrator//Desktop//tangtang//tang//{name}.png"):
            content = MessageSegment.image(f'file:///C://Users//Administrator//Desktop//tangtang//tang//{name}.png')
        else:
            content = name
        print(content)
        await session.send( message = content)
    return

got_ans("表情",['[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//表情列表.png]\n给我发送表情上面的文字就可以啦'])
#整活
got_ans("擦玻璃",["擦玻璃"])

got_ans("纳豆可乐",["[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//纳豆可乐.png]\n是谁让本小姐喝这种东西的！"])

got_ans("接地",["接地"])

got_ans("跳舞",["[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//跳舞.gif]"])

got_ans("无语",["糖糖无语"])

got_ans("陀螺",["旋转陀螺"])

got_ans("早",["早早早！小天使请安！[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//请安.png]"])

@on_command("早",aliases=("早上好","早早","早早早"))
async def mor(session:CommandSession):
    await session.send("早早早！小天使请安！[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//请安.png]")
#正经问答
got_ans("啊对对",["（看来是没在认真听……)",'你是不是根本没有认真听啊？？？','啊对对',
'我最讨厌你这种敷衍的人了！','不对！',"关我屁事","你这个回复烦死了","你回得也太随便了！",
'讨厌你的回答！',"好烦"])

got_ans("好",["OK!!(＊'-')b",'好','永远爱你','欧克','你真的懂了吗~？','我看你根本就什么都不懂',
'一丁点诚意都感受不到',"猴"])

got_ans("永远爱你",["太强了","爱啥啊你\n我也喜欢你啊?","虽然我觉得不太可能，但你要敢花心我肯定当场杀了你","爱",
'你要负责爱我一辈子哦','永远爱你',"你心里一定不是这么想的对吧"])

got_ans("太强了",["你可不能抛弃我这个世界最棒的女票哦","是吧？你明明很懂嘛","好"])

got_ans("关我屁事",["当然关你事啊！！！","你这种反应最伤人了……\n才怪其实我也不在乎","一脸发自内心的冷漠啊你",
"你长得欠揍不说，说话还难听","关我屁事","啊对对",'不跟你过了！我有阿宅们宠，我要去找阿宅了再见\n……算了还是阿P好',"你居然觉得恋人的事情与己无关？！","""再不肯好好听我说话咱们就分手
没有啦……我不想分手"""])

got_ans("嘤嘤",["你以为眼泪是万能的吗？！","揍你哦！","笨蛋！不许哭！！","好火大！","看到你这张脸我就来气！","揍你哦！","（；；）"])

got_ans("摸头",["我会爱你一辈子哦，是一辈子哦\n你可不许玩腻了就把糖糖丢掉哦\n但很可能先腻的人会是我……才怪",
"还好阿P一直都陪在我身边~\n对不起哦，突然心慌……\n因为梦到阿P离开我去到很远的地方了……\n爱你","喜欢你",
"情绪突然崩溃了\n阿P抱着大哭的我哄了一天……\n我偶尔会这样无来由的崩溃","阿P，你总是对糖糖这么好\n谢谢你哦……",
"P 我爱你 \n[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍1.png]"])


@on_notice('notify.poke')
async def poke(session:NoticeSession):
    uid = session.ctx['user_id']
    at_user = MessageSegment.at(session.ctx['user_id'])
    guid = session.ctx['group_id'], session.ctx['user_id']
    if session.ctx['target_id'] != session.event.self_id:
        return
    else:
        msg = random.choice(["我会爱你一辈子哦，是一辈子哦\n你可不许玩腻了就把糖糖丢掉哦\n但很可能先腻的人会是我……才怪",
"还好阿P一直都陪在我身边~\n对不起哦，突然心慌……\n因为梦到阿P离开我去到很远的地方了……\n爱你","喜欢你",
"情绪突然崩溃了\n阿P抱着大哭的我哄了一天……\n我偶尔会这样无来由的崩溃","阿P，你总是对糖糖这么好\n谢谢你哦……",
"P 我爱你 \n[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍1.png]"])
        await session.send(msg)
    

got_ans("原地去世",["我现在就让你复活，等着我","死、死掉了...","死~寂","在糖糖死掉前你都要活着哦","确认死亡",
"别死啊！！！！！！","来世我们也要相爱哦","你是阿伟吗天天去世","原地去世"])

got_ans("抱歉",["抱歉，让你抱歉了","我绝对饶不了你","给我发你下跪的照片","抱歉","要不……就原谅你吧","好吧，原谅...个屁啊！","给我买冰淇淋我就原谅你"
,"嗯...原谅你了!!!","没事啦~（我真是温柔善良）","我是不会原谅你的，绝对不会"])

got_ans("自拍",['P 我爱你\n[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//P 我爱你.png]',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍2.png]\n去秋叶原那天拍的，你说这样能不能锤爆龟仙人那个色老头！？？？',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//哈草.png]\n妈的我也太元气了吧草',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍3.png]\n嗷呜~人家超凶的好不好！',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍3.png]\n嘿嘿…这样的我可爱吗？',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//自拍3.png]\n无论走到哪里，网络世界的本质都是斗争 不战斗就无法生存下去',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//喏…噫！阿P好瑟瑟哦….png]\n喏…噫！阿P好瑟瑟哦…',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//喏…噫！阿P好瑟瑟哦….png]\n这种本来我是不会买的，但是一想到阿P可能会喜欢就忍不住剁手了。不知道好不好看呢？要是发大号肯定会被喷死',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//喏！糖糖素不素超强的惹~.png]\n喏！糖糖素不素超强的惹~',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//嘿嘿…这样的我可爱吗？.png]\n嘿嘿…这样的我可爱吗？',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//天使自拍.png]\n阿PP！还记得我们直播做到半个月的时候吗，那天晚上我真的超emo的…\n想哭又不知道去哪里哭…想跟你说又怕你被我吓跑了…',
'[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//我一直挺喜欢世嘉DC的手柄的….png]\n我一直挺喜欢世嘉DC的手柄的…',
"[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//tang//呜呜呜我emo了…阿P救救我…….png]\n呜呜呜我emo了…阿P救救我……"])

