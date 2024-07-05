from Models import parameters
from Models.utils import dialog_choice
from Models.Maps.town import Town
from Models.Characters.Players import player_models
from Scripts import dialogue, save
from os import system

menu = ['New game', 'Load game']

if __name__ == '__main__':
    system('clear')
    if len(save.listdir(save.save_folder)) == 0:
        menu[1] = None
        dialogue.tutorial()

    print("---------------------------------------------------------------")
    input("The hunt for the nameless blade is upon us.")
    input("Like a star fallen from the sky, hundreds of the greatest warriors, tacticians and world-shapers the province has ever seen are after this legendary weapon that seemed to have been sent by the gods themselves.")
    input("Hidden deep in the center of Izanami's Forest, do you have the strength to obtain the greatest treasure? Or will you fall like the others that came before?")

    mode = dialog_choice('Welcome to Izanami', menu, back=False)
    if mode == 1:
        # New game stuff
        name = input("What do they call you (input your name): ")

        while True:
            character = dialog_choice("Before finding yourself wound up in such an untenable quest, what work did your hands find themselves in", parameters.characters)
            match character:
                case 1:
                    print("A man of the earth who finds himself in depths far beyond him, you are strong from years of backbreaking labour and have always been known for your wit")
                    confirm = dialog_choice("Confirm: ", back=False)
                    if confirm:
                        player = player_models.Farmer(name)
                        break
                    else:
                        continue
                case 2:
                    print("Born into poverty, not even the scraps on your back belong to you. Your birth was insignificant and your life a meaningless struggle, but alas you may yet find your worth in the pit.")
                    confirm = dialog_choice("Confirm: ", back=False)
                    if confirm:
                        player = player_models.Destitute(name)
                        break
                    else:
                        continue
                case 3:
                    print("A healer of men, a combat medic, a learned medicine man. Though you've spent your whole life giving life those who may not even deserve, you seek a weapon that can only take. Your skill with people and bodies will serve you well")
                    confirm = dialog_choice("Confirm: ", back=False)
                    if confirm:
                        player = player_models.Doctor(name)
                        break
                    else:
                        continue
                case 4:
                    print("A former samurai who has performed a slight against his lord, whether intentionally or not, whether righteously or not")
                    confirm = dialog_choice("Confirm: ", back=False)
                    if confirm:
                        player = player_models.Ronin(name)
                        break
                    else:
                        continue
                case 5:
                    print("The shinobi are warriors whose existence is myth. They dance in shadow and attack only when moonlight strikes their targets eyes.")
                    confirm = dialog_choice("Confirm: ", back=False)
                    if confirm:
                        player = player_models.Shinobi(name)
                        break
                    else:
                        continue

        print('These are your parameters: ')
        print(player.stats)
        dialogue.fall(player)
        save.save(player)

        dialogue.one_horned_lady(player)
        dialogue.kobaneko()
        save.save(player)
        # End of new game stuff
    else:
        player= save.load()

    Town().main(player)
    print("Town function Was Broken out of; Critical Error :skull_emoji:")
