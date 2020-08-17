label story_char_1:
    window hide dissolve
    $ quick_menu = False
    show screen race_prepare("伏拉夫\n会飞的猪", "小孩\nxxs") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    "..."
    scene fix_house with dissolve
    show car_fixing with dissolve
    show dew_bottle with dissolve
    "你找到了一瓶香水，可以有效驱赶头顶上的苍蝇。"
    hide dew_bottle with dissolve
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
                    window hide dissolve
                    stop music
                    scene dead with dissolve
                    play sound gameover
                    show screen reload_prompt("伏拉夫不管三七二十一地抓住你了！")
                    pause
                    stop sound
                    $ quick_menu = True
                    jump endgame
                "驱赶":
                    pass
        "挂机":
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
            show screen reload_prompt("你被踢出了游戏！")
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
            "现在可以进入洞穴里了。要去那里避难吗？"
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
                $ quick_menu = False
                window hide dissolve
                stop music
                scene fail with dissolve
                play sound gameover
                show screen reload_prompt("你像个人渣一样的进入了洞穴。机子修不好了！")
                pause
                stop sound
                $ quick_menu = True
            "请给我提示！":
                $ _history_list.pop()
                show screen notify("洞穴wx")
                jump story_char_1_contiune
            "死掉":
                $ _history_list.pop()
                $ quick_menu = False
                window hide dissolve
                stop music
                scene dead with dissolve
                play sound gameover
                show screen reload_prompt("你“死掉”了。你感觉自己像个人渣！")
                pause
                stop sound
                $ quick_menu = True
    jump endgame