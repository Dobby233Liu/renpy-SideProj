label story_char_0:
    # "技能：{w=1.0}{nw}"
    # $ _history_list.pop()
    # show screen spell_showcase("images/spell_publish_bs.png", 0.5) with dissolve
    # "发布作品：又叫“我爱中国”，使忠粉攻击小孩，以使小孩眩晕 10 秒。"
    # hide screen spell_showcase with dissolve
label story_char_0_true:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("伏拉夫\n会飞的鸡", "小孩\nxxs") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    # jump story_char_0_legacy_battle
    flying_chicken "这是什么神仙画技？？？"
    flying_chicken "算了"
    flying_chicken "从这个房间开始吧"
    show child_with_pan with blinds
    child_lead "这是什么地方"
    child_lead "等会"
    child_lead "伏拉夫已经来了？？？"
    flying_chicken "！！！"

# dumb pokemon ripoff start
label story_char_0_battle_intro:
    $ quick_menu = False
    window hide
    play music poke_mus_battle27
    show black at blink
    pause 2.5
    hide black
    scene black with blinds
    pause 1.5 # emulate the tiny pause
label story_char_0_battle_appear:
    $ renpy.change_language("poke") # gui changes (FIXME houyiz to other playthroughs)
    $ quick_menu = True
    scene fake_battle with dissolve
    show fulafu_battle_normal with easeinright:
        xalign 0.2
        yalign 0.2
    show child_with_pan with squares:
        zoom 0.5
        xalign 0.9
        yalign 0.15
    window show dissolve
    play sound child_cry
    pause 0.5
    "小孩♂ xxs 出现了！"
label story_char_0_battle_myround:
    menu:
        with dissolve
        "要做点什么呢？"
        "攻击":
            menu:
                with dissolve
                "要使用哪个招数？"
                "马上就到你家门口":
                    "会飞的鸡 使用了 马上就到你家门口！" nointeract
                    hide fulafu_battle_normal with squares
                    play sound run
                    show fulafu_battle_cast with easeinright:
                        xalign 0.8
                        yalign 0.19
                    pause 1.0
                    show danger at blink:
                        truecenter
                        zoom 2.0
                        alpha .25
                    play sound dizzy
                    play sound punchs
                    with vpunch
                    with hpunch
                    hide danger with dissolve
                    hide fulafu_battle_cast with squares
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    hide child_with_pan with easeoutright
                    play sound child_faint
                    pause 0.5
                    "KO！" # 皮一下
                    # temp
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    "小孩♂ xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                "发布作品": # maybe FIXME：引战
                    "会飞的鸡 使用了 发布作品！" nointeract
                    pause 1.0
                    hide fulafu_battle_normal
                    show fulafu_battle_cast:
                        xalign 0.2
                        yalign 0.22
                    show comment_stream_spelling with easeinleft:
                        xalign 0.9
                        yalign 0.5
                    with hpunch
                    play sound dizzypt2
                    show comment_stream_bottom with easeintop:
                        xalign 0.9
                        yalign 0.9
                    with hpunch
                    pause 0.5
                    show comment_stream_right with easeinleft:
                        xalign 0.9
                        yalign 0.15
                    with vpunch
                    hide fulafu_battle_cast with squares
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    hide comment_stream_spelling with blinds
                    hide comment_stream_bottom with blinds
                    hide comment_stream_right with blinds
                    hide child_with_pan with easeoutright
                    play sound child_faint
                    pause 0.5
                    "致命一击！"
                    # temp
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    "小孩♂ xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                "眩晕":
                    "会飞的鸡 使用了 眩晕！" nointeract
                    hide fulafu_battle_normal
                    show fulafu_battle_cast:
                        xalign 0.2
                        yalign 0.22
                    play sound dizzy
                    show circle with dissolve:
                        xalign 0.9
                        yalign 0.15
                    pause 0.5
                    hide circle with blinds
                    hide fulafu_battle_cast
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    child_lead "zzzzzzzzzz"
                    "3..." nointeract
                    pause 1.0
                    child_lead "zzzzzzzzzz"
                    "2..." nointeract
                    pause 1.0
                    if renpy.random.randint(0,3) == 2:
                        child_lead "啊啊啊啊啊啊啊啊啊啊"
                        "小孩♂ xxs 做了个噩梦，又醒来了！"
                        "攻击不是很有效果...！"
                        jump story_char_0_battle_myround
                    else:
                        child_lead "zzzzzzzzzz"
                        "1..." nointeract
                        pause 1.0
                        "..." nointeract
                        pause 1.0
                        window hide
                        hide child_with_pan
                        show screen chat("xxs 因为 AFK 被系统踢出游戏")
                        pause 0.5
                        hide screen chat with dissolve
                        window show
                        # temp
                        stop music fadeout 1.0
                        pause 1.0
                        play music pokerg_mus_win
                        "你胜利了！"
                        "获得了 0 GOLD！"
        "逃跑":
            if renpy.random.randint(0,3) == 2:
                flying_chicken "那我就逃—" nointeract
                play sound run
                pause 0.083
                window hide
                show black
                stop sound
                show fulafu_overworld_jumpscare
                play sound dizzypt2
                with vpunch
                with hpunch
                play sound run
                hide fulafu_overworld_jumpscare
                hide black
                pause 0.08
                window show
                "不，你不想！"
            else:
                play sound run
                hide fulafu_battle_normal with easeoutleft
                $ quick_menu = False
                "成功地逃跑了！"
                window hide dissolve
                stop music fadeout 1.0
                pause 1.0
                play music pokerg_mus_win fadein 1.0
                $ quick_menu = True
                window show dissolve
                child_lead "？？？"
                child_lead "伏拉夫不是要吃小孩火锅吗"
                child_lead "怎么又跑了"
    stop music fadeout 0.5
    $ quick_menu = False
    window hide dissolve
    scene black with dissolve
    $ renpy.change_language(None)
    return
# dumb pokemon ripoff end

# legacy_battle - goodbye everyone
