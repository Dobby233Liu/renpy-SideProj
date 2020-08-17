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
    "xxs 出现了！"
label story_char_0_battle_myround:
    menu:
        with dissolve
        "要做点什么呢？"
        "攻击":
            menu:
                with dissolve
                "要使用哪个招数？"
                "马上就到你面前":
                    "会飞的猪 使用了 马上就到你面前！" nointeract
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
                    play sound child_faint
                    pause 0.5
                    "致命一击！"
                    # temp
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    hide child_with_pan with easeoutright
                    "xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    "xxs" "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                "发布作品": # FIXME：引战
                    "会飞的猪 使用了 发布作品！" nointeract
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
                    play sound child_faint
                    pause 0.5
                    "致命一击！"
                    # temp
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    hide child_with_pan with easeoutright
                    "xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    "xxs" "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                "眩晕":
                    "会飞的猪 使用了 眩晕！" nointeract
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
                    "3..."
                    child_lead "zzzzzzzzzz"
                    "2..."
                    if renpy.random.randint(0,3) == 2:
                        child_lead "啊啊啊啊啊啊啊啊啊啊"
                        "xxs 做了个恶梦，所以又起来了！"
                        "攻击没有效果！！！"
                        jump story_char_0_battle_myround
                    else:
                        child_lead "zzzzzzzzzz"
                        "1..."
                        pause 0.5
                        "..." nointeract
                        pause 0.5
                        # temp
                        stop music fadeout 1.0
                        pause 1.0
                        play music pokerg_mus_win
                        "你胜利了！"
                        "获得了 0 GOLD！"
        "逃跑":
            if renpy.random.randint(0,3) == 2:
                "但是，你突然又不想跑了..."
            else:
                play sound run
                hide fulafu_battle_normal with easeoutleft
                "成功地逃跑了！"
                $ quick_menu = False
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

# ~~~
label story_char_0_legacy_battle:
    show child_with_pan with dissolve
    "你看见了一些小孩（xxs）。是否攻击？{w=2.0}{nw}"
    $ _history_list.pop()
    hide child_with_pan with dissolve
    menu:
        with dissolve
        "你看见了一些小孩（xxs）。是否攻击？"
        "是":
            $ _history_list.pop()
            scene black with dissolve
            show screen battle_status("会飞的鸡 击败了 xxs\n剩余 2 击败 1") with dissolve
            "你抓住了 xxs 并淘汰了他。"
            menu:
                with dissolve
                "是否对 知道的93 攻击并释放技能？"
                "是":
                    $ _history_list.pop()
                    pass
                "使用技能 眩晕 并击败他":
                    $ _history_list.pop()
                    $ quick_menu = False
                    "会飞的鸡 使用了 眩晕！{p=1.0}{nw}"
                    window hide dissolve
                    play sound dizzy
                    pause 1.0
                    play sound dizzypt2
                    pause 1.5
                    stop music
                    hide screen battle_status with dissolve
                    scene fail with dissolve
                    play sound gameover
                    show screen reload_prompt("小孩们乘机开机子跑了！")
                    pause
                    stop sound
                    $ quick_menu = True
                    jump endgame
        "撤退":
            $ _history_list.pop()
            stop music
            $ quick_menu = False
            window hide dissolve
            scene black with dissolve
            play sound run
            pause 1.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你最终被陷害了。你死了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    stop music
    $ quick_menu = False
    hide screen battle_status with dissolve
    window hide dissolve
    scene win with dissolve
    play sound win
    show screen reload_prompt("你又淘汰了最后两个人。你赢了！")
    pause
    stop sound
    $ quick_menu = True
    jump endgame