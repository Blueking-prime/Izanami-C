from .utils import dialog_choice
import checks
from .Characters.Players.base_player import Base_Player


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
    input("The beautiful and deathly winter sprits dance around the fringes of this unending vortex, callously baiting all adventurers who dare come close to enter.")
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
        topic = dialog_choice('', checks.white_active_list)
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
            case _:
                break


def minamoto(player: Base_Player):
    input("The cold darkness ensnares you. Your body falls still and numbness overtakes you.")
    input("You can feel it, your very soul being washed away by the churning tides of time.")
    input("But deep in the back of your mind's eye, you see something. An impossibly bright light.")
    input("So incandescent that merely observing it seems to blow back the darkness out of reach.")

    choice = dialog_choice('', ["Reach Out" "Give Up"])
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

    choice = dialog_choice('', ["I want to Fight!", "I want to Win!", "I want to Live!"])
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
        response = dialog_choice("{May I be of assistance?}", checks.crowley_active_list)
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
            case _:
                break
