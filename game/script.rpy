﻿# 游戏在此开始。

define player_character = 0 # 0: fulafu, 1: child, 2: laoba, 3: laoqi, 4: ropejumper

label start:
    scene black

    window show dissolve
    menu:
        with dissolve
        "请选择阵营。"
        "狩猎":
            $ _history_list.pop()
            menu:
                with dissolve
                "请选择角色。"
                "黑曼君":
                    $ _history_list.pop()
                    jump story_heimankun
                "伏拉夫":
                    $ _history_list.pop()
                    $ player_character = 0
                "老八":
                    $ _history_list.pop()
                    $ player_character = 2
                "老祺":
                    $ _history_list.pop()
                    $ player_character = 3
        "逃离":
            $ _history_list.pop()
            menu:
                with dissolve
                "小孩":
                    $ player_character = 1
                    $ _history_list.pop()
                "跳绳小妞":
                    $ player_character = 4
                    $ _history_list.pop()
    
label search:
    window hide dissolve
    $ quick_menu = False
    show screen fake_search("匹配中...") with dissolve
    pause 1.25
    hide screen fake_search with dissolve
    window show dissolve
    "匹配成功。"
    $ _history_list.pop()
    $ jump_to_label = "story_char_" + str(player_character)
    $ quick_menu = True
    jump expression jump_to_label
    jump endgame

# see story-char-0.rpy

# see story-char-1.rpy

# see story-heimankun.rpy

label endgame:
    window hide dissolve
    return
