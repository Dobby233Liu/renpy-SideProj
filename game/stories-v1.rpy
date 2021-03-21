image game_menu_ow = "gui/overlay/game_menu.png"
label story_fulafu_simulator:
    if persistent.introduced_sim_character_fulafu:
        jump flfsim_choose_type
    scene game_menu_ow with dissolve
    show fulafu_overworld with dissolve
    "你是伏拉夫，抖音上的一个俄罗斯博主。"
    "你以前四处苦苦代言红酒、开包子店等等，可是却一直没有生意。"
    if not persistent.bad_fund:
        $ persistent.bad_fund = renpy.random.choice(["做起了吃播", "恰烂钱"])
    $ bad_fund = persistent.bad_fund # have fulafu remember his passion (for boredom)
    $ zzz = "去了火锅气味" if bad_fund == "恰烂钱" else "吃了火锅"
    $ r = "突然想到了一条财富之路" if bad_fund == "恰烂钱" else "感觉很好吃"
    "但是自从加入了抖音，并在某个火锅店［zzz]之后，[r]，就开始[bad_fund]了。"
    $ ugh = "天上还真会掉馅饼" if bad_fund == "恰烂钱" else "这里的火锅还挺好吃的"
    "中国各个方面都很好，而且[ugh]，使你爱起中国，入了中国国籍。"
    # be aware about some strange glitch that changes the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:21] + ">audio/c2g.ogg"
        hide fulafu_overworld
        show fulafu_overworld_jumpscare
        "现在每几天都去各种小孩家里拿“火锅底料”。{p=1.0}{nw}"
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide fulafu_overworld_jumpscare
        #show fulafu_overworld
label flfsim_choose_type:
    scene bg_sunny_outside with dissolve
    show fulafu_overworld with dissolve
    "这天，你又想拍一个作品上传到抖音和西瓜视频。"
    hide fulafu_overworld with dissolve
    $ persistent.introduced_sim_character_fulafu = True
#label flfsim_choose_type:
    #if persistent.introduced_sim_character_fulafu:
    #    scene bg_sunny_outside with dissolve
    menu:
        with dissolve
        "那么，要拍什么类型的作品呢？"
        "狂舔中国":
            pass
        "回归老本行，推销红酒":
            scene black with dissolve
            "...{p=1.0}{nw}"
            scene fix_house with dissolve
            
            "然后，你就被喷子们喷了一顿。"
            scene black with pixelate
            $ this_is = renpy.random.choice(["这里是", "我是", "我素", "这是", ""])
            $ postfix = renpy.random.choice(["★_", "★", "_", "_★", "★_★", ""])
            $ feed = renpy.random.choice([" 不要投喂", "，不要投喂！", ""])
            $ inm_ref = renpy.random.choice(["CoCo", "coco", "Coco", "COCO", "CO2", "kekker", ""])
            "[this_is]可可[inm_ref][postfix]" "文明观猴[feed]"
            $ blackened = renpy.random.choice(["丶", "丶（已黑化）", "（已黑化）", ""])
            "细雨的温柔[blackened]" "这不是我们中国的知名猴戏🐒"
            $ pls_no = renpy.random.choice(["烂钱是不可能不恰的，只能越恰花样越多，，，", "我爱中国的Q", "你以为我不知道你又要恰烂钱？", "他居然学会加密取款了！11", "帐号正确，但是密码永远不会对"])
            "用户1145141919" "[pls_no]"
            $ recall_methodlogy = "骗人的把戏"
            $ oneninethreefour = "1934"
            if persistent.bad_fund == "恰烂钱":
                $ recall_methodlogy = renpy.random.choice(["恰烂钱", "赚钱"]) + "的手法"
                $ oneninethreefour = "2016"
            $ fake_user_pfx = renpy.random.choice(["火山", "西瓜", "头条", ""])
            "[fake_user_pfx]用户810234[oneninethreefour]" "这[recall_methodlogy]，智力没有问题的都看得出来吧"
            if bad_fund == "恰烂钱":
                scene fix_house with pixelate
                jump start_the_buyaolian
            stop music fadeout 1.0
            with vshake
            pause 1.0
            with vshake
            pause 1.0
            "想好好再做一次真正的生意，却仍然被人矛头相对..."
            "..."
            "......" nointeract
            $ renpy.pause(0.25, interact=False)
            pause
            ".........{w=0.25}这真的是让人想叹气连连啊..."
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("你伤心地退抖了...")
            pause
            stop sound fadeout 1.0
            scene black with dissolve
            window show dissolve
            "你早就给人留下了不好的印象了..."
            "再想怎样挽救，也已经无济于事了..."
            $ quick_menu = True
            jump endgame
    "你录了一段作品。"
    "现在，只要睡个午觉..."
    scene black with dissolve
    "...{p=1.0}{nw}"
    scene fix_house with dissolve
    "就可以看到喷子们在评论区云观猴了。"
    "(此处省略1w+的观猴评论。)"
    label start_the_buyaolian:
    menu:
        with dissolve
        "你要怎么对付这些喷子呢？"
        "问候他们的父母":
            stop music
            $ quick_menu = False
            scene black with dissolve
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("喷了他们没多久，你就被封号了！")
            pause
        "提醒他们网络不是法外之地":
            scene black with dissolve
            "于是，你又拍了一个作品来提醒他们，你还把它置顶了。"
            "后来，你逐渐过气，最后就此消失了..."
            stop music
            $ quick_menu = False
            window hide dissolve
            #window hide dissolve
            #scene fail with dissolve
            #play sound gameover
    stop sound fadeout 1.0
    pause 1.0
    scene black with dissolve
    window show dissolve
    "记住，真正给你流量的，不是金主，不是你所谓的千万粉丝，也不是神。"
    "而是你实际上寥寥无几的真粉，还有那些喷子们。"
    "没有了这些，你又是个什么东西呢..."
    window hide dissolve
    $ quick_menu = True
    jump endgame

# ~~~

label story_char_1_pre2:
    window hide dissolve
    $ quick_menu = False
    # editme: whatthefuck is this
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
    pause 0.5
    window hide dissolve
    hide screen spell_showcase with dissolve
    play voice pong # collect
    play voice haoci
    pause 0.125
    "还剩两把钥匙没有收集。"
    window hide
    stop music fadeout 0.25
    play music poke_mus_battle27
    show black at blink
    pause 2.5
    hide black
    # be aware about some strange glitch that change the music
    if renpy.random.randint(0,3) == 1:
        # "glitch out"
        play music c2g
        show fulafu_overworld_jumpscare
        pause 0.5
        hide fulafu_overworld_jumpscare
        show fulafu_overworld
    else:
        show fulafu_overworld with blinds
    with vpunch
    play voice fulafu_cry
    pause 0.25
    window show
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
            hide fulafu_overworld with squares
            play music china2 fadein 2.0
            "xxs 胜利了！"
            "你的平底锅损毁了。作为补偿，你得到了 10 经验。"
            $ quick_menu = True
    show screen spell_showcase("images/key.png", 1.25) with dissolve
    "从 伏拉夫 身上掉落一把 钥匙。"
    "你得到了 钥匙！" nointeract
    pause 0.5
    window hide dissolve
    hide screen spell_showcase with dissolve
    play sound pong # collect
    play voice haoci
    pause 0.125
    "只剩一把钥匙没有收集。"
    menu:
        with dissolve
        "接下来要..."
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
            call story_char_1_pre2_end("之后你找到了最后一把钥匙！", "win", audio.win)
        "去挖地道":
            $ _history_list.pop()
            $ quick_menu = False
            scene black with dissolve
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            call story_char_1_pre2_end
        "去打猎别的伏拉夫":
            $ _history_list.pop()
            $ quick_menu = False
            "额...我觉得还是-{w=0.25}{nw}"
            play sound run
            scene bg_sunny_outside with dissolve
            "诶诶诶，锁还没开呢！{p=0.5}{nw}"
            "你这是去干嘛！{p=0.8}{nw}"
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
