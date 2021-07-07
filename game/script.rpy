# 游戏在此开始。

define player_character = 0
default persistent.dew_bottle = 0

#init python:
    # Overwrite some Ren'Py random function to seed automatically
    #import random
    #_old_renpy_random = renpy.random.random
    #def _renpy_random(*args):
    #    renpy.random.reset()
    #    renpy.random.seed()
    #    return _old_renpy_random(*args)
    #renpy.random.random = _renpy_random
    #_old_renpy_randint = renpy.random.randint
    #def _renpy_randint(*args):
    #    renpy.random.reset()
    #    renpy.random.seed()
    #    return _old_renpy_randint(*args)
    #renpy.random.randint = _renpy_randint
    #_old_renpy_choice = renpy.random.choice
    #def _renpy_choice(*args):
    #    renpy.random.reset()
    #    renpy.random.seed()
    #    return _old_renpy_choice(*args)
    #renpy.random.choice = _renpy_choice
    #_old_renpy_shuffle = renpy.random.shuffle
    #def _renpy_shuffle(*args):
    #    renpy.random.reset()
    #    renpy.random.seed()
    #    return _old_renpy_shuffle(*args)
    #renpy.random.shuffle = _renpy_shuffle

init python:
    _oldrandom = renpy.random.random
    _oldseed = renpy.random.seed
   
    renpy.random.seed()
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
    $ player_character = 0

    scene black with dissolve

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
    show screen fake_search("匹配中...") with dissolve
    pause 1.25
    hide screen fake_search
    window show(None)
    "匹配成功。"
    $ _history_list.pop()
    $ jump_to_label = "story_char_" + str(player_character)
    $ quick_menu = True
    jump expression jump_to_label
    jump endgame

label endgame:
    window hide dissolve
    return
