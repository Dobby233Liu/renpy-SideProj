label story_heimankun:
    "技能了解：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("heiman_spell_coming2urhome") with dissolve
    "很快就到你家门口：所有小孩全部眩晕 10 秒。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("spell_heilafu") with dissolve
    "我是黑拉夫：附近倒地者死亡时间减少 10 秒（有概率直接秒死）。"
    window hide dissolve
    hide screen spell_showcase with dissolve
label heimankun_start:
    $ quick_menu = False
    show screen race_prepare("黑曼君", "小孩") with dissolve
    pause
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    show child_with_pan with dissolve
    "你看见了一个拿着平底锅的小孩。你准备做点什么？{w=2.0}{nw}"
    $ _history_list.pop()
    hide child_with_pan with dissolve
    menu:
        "你看见了一个拿着平底锅的小孩。你准备做点什么？"
        "跑！":
            window hide dissolve
            $ quick_menu = False
            stop music
            scene black with dissolve
            play sound run
            pause 2.0
            play sound pong
            pause 2.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你被小孩打死了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
        "干就完了":
            pass
    show screen spell_showcase("decomap") with dissolve
    "你看见了一张地图。你要去哪里呢？{w=2.0}{nw}"
    $ _history_list.pop()
    hide screen spell_showcase with dissolve
    menu:
        "你看见了一张地图。你要去哪里呢？"
        "厨房":
            pass
        "卧室":
            window hide dissolve
            $ quick_menu = False
            stop music
            scene black with dissolve
            play sound run
            pause 2.0
            play sound pong
            pause 2.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你被陷害了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    scene kitchen with dissolve
    show screen spell_showcase("wowotou") with dissolve
    "你找到了一个窝窝头。它可能会提升你的移动速度。"
    hide screen spell_showcase with dissolve
    menu:
        "要吃它吗？"
        "是":
            window hide dissolve
            $ quick_menu = False
            stop music
            scene black with dissolve
            play sound chomp
            pause 2.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你被毒死了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
        "否":
            pass
    window hide dissolve
    $ quick_menu = False
    stop music
    scene win with dissolve
    play sound win
    show screen reload_prompt("时间被消耗光了，你胜利了！")
    pause
    stop sound
    $ quick_menu = True