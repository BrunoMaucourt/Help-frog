########################
#	HelpFrog
#	Bruno MAUCOURT
#	Novembre 2022
#	Python 3.10.6
#	Pygame 2.1.2
########################

#   Importer les modules
import pygame
import sys
import os
import random

# Récupérer le chemin du dossier
DIRECTORYNAME = os.getcwd()

pygame.init()

####
#
#	Initialiser l'écran
#
####

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

fen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#   Choisir le nom de l'écran
pygame.display.set_caption("help(frog)")

####
#
#	Définir les couleurs
#
####

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0,0,0)
BLUE = (30, 209, 215)
RED = (255, 0, 0)
BLUE_DARK = (16, 107, 117)
GREEN_LIGHT = (154, 239, 80)
GREEN_DARK = (52,131,6)

####
#
#	Gestion du temps
#
####

# Nombre de frames par secondes
FPS = 25

#   Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

####
#
#	Initialiser le texte
#
####

# Taille (en points) utilisée pour les textes qui sont affichés
FONT_CLASSIC_SIZE = 25
FONT_MENU_SIZE = 50
FONT_TITLE_SIZE = 150

# Préparation de la Police utilisée pour l'affichage des textes
FONT_CLASSIC = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_CLASSIC_SIZE)
FONT_MENU = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_MENU_SIZE)
FONT_TITLE = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_TITLE_SIZE)

# Préparation du rendu du texte
TITLE = FONT_TITLE.render("help(frog)", True, WHITE)
MENU_PLAY = FONT_MENU.render("Jouer", True, BLACK)
MENU_OPTION = FONT_MENU.render("Options", True, BLACK)
MENU_CREDIT = FONT_MENU.render("Crédits", True, BLACK)
MENU_CREDIT_BRUNO = FONT_CLASSIC.render("Le jeu a été créé par Bruno MAUCOURT en Python.", True, BLACK)
MENU_CREDIT_GRAPHISME = FONT_CLASSIC.render("Le graphisme a aussi été réalisé par Bruno MAUCOURT.", True, BLACK)
MENU_CREDIT_FONT = FONT_CLASSIC.render("La police utilisée est Magical Story (créée par Gilar Studio).", True, BLACK)
MENU_CREDIT_SOUND = FONT_CLASSIC.render("Les bruitages proviennent du site internet BBC Sound Effects.", True, BLACK)
MENU_QUIT = FONT_MENU.render("Quitter", True, BLACK)
RETURN_MENU = FONT_CLASSIC.render("Retourner au menu", True, BLACK)
MSG_GAME_START = FONT_CLASSIC.render("La méchante grenouille veut voler les insectes que j'ai chasé. Aide moi à les cacher dans mon étang.", True, BLACK)
MSG_GAME_START_RULES = FONT_CLASSIC.render("Clique sur les cases pour cacher mes insectes.", True, BLACK)
MSG_PLAYER_TURN = FONT_CLASSIC.render("C'est à mon tour de jouer. Aide moi à trouver les insectes que l'on m'a volé.", True, BLACK)
MSG_PLAYER_TURN_RULES = FONT_CLASSIC.render("Clique sur les cases de l'étang de l'adversaire pour chercher mes insectes.", True, BLACK)
MSG_OPPONNENT_TURN = FONT_CLASSIC.render("C'est au tour de mon adversaire de jouer. J'espère qu'il ne trouvera pas mes insectes.", True, BLACK)
MSG_SOUND_OPTION = FONT_MENU.render("Son :", True, BLACK)
MSG_SOUND_OFF = FONT_MENU.render("Désactivé", True, BLACK)
MSG_SOUND_ON = FONT_MENU.render("Activé", True, BLACK)
NUMBER_0 = FONT_CLASSIC.render("0", True, BLACK)
NUMBER_1 = FONT_CLASSIC.render("1", True, BLACK)
NUMBER_2 = FONT_CLASSIC.render("2", True, BLACK)
NUMBER_3 = FONT_CLASSIC.render("3", True, BLACK)
NUMBER_4 = FONT_CLASSIC.render("4", True, BLACK)
NUMBER_5 = FONT_CLASSIC.render("5", True, BLACK)
NUMBER_6 = FONT_CLASSIC.render("6", True, BLACK)
NUMBER_7 = FONT_CLASSIC.render("7", True, BLACK)
NUMBER_8 = FONT_CLASSIC.render("8", True, BLACK)
NUMBER_9 = FONT_CLASSIC.render("9", True, BLACK)
LEVEL_1 = FONT_MENU.render("Niveau 1", True, BLACK)
LEVEL_2 = FONT_MENU.render("Niveau 2", True, BLACK)
LEVEL_3 = FONT_MENU.render("Niveau 3", True, BLACK)
LEVEL_4 = FONT_MENU.render("Niveau 4", True, BLACK)
LEVEL_5 = FONT_MENU.render("Niveau 5", True, BLACK)
LEVEL_6 = FONT_MENU.render("Niveau 6", True, BLACK)
LEVEL_7 = FONT_MENU.render("Niveau 7", True, BLACK)
LEVEL_8 = FONT_MENU.render("Niveau 8", True, BLACK)
LEVEL_9 = FONT_MENU.render("Niveau 9", True, BLACK)
LEVEL_10 = FONT_MENU.render("Niveau 10", True, BLACK)
BUGS_NUMBER_TO_HIDE = FONT_CLASSIC.render("Insectes à cacher", True, BLACK)
ETANG_JOUEUR = FONT_CLASSIC.render("Etang du joueur", True, WHITE)
ETANG_ADVERSAIRE = FONT_CLASSIC.render("Etang de l'adversaire", True, WHITE)
MSG_SUPER = FONT_CLASSIC.render("Super", True, BLACK)
MSG_BUG_FOUND = FONT_CLASSIC.render("Super, j'ai retrouvé l'un de les insectes.", True, BLACK)
MSG_NO_BUG_FOUND = FONT_CLASSIC.render("Mince, je n'ai pas retrouvé mes insectes.", True, BLACK)
MSG_OUF_NO_BUG_FOUND = FONT_CLASSIC.render("Ouf, il n'a pas trouvé mes insectes.", True, BLACK)
MSG_BUG_PLAYER_FOUND = FONT_CLASSIC.render("Mince, il a encore volé un de mes insectes.", True, BLACK)
MSG_BUG_OPPONENT_FOUND = FONT_CLASSIC.render("Super, j'ai retrouvé l'un de mes insectes.", True, BLACK)
MSG_END_GAME = FONT_CLASSIC.render("La partie est finie !", True, BLACK)
MSG_END_LOSE = FONT_CLASSIC.render("Saperlipopette, la méchante grenouille a volé tous mes insectes. Je ne te remercie pas pour ton aide", True, BLACK)
MSG_END_WIN = FONT_CLASSIC.render("Hourra, j'ai bien mangé. Merci pour ton aide.", True, BLACK)

# Pour calculer la taille que prend le texte et le centrer
TITLE_RECT = TITLE.get_rect(center=(600, 200))

####
#
#	Initialiser les images
#
####

FROG_DISAPPOINTED = pygame.image.load("Pictures/Frog_disappointed.png").convert_alpha()
FROG_EATING = pygame.image.load("Pictures/Frog_eating.png").convert_alpha()
FROG_GREEN = pygame.image.load("Pictures/Frog_green.png").convert_alpha()
FROG_HAPPY = pygame.image.load("Pictures/Frog_happy.png").convert_alpha()
FROG_RED = pygame.image.load("Pictures/Frog_red.png").convert_alpha()
FROG_YELLOW = pygame.image.load("Pictures/Frog_yellow.png").convert_alpha()
PICTURE_BUG = pygame.image.load("Pictures/Bug.png").convert_alpha()
MAGNIFYING_GLASS = pygame.image.load("Pictures/Magnifying_glass.png").convert_alpha()
LOGO_FROG = pygame.image.load("Pictures/Frog_green.png").convert_alpha()
BACKGROUND_MENU = pygame.image.load("Pictures/Background_menu.png")

#	Modifier la taille d'images
PICTURE_BUG = pygame.transform.scale(PICTURE_BUG, (75, 75))
MAGNIFYING_GLASS = pygame.transform.scale(MAGNIFYING_GLASS, (75, 75))
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU, (1200, 800))

#	Utiliser un logo pour la fenêtre
pygame.display.set_icon(LOGO_FROG)

####
#
#	Initialiser les bruitages
#
####

pygame.mixer.init()
PLOUF_SOUND = pygame.mixer.Sound("Sounds/Plouf.mp3")
ERROR_SOUND = pygame.mixer.Sound("Sounds/Succes.mp3")
SUCCES_SOUND = pygame.mixer.Sound("Sounds/Succes.mp3")

####
#
#	Variables à initialiser en début de partie
#
####

page = "menu"
RUNNING = True

####
#
#	Fonctions
#
####

def initialisation_checkerboard_player():
    position = 0
    global initialisation_player
    global checkerboard_player
    if initialisation_player == False:
        for i in range(0, NUMBER_OF_ROW,1):
            for j in range(0, NUMBER_OF_COLUMN,1):
                checkerboard_player.insert(position, "Empty")
            position +=1
    return True

def initialisation_checkerboard_opponent():
    position = 0
    global initialisation_opponent
    global checkerboard_opponent
    if initialisation_opponent == False:
        for i in range(0, NUMBER_OF_ROW,1):
            for j in range(0, NUMBER_OF_COLUMN,1):
                checkerboard_opponent.insert(position, "Empty")
            position +=1
    return True

def display_checkerboard(perso, pos_x, pos_y):
    position = 0
    #global checkerboard_player
    pos_x_initial = pos_x
    for i in range(0,NUMBER_OF_ROW,1):
        for j in range(0,NUMBER_OF_COLUMN,1):
            if perso[position] == "Empty" or perso[position] == "Bugs_opponent":
                pygame.draw.rect(fen, BLUE, (pos_x, pos_y, 75, 75))
                show_bugs_to_hide(PLAYER_POS_X, PLAYER_POS_Y)
            elif perso[position] == "Bugs":
                pygame.draw.rect(fen, BLUE_DARK, (pos_x, pos_y, 75, 75))
                fen.blit(PICTURE_BUG, (pos_x, pos_y))
            elif perso[position] == "Empty_cliked":
                pygame.draw.rect(fen, GREY, (pos_x, pos_y, 75, 75))
            elif perso[position] == "Bugs_player_cliked":
                pygame.draw.rect(fen, RED, (pos_x, pos_y, 75, 75))
                fen.blit(PICTURE_BUG, (pos_x, pos_y))
            elif perso[position] == "Bugs_opponent_cliked":
                pygame.draw.rect(fen, GREEN_DARK, (pos_x, pos_y, 75, 75))
                fen.blit(PICTURE_BUG, (pos_x, pos_y))
            position +=1
            pos_x += 100
        pos_x = pos_x_initial
        pos_y += 100

def find_position(pos_x, pos_y):
    x,y = 0,0
    if event.type == pygame.MOUSEBUTTONDOWN:
        #	Récupérer la position du clic
        x,y = event.pos
    for i in range(0, NUMBER_OF_ROW, 1):
        if pos_y+(i*100) < y < (75+pos_y)+(i*100):
            for j in range(0, NUMBER_OF_COLUMN, 1):
                if pos_x+(j*100) < x < (75+pos_x)+(j*100):
                    #	Calculer le numéro de la case
                    case = i*NUMBER_OF_COLUMN+(j+1)
                    return case

def hide_bugs():
    global bugs_to_hide
    global checkerboard_player
    if event.type == pygame.MOUSEBUTTONDOWN and find_position(PLAYER_POS_X,PLAYER_POS_Y) != None:
        if checkerboard_player[find_position(PLAYER_POS_X,PLAYER_POS_Y)-1] == "Empty" and bugs_to_hide > 0:
            checkerboard_player[find_position(PLAYER_POS_X,PLAYER_POS_Y)-1] = "Bugs"
            bugs_to_hide -= 1
            PLOUF_SOUND.play()

def opponent_hide_bugs(bugs_number):
    global checkerboard_opponent
    while bugs_number > 0 and opponent_bugs_hidden == False:
        #   Choisir un nombre entre 0 et le maximum
        nb_case = (NUMBER_OF_ROW * NUMBER_OF_COLUMN)-1
        nb_aleatoire = random.randrange(0,nb_case,1)
        if checkerboard_opponent[nb_aleatoire] == "Empty":
            checkerboard_opponent[nb_aleatoire] = "Bugs_opponent"
            bugs_number -= 1
    if bugs_number == 0 :
        return True

def show_bugs_number_to_hide():
        #global bugs_to_hide
        fen.blit(BUGS_NUMBER_TO_HIDE, (600, 50))
        if bugs_to_hide ==1:
            fen.blit(NUMBER_1, (600, 100))
        elif bugs_to_hide ==2:
            fen.blit(NUMBER_2, (600, 100))
        elif bugs_to_hide ==3:
            fen.blit(NUMBER_3, (600, 100))

def show_bugs_to_hide(pos_x, pos_y):
    pos_x_initial = pos_x
    pos_y_initial = pos_y
    #	Récupérer la position du clic
    if bugs_hidden == False:
        x,y = mouse_pos
        for i in range(0, NUMBER_OF_ROW, 1):
            if pos_y_initial+(i*100) < y < (75+pos_y_initial)+(i*100):
                for j in range(0, NUMBER_OF_COLUMN, 1):
                    if pos_x_initial+(j*100) < x < (75+pos_x_initial)+(j*100):
                        #	Calculer le numéro de la case
                        case = i*NUMBER_OF_COLUMN+(j+1)
                        if checkerboard_player[case-1] == "Empty":
                            #pygame.mouse.set_visible(False)
                            fen.blit(PICTURE_BUG, (pos_x, pos_y))
                    pos_x += 100
            pos_x = pos_x_initial
            pos_y += 100

def end_of_turn(perso):
    '''
    Fonction pour changer de tour
    '''
    global turn_counter
    if perso == "player":
        turn_counter += 1
        return False
    elif perso == "opponent":
        return True

def player_search_action():
    '''
    Action lorsque le joueur clique sur une case de l'étang adverse
    '''
    global checkerboard_opponent
    global opponent_bugs
    global player_turn
    if event.type == pygame.MOUSEBUTTONDOWN and find_position(OPPONENT_POS_X,OPPONENT_POS_Y) != None and checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] != "Empty_cliked" and checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] != "Bugs_opponent_cliked":
        if checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] == "Empty":
            checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] = "Empty_cliked"
            PLOUF_SOUND.play()
            replace_text(MSG_NO_BUG_FOUND, FROG_YELLOW, 1300)
        elif checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] == "Bugs_opponent":
            checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] = "Bugs_opponent_cliked"
            SUCCES_SOUND.play()
            opponent_bugs -= 1
            replace_text(MSG_BUG_FOUND, FROG_EATING, 1300)
        player_turn = end_of_turn("player")

def show_manifying_glass(pos_x, pos_y):
    pos_x_initial = pos_x
    pos_y_initial = pos_y
    #	Récupérer la position du clic
    if bugs_hidden == True:
        x,y = mouse_pos
        for i in range(0, NUMBER_OF_ROW, 1):
            if pos_y_initial+(i*100) < y < (75+pos_y_initial)+(i*100):
                for j in range(0, NUMBER_OF_COLUMN, 1):
                    if pos_x_initial+(j*100) < x < (75+pos_x_initial)+(j*100):
                        #	Calculer le numéro de la case
                        case = i*NUMBER_OF_COLUMN+(j+1)
                        if checkerboard_opponent[case-1] == "Empty" or checkerboard_opponent[case-1] == "Bugs_opponent":
                            #	Masquer la sourie
                            #pygame.mouse.set_visible(False)
                            fen.blit(MAGNIFYING_GLASS, (pos_x, pos_y))
                    pos_x += 100
            pos_x = pos_x_initial
            pos_y += 100

def replace_text(msg, frog_color, duration):
    '''
    Fonction pour remplacer de façon temporaire du texte
    '''
    # Effacer le contenu de l'écran
    fen.fill(GREEN_LIGHT)
    display_checkerboard(checkerboard_player, PLAYER_POS_X, PLAYER_POS_Y)
    display_checkerboard(checkerboard_opponent, OPPONENT_POS_X, OPPONENT_POS_Y)
    pygame.draw.rect(fen, WHITE, (0, 600, 1200, 200))
    fen.blit(frog_color, (0,600))
    fen.blit(ETANG_JOUEUR, (200, 25))
    fen.blit(ETANG_ADVERSAIRE, (850, 25))
    fen.blit(msg, (225, 650))
    pygame.display.update()
    pygame.time.wait(duration)

def checkSoundStatus():
    '''
    Fonction pour vérifier si le son est activé ou désactivé
    Vérifier l'information dans le fichier Options.txt
    '''
    SOUND_MUTE = 0
    SOUND_PLAY = 1
    soundFile = open(DIRECTORYNAME + "/Data/Options.txt", "r", encoding="utf8")
    for line in soundFile:
        line = line.strip()
        if (line == "Sound: ON"):
            PLOUF_SOUND.set_volume(SOUND_PLAY)
            ERROR_SOUND.set_volume(SOUND_PLAY)
            SUCCES_SOUND.set_volume(SOUND_PLAY)
            return True
        elif(line == "Sound: OFF"):
            PLOUF_SOUND.set_volume(SOUND_MUTE)
            ERROR_SOUND.set_volume(SOUND_MUTE)
            SUCCES_SOUND.set_volume(SOUND_MUTE)
            return False
    soundFile.close()

def modifySoundStatus():
    '''
    Fonction pour gérer le niveau sonore
    Modifier l'information dans le fichier Options.txt
    Recherche la ligne Sound puis modifie son contenu par celui de la variable changes
    '''
    soundFile = open(DIRECTORYNAME + "/Data/Options.txt", "r", encoding="utf8")
    replacement = ""
    # Tester chaque ligne du fichier
    for line in soundFile:
        # Enlever les espaces vides à l'avant et à la fin de la chaine de caractère
        line = line.strip()
        if (line == "Sound: ON"):
            changes = line.replace("Sound: ON", "Sound: OFF")
            replacement = replacement + changes + "\n"
        elif(line == "Sound: OFF"):
            changes = line.replace("Sound: OFF", "Sound: ON")
            replacement = replacement + changes + "\n"
        else:
            replacement = replacement + line + "\n"
    soundFile.close()
    # Modifier le contenu du fichier avec les modifications
    soundFileWriting = open(DIRECTORYNAME + "/Data/Options.txt", "w", encoding="utf8")
    soundFileWriting.write(replacement)
    soundFileWriting.close()
    checkSoundStatus()

def highScoreSaving():
    '''
    Comparer le score avec celui enregistré et remplacer s'il est meilleur
    '''
    print("Procédure high-score")
    highScoreFile = open(DIRECTORYNAME + "/Data/HighScore.txt", "r", encoding="utf8")
    replacement = ""
    # Tester chaque ligne du fichier
    for line in highScoreFile:
        print(line)
        if(line.find(levelName) != -1):
            print("bon niveau")
            lineParsed = line.split(" ")
            actualScore = int(lineParsed[1])
            print("actualScore", actualScore)
            print("turn_counter", turn_counter)
            if (actualScore > turn_counter):
                replacement = replacement + lineParsed[0] + " " + str(turn_counter) + "\n"
            else:
                replacement = replacement + line #+ "\n"
        else:
            replacement = replacement + line #+ "\n"
    highScoreFile.close()
    # Modifier le contenu du fichier avec les modifications
    highScoreFileWriting = open(DIRECTORYNAME + "/Data/HighScore.txt", "w", encoding="utf8")
    highScoreFileWriting.write(replacement)
    highScoreFileWriting.close()

def choose_level(level):
    '''
    Fonction pour le choix du niveau
    '''
    initialisation_of_variables(level)
    pygame.time.wait(100)
    return "level"

def initialisation_of_variables(level):
    '''
    Réinitialiser les variables pour chaque niveau
    '''
    global turn_counter
    global checkerboard_player
    global checkerboard_opponent
    global initialisation_player
    global initialisation_opponent
    global player_turn
    global bugs_hidden
    global opponent_bugs_hidden
    global levelName
    global player_bugs
    global opponent_bugs
    global scoreSaving
    global bugs_to_hide
    global PLAYER_POS_X
    global PLAYER_POS_Y
    global OPPONENT_POS_X
    global OPPONENT_POS_Y
    global NUMBER_OF_COLUMN
    global NUMBER_OF_ROW

    turn_counter = 0
    checkerboard_player = []
    checkerboard_opponent = []
    initialisation_player = False
    initialisation_opponent = False
    player_turn = True
    bugs_hidden = False
    opponent_bugs_hidden = False
    scoreSaving = True
    #	Niveau 1
    if level == "level1":
        levelName = "Level_01"
        player_bugs = 1
        opponent_bugs = 1
        bugs_to_hide = 1
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 1
    elif level == "level2":
        levelName = "Level_02"
        player_bugs = 1
        opponent_bugs = 1
        bugs_to_hide = 1
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 2
    elif level == "level3":
        levelName = "Level_03"
        player_bugs = 2
        opponent_bugs = 2
        bugs_to_hide = 2
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 3
    if level == "level4":
        levelName = "Level_04"
        player_bugs = 2
        opponent_bugs = 2
        bugs_to_hide = 2
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 4
    elif level == "level5":
        levelName = "Level_05"
        player_bugs = 1
        opponent_bugs = 1
        bugs_to_hide = 1
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5
    elif level == "level6":
        levelName = "Level_06"
        player_bugs = 3
        opponent_bugs = 3
        bugs_to_hide = 3
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5
    if level == "level7":
        levelName = "Level_07"
        player_bugs = 3
        opponent_bugs = 3
        bugs_to_hide = 3
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5
    elif level == "level8":
        levelName = "Level_08"
        player_bugs = 3
        opponent_bugs = 3
        bugs_to_hide = 3
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5
    elif level == "level9":
        levelName = "Level_09"
        player_bugs = 3
        opponent_bugs = 3
        bugs_to_hide = 3
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5
    elif level == "level10":
        levelName = "Level_10"
        player_bugs = 3
        opponent_bugs = 3
        bugs_to_hide = 3
        PLAYER_POS_X = 25
        PLAYER_POS_Y = 75
        OPPONENT_POS_X = 700
        OPPONENT_POS_Y = 75
        NUMBER_OF_COLUMN = 5
        NUMBER_OF_ROW = 5

####
#
#	Lancer la partie
#
####

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            RUNNING = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    if page == "menu":
        fen.fill(GREEN_LIGHT)
        fen.blit(BACKGROUND_MENU, (0,0))
        fen.blit(TITLE, TITLE_RECT)
        RECT_MENU_PLAY = fen.blit(MENU_PLAY, (500, 400))
        RECT_MENU_OPTION = fen.blit(MENU_OPTION, (500, 500))
        RECT_MENU_CREDIT = fen.blit(MENU_CREDIT, (500, 600))
        RECT_MENU_QUIT = fen.blit(MENU_QUIT, (500, 700))
        #initialisation of sound
        checkSoundStatus()
        # Check if position is in the rect
        if RECT_MENU_PLAY.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu_level"
        elif RECT_MENU_OPTION.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "options"
        elif RECT_MENU_CREDIT.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "credits"
        elif RECT_MENU_QUIT.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            RUNNING = False

    elif page == "credits":
        fen.fill(GREEN_LIGHT)
        fen.blit(MENU_CREDIT_BRUNO, (200, 200))
        fen.blit(MENU_CREDIT_GRAPHISME, (200, 300))
        fen.blit(MENU_CREDIT_FONT, (200, 400))
        fen.blit(MENU_CREDIT_SOUND, (200, 500))
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, (225, 750))
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "menu_level":
        fen.fill(GREEN_LIGHT)
        RECT_LEVEL_1 = fen.blit(LEVEL_1, (125,200))
        RECT_LEVEL_2 = fen.blit(LEVEL_2, (325,200))
        RECT_LEVEL_3 = fen.blit(LEVEL_3, (525,200))
        RECT_LEVEL_4 = fen.blit(LEVEL_4, (725,200))
        RECT_LEVEL_5 = fen.blit(LEVEL_5, (925,200))
        RECT_LEVEL_6 = fen.blit(LEVEL_6, (125,500))
        RECT_LEVEL_7 = fen.blit(LEVEL_7, (325,500))
        RECT_LEVEL_8 = fen.blit(LEVEL_8, (525,500))
        RECT_LEVEL_9 = fen.blit(LEVEL_9, (725,500))
        RECT_LEVEL_10 = fen.blit(LEVEL_10, (925,500))
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, (225, 750))
        if RECT_LEVEL_1.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level1")
        if RECT_LEVEL_2.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level2")
        if RECT_LEVEL_3.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level3")
        if RECT_LEVEL_4.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level4")
        if RECT_LEVEL_5.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level5")
        if RECT_LEVEL_6.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level6")
        if RECT_LEVEL_7.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level7")
        if RECT_LEVEL_8.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level8")
        if RECT_LEVEL_9.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level9")
        if RECT_LEVEL_10.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = choose_level("level10")
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "options":
        fen.fill(GREEN_LIGHT)
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, (225, 750))
        fen.blit(MSG_SOUND_OPTION, (225, 250))
        if(checkSoundStatus() == True):
            RECT_SOUND_MENU = fen.blit(MSG_SOUND_ON, (350, 250))
        else:
            RECT_SOUND_MENU = fen.blit(MSG_SOUND_OFF, (350, 250))
        
        if RECT_SOUND_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            modifySoundStatus()
            pygame.time.wait(250)
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "level":
        #	Création des listes correspondantes aux damiers
        initialisation_player = initialisation_checkerboard_player()
        initialisation_opponent = initialisation_checkerboard_opponent()
        #   Affichage de l'arrière plan
        fen.fill(GREEN_LIGHT)
        display_checkerboard(checkerboard_player, PLAYER_POS_X, PLAYER_POS_Y)
        pygame.draw.rect(fen, WHITE, (0, 600, 1200, 200))
        fen.blit(ETANG_JOUEUR, (200, 25))
        if bugs_hidden == False:
            fen.blit(FROG_GREEN, (0,600))
            fen.blit(MSG_GAME_START, (225, 650))
            fen.blit(MSG_GAME_START_RULES, (225, 700))
            show_bugs_number_to_hide()
            hide_bugs()
            if bugs_to_hide == 0:
                bugs_hidden = True
        elif bugs_hidden == True:
            fen.blit(ETANG_ADVERSAIRE, (850, 25))
            display_checkerboard(checkerboard_opponent, OPPONENT_POS_X, OPPONENT_POS_Y)
            #	Hidde bugs in opponent pond
            opponent_bugs_hidden = opponent_hide_bugs(opponent_bugs)
            #	Hidde bugs in opponent pond
            show_manifying_glass(OPPONENT_POS_X, OPPONENT_POS_Y)
            if player_bugs > 0 and opponent_bugs > 0:
                if player_turn == True:
                    fen.blit(FROG_GREEN, (0,600))
                    fen.blit(MSG_PLAYER_TURN, (225, 650))
                    fen.blit(MSG_PLAYER_TURN_RULES, (225, 700))
                    #   Afficher une image pour indiquer que c'est au joueur de jouer
                    #	Action lorsque l'on clique sur une case de l'adversaire
                    player_search_action()
                    opponent_turn_start = True
                else:
                    if opponent_turn_start == True and player_turn == False:
                        fen.blit(FROG_DISAPPOINTED, (0,600))
                        fen.blit(MSG_OPPONNENT_TURN, (225, 650))
                        pygame.display.update()
                        pygame.time.wait(1300)
                        opponent_turn_start = False
                    # Action of opponent
                    random_number = random.randrange(0,((NUMBER_OF_ROW * NUMBER_OF_COLUMN)-1),1)
                    while checkerboard_player[random_number] == "Empty_cliked" or checkerboard_player[random_number] == "Bugs_cliked" or random_number == -1:
                        random_number = random.randrange(0,((NUMBER_OF_ROW * NUMBER_OF_COLUMN)-1),1)
                    if checkerboard_player[random_number] == "Empty":
                        checkerboard_player[random_number] = "Empty_cliked"
                        PLOUF_SOUND.play()
                        replace_text(MSG_OUF_NO_BUG_FOUND, FROG_GREEN, 1300)
                    elif checkerboard_player[random_number] == "Bugs":
                        checkerboard_player[random_number] = "Bugs_player_cliked"
                        player_bugs -= 1
                        ERROR_SOUND.play()
                        replace_text(MSG_BUG_PLAYER_FOUND, FROG_RED, 1300)
                    player_turn = end_of_turn("opponent")
            elif player_bugs == 0 or opponent_bugs == 0:
                if player_bugs == 0:
                    fen.blit(FROG_RED, (0,600))
                    fen.blit(MSG_END_LOSE, (225, 650))
                else:
                    fen.blit(FROG_HAPPY, (0,600))
                    fen.blit(MSG_END_WIN, (225, 650))
                    if(scoreSaving == True):
                        highScoreSaving()
                        scoreSaving = False
                RECT_RETURN_MENU = fen.blit(RETURN_MENU, (225, 750))
                if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    page = "menu"

    #	Mise à jour de l'écran
    pygame.display.update()
    horloge.tick(FPS)