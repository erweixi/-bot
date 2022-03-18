from .test import createrr
from nonebot import on_command, CommandSession,scheduler
import os

number = 1
justyes=[]

@on_command("签到",only_to_me = False)
async def qiandao(session: CommandSession):
    if session.ctx['user_id'] in justyes:
        await session.send("今天已经签到过啦，明天再来找糖糖玩吧~")
        return
    unm = session.ctx['sender']["nickname"]
#    guid = session.ctx['group_id'], session.ctx['user_id']
    global number
    createrr(user_name=unm,gid=session.ctx['group_id'],number = str(number).rjust(4,'0'),uid = session.ctx['user_id'])
    await session.send(f"小天使请安！欢迎回来，阿P！\n[CQ:image,file=file:///C://Users//Administrator//Desktop//tangtang//qiandao//{session.ctx['user_id']}.png]")
    number += 1
    os.remove(f".\\qiandao\\{session.ctx['user_id']}.png")
    justyes.append(session.ctx["user_id"])

@scheduler.scheduled_job(
    'cron',
    day='*',
    hour='0',
    minute='0'
)
async def hunsband_goodMorning():
    global number
    number = 1
    justyes.clear()