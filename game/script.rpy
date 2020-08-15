# 游戏在此开始。

define player_character = 0 # 0: fulafu, 1: child

label start:
    scene black

    window show dissolve
    menu:
        "请选择阵营。"
        "狩猎":
            menu:
                "请选择角色。"
                "黑曼君":
                    jump story_heimankun
                "伏拉夫":
                    $ player_character = 0
        "逃离":
            $ player_character = 1
            "已自动选择小孩。"
    
label search:
    window hide dissolve
    $ quick_menu = False
    show screen fake_search("匹配中...") with dissolve
    pause 1.25
    hide screen fake_search with dissolve
    window show dissolve
    "匹配成功。"
    $ quick_menu = True
    $ jump_to_label = "story_char_" + str(player_character)
    jump expression jump_to_label
    jump endgame

# see story-char-0.rpy

# see story-char-1.rpy

# see story-heimankun.rpy

label endgame:
    window hide dissolve
    return