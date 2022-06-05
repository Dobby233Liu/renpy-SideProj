label story_char_1:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare(_("伏拉夫\n会飞的猪"), _("小孩\nxxs")) with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene fix_house with dissolve
    show car_fixing with dissolve
    "一开局，你就必须修机子。"
    if persistent.dew_bottle == 0:
        show dew_bottle with dissolve
        "无聊的你从背包里拿出一瓶开局就有的香水。"
        "攻略里说它能有效驱赶头顶上的苍蝇。"
        "但是游戏里却说它只是个装饰性物品，没有用。"
        "就算真如攻略所言，这里也没有苍蝇。"
        hide dew_bottle with easeoutright
        "果然攻略不可信，丢了丢了。"
        $ persistent.dew_bottle = 1
    elif persistent.dew_bottle == 1:
        $ persistent.dew_bottle = -1
        "对了，你吸取了上次的教训，这次没手贱去捡垃圾。"
    menu:
        with dissolve
        "接下来要修哪台机子？"
        "第一台":
            pass
        "第二台":
            $ quick_menu = False
            "第二台在外面，所以你去扛回来。{w=1}{nw}"
            window hide dissolve
            stop music fadeout 0.5
            pause 0.5
            hide car_fixing with dissolve
            play sound run
            pause 0.28
            stop sound
            scene bg_sunny_outside with fade
            pause 0.5
            play sound run
            pause 0.924
            stop sound
            scene black
            play sound pong
            pause 2
            call endscreen(content=_("潜伏在第二台处的伏拉夫把你抓走了！"), screen="fail", music=audio.gameover)
            return
        "发呆":
            $ quick_menu = False
            hide car_fixing with dissolve
            scene black with dissolve
            stop music fadeout 1
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            window hide dissolve
            show screen chat(_("xxs 因为 AFK 被系统踢出游戏"))
            pause 2.0
            hide screen chat with dissolve
            pause 1.0
            call endscreen(content=_("你因为挂机被踢出了游戏！"), screen="fail", music=audio.gameover)
            return

    pause 1.0
    hide car_fixing with dissolve
    "已经修好了一台机子，还剩 2 台。"
    menu:
        with dissolve
        "你的头上出现了乌鸦！"
        "修别的机子":
            pass
        "等伏拉夫，然后去溜他":
            $ quick_menu = False
            scene black with dissolve
            "..."
            call endscreen(content=_("伏拉夫把你抓到了！\n记住，休想溜他！"), screen="dead", music=audio.gameover)
            return
        "驱赶":
            pass

    show car_fixing with dissolve
    pause 1.0
    hide car_fixing with dissolve
    "已经修好了第二台机子，也解决了乌鸦。只剩 1 台。"
    label story_char_1_contiune:
        menu:
            with dissolve
            "你的朋友突然告诉你洞穴被他挖通了。要去那里避难吗？"
            "再修一台":
                $ _history_list.pop()
                call endscreen(content=_("你修好了第三台机子。你们赢了！"), screen="win", music=audio.win)
                return
            "去洞穴":
                $ _history_list.pop()
                scene cave with dissolve
                "你来到洞穴里。"
                "这里看起来不太宽敞，不过毕竟紧急时刻，也还可以。"
                stop music fadeout 0.5
                $ quick_menu = False
                "..." nointeract
                $ renpy.pause(2, hard=True)
                play music run fadein 0.125
                "突然，你发现成群的人正在冲进洞穴里。" nointeract
                $ renpy.pause(0.5*8, hard=True)
                play sound run loop
                "你的队友，还有发现洞穴的敌人。" nointeract
                $ renpy.pause(0.25*10, hard=True)
                stop music
                stop sound fadeout 0.0625
                $ renpy.pause(0.0625, hard=True)
                play sound pong
                $ renpy.pause(0.125, hard=True)
                "那是什么声音？..." nointeract
                $ renpy.pause(4, hard=True)
                play music punchs fadein 0.25
                "...洞穴要塌了...！" nointeract
                $ renpy.pause(1.2, hard=True)
                window hide(None)
                $ i = 0
                while i < 6:
                    play voice punchs
                    with vpunch
                    with hpunch
                    $ renpy.pause(0.01, hard=True)
                    $ i += 1
                stop music
                stop voice fadeout 0.05
                scene black with blinds
                #window hide(None)
                $ renpy.pause(4, hard=True)
                call endscreen(content=_("机子没人修，人也只能挤在一起，洞穴就这样崩了！"), screen="fail", music=audio.gameover)
                return
            "给我提示！":
                $ _history_list.pop()
                show screen notify(_("洞穴wx")) with dissolve
                "你真菜。"
                jump story_char_1_contiune
            "死掉":
                $ _history_list.pop()
                call endscreen(content=_("你自裁了。你感觉自己像个人渣！"), screen="dead", music=audio.gameover)
                return
    return
