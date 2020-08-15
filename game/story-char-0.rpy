label story_char_0:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase_small("images/spell_publish_bs.png") with dissolve
    "发布作品：又叫“我爱中国”，使忠粉攻击小孩，以使小孩眩晕 10 秒。"
    hide screen spell_showcase_small with dissolve
label story_char_0_true:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("伏拉夫\n会飞的鸡", "小孩\n我要伏拉夫吃我\n奥利给\n火锅") with dissolve
    pause
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    show child_with_pan with dissolve
    "你看见了一些小孩（xxs）。是否攻击？{w=2.0}{nw}"
    $ _history_list.pop()
    hide child_with_pan with dissolve
    menu:
        "你看见了一些小孩（xxs）。是否攻击？"
        "是":
            $ _history_list.pop()
            scene black with dissolve
            show screen battle_status("会飞的猪 击败了 xxs\n剩余 2 击败 1") with dissolve
            "你抓住了 xxs 并淘汰了他。"
            menu:
                "是否对 知道的93 攻击并释放技能？"
                "是":
                    $ _history_list.pop()
                    pass
                "使用技能 眩晕 并击败他":
                    $ _history_list.pop()
                    stop music
                    play sound dizzy
                    pause 1.0
                    play sound dizzypt2
                    pause 1.5
                    hide screen battle_status with dissolve
                    $ quick_menu = False
                    window hide dissolve
                    scene fail with dissolve
                    play sound gameover
                    show screen reload_prompt("小孩们乘机开机子跑了！")
                    pause
                    stop sound
                    $ quick_menu = True
                    jump endgame
        "撤退":
            $ _history_list.pop()
            window hide dissolve
            scene black with dissolve
            $ quick_menu = False
            stop music
            play sound run
            pause 1.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你最后被陷害了。你死了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    hide screen battle_status with dissolve
    stop music
    $ quick_menu = False
    window hide dissolve
    scene win with dissolve
    play sound win
    show screen reload_prompt("你又淘汰了最后两个人，你赢了！")
    pause
    stop sound
    $ quick_menu = True
    jump endgame