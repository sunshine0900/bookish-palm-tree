# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 14:18:41 2025

@author: Dashka
"""
#this function wrote me chat GPT but it totally worth it!
import time
import sys

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def typewriterlong(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

typewriter('Good afternoon, traveler!\n\n'
      'You are in the year 2080, where the cataclysms of our beloved planet clearly signal that you can no longer remain here.\n'
      'Countless lives have been lost, yet the path to salvation had been meticulously developed for many years prior to this disaster.\n')

typewriter('You have been selected as the primary pilot for the Sirius capsule, equipped with enough food and oxygen for a three-year journey.')

yn = int(input('This is a one-way trip—you must understand that.\n\n'
               'Are you ready?\n'
               '1 - Yes\n'
               '2 - No\n'))

if yn == 2:
    typewriter('Unfortunately, due to your refusal to pilot the mission, you remained on Earth.\n\n'
          'A devastating earthquake soon swallowed your city kilometers deep into the ground, and you perished—just like so many others.\n')
    typewriterlong('GAME OVER')
else:
    typewriter('Excellent!! You now have the honor—bestowed by the corporation upon its most trusted individuals—to choose your companion for this challenging expedition. Choose wisely; every decision carries consequences.\n')

    companion = input('== Companion Selection\n'
                      '-- John. Research Engineer. An old-school man with decades of service at the state space agency behind him—responsible, serious, and entrusted with humanity\'s genetic code. He is desperately determined to survive, believing his wife’s genetic code can be revived at your new home.\n\n'
                      '-- Steve. Technology Engineer. A 27-year-old young man who joined the space corporation at age 19. His entire conscious life has been devoted to dreaming of interstellar travel and relocation beyond the Solar System. Also responsible for humanity’s genetic code, Steve is charismatic, optimistic, and always able to lift spirits—even in the darkest moments.\n')

    typewriter('Your choice has been made.\n'
          'Remember:\n'
          'Your mission’s primary goal is to give Earth’s civilization a second chance somewhere beyond our Solar System.\n'
          'The nation’s top bioengineers have developed a genetic code capable of enablinging human rebirth outside the Solar System.\n\n'
          'Meanwhile, astrophysicists have identified several potential destinations—but no one knows for certain what the universe has in store for humanity. You travel as a pair, as planetary resource depletion leaves no room for more.\n'
          'Give humanity a chance to survive.\n\n')
    typewriterlong('Launch in\n'
          '3…\n'
          '2…\n'
          '1…\n\n')
    
    typewriter('During the first hour of your expedition, you remain within the Solar System—but where are you headed?')

    if companion == 'John':
        typewriter('John:\n'
              '-- Hey, kid—so, where are we steering this tub? Any ideas on our destination?\n')

        location = int(input('1. Sagittarius Dwarf Spheroidal Galaxy (70,000 light-years away)\n'
                             '(According to our game’s logic, you’ll arrive in 1.5 years)\n\n'
                             '2. Fornax Dwarf (460,000 light-years away)\n'
                             '(Exactly 3 years—risk of running out of resources before arrival)\n\n'
                             '3. Large Magellanic Cloud (163,000 light-years away)\n'
                             '(You’ll arrive in 2 years)\n'))

        typewriter('Your choice is final.\n\n'
              'John fully trusts your decision. Hopefully, you chose correctly—this was your only chance, and the course can no longer be altered.\n'
              'Or can it?')

        typewriter('You’ve been traveling for a full year now.\n'
              'Darkness surrounds you, broken only occasionally by the distant glimmer of bright stars.\n'
              'As you pass through nebulae, you realize they’re nothing like the colorful telescope images—they’re not vibrant pictures at all, just sparse gas invisible to the naked eye.\n'
              'Only your radar and navigation charts confirm you’re flying through a nebula.\n'
              'Your companion remains enthusiastic.\n\n'
              'And you?')

        mood = int(input('– 1. I genuinely want to find out if we’ll succeed or not. I’m ready to go all the way!\n\n'
                         '– 2. I’m starting to lose faith a bit. What if I chose the wrong destination?\n\n'
                         '– 3. I’m so bored—every day is the same! Nothing changes outside the viewport for days on end. I don’t even know if we’re moving anymore! I’m scared.\n\n'
                         '– 4. I don’t really care—but we’ll see this through to the end.\n'))

        if mood == 1:
            typewriter('Great attitude!! Let’s see what the next day brings.')
        elif mood == 2:
            typewriter('Doubts are normal. Let’s see what the next day brings.')
        elif mood == 3:
            typewriter('You’re on the verge of panic. Maybe talk to John—these thoughts are better faced together, not alone. Let’s see what the next day brings.')
        else:
            typewriter('Chin up! Let’s see what the next day brings.')

        typewriter('The next morning\n'
              'You wake to the sharp, unpleasant beeping of navigation sensors—and something is definitely wrong with the fuel tank.\n'
              'But the first thing you hear are footsteps approaching your bunk.')

        response = int(input('John approaches, speaking in a grave tone:\n'
                             '-- I must warn you—there’s something on the horizon. We’re passing near a cosmic object.\n'
                             '   I’d advise caution and against making any hasty decisions..\n'
                             '   It’s a black hole.\n\n'
                             '*what is your answer?*\n'
                             '-- 1. HOLY SHMOLY!\n'
                             '-- 2. Wait—what about the sensors? Why is everything beeping? Is it because of the black hole?\n'
                             '-- 3. What decisions are you talking about?\n'))

        if response == 1:
            typewriter("--Alright, maybe I wasn’t being emotional enough—but what do we do now?\n"
                  "We’ve got a fuel leak. I fixed it, but we only have enough for one more year.\n"
                  "What’s your call, pilot?")
        elif response == 2:
            typewriter('Yes—the sensors are acting up due to the black hole’s gravity.\n'
                  'And we’ve got a fuel leak. I patched it, but fuel will last only one more year.\n'
                  'What’s our move, pilot?')
        elif response == 3:
            typewriter('You’ve surely heard the theory: black holes might be gateways to wormholes—hypothetical spacetime tunnels connecting distant regions of the universe (or even other universes).\n'
                  'It’s speculative, sure—but we only have fuel for one more year.\n'
                  'What do you think—do we risk it?')

        if location == 1 and response == 1:
            risk = int(input('1. We’ll manage just fine—no need to risk it.\n'
                             '   Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk!\n'
                             '   Change course to the black hole.\n'))
        elif location == 2 and response == 1:
            risk = int(input('1. We won’t make it to Fornax—fuel’s insufficient. But jumping into a black hole is reckless.\n'
                             '   It’s pure speculation. We’ll run out of fuel… but I can’t send us straight into death’s hands.\n\n'
                             '2. We won’t make it to Fornax—fuel’s insufficient.\n'
                             '   I see only one option: we risk it! Humanity must be saved, even if we perish—we tried.\n'))
        elif location == 3 and response == 1:
            risk = int(input('1. We’ll manage just fine—no need to risk it. Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk! Change course to the black hole.\n'))
        elif location == 1 and response == 2:
            risk = int(input('1. We’ll manage just fine—no need to risk it.\n'
                             '   Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk!\n'
                             '   Change course to the black hole.\n'))
        elif location == 2 and response == 2:
            risk = int(input('1. We won’t make it to Fornax—fuel’s insufficient. But jumping into a black hole is reckless.\n'
                             '   It’s pure speculation. We’ll run out of fuel… but I can’t send us straight into death’s hands.\n\n'
                             '2. We won’t make it to Fornax—fuel’s insufficient.\n'
                             '   I see only one option: we risk it! Humanity must be saved, even if we perish—we tried.\n'))
        elif location == 3 and response == 2:
            risk = int(input('1. We’ll manage just fine—no need to risk it. Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk! Change course to the black hole.\n'))
        elif location == 1 and response == 3:
            risk = int(input('1. We’ll manage just fine—no need to risk it.\n'
                             '   Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk!\n'
                             '   Change course to the black hole.\n'))
        elif location == 2 and response == 3:
            risk = int(input('1. We won’t make it to Fornax—fuel’s insufficient. But jumping into a black hole is reckless.\n'
                             '   It’s pure speculation. We’ll run out of fuel… but I can’t send us straight into death’s hands.\n\n'
                             '2. We won’t make it to Fornax—fuel’s insufficient.\n'
                             '   I see only one option: we risk it! Humanity must be saved, even if we perish—we tried.\n'))
        elif location == 3 and response == 3:
            risk = int(input('1. We’ll manage just fine—no need to risk it. Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk! Change course to the black hole.\n'))
    if companion == 'Steve':
        typewriter('Steve:\n'
              '-- Well? How are you holding up? Feeling nervous? I sure am!)\n'
              'But alright, alright—let’s finally decide where our Sirius is going. Got any thoughts?\n')

        location = int(input('1. Sagittarius Dwarf Spheroidal Galaxy (70,000 light-years away)\n'
                             '(According to our game’s logic, you’ll arrive in 1.5 years)\n\n'
                             '2. Fornax Dwarf (460,000 light-years away)\n'
                             '(Exactly 3 years—risk of running out of resources before arrival)\n\n'
                             '3. Large Magellanic Cloud (163,000 light-years away)\n'
                             '(You’ll arrive in 2 years)\n'))

        typewriter('Your choice is final.\n\n'
              'Steve fully trusts your decision. Hopefully, you chose correctly—this was your only chance, and the course can no longer be altered.\n'
              'Or can it?')

        typewriter('You’ve been traveling for a full year now.\n'
              'Darkness surrounds you, broken only occasionally by the distant glimmer of bright stars.\n'
              'As you pass through nebulae, you realize they’re nothing like the colorful telescope images—they’re not vibrant pictures at all, just sparse gas invisible to the naked eye.\n'
              'Only your radar and navigation charts confirm you’re flying through a nebula.\n'
              'Your companion remains enthusiastic.\n\n'
              'And you?')

        mood = int(input('– 1. I genuinely want to find out if we’ll succeed or not. I’m ready to go all the way!\n\n'
                         '– 2. I’m starting to lose faith a bit. What if I chose the wrong destination?\n\n'
                         '– 3. I’m so bored—every day is the same! Nothing changes outside the viewport for days on end. I don’t even know if we’re moving anymore! I’m scared.\n\n'
                         '– 4. I don’t really care—but we’ll see this through to the end.\n'))

        if mood == 1:
            typewriter('Great attitude!! Let’s see what the next day brings.')
        elif mood == 2:
            typewriter('Doubts are normal. Let’s see what the next day brings.')
        elif mood == 3:
            typewriter('You’re on the verge of panic. Maybe talk to John—these thoughts are better faced together, not alone. Let’s see what the next day brings.')
        else:
            typewriter('Chin up! Let’s see what the next day brings.')

        typewriter('The next morning\n'
              'You wake to the sharp, unpleasant beeping of navigation sensors—and something is definitely wrong with the fuel tank.\n'
              'But the first thing you hear are footsteps approaching your bunk.')

        response = int(input('Steve rushes over, visibly shaken and still unable to believe his eyes:\n'
                             '-- Look at the map!! There’s a massive spatial disturbance!!\n'
                             'It’s a black hole! Not as huge as the one at our galaxy’s center—just a tiny one—but don’t you get it?\n'
                             'We finally have a chance to test those wormhole theories!\n'
                             'This could be our breakthrough!! Let’s move closer!\n\n'
                             '*what is your answer?*\n'
                             '-- 1. Wait—what about the sensors? Why is everything beeping? Is it because of the black hole?\n'
                             '-- 2. Whoa, whoa—slow down! Too many words. What “travel” are you talking about?\n'
                             '-- 3. No, no, no!! Absolutely not! Are you out of your mind? We’ll get spaghettified! Stick to our original course!\n'))

        if response == 1:
            typewriter('--Oh, right—yeah, we’ve got minor issues.\n'
                  'Navigation sensors are glitching, probably due to the black hole’s influence.\n'
                  'And we’ve got a fuel tank leak—I’m afraid we only have enough fuel for one more year.\n'
                  'The black hole might be our solution!')
        elif response == 2:
            typewriter('--Well, you know—black holes could theoretically be entrances to wormholes:\n'
                  'hypothetical \'tunnels\' through spacetime connecting distant points in the universe (or even different universes).')
        elif response == 3:
            typewriter('--Fine… but at least take a quick look. You might never see something like this again in your lifetime…')

        if location == 1 and response == 1:
            risk = int(input('1. We’ll make it—we’ve only got six months left\n'
                             '   The black hole idea seems too uncertain…\n\n'
                             '2. We’ll make it—we’ve only got six months left.\n'
                             '   But honestly… the black hole idea is tempting\n'))
        elif location == 2 and response == 1:
            risk = int(input('1. We won’t make it to Fornax—fuel’s insufficient. But jumping into a black hole is reckless.\n'
                             '   It’s pure speculation. We’ll run out of fuel… but I can’t send us straight into death’s hands.\n\n'
                             '2. We won’t make it to Fornax—fuel’s insufficient.\n'
                             '   I see only one option: we risk it! Humanity must be saved, even if we perish—we tried.\n'))
        elif location == 3 and response == 1:
            risk = int(input('1. We’ll manage just fine—no need to risk it. Travel via black hole is purely hypothetical.\n\n'
                             '2. We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk! Change course to the black hole.\n'))
        elif location == 1 and response == 2:
            risk = int(input('1. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns! Still… we’ve got a fuel problem.\n'
                             '   We might not reach our destination. The black hole scares me with its uncertainty.\n'
                             '   Let’s stick to our course."\n\n'
                             '2. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns! Still… we’ve got a fuel problem.\n'
                             '   We might not reach our destination. Let’s take the risk!\n'
                             '   We weren’t chosen by accident—we’re making human history, and this might be our only chance to survive."\n'))
        elif location == 2 and response == 2:
            risk = int(input('1. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns! Still… we’ve got a fuel problem.\n'
                             '   We won’t make it to Fornax—fuel’s insufficient. But jumping into a black hole is reckless.\n'
                             '   We’ll run out of fuel… but I can’t send us straight into death’s hands.\n\n'
                             '2. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns! Still… we’ve got a fuel problem.\n'
                             '   We might not reach our destination. Let’s take the risk!\n'
                             '   We weren’t chosen by accident—we’re making human history, and this might be our only chance to survive."\n'))
        elif location == 3 and response == 2:
            risk = int(input('1.1. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns!\n'
                             '   We’ll manage just fine—no need to risk it. Travel via black hole is purely hypothetical.\n\n'
                             '2. I’ve heard about that!\n'
                             '   But it’s all just hypotheses and guesses—too many unknowns!\n'
                             '   We’ll manage—fuel’s sufficient—but a black hole wasn’t on our course.\n'
                             '   Maybe this is a sign? Nothing happens by accident.\n'
                             '   Let’s take the risk! Change course to the black hole.\n'))
        elif location == 1 and response == 3:
            risk = 1
        elif location == 2 and response == 3:
            risk = 1
        elif location == 3 and response == 3:
            risk = 1
        
        #RISK / NO RISK
        if risk == 2:
            typewriter('The decision is made. Course altered—Sirius now heads straight into the black hole’s grasp. You’re both terrified yet exhilarated. A single moment passes.')
            typewriter('Scientists back on Earth would’ve certainly won a Nobel Prize—not just for mathematical proof, but for demonstrating that such travel is possible.\n'
                  'Congratulations! You’re alive! But… where are you?\n'
                  'Radar unresponsive. All sensors malfunctioning. Darkness everywhere. Are you in a new galaxy? A new universe? You argue endlessly about your location—but outside, nothing changes. Just darkness. Emptiness.\n'
                  'One month passes. Nothing.\n'
                  'Two… three…\n'
                  'A full year. Despair sets in. Fuel is gone.\n'
                  'Unfortunately… this is your end. A price paid for chasing the unknown.')
            typewriterlong('GAME OVER')

        elif risk == 1:
            typewriter('The black hole fades behind you—but unease lingers. Questions haunt you: What if? Is it possible? What’s it like? Yet your mission isn’t to test theories—it’s to save humanity.')
            
            if location == 1:
                typewriter('Your chosen course proves perfect. On the horizon appears one of the planetary systems identified by scientists.\n'
                      'You decide to land on a world that eerily resembles Earth as it was 50 years ago! You can hardly believe your eyes!\n'
                      'Exhausted but awestruck, you see floating rocks hovering above the surface, and everything bathed in an ethereal blue hue (blue—not green—which strikes you as wondrous).\n'
                      'In that moment, you know: this is it. What you’ve been searching for.\n'
                      'Mission: Human resettlement in the Sagittarius Dwarf Spheroidal Galaxy, in the Blue-Eyed Planet system—SUCCESSFUL.\n'
                      'Congratulations!')
            
            elif location == 3: 
                typewriter('Your chosen course proves perfect. On the horizon appears one of the planetary systems identified by scientists.\n'
                      'You decide to land on a world that eerily resembles Earth as it was 50 years ago! You can hardly believe your eyes!\n'
                      'Exhausted but awestruck, you see floating rocks hovering above the surface, and everything bathed in an ethereal blue hue (blue—not green—which strikes you as wondrous).\n'
                      'In that moment, you know: this is it. What you’ve been searching for.\n'
                      'Mission: Human resettlement in the Large Magellanic Cloud, in the Blue-Eyed Planet system—SUCCESSFUL.\n'
                      'Congratulations!')
            
            elif location == 2:
                typewriter('Your original course may have been promising—but the black hole encounter threw you off track.\n'
                      'Your ship drifted, powerless, lost in the void of Nowhere.\n'
                      'You never arrived.\n'
                      'Mission FAILED')
                typewriterlong('GAME OVER')

        else:
            typewriter("Invalid choice. The ship drifts aimlessly...")
            typewriterlong("GAME OVER")
            
        
            
        