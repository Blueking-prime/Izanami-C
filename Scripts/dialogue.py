from Models.utils import dialog_choice
from Models import checks
from Models.Characters.Players.base_player import Base_Player
from Models.Characters.Enemies import enemy_models
from battle import battle


def tutorial():
    print('[TUTORIAL]')
    input("Hit ENTER to go to next line")

    test_choices = ["Hit 1 for me", "Type 2 for me", "Press 3 for me"]
    ans = dialog_choice("When given a choice, input the number of the option you wish to select. Example:", test_choices)

    if ans in range(1, 4):
        print("Very Good!")

    print("[TUTORIAL FINISHED]")


def fall(player: Base_Player):
    input("Before you, lies a massive hole. It seemed to stretch downwards infinitely. The flakes of snow that fall within only seen to disappear into the unflinching darkness.")
    input("The beautiful and deathly winter sprits dance around the fringes of this unend vortex, callously baiting all adventurers who dare come close to enter.")
    input("This is the Shonyudo no Hitomi. The gate to Hell and the Unnamed Katana.")
    input("You step beyond the boundary; and you fall. You seep into untenable nothingness till darkness covers you like a cloak, even the light from the snowfield above you is muffled until barely a pinpoint shimmer can be seen. And yet you continue to sink.")
    input("You notice this fact explicitly, that you are not falling. You are sinking, the darkness around you is brushing on your skin and you are sinking as though a great weight anchored you down. As though you fell into an ocean of black and the pressure is crushing you from all directions.")
    input("Deeper and deeper, and yet deeper still. Until depth had lost all meaning. Then you saw it, in brilliant red, the first light you had seen in unknowable time, the world around you blasts into a cacophony of colours so strong that you shield your eyes.")
    input("The ground below erupted into geysers of purple and pink, crystalline obelisks dotted the horizon as far as you could see, and the sky's firmament is filled with the howls and calls of myriad creatures who violently stream across her. Demons. This is your destination. This is Yomi.")
    input("But before you take in the splendor of this new world, a significantly more pressing matter comes to the forefront of your mind. How you're planning on sticking this landing.")

    if player.stats['AGI'] > 10:
        input("You land, more or less, safely. At the very least alive. Your legs shake and wobble from the test it was just put through, and you only barely keep your balance, the ground twisting beneath you")
    else:
        input("You slam into the ground at full speed. Fortunately the earth beneath you was malleable, but it still left a mark.")

    input("You turn your gaze upwards, taking an immediate survey of where you are. From the sky it looked like nothing but red earth was beneath you, but now in place of spires and trees, an entire town stood.")
    input("Humans? Not as far as you could tell. Close enough? You manage to notice things with red skin and more limbs and teeth than they should have among them, but the vast majority looked terribly… normal? Undeniably demons, but normal.")
    input("You turn around and a woman looks down at you, she stands easily four heads above you and scowled downwards with nothing but repulsion. On the right side of her forehead was a large ebon horn and on the left side was a deep gnarled scar that ate across half her face. The atmosphere was oppressive. In her right hand, was a small book and in her left a thin crooked stick dipped in some dark fluid")


def white():
    print("{Talk is cheap, but I will hear you out for now}")
    while True:
        topic = dialog_choice('', checks.white_active_list, back=False)
        match topic:
            case 1:
                input("WHITE: I'm merely a shadow of a time past. My Identity is of no meaning.")
                continue
            case 2:
                input("WHITE: A weak man hiding behind a dead ideal. He'd rather his lackeys do his dirty work than ever sully his hands. If I were you I'd be wary of his machinations.")
                continue
            case 3:
                input("WHITE: A uniquely ambitious demon. I can see the zeal in her eyes, she seeks something far greater than most of her kin, and she intends to use you to obtain it.")
                continue
            case 4:
                input("[he laughs out loud]")
                input("WHITE: Daimaou Kagutsuchi. An unbelievably powerful demon.")
                input("WHITE: It's said in his final clash, so loud were his roars and so heavy were his swings that volcanoes began to cry in anguish overhead. Such stupendous power, brought down by holy judgement.")
                continue
            case 5:
                input("WHITE: Minamoto no Raiko was given a divine mandate, and tasked with the destruction of the leader of the demon realm.")
                continue
            case 6:
                input("WHITE: A tombstone almost, a pure fragment of the goddess used by her partner to seal her corpse at the very bottom of hell. Who knows what taking it would do.")
                input("WHITE: Of course, a warrior like yourself is beyond such technicalities.")
                continue
            case 7:
                break


def minamoto(player: Base_Player):
    input("The cold darkness ensnares you. Your body falls still and numbness overtakes you.")
    input("You can feel it, your very soul being washed away by the churning tides of time.")
    input("But deep in the back of your mind's eye, you see something. An impossibly bright light.")
    input("So incandescent that merely observing it seems to blow back the darkness out of reach.")

    choice = dialog_choice('', ["Reach Out" "Give Up"], back=False)
    match choice:
        case 1:
            input("As you reach closer and closer into the light, a figure manifests.")
            input("???: Ah, you can see me, can you.")
            input("???: It has been a long time since I've seen a soul so pathetically cling onto life.")
            input("???: Tell me, what exactly is awaiting you in the land of the living. To what purpose do you grasp so desperately at the threads of your fate?")
            input("???: Do you want to fight?")
            input("???: Do you want to win?")
            input("???: Or do you just want to live…")
        case 2:
            player.die()
            return

    choice = dialog_choice('', ["I want to Fight!", "I want to Win!", "I want to Live!"], back=False)
    match choice:
        case 1:
            input("???: ...")
            input("???: Just fighting for its own sake is meaningless.")
            input("???: Tell me, how are you different from the demons that tore your stomach open and strew your intestines about. The warmongers who burn and pillage in the name of lord and country.")
            input("???: A thug at best, your soul is worthless. Goodbye.")
            player.die()
        case 2:
            input("[the light erupts around you, so brightly that you feel you might go blind.]")
            input("???: [A booming laughter circles around you from every direction. The freezing darkness you once felt was now replaced by an almost unbearable painful heat.]")
            input("???: You're precisely correct! Winning is the only possible outcome, isn't it!")
            input("???: I can see within you, your soul burns with an unquenchable flame.")
            input("???: Continue to struggle!")
            input("???: Continue to fight!")
            input("???: Continue to attain strength!  Until none can bear to stand before you, until you are unparalleled.")
            input("???: You may call me 'White'")
            input("White: You have my permission to rise once again.")

            checks.dialogue_checks['endWhiteCheck'] = True
            checks.crowley_active_list += ["I met a person name White"]
            checks.talk_arr += ["White"]
        case 3:
            input("???: ...")
            input("???: Mere survival is the purpose of the most base of creatures.")
            input("???: Tell me, how are you different from a wild beast on the hunt for its next meal, who turns tail at the sight of the hunter.")
            input("???: Your soul is like that of a mealworm, the belly of the demon world suits you. Begone.")
            player.die()


def crowley():
    if checks.dungeon_level > 1 and checks.dialogue_checks['dungLevelCrowleycheck'] == 0:
            checks.dialogue_checks['dungLevelCrowleycheck']=1
            checks.crowley_active_list +=("I’ve cleared the first level of the dungeon")
    if checks.dungeon_level > 3 and checks.dialogue_checks['dungLevelCrowleycheck'] == 1:
            checks.dialogue_checks['dungLevelCrowleycheck']=2
            checks.crowley_active_list +=("I’ve cleared the third floor")
    if checks.dungeon_level > 4 and checks.dialogue_checks['dungLevelCrowleycheck'] == 2:
            checks.dialogue_checks['dungLevelCrowleycheck']=3
            checks.crowley_active_list +=("I’ve cleared the fourth floor")

    while True:
        response = dialog_choice("{May I be of assistance?}", checks.crowley_active_list, back=False)
        match response:
            case 1:
                input("Crowley: Why yes of course you were.")
                input("Crowley: Every sorry lord or lost champion tumbles down this hole in search of the <power to rule the world below and above>")
                input("Crowley: But do you even know what the blade is? What it can do?")
                continue
            case 2:
                input("Crowley: [he leers at you analytically, then makes a flippant hand gesture] Get to the second floor of the dungeon, then I’ll talk to you.")
                continue
            case 3:
                input("Crowley: We sell demons and we sell Magic Element, my child. If you need fuel for your magic, or you need to cut something down to size, I’m the man to meet.")
                continue
            case 4:
                input("Crowley: Hmmm? Oh I have a charm against the poisons of the demonic world. I wouldn’t dare breath the filth of these creatures")
                continue
            case 5:
                input("Crowley: If they hit you, hit them back.")
                input("Crowley: Don’t run out of stamina.")
                input("Crowley: If the enemy looks like it’s about to swing something nasty, defend yourself. The rest you’ll learn on the field.")
                input("Crowley: Ah, and if you run into the Great Devourer out there run like your life depends on it.")
                continue
            case 6:
                input("Crowley: Hmm. You came back from the brink of death? Are you sure you weren’t hallucinating from pain?")
                input("Crowley: A person named White? Pure light? Doesn’t sound like any demonic phenotypes I know. This is purely conjecture but it’s likely what you met was a Phantom.")
                input("Crowley: An apparition that is born when a particularly stubborn soul clings onto nearby Seithr.")
                input("Crowley: It’s said only those on the brink of death have the ability to even see one, so perhaps there is merit to your story. [he laughs a bit]")
                input("Crowley: Keep me updated on this ‘White’ if you can.")
                continue
            case 7:
                input("Crowley: Ahh. Daimaou Kagutsuchi.")
                input("Crowley: A ruthless, terrible demon. His reign knew no bound and he burned all that he found unsightly.")
                input("Crowley: Yet the savage demons absolutely adored him. He and his most powerful kin would make their way to the human world and wage war on the shogunate.")
                input("Crowley: His presence was always marked with dark skies and liquid fire, and all land he passed over was blackened for 10 generations.")
                input("Crowley: It is said he was eventually felled by Lord Minamoto-no-Raiko.")
                continue
            case 8:
                input("Crowley: I’m impressed. Sure, I’ll tell you. The goddess slumbers deep within the earth, and the blade sleeps even deeper within her undying corpse. You must crawl and fight to the lowest level to obtain it.")
                input("Crowley: Many have come before you and many have fallen. But I see a glint in your eye. See, some benefactors and I have strong vested interest in that blade, and we’re looking for associates to help us attain it. Get through the next two layers and come back to me.")
                input("Crowley: I'm sure that mangy grimalkin has told you a lot as well. Do what you wish but be wary of vesting trust in a demon.")
                if not checks.dialogue_checks['kobaguidecheck']:
                    checks.kobaneko_active_list += ["Crowley gave me some guidance."]
                    checks.dialogue_checks['kobaguidecheck'] = True
                continue
            case 9:
                input("Crowley: You show unprecedented promise, my child. I think we are of a kind.")
                input("Crowley: You are privy to the existence of the Society of the Deep Blue, I’m sure? You may know us as librarians. Keepers of the occult and esoteric. In some sense that is our task in modernity. But this is merely a holdover from our true task for the past 500 years.")
                input("Crowley: Even as states and bloodlines dissolved, and power shifted from one to another. We remained the same, our irrefutable duty never changed. To protect mankind from the torment of demonkind.")
                input("Crowley: As fellow humans, we share the same goals, and I continue to pray earnestly for your wellbeing. Like I mentioned, I wantyou to help us achieve our goals, don’t worry about the details for now. Just focus on getting through the next floor safely. It is guarded by an incredibly powerful demon from the last era. Take this charm and stay safe.")
                continue
            case 10:
                input("Crowley: You are simply incredible, my child. I haven’t seen this much potential since Lord Minamoto. I must have mentioned this to you already, but there used to be a King. A King of Hell. Daimaou, the demons called it. A Demon Lord.")
                input("Crowley: Its will was absolute and even the most cantankerous and bloodthirsty among them would grovel beneath it. It was not a king by nature of its birth mind you, nor by common vote. [he chuckles mildly, as if to imply it was a laughable concept]. No, it ruled with sheer force. Only by its inarguable might did other demons bow.")
                input("Crowley: So there then begs the question, could it mean that in all the infinite millenia that demons have crawled and struggled and consumed and lied and fought for power, that this creature was their ultimate evolution? That there could exist none other, that no demon was ever successful in having its head? Of course not.")
                input("Crowley: As it is in the nature of those beasts to struggle and grow ever more, eventually something emerges from the pits of hell so powerful that the dynamic is upset. These two impossible forces clash, and thus would demons spill forth from every chasm and every unholy place, bringing death and disease, chaos and famine.")
                input("Crowley: In the end, when the dust settles and the corpses return to the earth, a new Daimaou sits atop its throne. Of course this must all sound outlandish to you, but these were the times our forefathers survived in. You may take pride in your strength, but against an unrelenting flood of demons mankind could do nothing but cower and hide.")
                input("Crowley: Our research indicates that through the unnamed sword's power to manipulate seithr, it as well has the power to absolutely control the hearts of demons, given that the proper ritual is performed.")
                input("Crowley: With this in our grasp, the entirety of the demon realm will become but a stepping stone for mankind's future. Our future.")
                input("Crowley: Come, we must arrive at the last floor without delay. I fear external actors are acting against us.")
                checks.dialogue_checks['endCrowCheck'] = True
                continue
            case 11:
                break


def kobaneko():
    if checks.dialogue_checks['kobanBreak']:
        input("Kobaneko: You and I have nothing to discuss. Leave.")
    if checks.dungeon_level > 1 and checks.dialogue_checks['dungLevelKobancheck'] == 0:
        checks.dialogue_checks['dungLevelKobancheck'] = 1
        checks.kobaneko_active_list += ["I’ve been to the dungeon"]
    if checks.dungeon_level > 3 and checks.dialogue_checks['dungLevelKobancheck'] == 1:
        checks.dialogue_checks['dungLevelKobancheck'] = 2
    if checks.dialogue_checks['kobanBreak']:
        input("Kobaneko: We have nothing else to discuss. Leave.")
    while True:
        response = dialog_choice("{How can nya help you~}", checks.kobaneko_active_list, back=False)
        match response:
            case 1:
                input("Kobaneko: [she leans in awfully close] You humans are so deliciously unpurrrr-dictable. You wish to throw away all the comforts of the world above and dig your way into hell for some flimsy sword?")
                input("Kobaneko: If the unnamed katana is what you seek then you must fall even deeper than you already have. Into a place so steeped in darkness that no man returns unchanged…")
                input("Kobaneko: [her expression reverts back to normal] Nya-sk Dr.Crowley at the Demonitorium for more info!")
                checks.kobaneko_active_list += ["Be seeing you"]
                continue
            case 2:
                input("Kobaneko: Nya! If strength is what you seek then go over to the demonitorium and slaughter to your hearts content. Nyihihi!")
                continue
            case 3:
                input("Kobaneko: Ohh. Ichor is a wonderful place!")
                input("Kobaneko: If you’re hurt you can go to the church!")
                input("Kobaneko: If you need herbs or tools you can visit the apothecary!")
                input("Kobaneko: And if you want to test your skills against demons, head over to the demonitorium!")
                continue
            case 4:
                input("Kobaneko: Talk like how? This is just the tongue of Nya’s people!")
                continue
            case 5:
                input("Kobaneko: We’re everything inbetween! When a human is exposed to a lot of seithr at once, overtime they start to gain traits, and these are passed down to their children! And their childrens children!")
                input("Kobaneko: Ah the cycle of life is so beautiful!")
                input("Kobaneko: Of course, some of us are half-demons! We even allow regular demons if they agree to behave.")
                input("Kobaneko: Ichor is welcoming to all who are willing to abide by its absolute NO VIOLENCE clause!")
                checks.kobaneko_active_list += ["Seithr? What’s that"]
                checks.kobaneko_active_list += ["No Violence clause?"]
                continue
            case 6:
                input("Kobaneko: It’s all around nya’s world! It’s the wonderful clay of creation!")
                input("Kobaneko: However, it's most concentrated in the demon world, and any human that stays here for too long starts to change.")
                continue
            case 7:
                input("Kobaneko: Yes! Nya can rip and tear all you want in the dungeons or the demonitorium but absolutely NO fighting is allowed between citizens")
                continue
            case 8:
                input("Kobaneko: Oh? Really, you talked to Crowley too?")
                input("Kobaneko: So how was it? Enjoyed your first taste of demon blood?")
                input("Kobaneko: Oh don’t be coy, out there it’s kill or be killed. It’s in the nature of this world for us to tear ourselves apart.")
                input("Kobaneko: Well, truth be told, It didn't always use to be like that.")
                if not checks.dialogue_checks['kobamaoucheck']:
                    checks.kobaneko_active_list += ["How was it before."]
                    checks.crowley_active_list += ["Kobaneko mentioned a demon king?"]
                    checks.dialogue_checks['kobamaoucheck'] = True
                continue
            case 9:
                input("Kobaneko: When I was still just a kitten, and when the Demon Lord was still alive… Weak demons were protected and stronger demons were given purpose…")
                input("Kobaneko: It wasn’t absolute chaos. He ruled by strength as all demons should— he gave us safe territories and showed no mercy to those who broke them.")
                continue
            case 10:
                input("Kobaneko: That old coot sure seems to have taken a liking to you. But yes, everything he said was true. The blade is a crystallization of the goddess’s power.")
                input("Kobaneko: One who wields it has the power to shape the demon world, but the depths are far too dangerous, and at the end of the 4th floor stands a demon from an era long gone. Said to be so powerful that none could ever manage to stand up to him...")
                input("Kobaneko: Good luck! Here's a lucky charm from yours truly.")
                input("[Kobaneko gives you a brilliant gold coin... the way her countenance can change in such a short time is eery.]")
                # add_item KobanCoin
                continue
            case 11:
                if not checks.dialogue_checks['kobasubjcheck']:
                    input("Kobaneko: I figured as much, that man always had such a catty~ attitude about him.")
                    input("Kobaneko: Well, he says that’s what you’re meant to do, right? Because you’re human. Right? Surely, you must share his goals.")
                    input("Kobaneko: Although, the fact you came all the way to tell me this begs to differ. So then, I ask you, my dear human. Is this truly your heart's desire? Do you earnestly with all your heart seek the eradication of free will within all demonkind?")
                    ans = dialog_choice('', ["Yes", "I'm unsure", "No"], False)
                    match ans:
                        case 1:
                            input("Kobaneko: [she seems somewhat disappointed]")
                            input("Kobaneko: Then we have nothing else to discuss…")
                            checks.dialogue_checks['kobanBreak'] = True
                            break # ask if this is supposed to end the whole conversation
                        case 2:
                            input("Kobaneko: You seek the blade for yourself, don’t you? You came here seeking power and you’re at the cusp of it.")
                            input("Kobaneko: Do what you humans do best and keep moving forward. The rest will fall into place eventually.")
                            checks.dialogue_checks['endKobanCheck'] = True
                            continue
                        case 3:
                            input("Kobaneko: Even knowing our nature you still seek to protect us. You’re a curious one, ${name}.")
                            input("Kobaneko: To have defeated the Gigas, your strength is without question. Many demons are watching you already. Ever since you came out of the 3rd floor unscathed, innumerable eyes have been placed on you. Watching your evergrowing power.")
                            input("Kobaneko: Allow me to let you in on a secret so steeped in hell and wrapped in the secrets of demon-tongue, that not even those of the Blue know this.")
                            input("Kobaneko: ‘The Goddess is alive’.")
                            input("Kobaneko: Not an undying corpse, or in some deep sleep, but Alive. Shocking, I know, but we can feel it. All demons can, she is our mother, after all. We feel the soft thumping under the earth with every beat of her heart. She is awake, but quiet.")
                            checks.dialogue_checks['endKobanCheck'] = True
                            continue
                    input("Kobaneko: The former Daimaou was slain by a man called Minamoto no Raiko. He tore through the demon realm with naught but sword and lightning stolen from the heavens.")
                    input("Kobaneko: He was an unseen flash of pure white and rumbling thunder, and even though he was undoubtedly human, he moved with a viciousness unseen even among demonkind. In their grand ensuing battle, they slew each other.")
                    input("Kobaneko: This ‘sword’ was born soon after. It is unknown what was so special about their bout that caused this to happen, or if both events are even related, but we know for a fact that whoever wields it has the power to become a new Daimaou.")
                    input("Kobaneko: Whether protecting mankind is your wish, or obtaining absolute power is your wish, the only path to either is to take up this unholy mantle.")
                    checks.dialogue_checks['kobasubjcheck'] = True
                input("Kobaneko: I'll wait for you on the final floor.")
                continue
            case 12:
                input("Kobaneko: Bye-bye!")
                break


def one_horned_lady(player: Base_Player):
    qasked = False
    while True:
        question = dialog_choice('', ["Who are you?" "Where am I" f"My name is {player.name}"], False)
        match question:
            case 1:
                input("Angry woman: *glares* I’m your guide, I’m to register you. Name.")
                qasked = True
                continue
            case 2:
                input("Angry woman: This is the town of Ichor, where the dregs of mankind wind up when the above world is done with them. Name.")
                qasked = True
                continue
            case 3:
                input("Angry woman: Good.")
                if  qasked:
                    input("Angry woman: Talk to Koban if you want to ask anymore stupid questions.")
                else:
                    input("Angry woman: Go talk to Koban next.")
                input("Before you can respond you're immediately accosted by another smaller woman, not as intimidating as the last but her catlike physiology and clear disregard for personal space was still startling.")
                input("Kobaneko: Nya-hallo. My name is Kobaneko! I'm here to be your guide through the demon world!")
                input("Kobaneko: This is Ichor; no matter where you enter from, all humans end up here! Isn't this place great!")
                input("Kobaneko: So… What dragged nya’s sorry behind down here…")
                break


def final_floor(player):
    input("You take extreme care as you step lower and lower into the abyss, a dull thudding sound seems to move through the entire structure. Beneath your feet lay colorful rolls of fabric with myriad patterns, the density increasing as you pierced lower and lower.")
    input("By the point you had reached the bottom of the staircase, there were so many of them that they covered up the entire floor, and as you lift your gaze up you see the decorated corpse of the goddess. A macabre carcass, its chest cavity spread open like a blooming flower, as streams of cloth flowed out of it like a gushing wound. Its arms lay splayed at the sides and its head nailed to the wall. It looked almost ritualistic.")
    input("And inside, deep within all that, a rigid beam of pure light shot out where her heart would be. Your eyes had trouble focusing on it, it shone with an excruciating incandescence, but you were sure somehow, there wasn’t even an inkling of doubt in your heart, that this was the sword of myth.")
    input("It stirs.")
    input("The grey rotten corpse lurches forward, ripping off its own affixed head and leaving it dangling behind. A headless lanky creature hunched over you at least thrice your height, all the while fabric continued to pour out of its chest. Only one word it muttered, even though where once stood its head now was a mere stump, you were sure beyond doubt that this was being made by it.")
    print('')
    input("'Avenge...'")
    print('')
    battle(player, [enemy_models.Izanami()])
    if checks.dialogue_checks['endKobanCheck'] or checks.dialogue_checks['endKobanCheck']:
        input("You are successful in dispatching the goddess. Crowley steps in just behind you.")
        input("Crowley: That was no goddess, merely the lingering embers of one. More akin to a demon than anything.")
        input("Crowley: But your work is splendid nonetheless. All you need do now is simply reach out for it, and all the power is yours.")
        input("Kobaneko, who neither of you seems to have noticed slink in, is standing to your right. The look of revulsion on Crowley's face is evident and immediate. She stood with the head of the corpse in her arms, holding it like it were a child.")
        input("Kobaneko: Dearest mother. Forgive these humans who so brazenly desecrate your grave…")
        input("Kobaneko: Do you believe he has your best wishes at heart? I know what the society of Blue does, and what they are. You’re less than a tool to them.")
        input("Kobaneko: What do you think will become of your beloved human world when one party wields the entire force of the demonic realm.")
        input("Kobaneko: The answer is hell on earth, more guided and precise than anything a demonic incursion could ever cause.")
        input("Kobaneko: I’m not saying that you should trust only me. I am a demon after all. But there is a reason why new demon kings are created time and time again. The balance between man’s destiny and ours rests on an impossibly thin knife edge.")
        input("Kobaneko: If you want to subjugate demons then do it with your own strength. If you want to save humanity, then do it of your own will.")

        input("Crowley: Utter drivel!")
        input("Crowley: The poisonous words of a demon. Demons kill and take as they please, yet we can do naught but mewl and rebuild. Even merely to step foot in their domain causes us to become filthy facsimiles of their kind.")
        input("Crowley: It brings up such unknowable disgust within me to admit, yet I am neither foolish nor blind to the truth before my eyes. They outnumber us and are far more powerful.")
        input("Crowley: Do you understand what this means? Each Daimaou is inevitably more powerful than the last,and mankind cannot keep them at bay til eternity. One day, the dam will break and we will fall under the might of a Demon King powerful enough to tear the bridge between our worlds open.")
        input("Crowley: So you see, this is why we must obtain the sword. For the sake of mankind, for the absolute subjugation of the enemy, you… we must ascend.")

    endarr = ["Take the Sword in your own Name"]
    if checks.dialogue_checks['endKobanCheck']:
        endarr += ["Become the King of Hell"]
    if checks.dialogue_checks['endCrowCheck']:
        endarr += ["Enslave demonkind in the name of Humanity"]

    input("[you hear a voice]")
    input("???: Reach for the blade and your true heart’s desire will be crystallized.")
    choice = dialog_choice('', endarr, False)
    match choice:
        case 1:
            print("redeemed")
            end = "redeemed"
        case _:
            if endarr[choice - 1] == "Become the King of Hell":
                print("ascend")
                end = "ascend"
            elif endarr[choice - 1] == "Enslave demonkind in the name of Humanity":
                print("subjugate")
                end = "subjugate"

    match end:
        case "redeemed":
            input("Light swirls around your body and you draw a blade of gold and silver.")
            input("It seems less majestic than you expected.")
            input("Almost... inconsequential.")
        case "ascend":
            input("You reach out and draw the beam of light, its form begins to coalesce immediately.")
            input("Crowley: Impossible! You drew the blade of the former demon king!?")
            input("Kobaneko: 'Hi-no-Kagutsuchi'")
            input("[the look on his face is almost indecipherable, but his eyes were locked solely on you]")
            input("Crowley: Why would a human want to mingle with subhuman filth… Above his own kind. It defies all logic. No, it goes against nature itself.")
            input("Crowley: An aberration like you- with all the knowledge I’ve given you. Becoming Demon King? I cannot suffer you leave this place alive")
            battle(player, [enemy_models.Crowley()])
        case "subjugate":
            input("You reach out and draw the beam of light, its form begins to coalesce immediately.")
            input("Kobaneko: Ah, the blade of Emperor Sutoku. So this is the path you have chosen, dear Human.")
            input("Kobaneko: Maybe I did rely on you far too much. Either way, I can’t very well let you leave this place knowing what you plan to do with that.")
            input("[the ribbons around you seem to coalesce, bundling and knotting together into a terrifying figure]")
            input("Kobaneko: If you truly believe yourself to be worthy of subjugating all demonkin, then a simple thing as defeating a Daimaou should be an afterthought")
            battle(player, [enemy_models.Kobagami()])

    if checks.dialogue_checks['endWhiteCheck']:
        input("A figure manifests before you in a flash of white. The same one who saved you from the brink of death. He stood with his arms folded, and a look of pride on his face.")
        input("White: You are incredible.")
        input("Without a second word, he is upon you.")
        battle(player, [enemy_models.Whiten()])
        input("White: Your strength is unparalleled. You are-...")
        input("His last few words were muffled, as the room began to unfold and warp. Above you, which should’ve been the upper floors of the depth, now bore open the crimson skies of the demon realm.")
        end = izanagi(end)
    ending(player, end)


def izanagi(end):
    input("Amidst the red, a ray of swirling light falls down before you, and from it emerges a man.")
    input("???: You wield untenable power, mortal. You may witness me.")
    while True:
        question = dialog_choice('', checks.izanagi_active_list, False)
        match question:
            case 1:
                input("Izanagi-no-Mikoto: My name is Izanagi no Mikoto. Your ancestors one hundred generations ahead of your father would build shrines in my name.")
                continue
            case 2:
                input("Izanagi-no-Mikoto: If she is able to break the cloths that bind her and make her way to the human realm, she will bring with her death of an unimaginable scale")
                continue
            case 3:
                input("Izanagi-no-Mikoto: That power you wield in your hand is a weapon of my crafting. A spear of light meant to keep my wife from being resurrected.")
                checks.izanagi_active_list += ["What happens if she resurrects?"]
                continue
            case 4:
                input("Izanagi-no-Mikoto: You refer to the boy you bested in combat? He was an aid that has served its purpose. A role that has been opened anew")
                checks.izanagi_active_list += ["Purpose?"]
                continue
            case 5:
                input("Izanagi-no-Mikoto: Yes. The only way for her to be free is for a powerful enough Daimaou to break the seals I placed on her almost a millennia ago.")
                input("Izanagi-no-Mikoto: His former purpose, and your new one, is to take the head of any demon king who attempts such an act. That sword you wield was merely a stopgap until a new ‘Messenger’ could be found.")
                input("Izanagi-no-Mikoto: So fierce warrior, do you pledge loyalty to me?")
                response = dialog_choice('', back=False)
                if response:
                    end="whitewar"
                    break
                else:
                    input("Izanagi-no-Mikoto: ...")
                    input("Izanagi-no-Mikoto: You deny a god? I hope then for your sake that whatever you have obtained is worth the heavenly ire you have drawn.")
                    input("The so called god vanishes as abruptly as it manifested.")
                    break
    return end


def ending(player: Base_Player, end):
    match end:
        case "redeemed":
            input("You manage to return to the human world, gold-silver blade in hand. The tale of your adventures in the pit spread far and wide, and you become something of a local legend.")
            input("Your legend washes over your unseemly past and your popularity gets you mercenary work from powerful lords. You grow rich in treasure and favour, and retire not too long after.")
            input("On a night like any other, while asleep in your home, an unassailable swarm of demons rolls over the land and you are consumed.")
        case "ascend":
            input("As you wield the sword, ‘Hi-no-Kagutsuchi’, you feel demonic energy swell within you. Your body is permanently transformed. You can see much more than before and your power only seems to grow by the second. With this newfound strength, you set out into the realms of hell as the New Daimaou.")
            input("Most demons you encounter wilt in your presence, some would simply show reverence. Others would challenge you for your title. You take back territory from demons that once belonged to Ichor.")
            input("Eventually, Ichor is expanded out tremendously and the narrow pit that connected both worlds widens into a gaping maw as a result. Using your experience living in both, you allow for trade and communication to spur between both worlds.")
            input(f"Demons and humans find more in common and you create a somewhat uneasy alliance between both races. Your image is immortalized in the center of Ichor as Daimaou {player.name}")
        case "subjugate":
            input("With the power of the Imperial Blade, you bring all of demonkind to heel. Though they wail and howl with ferocity, their bodies no longer belong to them.")
            input("Leading your monstrous hoard out of the pit, you wash over the eastern half of the country like a plague, swallowing any arrant lord who dared to challenge your rule. Not long after you become known as an impossibly skilled sorcerer capable of commanding infinite terrible demons.")
            input("Alongside the assistance of the Order of Blue and the shrewd Crowley, you take over the majority of Japan and entitle yourself as 'The Emperor Mandated by Hell'")
        case "whitewar":
            input("You become as light, your body and blade is weightless and your mind is scattered against time and space. You are engulfed in pure white and for a time, you sleep.")
            input("You don’t know for how long, but soon enough you awaken elsewhere. Before you stands the visage of a woman and in front of her lay a terrible demon wielding a flaming sword.")
            input("Your memories are a haze and you are unsure where you are, but you understand deep within yourself that you are here to slaughter. A feeling so deep and inscribed that it seemed as though it was what you were born for.")
            input("And so with thundering steel, the fated clash begins anew.")
    credits()


def credits():
    print("originally developed in bash by AxiomDays")
    print("")
    print("ported to python by King Zero")
    print("")
    print("written by AxiomDays")
    print("")
    print("Thanks for Playing!")
    # save
    exit()
