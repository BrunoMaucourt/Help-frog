########################
#	Help(Frog)
#	Bruno MAUCOURT
#	January 2023
#	Python 3.10.6
#	Pygame 2.1.2
########################

#   Import of modules
import pygame
import sys
import os
import random

# Get current folder path
DIRECTORYNAME = os.getcwd()

pygame.init()

####
#
#	Screen initialization
#
####

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

fen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#   Set name of screen
pygame.display.set_caption("help(frog)")

####
#
#	Set colors constants
#
####

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GOLD = (233, 128, 14)
BLACK = (0,0,0)
BLUE = (30, 209, 215)
RED = (255, 0, 0)
BLUE_DARK = (16, 107, 117)
GREEN_LIGHT = (89, 166, 89)
GREEN_DARK = (52,131,6)

####
#
#	Time
#
####

#   Number of frames per seconde
FPS = 25

#   Wait before update screen
CLOCK = pygame.time.Clock()

####
#
#	Text initialization
#
####

#   Define size of fonts
FONT_CLASSIC_SIZE = 25
FONT_MENU_SIZE = 50
FONT_TITLE_SIZE = 150

#   Define font before to display texts
FONT_CLASSIC = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_CLASSIC_SIZE)
FONT_MENU = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_MENU_SIZE)
FONT_TITLE = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_TITLE_SIZE)

#   Initialize text
TITLE = FONT_TITLE.render("help(frog)", True, WHITE)
MENU_PLAY = FONT_MENU.render("Jouer", True, BLACK)
MENU_OPTION = FONT_MENU.render("Options", True, BLACK)
MENU_CREDIT = FONT_MENU.render("Crédits", True, BLACK)
MENU_QUIT = FONT_MENU.render("Quitter", True, BLACK)
MENU_PLAY_GREY = FONT_MENU.render("Jouer", True, GREY)
MENU_OPTION_GREY = FONT_MENU.render("Options", True, GREY)
MENU_CREDIT_GREY = FONT_MENU.render("Crédits", True, GREY)
MENU_QUIT_GREY = FONT_MENU.render("Quitter", True, GREY)
MENU_PAUSE = FONT_MENU.render("Menu pause", True, BLACK)
MENU_CREDIT_BRUNO = FONT_CLASSIC.render("Le jeu a été créé par Bruno MAUCOURT en Python.", True, BLACK)
MENU_CREDIT_GRAPHISME = FONT_CLASSIC.render("Le graphisme a aussi été réalisé par Bruno MAUCOURT.", True, BLACK)
MENU_CREDIT_FONT = FONT_CLASSIC.render("La police utilisée est Magical Story (créée par Gilar Studio).", True, BLACK)
MENU_CREDIT_SOUND = FONT_CLASSIC.render("Les bruitages proviennent du site internet BBC Sound Effects.", True, BLACK)
MENU_TURN_NUMBER = FONT_MENU.render("Tour numéro", True, BLACK)
MENU_PAUSE_HIGH_SCORE = FONT_MENU.render("Meilleur score", True, BLACK)
RETURN_MENU = FONT_CLASSIC.render("Retourner au menu", True, BLACK)
RETURN_GAME = FONT_MENU.render("Reprendre la partie", True, BLACK)
RETURN_MENU_FROM_PAUSE = FONT_MENU.render("Retourner au menu", True, BLACK)
MSG_GAME_START = FONT_CLASSIC.render("La méchante grenouille veut voler les insectes que j'ai chassés Aide-moi à les cacher dans mon étang.", True, BLACK)
MSG_GAME_START_RULES = FONT_CLASSIC.render("Clique sur les cases pour cacher mes insectes.", True, BLACK)
MSG_PLAYER_TURN = FONT_CLASSIC.render("C'est à mon tour de jouer. Aide-moi à trouver les insectes que l'on m'a volés.", True, BLACK)
MSG_PLAYER_TURN_RULES = FONT_CLASSIC.render("Clique sur les cases de l'étang de l'adversaire pour chercher mes insectes.", True, BLACK)
MSG_OPPONNENT_TURN = FONT_CLASSIC.render("C'est au tour de mon adversaire de jouer. J'espère qu'il ne trouvera pas mes insectes.", True, BLACK)
OPTION_SOUND_OPTION = FONT_MENU.render("Son :", True, BLACK)
OPTION_SOUND_OFF = FONT_MENU.render("Désactivé", True, BLACK)
OPTION_SOUND_ON = FONT_MENU.render("Activé", True, BLACK)
OPTION_ERASE = FONT_MENU.render("Effacer les scores sauvegardés", True, BLACK)
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
NUMBER_0_XL = FONT_MENU.render("0", True, BLACK)
NUMBER_1_XL = FONT_MENU.render("1", True, BLACK)
NUMBER_2_XL = FONT_MENU.render("2", True, BLACK)
NUMBER_3_XL = FONT_MENU.render("3", True, BLACK)
NUMBER_4_XL = FONT_MENU.render("4", True, BLACK)
NUMBER_5_XL = FONT_MENU.render("5", True, BLACK)
NUMBER_6_XL = FONT_MENU.render("6", True, BLACK)
NUMBER_7_XL = FONT_MENU.render("7", True, BLACK)
NUMBER_8_XL = FONT_MENU.render("8", True, BLACK)
NUMBER_9_XL = FONT_MENU.render("9", True, BLACK)
NUMBER_0_XL_GOLD = FONT_MENU.render("0", True, GOLD)
NUMBER_1_XL_GOLD = FONT_MENU.render("1", True, GOLD)
NUMBER_2_XL_GOLD = FONT_MENU.render("2", True, GOLD)
NUMBER_3_XL_GOLD = FONT_MENU.render("3", True, GOLD)
NUMBER_4_XL_GOLD = FONT_MENU.render("4", True, GOLD)
NUMBER_5_XL_GOLD = FONT_MENU.render("5", True, GOLD)
NUMBER_6_XL_GOLD = FONT_MENU.render("6", True, GOLD)
NUMBER_7_XL_GOLD = FONT_MENU.render("7", True, GOLD)
NUMBER_8_XL_GOLD = FONT_MENU.render("8", True, GOLD)
NUMBER_9_XL_GOLD = FONT_MENU.render("9", True, GOLD)
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
ETANG_JOUEUR = FONT_CLASSIC.render("Etang du joueur", True, BLACK)
ETANG_ADVERSAIRE = FONT_CLASSIC.render("Etang de l'adversaire", True, BLACK)
MSG_SUPER = FONT_CLASSIC.render("Super", True, BLACK)
MSG_BUG_FOUND = FONT_CLASSIC.render("Super, j'ai retrouvé l'un de les insectes.", True, BLACK)
MSG_NO_BUG_FOUND = FONT_CLASSIC.render("Mince, je n'ai pas retrouvé mes insectes.", True, BLACK)
MSG_OUF_NO_BUG_FOUND = FONT_CLASSIC.render("Ouf, il n'a pas trouvé mes insectes.", True, BLACK)
MSG_BUG_PLAYER_FOUND = FONT_CLASSIC.render("Mince, il a encore volé un de mes insectes.", True, BLACK)
MSG_BUG_OPPONENT_FOUND = FONT_CLASSIC.render("Super, j'ai retrouvé l'un de mes insectes.", True, BLACK)
MSG_END_GAME = FONT_CLASSIC.render("La partie est finie !", True, BLACK)
MSG_END_LOSE = FONT_CLASSIC.render("Saperlipopette, la méchante grenouille a volé tous mes insectes. Je ne te remercie pas pour ton aide.", True, BLACK)
MSG_END_WIN = FONT_CLASSIC.render("Hourra, j'ai bien mangé. Merci pour ton aide.", True, BLACK)

#   Center texts
TITLE_CENTER = TITLE.get_rect(center=(WINDOW_WIDTH/2, 150))
MENU_PLAY_CENTER = MENU_PLAY.get_rect(center=(WINDOW_WIDTH/2, 400))
MENU_OPTION_CENTER = MENU_OPTION.get_rect(center=(WINDOW_WIDTH/2, 500))
MENU_CREDIT_CENTER = MENU_CREDIT.get_rect(center=(WINDOW_WIDTH/2, 600))
MENU_QUIT_CENTER = MENU_QUIT.get_rect(center=(WINDOW_WIDTH/2, 700))
MENU_PLAY_GREY_CENTER = MENU_PLAY_GREY.get_rect(center=(WINDOW_WIDTH/2, 400))
MENU_OPTION_GREY_CENTER = MENU_OPTION_GREY.get_rect(center=(WINDOW_WIDTH/2, 500))
MENU_CREDIT_GREY_CENTER = MENU_CREDIT_GREY.get_rect(center=(WINDOW_WIDTH/2, 600))
MENU_QUIT_GREY_CENTER = MENU_QUIT_GREY.get_rect(center=(WINDOW_WIDTH/2, 700))
RETURN_GAME_CENTER = RETURN_GAME.get_rect(center=(WINDOW_WIDTH/2, 650))
MENU_PAUSE_CENTER = MENU_PAUSE.get_rect(center=(WINDOW_WIDTH/2, 175))
RETURN_MENU_FROM_MENU_CENTER = RETURN_MENU.get_rect(center=(WINDOW_WIDTH/2, 750))
RETURN_MENU_FROM_PAUSE_CENTER = RETURN_MENU_FROM_PAUSE.get_rect(center=(WINDOW_WIDTH/2, 560))
MENU_CREDIT_BRUNO_CENTER = MENU_CREDIT_BRUNO.get_rect(center=(WINDOW_WIDTH/2, 200))
MENU_CREDIT_GRAPHISME_CENTER = MENU_CREDIT_GRAPHISME.get_rect(center=(WINDOW_WIDTH/2, 300))
MENU_CREDIT_FONT_CENTER = MENU_CREDIT_FONT.get_rect(center=(WINDOW_WIDTH/2, 400))
MENU_CREDIT_SOUND_CENTER = MENU_CREDIT_SOUND.get_rect(center=(WINDOW_WIDTH/2, 500))

####
#
#	Initialize images
#
####

FROG_DISAPPOINTED = pygame.image.load("Pictures/Frog_disappointed.png").convert_alpha()
FROG_EATING = pygame.image.load("Pictures/Frog_eating.png").convert_alpha()
FROG_GREEN = pygame.image.load("Pictures/Frog_green.png").convert_alpha()
FROG_HAPPY = pygame.image.load("Pictures/Frog_happy.png").convert_alpha()
FROG_RED = pygame.image.load("Pictures/Frog_red.png").convert_alpha()
FROG_YELLOW = pygame.image.load("Pictures/Frog_yellow.png").convert_alpha()
PICTURE_BUG_BLACK = pygame.image.load("Pictures/bug_black.png").convert_alpha()
PICTURE_BUG_RED = pygame.image.load("Pictures/bug_red.png").convert_alpha()
PICTURE_BUG_GREEN = pygame.image.load("Pictures/bug_green.png").convert_alpha()
CASE_EMPTY = pygame.image.load("Pictures/case_empty.png").convert_alpha()
CASE_BLUE = pygame.image.load("Pictures/case_blue.png").convert_alpha()
CASE_GREEN = pygame.image.load("Pictures/case_green.png").convert_alpha()
CASE_GREY = pygame.image.load("Pictures/case_grey.png").convert_alpha()
CASE_RED = pygame.image.load("Pictures/case_red.png").convert_alpha()
PAUSE_MENU = pygame.image.load("Pictures/pause_menu.png")
MAGNIFYING_GLASS = pygame.image.load("Pictures/Magnifying_glass.png").convert_alpha()
LAUREL_WREATH = pygame.image.load("Pictures/laurel_wreath.png").convert_alpha()
RED_CROSS = pygame.image.load("Pictures/cross_red.png").convert_alpha()
LOGO_FROG = pygame.image.load("Pictures/Frog_green.png").convert_alpha()
BACKGROUND_MENU = pygame.image.load("Pictures/background_menu.png")
BACKGROUND_GAME = pygame.image.load("Pictures/background_game.png")
BACKGROUND_GAME6 = pygame.image.load("Pictures/background_game06.png")
BACKGROUND_GAME7 = pygame.image.load("Pictures/background_game07.png")
BACKGROUND_GAME8 = pygame.image.load("Pictures/background_game08.png")
BACKGROUND_GAME9 = pygame.image.load("Pictures/background_game09.png")
BACKGROUND_GAME10 = pygame.image.load("Pictures/background_game10.png")
BACKGROUND_PAUSE = pygame.image.load("Pictures/background_pause.png").convert_alpha()

#	Edit size of pictures
PICTURE_BUG_BLACK = pygame.transform.scale(PICTURE_BUG_BLACK, (75, 75))
PICTURE_BUG_GREEN = pygame.transform.scale(PICTURE_BUG_GREEN, (75, 75))
PICTURE_BUG_RED = pygame.transform.scale(PICTURE_BUG_RED, (75, 75))
CASE_EMPTY = pygame.transform.scale(CASE_EMPTY, (75, 75))
CASE_BLUE = pygame.transform.scale(CASE_BLUE, (75, 75))
CASE_GREEN = pygame.transform.scale(CASE_GREEN, (75, 75))
CASE_GREY = pygame.transform.scale(CASE_GREY, (75, 75))
CASE_RED = pygame.transform.scale(CASE_RED, (75, 75))
PAUSE_MENU = pygame.transform.scale(PAUSE_MENU, (25, 25))
MAGNIFYING_GLASS = pygame.transform.scale(MAGNIFYING_GLASS, (75, 75))
LAUREL_WREATH = pygame.transform.scale(LAUREL_WREATH, (45, 45))
RED_CROSS = pygame.transform.scale(RED_CROSS, (75, 75))
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU, (1200, 800))

#	Logo for window
pygame.display.set_icon(LOGO_FROG)

####
#
#	Initialize sounds
#
####

pygame.mixer.init()
PLOUF_SOUND = pygame.mixer.Sound("Sounds/Plouf.mp3")
ERROR_SOUND = pygame.mixer.Sound("Sounds/Succes.mp3")
SUCCES_SOUND = pygame.mixer.Sound("Sounds/Succes.mp3")

####
#
#	Variables to initialize at the start of the game
#
####

page = "menu"
RUNNING = True

####
#
#	Functions
#
####

def choose_level(levelNumber):
    '''
    Function to create and choose level
    '''
    global level
    initialisation_of_variables()
    match levelNumber:
        case "level1":
            level = Level("level_01", 1, 1, 1, 25, 100, 700, 100, 5, 1, BACKGROUND_GAME)
        case "level2":
            level = Level("level_02", 1, 1, 1, 25, 100, 700, 100, 5, 2, BACKGROUND_GAME)
        case "level3":
            level = Level("level_03", 2, 2, 2, 25, 100, 700, 100, 5, 3, BACKGROUND_GAME)
        case "level4":
            level = Level("level_04", 2, 2, 2, 25, 100, 700, 100, 5, 4, BACKGROUND_GAME)
        case "level5":
            level = Level("level_05", 3, 3, 3, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME)
        case "level6":
            level = Level("level_06", 5, 5, 5, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME6)
        case "level7":
            level = Level("level_07", 5, 5, 5, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME7)
        case "level8":
            level = Level("level_08", 5, 5, 5, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME8)
        case "level9":
            level = Level("level_09", 5, 5, 5, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME9)
        case "level10":
            level = Level("level_10", 5, 5, 5, 25, 100, 700, 100, 5, 5, BACKGROUND_GAME10)
    pygame.time.wait(100)
    return "level"

def initialisation_checkerboard_player():
    position = 0
    global initialisation_player
    global checkerboard_player
    if initialisation_player == False:
        for i in range(0, level.NUMBER_OF_ROW,1):
            for j in range(0, level.NUMBER_OF_COLUMN,1):
                checkerboard_player.insert(position, "Empty")
            position +=1
    return True

def initialisation_checkerboard_opponent():
    position = 0
    global initialisation_opponent
    global checkerboard_opponent
    if initialisation_opponent == False:
        for i in range(0, level.NUMBER_OF_ROW,1):
            for j in range(0, level.NUMBER_OF_COLUMN,1):
                checkerboard_opponent.insert(position, "Empty")
            position +=1
    return True

def display_checkerboard(perso, pos_x, pos_y):
    position = 0
    pos_x_initial = pos_x
    for i in range(0,level.NUMBER_OF_ROW,1):
        for j in range(0,level.NUMBER_OF_COLUMN,1):
            if perso[position] == "Empty" or perso[position] == "Bugs_opponent":
                fen.blit(CASE_EMPTY, (pos_x, pos_y))
                show_bugs_to_hide(level.PLAYER_POS_X, level.PLAYER_POS_Y)
            elif perso[position] == "Bugs":
                fen.blit(CASE_BLUE, (pos_x, pos_y))
                fen.blit(PICTURE_BUG_BLACK, (pos_x, pos_y))
            elif perso[position] == "Empty_cliked":
                fen.blit(CASE_GREY, (pos_x, pos_y))
            elif perso[position] == "Bugs_player_cliked":
                fen.blit(CASE_RED, (pos_x, pos_y))
                fen.blit(PICTURE_BUG_RED, (pos_x, pos_y))
            elif perso[position] == "Bugs_opponent_cliked":
                fen.blit(CASE_GREEN, (pos_x, pos_y))
                fen.blit(PICTURE_BUG_GREEN, (pos_x, pos_y))
            position +=1
            pos_x += 100
        pos_x = pos_x_initial
        pos_y += 100

def find_position(pos_x, pos_y):
    x,y = 0,0
    if event.type == pygame.MOUSEBUTTONDOWN:
        #	Récupérer la position du clic
        x,y = event.pos
    for i in range(0, level.NUMBER_OF_ROW, 1):
        if pos_y+(i*100) < y < (75+pos_y)+(i*100):
            for j in range(0, level.NUMBER_OF_COLUMN, 1):
                if pos_x+(j*100) < x < (75+pos_x)+(j*100):
                    #	Calculer le numéro de la case
                    case = i*level.NUMBER_OF_COLUMN+(j+1)
                    return case

def hide_bugs():
    global bugs_to_hide
    global checkerboard_player
    if event.type == pygame.MOUSEBUTTONDOWN and find_position(level.PLAYER_POS_X,level.PLAYER_POS_Y) != None:
        if checkerboard_player[find_position(level.PLAYER_POS_X,level.PLAYER_POS_Y)-1] == "Empty" and level.bugs_to_hide > 0:
            checkerboard_player[find_position(level.PLAYER_POS_X,level.PLAYER_POS_Y)-1] = "Bugs"
            level.bugs_to_hide -= 1
            PLOUF_SOUND.play()

def opponent_hide_bugs(bugs_number):
    global checkerboard_opponent
    while bugs_number > 0 and opponent_bugs_hidden == False:
        #   Choisir un nombre entre 0 et le maximum
        nb_case = (level.NUMBER_OF_ROW * level.NUMBER_OF_COLUMN)-1
        nb_aleatoire = random.randrange(0,nb_case,1)
        if checkerboard_opponent[nb_aleatoire] == "Empty":
            checkerboard_opponent[nb_aleatoire] = "Bugs_opponent"
            bugs_number -= 1
    if bugs_number == 0 :
        return True

def show_bugs_number_to_hide():
        '''
        Function that count number of bugs to hidde
        '''
        fen.blit(BUGS_NUMBER_TO_HIDE, (600, 25))
        if level.bugs_to_hide ==1:
            fen.blit(NUMBER_1, (800, 25))
        elif level.bugs_to_hide ==2:
            fen.blit(NUMBER_2, (800, 25))
        elif level.bugs_to_hide ==3:
            fen.blit(NUMBER_3, (800, 25))
        elif level.bugs_to_hide ==4:
            fen.blit(NUMBER_4, (800, 25))
        elif level.bugs_to_hide ==5:
            fen.blit(NUMBER_5, (800, 25))

def show_bugs_to_hide(pos_x, pos_y):
    '''
    Function that display a bug picture when mouse is over case of player checkerboard
    '''
    pos_x_initial = pos_x
    pos_y_initial = pos_y
    #	Get position of click
    if bugs_hidden == False:
        x,y = mouse_pos
        for i in range(0, level.NUMBER_OF_ROW, 1):
            if pos_y_initial+(i*100) < y < (75+pos_y_initial)+(i*100):
                for j in range(0, level.NUMBER_OF_COLUMN, 1):
                    if pos_x_initial+(j*100) < x < (75+pos_x_initial)+(j*100):
                        #	Calculate new number of case
                        case = i*level.NUMBER_OF_COLUMN+(j+1)
                        if checkerboard_player[case-1] == "Empty":
                            #pygame.mouse.set_visible(False)
                            fen.blit(PICTURE_BUG_BLACK, (pos_x, pos_y))
                    pos_x += 100
            pos_x = pos_x_initial
            pos_y += 100

def end_of_turn(perso):
    '''
    Function to change turn number
    '''
    global turn_counter
    if perso == "player":
        turn_counter += 1
        return False
    elif perso == "opponent":
        return True

def player_search_action():
    '''
    Player action after click on case in opponnent checkerboard
    '''
    global checkerboard_opponent
    global opponent_bugs
    global player_turn
    if event.type == pygame.MOUSEBUTTONDOWN and find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y) != None and checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] != "Empty_cliked" and checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] != "Bugs_opponent_cliked":
        if checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] == "Empty":
            checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] = "Empty_cliked"
            PLOUF_SOUND.play()
            replace_text(MSG_NO_BUG_FOUND, FROG_YELLOW, 1300)
        elif checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] == "Bugs_opponent":
            checkerboard_opponent[find_position(level.OPPONENT_POS_X,level.OPPONENT_POS_Y)-1] = "Bugs_opponent_cliked"
            SUCCES_SOUND.play()
            level.opponent_bugs -= 1
            replace_text(MSG_BUG_FOUND, FROG_EATING, 1300)
        player_turn = end_of_turn("player")

def show_manifying_glass():
    '''
    Display a manifying glass when mouse is ovser case in opponnent checkerboard
    '''
    pos_x_initial = level.OPPONENT_POS_X
    pos_x = level.OPPONENT_POS_X
    pos_y_initial = level.OPPONENT_POS_Y
    pos_y = level.OPPONENT_POS_Y
    #	Get position of click
    if bugs_hidden == True:
        x,y = mouse_pos
        for i in range(0, level.NUMBER_OF_ROW, 1):
            if pos_y_initial+(i*100) < y < (75+pos_y_initial)+(i*100):
                for j in range(0, level.NUMBER_OF_COLUMN, 1):
                    if pos_x_initial+(j*100) < x < (75+pos_x_initial)+(j*100):
                        #	Calculate new number of case
                        case = i*level.NUMBER_OF_COLUMN+(j+1)
                        if checkerboard_opponent[case-1] == "Empty" or checkerboard_opponent[case-1] == "Bugs_opponent":
                            #	Hidde mouse
                            #   pygame.mouse.set_visible(False)
                            fen.blit(MAGNIFYING_GLASS, (pos_x, pos_y))
                    pos_x += 100
            pos_x = pos_x_initial
            pos_y += 100

def show_red_cross():
    '''
    Display a red cross when mouse is over player checkerboard after hidde of bugs
    '''
    pos_x_initial = level.PLAYER_POS_X
    pos_x = level.PLAYER_POS_X
    pos_y_initial = level.PLAYER_POS_Y
    pos_y = level.PLAYER_POS_Y
    #	Get mouse position
    if bugs_hidden == True:
        x,y = mouse_pos
        for i in range(0, level.NUMBER_OF_ROW, 1):
            if pos_y_initial+(i*100) < y < (75+pos_y_initial)+(i*100):
                for j in range(0, level.NUMBER_OF_COLUMN, 1):
                    if pos_x_initial+(j*100) < x < (75+pos_x_initial)+(j*100):
                        #	Calculer le numéro de la case
                        case = i*level.NUMBER_OF_COLUMN+(j+1)
                        if checkerboard_player[case-1] == "Empty":
                            #	Masquer la sourie
                            #   pygame.mouse.set_visible(False)
                            fen.blit(RED_CROSS, (pos_x, pos_y))
                    pos_x += 100
            pos_x = pos_x_initial
            pos_y += 100

def replace_text(msg, frog_color, duration):
    '''
    Function that replace text
    '''
    #   Erase element in screen
    fen.fill(WHITE)
    fen.blit(level.BACKGROUND_GAME, (0,0))
    display_checkerboard(checkerboard_player, level.PLAYER_POS_X, level.PLAYER_POS_Y)
    display_checkerboard(checkerboard_opponent, level.OPPONENT_POS_X, level.OPPONENT_POS_Y)
    fen.blit(frog_color, (0,600))
    fen.blit(ETANG_JOUEUR, (200, 25))
    fen.blit(ETANG_ADVERSAIRE, (850, 25))
    fen.blit(msg, (225, 650))
    #   Call pause menu
    RECT_PAUSE = fen.blit(PAUSE_MENU, (1100, 20))
    if RECT_PAUSE.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
        page = "pauseMenu"
    pygame.display.update()
    pygame.time.wait(duration)

def checkSoundStatus():
    '''
    Function that check in Options.txt file if sound is actived or disabled
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
    Sound option
    Edit data in Options.txt file
    Search sound line in file then edit with new status
    '''
    soundFile = open(DIRECTORYNAME + "/Data/Options.txt", "r", encoding="utf8")
    replacement = ""
    #   Read each lines of options file
    for line in soundFile:
        #   Remove empties spaces before and after string
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
    #   Edit options file
    soundFileWriting = open(DIRECTORYNAME + "/Data/Options.txt", "w", encoding="utf8")
    soundFileWriting.write(replacement)
    soundFileWriting.close()
    checkSoundStatus()

def highScoreSaving():
    '''
    Compare highscore in file with new score in game and write new highscore if it's better
    '''
    highScoreFile = open(DIRECTORYNAME + "/Data/HighScore.txt", "r", encoding="utf8")
    replacement = ""
    #   Read each lines of highscore file
    for line in highScoreFile:
        if(line.find(level.levelName) != -1):
            lineParsed = line.split(" ")
            actualScore = int(lineParsed[1])
            if (actualScore > turn_counter):
                replacement = replacement + lineParsed[0] + " " + str(turn_counter) + "\n"
            else:
                replacement = replacement + line #+ "\n"
        else:
            replacement = replacement + line #+ "\n"
    highScoreFile.close()
    #   Edit highscore file
    highScoreFileWriting = open(DIRECTORYNAME + "/Data/HighScore.txt", "w", encoding="utf8")
    highScoreFileWriting.write(replacement)
    highScoreFileWriting.close()

def highScoreReading(currentLevel):
    '''
    Read and return highscore for current level
    '''
    highScoreFile = open(DIRECTORYNAME + "/Data/HighScore.txt", "r", encoding="utf8")
    #   Read each lines of highscore file
    for line in highScoreFile:
        if(line.find(currentLevel.levelName) != -1):
            lineParsed = line.split(" ")
            highScore = int(lineParsed[1])
            return highScore
    highScoreFile.close()

def resetHighScore():
    '''
    Reset high-scores
    '''
    scoreFile = open(DIRECTORYNAME + "/Data/HighScore.txt", "r", encoding="utf8")
    replacement = ""
    #   Read each lines of highscore file
    for line in scoreFile:
        lineParsed = line.split(" ")
        replacement = replacement + lineParsed[0] + " " + "99" + "\n"
    scoreFile.close()
    #   Edit highscore file with "99"
    resetScoreWriting = open(DIRECTORYNAME + "/Data/HighScore.txt", "w", encoding="utf8")
    resetScoreWriting.write(replacement)
    resetScoreWriting.close()

def displayCounter(number, posX, posY):
    '''
    Function that display a counter
    '''
    numberString = str(number)
    if(len(numberString) == 1):
        fen.blit(NUMBER_0_XL, (posX, posY))
        fen.blit(chooseNumberCounter(numberString[0], "black"), (posX + 35, posY))
    elif(len(numberString) == 2):
        fen.blit(chooseNumberCounter(numberString[0], "black"), (posX, posY))
        fen.blit(chooseNumberCounter(numberString[1], "black"), (posX + 35, posY))

def displayLaurelWreath(currentLevel, posX, posY):
    '''
    Function that display a laurel wreath and high-score in level menu
    '''
    highScoreFile = open(DIRECTORYNAME + "/Data/HighScore.txt", "r", encoding="utf8")
    #   Read each lines of highscore file
    for line in highScoreFile:
        if(line.find(currentLevel) != -1):
            lineParsed = line.split(" ")
            numberString = lineParsed[1]
            if(int(numberString) != 99):
                fen.blit(LAUREL_WREATH, (posX + 100, posY + 75))
                numberString = str(numberString)
                if(len(numberString) == 2):
                    fen.blit(NUMBER_0_XL_GOLD, (posX +15, posY+75))
                    fen.blit(chooseNumberCounter(numberString[0], "gold"), (posX + 50, posY + 75))
                elif(len(numberString) == 3):
                    fen.blit(chooseNumberCounter(numberString[0], "gold"), (posX + 15, posY + 75))
                    fen.blit(chooseNumberCounter(numberString[1], "gold"), (posX + 50, posY + 75))
    highScoreFile.close()

def chooseNumberCounter(number, color):
    '''
    Function that return a text for number counter
    '''
    if(color == "black"):
        match number:
            case "0":
                return NUMBER_0_XL
            case "1":
                return NUMBER_1_XL
            case "2":
                return NUMBER_2_XL
            case "3":
                return NUMBER_3_XL
            case "4":
                return NUMBER_4_XL
            case "5":
                return NUMBER_5_XL
            case "6":
                return NUMBER_6_XL
            case "7":
                return NUMBER_7_XL
            case "8":
                return NUMBER_8_XL
            case "9":
                return NUMBER_9_XL
    elif(color == "gold"):
        match number:
            case "0":
                return NUMBER_0_XL_GOLD
            case "1":
                return NUMBER_1_XL_GOLD
            case "2":
                return NUMBER_2_XL_GOLD
            case "3":
                return NUMBER_3_XL_GOLD
            case "4":
                return NUMBER_4_XL_GOLD
            case "5":
                return NUMBER_5_XL_GOLD
            case "6":
                return NUMBER_6_XL_GOLD
            case "7":
                return NUMBER_7_XL_GOLD
            case "8":
                return NUMBER_8_XL_GOLD
            case "9":
                return NUMBER_9_XL_GOLD

def initialisation_of_variables():
    '''
    Reset variables at beginning of level
    '''
    global turn_counter
    global checkerboard_player
    global checkerboard_opponent
    global initialisation_player
    global initialisation_opponent
    global player_turn
    global bugs_hidden
    global opponent_bugs_hidden
    global scoreSaving

    turn_counter = 0
    checkerboard_player = []
    checkerboard_opponent = []
    initialisation_player = False
    initialisation_opponent = False
    player_turn = True
    bugs_hidden = False
    opponent_bugs_hidden = False
    scoreSaving = True

####
#
#	Class
#
####

class Level:
    '''
    Variables related to levels
    '''
    def __init__(self, levelName, player_bugs, opponent_bugs, bugs_to_hide, PLAYER_POS_X, PLAYER_POS_Y, OPPONENT_POS_X, OPPONENT_POS_Y, NUMBER_OF_COLUMN, NUMBER_OF_ROW, BACKGROUND_GAME):
        self._levelName = levelName
        self._player_bugs = player_bugs
        self._opponent_bugs = opponent_bugs
        self._bugs_to_hide = bugs_to_hide
        self._PLAYER_POS_X = PLAYER_POS_X
        self._PLAYER_POS_Y = PLAYER_POS_Y
        self._OPPONENT_POS_X = OPPONENT_POS_X
        self._OPPONENT_POS_Y = OPPONENT_POS_Y
        self._NUMBER_OF_COLUMN = NUMBER_OF_COLUMN
        self._NUMBER_OF_ROW = NUMBER_OF_ROW
        self._BACKGROUND_GAME = BACKGROUND_GAME

    '''
    Getter et setter
    '''
    @property
    def levelName(self):
        return self._levelName
    
    @levelName.setter
    def levelName(self, value):
        self._levelName = value

    @property
    def player_bugs(self):
        return self._player_bugs

    @player_bugs.setter
    def player_bugs(self, value):
        self._player_bugs = value

    @property
    def opponent_bugs(self):
        return self._opponent_bugs

    @opponent_bugs.setter
    def opponent_bugs(self, value):
        self._opponent_bugs = value

    @property
    def bugs_to_hide(self):
        return self._bugs_to_hide

    @bugs_to_hide.setter
    def bugs_to_hide(self, value):
        self._bugs_to_hide = value

    @property
    def PLAYER_POS_X(self):
        return self._PLAYER_POS_X

    @PLAYER_POS_X.setter
    def PLAYER_POS_X(self, value):
        self._PLAYER_POS_X = value

    @property
    def PLAYER_POS_Y(self):
        return self._PLAYER_POS_Y

    @PLAYER_POS_Y.setter
    def PLAYER_POS_Y(self, value):
        self._PLAYER_POS_Y = value

    @property
    def OPPONENT_POS_X(self):
        return self._OPPONENT_POS_X

    @OPPONENT_POS_X.setter
    def OPPONENT_POS_X(self, value):
        self._OPPONENT_POS_X = value

    @property
    def OPPONENT_POS_Y(self):
        return self._OPPONENT_POS_Y

    @OPPONENT_POS_Y.setter
    def OPPONENT_POS_Y(self, value):
        self._OPPONENT_POS_Y = value

    @property
    def NUMBER_OF_COLUMN(self):
        return self._NUMBER_OF_COLUMN

    @NUMBER_OF_COLUMN.setter
    def NUMBER_OF_COLUMN(self, value):
        self._NUMBER_OF_COLUMN = value

    @property
    def NUMBER_OF_ROW(self):
        return self._NUMBER_OF_ROW

    @NUMBER_OF_ROW.setter
    def NUMBER_OF_ROW(self, value):
        self._NUMBER_OF_ROW = value

    @property
    def BACKGROUND_GAME(self):
        return self._BACKGROUND_GAME

    @BACKGROUND_GAME.setter
    def BACKGROUND_GAME(self, value):
        self._BACKGROUND_GAME = value

####
#
#	Run game
#
####

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            RUNNING = False

    #   Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    if page == "menu":
        fen.fill(GREEN_LIGHT)
        fen.blit(BACKGROUND_MENU, (0,0))
        fen.blit(TITLE, TITLE_CENTER)
        RECT_MENU_PLAY =fen.blit(MENU_PLAY, MENU_PLAY_CENTER)
        RECT_MENU_OPTION = fen.blit(MENU_OPTION, MENU_OPTION_CENTER)
        RECT_MENU_CREDIT = fen.blit(MENU_CREDIT, MENU_CREDIT_CENTER)
        RECT_MENU_QUIT = fen.blit(MENU_QUIT, MENU_QUIT_CENTER)
        #   Initialisation of sound
        checkSoundStatus()
        #   Check if mouse position is in the rect
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
        fen.blit(MENU_CREDIT_BRUNO, MENU_CREDIT_BRUNO_CENTER)
        fen.blit(MENU_CREDIT_GRAPHISME, MENU_CREDIT_GRAPHISME_CENTER)
        fen.blit(MENU_CREDIT_FONT, MENU_CREDIT_FONT_CENTER)
        fen.blit(MENU_CREDIT_SOUND, MENU_CREDIT_SOUND_CENTER)
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, RETURN_MENU_FROM_MENU_CENTER)
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "menu_level":
        fen.fill(GREEN_LIGHT)
        RECT_LEVEL_1 = fen.blit(LEVEL_1, (125,200))
        displayLaurelWreath("level_01", 125, 200)
        RECT_LEVEL_2 = fen.blit(LEVEL_2, (325,200))
        displayLaurelWreath("level_02", 325, 200)
        RECT_LEVEL_3 = fen.blit(LEVEL_3, (525,200))
        displayLaurelWreath("level_03", 525, 200)       
        RECT_LEVEL_4 = fen.blit(LEVEL_4, (725,200))
        displayLaurelWreath("level_04", 725, 200)   
        RECT_LEVEL_5 = fen.blit(LEVEL_5, (925,200))
        displayLaurelWreath("level_05", 925, 200)   
        RECT_LEVEL_6 = fen.blit(LEVEL_6, (125,500))
        displayLaurelWreath("level_06", 125, 500)   
        RECT_LEVEL_7 = fen.blit(LEVEL_7, (325,500))
        displayLaurelWreath("level_07", 325, 500)  
        RECT_LEVEL_8 = fen.blit(LEVEL_8, (525,500))
        displayLaurelWreath("level_08", 525, 500)  
        RECT_LEVEL_9 = fen.blit(LEVEL_9, (725,500))
        displayLaurelWreath("level_09", 725, 500)  
        RECT_LEVEL_10 = fen.blit(LEVEL_10, (925,500))
        displayLaurelWreath("level_10", 925, 500)  
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, RETURN_MENU_FROM_MENU_CENTER)
        if RECT_LEVEL_1.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level1")
            page = "loadingPage"
        if RECT_LEVEL_2.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level2")
            page = "loadingPage"
        if RECT_LEVEL_3.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level3")
            page = "loadingPage"
        if RECT_LEVEL_4.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level4")
            page = "loadingPage"
        if RECT_LEVEL_5.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level5")
            page = "loadingPage"
        if RECT_LEVEL_6.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level6")
            page = "loadingPage"
        if RECT_LEVEL_7.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level7")
            page = "loadingPage"
        if RECT_LEVEL_8.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level8")
            page = "loadingPage"
        if RECT_LEVEL_9.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level9")
            page = "loadingPage"
        if RECT_LEVEL_10.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = choose_level("level10")
            page = "loadingPage"
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "options":
        fen.fill(GREEN_LIGHT)
        RECT_RETURN_MENU = fen.blit(RETURN_MENU, RETURN_MENU_FROM_MENU_CENTER)
        fen.blit(OPTION_SOUND_OPTION, (225, 250))
        if(checkSoundStatus() == True):
            RECT_SOUND_MENU = fen.blit(OPTION_SOUND_ON, (350, 250))
        else:
            RECT_SOUND_MENU = fen.blit(OPTION_SOUND_OFF, (350, 250))
        if RECT_SOUND_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            modifySoundStatus()
            pygame.time.wait(250)
        RECT_ERASE_SCORE = fen.blit(OPTION_ERASE, (225,350))
        if RECT_ERASE_SCORE.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            resetHighScore()
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "menu"

    elif page == "level":
        #	Creation of checkerboard's list
        initialisation_player = initialisation_checkerboard_player()
        initialisation_opponent = initialisation_checkerboard_opponent()
        fen.fill(WHITE)
        fen.blit(level.BACKGROUND_GAME, (0,0))
        if level.levelName == "level_06":
            checkerboard_player[5] = "Empty_cliked"
            checkerboard_player[10] = "Empty_cliked"
            checkerboard_player[15] = "Empty_cliked"
        elif level.levelName == "level_07":
            checkerboard_player[6] = "Empty_cliked"
            checkerboard_player[7] = "Empty_cliked"
            checkerboard_player[11] = "Empty_cliked"
            checkerboard_player[12] = "Empty_cliked"
        elif level.levelName == "level_08":
            checkerboard_player[6] = "Empty_cliked"
            checkerboard_player[7] = "Empty_cliked"
            checkerboard_player[8] = "Empty_cliked"
            checkerboard_player[11] = "Empty_cliked"
            checkerboard_player[12] = "Empty_cliked"
            checkerboard_player[13] = "Empty_cliked"
        elif level.levelName == "level_09":
            checkerboard_player[15] = "Empty_cliked"
            checkerboard_player[16] = "Empty_cliked"
            checkerboard_player[17] = "Empty_cliked"
            checkerboard_player[18] = "Empty_cliked"
            checkerboard_player[19] = "Empty_cliked"
            checkerboard_player[20] = "Empty_cliked"
            checkerboard_player[21] = "Empty_cliked"
            checkerboard_player[22] = "Empty_cliked"
            checkerboard_player[23] = "Empty_cliked"
            checkerboard_player[24] = "Empty_cliked"
        elif level.levelName == "level_10":
            checkerboard_player[0] = "Empty_cliked"
            checkerboard_player[1] = "Empty_cliked"
            checkerboard_player[2] = "Empty_cliked"
            checkerboard_player[3] = "Empty_cliked"
            checkerboard_player[4] = "Empty_cliked"
            checkerboard_player[5] = "Empty_cliked"
            checkerboard_player[6] = "Empty_cliked"
            checkerboard_player[7] = "Empty_cliked"
            checkerboard_player[8] = "Empty_cliked"
            checkerboard_player[9] = "Empty_cliked"

        display_checkerboard(checkerboard_player, level.PLAYER_POS_X, level.PLAYER_POS_Y)
        fen.blit(ETANG_JOUEUR, (200, 25))
        fen.blit(FROG_GREEN, (0,600))
        #   Show pause menu
        RECT_PAUSE = fen.blit(PAUSE_MENU, (1100, 20))
        if RECT_PAUSE.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(250)
            page = "pauseMenu"
        #   Show informations at beginning of game
        if bugs_hidden == False:
            fen.blit(MSG_GAME_START, (225, 650))
            fen.blit(MSG_GAME_START_RULES, (225, 700))
            show_bugs_number_to_hide()
            hide_bugs()
            if level.bugs_to_hide == 0:
                bugs_hidden = True
        elif bugs_hidden == True:
            #   Show opponent pond
            fen.blit(ETANG_ADVERSAIRE, (850, 25))
            display_checkerboard(checkerboard_opponent, level.OPPONENT_POS_X, level.OPPONENT_POS_Y)
            #	Hidde bugs in opponent pond
            opponent_bugs_hidden = opponent_hide_bugs(level.opponent_bugs)
            #	Show manifying glass or red cross when over cases
            show_manifying_glass()
            show_red_cross()
            if level.player_bugs > 0 and level.opponent_bugs > 0:
                if player_turn == True:
                    fen.blit(FROG_GREEN, (0,600))
                    fen.blit(MSG_PLAYER_TURN, (225, 650))
                    fen.blit(MSG_PLAYER_TURN_RULES, (225, 700))
                    #   Action when player click on opponent case
                    player_search_action()
                    opponent_turn_start = True
                else:
                    #   Display a message before action of opponnent
                    if opponent_turn_start == True and player_turn == False:
                        fen.fill(WHITE)
                        fen.blit(level.BACKGROUND_GAME, (0,0))
                        display_checkerboard(checkerboard_player, level.PLAYER_POS_X, level.PLAYER_POS_Y)
                        display_checkerboard(checkerboard_opponent, level.OPPONENT_POS_X, level.OPPONENT_POS_Y)
                        fen.blit(ETANG_JOUEUR, (200, 25))
                        fen.blit(ETANG_ADVERSAIRE, (850, 25))
                        fen.blit(PAUSE_MENU, (1100, 20))
                        fen.blit(FROG_DISAPPOINTED, (0,600))
                        fen.blit(MSG_OPPONNENT_TURN, (225, 650))
                        pygame.display.update()
                        pygame.time.wait(1300)
                        opponent_turn_start = False
                    #   Action of opponent
                    random_number = random.randrange(0,((level.NUMBER_OF_ROW * level.NUMBER_OF_COLUMN)-1),1)
                    while checkerboard_player[random_number] == "Empty_cliked" or checkerboard_player[random_number] == "Bugs_player_cliked" or random_number == -1:
                        random_number = random.randrange(0,((level.NUMBER_OF_ROW * level.NUMBER_OF_COLUMN)-1),1)
                    if checkerboard_player[random_number] == "Empty":
                        checkerboard_player[random_number] = "Empty_cliked"
                        PLOUF_SOUND.play()
                        replace_text(MSG_OUF_NO_BUG_FOUND, FROG_GREEN, 1300)
                    elif checkerboard_player[random_number] == "Bugs":
                        checkerboard_player[random_number] = "Bugs_player_cliked"
                        level.player_bugs -= 1
                        ERROR_SOUND.play()
                        replace_text(MSG_BUG_PLAYER_FOUND, FROG_RED, 1300)
                    player_turn = end_of_turn("opponent")
            elif level.player_bugs == 0 or level.opponent_bugs == 0:
                if level.player_bugs == 0:
                    fen.blit(FROG_RED, (0,600))
                    fen.blit(MSG_END_LOSE, (225, 650))
                else:
                    fen.blit(FROG_HAPPY, (0,600))
                    fen.blit(MSG_END_WIN, (225, 650))
                    if(scoreSaving == True):
                        highScoreSaving()
                        scoreSaving = False
                RECT_RETURN_MENU = fen.blit(RETURN_MENU, RETURN_MENU_FROM_MENU_CENTER)
                if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    page = "menu"

    elif page == "pauseMenu":
        '''
        Pause menu
        '''
        fen.blit(BACKGROUND_PAUSE, (100, 100))
        fen.blit(MENU_TURN_NUMBER, (425, 350))
        displayCounter(turn_counter, 725, 350)
        fen.blit(MENU_PAUSE, MENU_PAUSE_CENTER)
        RECT_PAUSE = fen.blit(PAUSE_MENU, (1100, 20))
        if RECT_PAUSE.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(250)
            page = "level"
        RECT_RETURN_GAME = fen.blit(RETURN_GAME, RETURN_GAME_CENTER)
        if RECT_RETURN_GAME.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "level"
        #   Edit on options
        fen.blit(OPTION_SOUND_OPTION, (425, 250))
        if(checkSoundStatus() == True):
            RECT_SOUND_MENU = fen.blit(OPTION_SOUND_ON, (600, 250))
        else:
            RECT_SOUND_MENU = fen.blit(OPTION_SOUND_OFF, (600, 250))
        if RECT_SOUND_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            modifySoundStatus()
            pygame.time.wait(250)
        #   Display best score
        fen.blit(MENU_PAUSE_HIGH_SCORE, (425, 450))
        if highScoreReading(level) != 99:
            displayCounter(highScoreReading(level), 725, 450)
        else:
            displayCounter(0, 725, 450)
        #   Return to main menu
        RECT_RETURN_MENU = fen.blit(RETURN_MENU_FROM_PAUSE, RETURN_MENU_FROM_PAUSE_CENTER)
        if RECT_RETURN_MENU.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            nextPage = "menu"
            page = "loadingPage"

    elif page =="loadingPage":
        fen.fill(BLUE_DARK)
        if (event.type == pygame.MOUSEBUTTONUP):
            page = nextPage    

    #	Update of screen
    pygame.display.update()
    CLOCK.tick(FPS)