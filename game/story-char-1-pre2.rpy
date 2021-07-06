label story_char_1_pre2:
    window hide dissolve
    $ quick_menu = False
    # FIXME: wtf is this
    show screen race_prepare("伏拉夫\n会飞的猪\n{i}sysmsg{/i}\n{i}还有两个...{/i}", "小孩\nxxs\n抖音小雨\n可可里加巧克力") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene kitchen with dissolve
    show screen spell_showcase("images/pan.png", 1.5, 0.25) with dissolve
    "你开局就在厨房里。这儿有个平底锅，旁边有一张说明书。" with dissolve
    show screen spell_showcase("images/pan_note.png") with dissolve
    "第一：平底锅是一次性物品，使用一次后销毁（无法使用）。"
    "第二：对敌人使用可以使敌人眩晕 30 秒，在坚固的固体上使用直接销毁，其它无效果。"
    hide screen spell_showcase with dissolve
    hide screen spell_showcase with dissolve # yeah i am noob
    menu:
        with dissolve
        "此时，你要："
        "尝试使用平底锅":
            $ _history_list.pop()
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            play sound pong
            pause 1.0
            play sound dizzypt2
            pause 1.0
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你因为太手残，不小心打晕了自己！") with dissolve
            pause
            stop sound
            $ quick_menu = True
            jump endgame
        "去找更多的物资":
            pass
    scene fix_house with slideawayleft
    show screen spell_showcase("images/key.png", 1.25) with dissolve
    "你找到了 钥匙！" nointeract with dissolve
    pause 1.5
    window hide dissolve
    hide screen spell_showcase with dissolve
    play voice pong # collect
    pause 0.25
    window show dissolve
    "还剩两把钥匙没有收集。"
    "听说集满三把可以打开大门。"
    scene kitchen with fade
    "这时候也没有什么可做的，你继续找钥匙。{w=1}{nw}" nointeract
    scene bg_sunny_outside with fade
    "这时候也没有什么可做的，你继续找钥匙。{w=1}{nw}" nointeract
    window hide
    stop music fadeout 0.25
    play music poke_mus_battle27
    show black at blink
    pause 1.25
    if renpy.random.randint(0,3) == 1:
        # "glitch out"
        play music c2g
        show fulafu_overworld_jumpscare
        pause 0.5
        hide fulafu_overworld_jumpscare
        show fulafu_overworld
    else:
        show fulafu_overworld with blinds
    pause 1.25
    hide black
    with vpunch
    play voice fulafu_cry
    pause 0.25
    window show dissolve
    "突然，伏拉夫来了！"
    menu:
        with dissolve
        "要对 伏拉夫 使用什么招数呢？"
        "撞（zhi）击（beng）":
            $ _history_list.pop()
            $ quick_menu = False
            "xxs 使用了 撞击！" nointeract
            with vpunch
            pause 0.25
            play sound punchs
            with hpunch
            pause 0.25
            scene black with dissolve
            play sound dizzypt2
            play sound child_faint
            pause 1.0
            window hide dissolve
            scene dead with dissolve
            stop music
            play sound gameover
            show screen reload_prompt("你打不过伏拉夫，倒下了！") with dissolve
            pause
            stop sound
            $ quick_menu = True
            jump endgame
        "放屁":
            # this was in 1.0; forgive me
            $ _history_list.pop()
            $ quick_menu = False
            "xxs 使用了 屁！" nointeract
            play sound dizzy
            pause 0.25
            play sound dizzypt2
            pause 0.25
            play voice fulafu_faint fadeout 0.125
            hide fulafu_overworld with squares
            "伏拉夫 晕倒了！"
            play music china2 fadein 2.0
            $ quick_menu = True
        "平底锅":
            $ _history_list.pop()
            $ quick_menu = False
            "xxs 使用了 平底锅！" nointeract
            play sound dizzy
            pause 0.25
            play sound pong
            pause 0.1
            play sound pong
            pause 0.1
            play sound pong
            pause 0.1
            with vpunch
            pause 0.25
            play voice fulafu_faint fadeout 0.125
            hide fulafu_overworld with blinds
            "伏拉夫 被击倒了！"
            play music china2 fadein 2.0
            "胜利！"
            "你的平底锅损毁了。作为补偿，你得到了 10 经验。"
            $ quick_menu = True
        "逃跑":
            $ _history_list.pop()
            $ quick_menu = False
            window hide dissolve
            scene black with dissolve
            play music run
            play sound run
            pause 0.25
            play sound run
            pause 0.25
            play sound run
            pause 0.25
            stop music fadeout 0.125
            stop sound
            play sound child_faint
            pause 1.0
            window hide dissolve
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你跑不过伏拉夫，被他抓走了！") with dissolve
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    show screen spell_showcase("images/key.png", 1.25) with dissolve
    "从 伏拉夫 身上掉落一把 钥匙。"
    "你得到了 钥匙！" nointeract
    pause 1
    window hide dissolve
    hide screen spell_showcase with dissolve
    play sound pong # collect
    play voice haoci
    pause 0.25
    "只剩一把钥匙没有收集到。"
    # FIXME: fix pauses
    menu:
        with dissolve
        "接下来要干什么呢？"
        "继续找钥匙":
            $ _history_list.pop()
            $ quick_menu = False
            scene black with dissolve
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            call story_char_1_pre2_end("最后你找到了最后一把钥匙，\n在伏拉夫靠近之前逃脱了！", "win", audio.win)
        "去挖地道":
            $ _history_list.pop()
            call story_char_1_pre2_end
        "去打猎别的伏拉夫":
            $ _history_list.pop()
            $ quick_menu = False
            "额...我觉得还是-{w=1}{nw}"
            play sound run
            scene bg_sunny_outside with dissolve
            "诶诶诶，锁还没开呢！{p=1.5}{nw}"
            "你这是去干嘛！{p=1.7}{nw}"
            call story_char_1_pre2_end
        "当场去世":
            $ _history_list.pop()
            call story_char_1_pre2_end
    jump endgame
label story_char_1_pre2_end(content="你背叛了你的队友！", scrn="fail", mus=audio.gameover):
    $ quick_menu = False
    window hide dissolve
    stop music
    if scrn == "win":
        scene win with dissolve
    else:
        scene fail with dissolve
    play sound mus
    show screen reload_prompt(content) with dissolve
    pause
    stop sound
    $ quick_menu = True
    return
