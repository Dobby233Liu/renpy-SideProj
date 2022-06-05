label story_char_heimankun:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("images/heiman_spell_coming2urhome.png") with dissolve
    "很快就到你家门口：所有小孩全部眩晕 10 秒。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("images/spell_heilafu.png") with dissolve
    "大家好我是黑拉夫：附近倒地者死亡时间减少 10 秒（有概率直接秒死）。"
    hide screen spell_showcase with dissolve
label story_char_heimankun_start:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare(_("黑曼君"), _("小孩")) with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    show child_with_pan with dissolve
    "你看见了一个拿着平底锅的小孩。你准备做点什么？{w=2.0}{nw}"
    $ _history_list.pop()
    hide child_with_pan with dissolve
    menu:
        with dissolve
        "你看见了一个拿着平底锅的小孩。你准备做点什么？"
        "跑！":
            $ _history_list.pop()
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            play sound run
            pause 2.0
            play sound pong
            pause 2.0
            call endscreen(content=_("你被小孩打死了！"), screen="dead", music=audio.gameover)
            return
        "干就完了":
            $ _history_list.pop()
            pass
    show screen spell_showcase("images/decomap.png", 1.25) with dissolve
    "你看见了一张地图。你要去哪里呢？{w=2.0}{nw}"
    $ _history_list.pop()
    hide screen spell_showcase with dissolve
    menu:
        with dissolve
        "你看见了一张地图。你要去哪里呢？"
        "厨房":
            $ _history_list.pop()
            pass
        "卧室":
            $ _history_list.pop()
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            play sound run
            pause 2.0
            play sound pong
            pause 2.0
            call endscreen(content=_("你被陷害了！"), screen="dead", music=audio.gameover)
            return
    scene kitchen with dissolve
    show screen spell_showcase("images/wowotou.png", 1.5, 0.25) with dissolve
    "你找到了一个窝窝头。它可能会提升你的移动速度。"
    hide screen spell_showcase with dissolve
    menu:
        with dissolve
        "要吃它吗？"
        "是":
            $ _history_list.pop()
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            play sound chomp
            pause 1.0
            play sound dizzypt2
            pause 1.0
            call endscreen(content=_("你被毒死了！"), screen="dead", music=audio.gameover)
            return
        "否":
            $ _history_list.pop()
            pass
    call endscreen(content=_("时间被消耗光了，你胜利了！"), screen="win", music=audio.win)
    return
