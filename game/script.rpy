# 游戏在此开始。

define player_character = 0
default persistent.dew_bottle = 0

init python:
    _oldrandom = renpy.random.random
    _oldseed = renpy.random.seed
   
    import time
    renpy.random.seed(time.clock())
    _globalrandstate = renpy.random.getstate()
    
    def _newrandom():
        global _globalrandstate
       
        renpy.random.setstate(_globalrandstate)
        rv = _oldrandom()
        _globalrandstate = renpy.random.getstate()
       
        return rv
        
    def _newseed(value):
        global _globalrandstate
            
        renpy.random.setstate(_globalrandstate)
        _oldseed(value)
        _globalrandstate = renpy.random.getstate()
   
    renpy.random.random = _newrandom
    renpy.random.seed = _newseed

label start:
    $ quick_menu = True
    $ player_character = 0

    scene black with dissolve

    window show dissolve
    menu:
        with dissolve
        "请选择阵营。"
        "!!环境变量测试!!" if renpy.android and config.developer:
            python:
                for k, v in os.environ.items():
                    if "ANDROID_" in k:
                        print("%s=%s" % (k, v))
                        renpy.say(Character(k), v)
            jump start
        "狩猎":
            $ _history_list.pop()
            menu:
                with dissolve
                "请选择角色。"
                "黑曼君":
                    $ _history_list.pop()
                    # FIXME: port to use numbers
                    $ player_character = "heimankun"
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
                "请选择角色。"
                "小孩（Pre-2.0）":
                    $ player_character = "1_pre2" # special hack
                    $ _history_list.pop()
                "小孩（2.0+）" if persistent.old_version_content:
                    $ player_character = 1
                    $ _history_list.pop()
                "跳绳小妞":
                    $ player_character = 4
                    $ _history_list.pop()
        "伏拉夫（模拟器）" if persistent.old_version_content:
            $ _history_list.pop()
            jump story_fulafu_simulator
    
label search:
    window hide dissolve
    $ quick_menu = False
    show screen fake_search(_("匹配中...")) with dissolve
    pause 1.25
    hide screen fake_search
    window show(None)
    "匹配成功。"
    $ _history_list.pop()
    $ jump_to_label = "story_char_" + str(player_character)
    $ quick_menu = True
    jump expression jump_to_label
    jump endgame

label endscreen(content=_("你背叛了你的队友！"), screen="fail", music=audio.gameover):
    $ quick_menu = False
    window hide dissolve
    stop music
    scene expression screen with dissolve
    play sound music
    show screen reload_prompt(content) with dissolve
    pause
    stop sound
    jump endgame
    return

label endgame:
    $ quick_menu = True
    window hide dissolve
    return
