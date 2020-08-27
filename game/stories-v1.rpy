label story_fulafu_simulator:
    scene bg_sunny_outside with dissolve
    if persistent.introduced_sim_character_fulafu:
        jump flfsim_choose_type
    show fulafu_overworld with dissolve
    "你是伏拉夫，抖音上的一个俄罗斯博主。"
    "你以前在优酷和线下代言红酒、开包子店等等。"
    if not persistent.bad_fund:
        $ persistent.bad_fund = renpy.random.choose("做起了吃播", "恰烂钱")
    $ bad_fund = persistent.bad_fund # have fulafu remember his passion (for boredom)
    "但是自从加入了抖音，并在某个火锅店吃了火锅并去了火锅气味之后，你开始[bad_fund]。"
    "中国的火锅如此好吃，中国的技术如此好，使你爱起中国，现在又变成了一名正式的中国人。"
    # be aware about some strange glitch that change the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:21] + ">audio/c2g.ogg"
        hide fulafu_overworld
        show fulafu_overworld_jumpscare
        "甚至每天都去中国小孩的家拿“火锅底料”。{p=1.0}{nw}"
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide fulafu_overworld_jumpscare
        show fulafu_overworld
    "这一天，你一时兴起，想拍一个作品上传到抖音和西瓜视频。"
    hide fulafu_overworld with dissolve
    $ persistent.introduced_sim_character_fulafu = True
label flfsim_choose_type:
    menu:
        with dissolve
        "那么，要拍什么类型的作品呢？"
        "我们中国的厉害之处":
            pass
        "与红酒的日常生活":
            scene black with dissolve
            "...{p=1.0}{nw}"
            "之后，你被喷子们喷了一顿。"
            $ this_is = renpy.random.choose("这里是", "我是", "我素", "这是", "")
            $ postfix = renpy.random.choose("★_", "★", "_", "_★", "★_★", "")
            $ feed = renpy.random.choose(" 不要投喂", "，不要投喂！", "")
            $ inm_ref = renpy.random.choose("CoCo", "coco", "Coco", "COCO", "CO2", "kekker", "")
            "[this_is]可可[inm_ref][postfix]" "文明观猴[feed]"
            $ blackened = renpy.random.choose("丶", "丶（已黑化）", "（已黑化）", "")
            "微雨的温柔[blackened]" "这不是我们中国的知名猴戏🐒"
            $ pls_no = renpy.random.choose("你是藏不住你取款的意图的1111", "我爱中国的Q", "你以为我们大家不知道你又要恰烂钱？", "我们的常客这次加密拿钱了！11", "帐号正确，密码错误")
            "用户1145141919" "[pls_no]"
            $ recall_methodlogy = "骗人的把戏"
            $ oneninethreefour = "1934"
            if persistent.bad_fund == "恰烂钱":
                $ recall_methodlogy = renpy.random.choose("恰烂钱", "赚钱") + "的手法"
                $ oneninethreefour = "2016"
            $ fake_user_pfx = renpy.random.choose("火山", "西瓜", "头条", "")
            "[fake_user_pfx]用户810234[oneninethreefour]" "这[recall_methodlogy]，是个人都看得出来吧"
            "于是，你伤心地退抖了..."
            stop music
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    "你录了一段作品，并且发出去了。"
    "现在，我们只需要睡个午觉..."
    scene black with dissolve
    "...{p=1.0}{nw}"
    scene fix_house with dissolve
    "然后就可以看到喷子们在云观猴了。"
    menu:
        with dissolve
        "你要怎么对付喷子呢？"
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
            stop sound
            $ quick_menu = True
        "提醒他们网络不是法外之地":
            scene black with dissolve
            "于是，你又拍了一个作品，把它发出去了。你还把它置顶了。"
            "后来，你逐渐退气，最后只能安静地隐退..."
            stop music
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            pause
            stop sound
            $ quick_menu = True
    jump endgame

# ~~~

label story_char_1_pre2:
    window hide dissolve
    $ quick_menu = False
    show screen race_prepare("伏拉夫\n会飞的猪\n{i}sysmsg{/i}\n{i}还有两个...{/i}", "小孩\nxxs\n抖音小雨\n可可里加巧克力") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene kitchen with dissolve
    show screen spell_showcase("images/pan.png", 1.5, 0.25) with dissolve
    "你开局就在厨房，厨房里有个平底锅，它旁边有一张说明书。" with dissolve
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
            show screen reload_prompt("你因为太手残，不小心打死了自己！") with dissolve
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
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:21] + ">audio/c2g.ogg"
        show fulafu_overworld_jumpscare
        pause 0.5
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
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
            play sound gameover
            show screen reload_prompt("你打不过伏拉夫，“昏倒”了！") with dissolve
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
            play sound pong
            play sound pong
            with vpunch
            pause 0.25
            play voice fulafu_faint fadeout 0.125
            hide fulafu_overworld with squares
            play music china2 fadein 2.0
            "xxs 胜利了！"
            "你的平底锅被销毁，同时你得到了 10 经验的补偿。"
    show screen spell_showcase("images/key.png", 1.25) with dissolve
    "从 伏拉夫 身上掉落一把 钥匙。"
    "你找到了 钥匙！" nointeract
    pause 0.5
    window hide dissolve
    hide screen spell_showcase with dissolve
    play voice pong # collect
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
            call story_char_1_pre2_end("之后，你找到了最后一把钥匙！", "win", "win")
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
            scene black with dissolve
            "额...我觉得...{w=0.25}{nw}"
            play sound run
            "诶诶诶，锁还没开呢！{p=0.5}{nw}"
            "你这是去干嘛！{p=0.8}{nw}"
            call story_char_1_pre2_end
        "当场去世":
            $ _history_list.pop()
            call story_char_1_pre2_end
    jump endgame
label story_char_1_pre2_end(content="你背叛了其他的队员！", scrn="fail", mus="gameover"):
    window hide dissolve
    stop music
    scene fail with dissolve
    play sound gameover
    show screen reload_prompt(content) with dissolve
    pause
    stop sound
    $ quick_menu = True
    return
