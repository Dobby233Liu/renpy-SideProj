label story_char_1:
    window hide dissolve
    $ quick_menu = False
    show screen race_prepare("伏拉夫\n会飞的猪", "小孩\nxxs") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    "..." nointeract
    pause 0.5
    scene fix_house with dissolve
    show car_fixing with dissolve
    "直奔主题，你又在修车。"
    if not persistent.dew_bottle or persistent.dew_bottle == 0:
        $ persistent.dew_bottle = 0
        show dew_bottle with dissolve
        "无聊的你从背包里拿出一瓶香水。"
        "攻略里说，它能有效驱赶头顶上的苍蝇。"
        "但是游戏里却说它只是个装饰性物品，没有用。"
        "就算真如攻略所言，这里也没有苍蝇。"
        "果然攻略不可信，丢了丢了。" nointeract
        hide dew_bottle with easeoutright
        $ persistent.dew_bottle = 1
        pause
    elif persistent.dew_bottle == 1:
        $ persistent.dew_bottle = 2
        "对了，你吸取了上次的教训，这次没手贱去捡垃圾。"
    menu:
        with dissolve
        "接下来要修哪台机子？"
        "第一个":
            $ _history_list.pop()
            pause 1.0
            hide car_fixing with dissolve
            "已经修好了一台机子，还剩 2 台。"
            menu:
                with dissolve
                "你的头上出现了乌鸦！"
                "修别的机子":
                    pass
                "等伏拉夫溜它":
                    $ quick_menu = False
                    scene black with dissolve
                    "..."
                    window hide dissolve
                    stop music
                    scene dead with dissolve
                    play sound gameover
                    show screen reload_prompt("伏拉夫来把乌鸦带走，顺便把你抓回去了！")
                    pause
                    stop sound
                    $ quick_menu = True
                    jump endgame
                "驱赶":
                    pass
        "发呆":
            hide car_fixing with dissolve
            scene black with dissolve
            stop music
            $ quick_menu = False
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            window hide dissolve
            play voice haoci
            show screen chat("xxs 因为 AFK 被系统踢出游戏")
            pause 2.0
            hide screen chat with dissolve
            pause 1.0
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("你因为挂机被踢出了游戏！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame

    show car_fixing with dissolve
    pause 1.0
    hide car_fixing with dissolve
    "已经修好了第二台机子，并解决了乌鸦，还剩 1 台。"
    label story_char_1_contiune:
        menu:
            with dissolve
            "你的朋友突然告诉你洞穴被他挖通了。要去那里避难吗？"
            "再修一台":
                $ _history_list.pop()
                $ quick_menu = False
                window hide dissolve
                stop music
                scene win with dissolve
                play sound win
                show screen reload_prompt("你修好了第三台机子。你赢了！")
                pause
                stop sound
                $ quick_menu = True
                jump endgame
            "去洞穴":
                $ _history_list.pop()
                scene black with dissolve
                "你来到洞穴里。"
                "这里看起来不太宽敞，不过还可以。"
                stop music fadeout 0.5
                "..." nointeract
                pause 1
                $ quick_menu = False
                play music run fadein 0.125
                "突然，你发现成群的人正在冲进洞穴里。" nointeract
                $ renpy.pause(0.5, hard=True)
                play sound run loop
                "你的队友，还有发现洞穴的敌人。" nointeract
                $ renpy.pause(0.25, hard=True)
                stop music
                stop sound fadeout 0.0625
                play sound pong
                "突然，你听见一声巨响..." nointeract
                pause 0.5
                play music punchs fadein 0.125
                "...洞穴要塌了...!" nointeract
                $ i = 0
                while i < 5:
                    play voice punchs
                    with vshake nointeract
                    with hshake nointeract
                    $ renpy.pause(0.1, hard=True)
                    $ i += 1
                stop music
                stop voice fadeout 0.05
                window hide(None)
                $ renpy.pause(1, hard=True)
                #$ quick_menu = False
                #window hide dissolve
                #stop music
                scene fail with dissolve
                play sound gameover
                show screen reload_prompt("机子没人修，也就只能挤在一起，洞穴就这样崩了！")
                pause
                stop sound
                $ quick_menu = True
            "请给我提示！":
                $ _history_list.pop()
                show screen notify("洞穴nx") with dissolve
                jump story_char_1_contiune
            "死掉":
                $ _history_list.pop()
                $ quick_menu = False
                window hide dissolve
                stop music
                scene dead with dissolve
                play sound gameover
                show screen reload_prompt("你自裁了。你感觉自己像个人渣！")
                pause
                stop sound
                $ quick_menu = True
    jump endgame
