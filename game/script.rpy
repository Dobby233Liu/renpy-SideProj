# 游戏在此开始。

define player_character = 0 # 0: heiman, 1: fulafu, 2: children

label start:
    scene black

    window show dissolve
    menu:
        "请选择阵营。"
        "狩猎":
            menu:
                "请选择角色。"
                "黑曼君":
                    $ player_character = 0
                    jump story_heimankun
                "伏拉夫":
                    $ player_character = 1
        "逃离":
            $ player_character = 2
            "已自动选择小孩。"
    
label search:
    show screen fake_search("匹配中...") with dissolve
    pause 1.25
    hide screen fake_search with dissolve
    "匹配成功。"
    jump endgame

label story_heimankun:
    "技能了解：{w=1.0}{nw}"
    show screen spell_showcase("heiman_spell_coming2urhome") with dissolve
    "很快就到你家门口：所有小孩全部眩晕 10 秒。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("spell_heilafu") with dissolve
    "我是黑拉夫：附近倒地者死亡时间减少 10 秒（有概率直接秒死）。"
    hide screen spell_showcase with dissolve
    menu:
        "开始游戏":
            pass
        "退出":
            jump endgame
    "TODO"

label endgame:
    window hide dissolve
    return