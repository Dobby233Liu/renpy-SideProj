label story_char_0:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("images/spell_publish_bs.png", 0.5) with dissolve
    "发布作品：又叫“我爱中国”，使忠粉攻击小孩，以使小孩眩晕 10 秒。"
    hide screen spell_showcase with dissolve
label story_char_0_true:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("伏拉夫\n会飞的鸡", "小孩\n我要伏拉夫吃我\n奥利给\n火锅") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
label story_char_0_battle_intro:
    $ quick_menu = False
    window hide
    $ srf = renpy.display.draw.screenshot(None, False)
    play music poke_mus_battle27
    show black at blink
    pause 2.5
    hide black
    scene black with blinds
    pause 1.5 # emulate the tiny pause
label story_char_0_battle_main:
    $ quick_menu = True
    window show
    "TODO"
    scene black with dissolve
    jump endgame

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