######################## 
#	HelpFrog
#	Bruno MAUCOURT
#	Novembre 2022
######################## 

#   Importer les modules
import pygame
import sys
import random

pygame.init()

####
#
#	Initialiser l'écran
#
####

fen = pygame.display.set_mode((1200, 800))
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

# fps = frames per second
# Plus fps est élevé, moins il y aura d'attente entre deux
# rafraîchissement d'images
# Une vidéo est diffusée à 25 FPS
FPS = 25

#   Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

####
#
#	Initialiser le texte
#
####

# Taille (en points) utilisée pour les textes qui sont affichés
FONT_CLASSIC = 25
FONT_TITLE = 150
FONT_MENU = 50

# Préparation de la Police utilisée pour l'affichage des textes
FONT_CLASSIC = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_CLASSIC)
FONT_MENU = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_MENU)
FONT_TITLE = pygame.font.Font("Fonts/Magical_Story.ttf", FONT_TITLE)

# Préparation du rendu du texte
TITLE = FONT_TITLE.render("help(frog)", True, WHITE)
MENU_PLAY = FONT_MENU.render("Jouer", True, BLACK)
MENU_QUIT = FONT_MENU.render("Quitter", True, BLACK)
RETURN_MENU = FONT_CLASSIC.render("Retourner au menu", True, BLACK)
MSG_GAME_START = FONT_CLASSIC.render("La méchante grenouille veut voler les insectes que j'ai chasé. Aide moi a les cacher dans mon étang.", True, BLACK)
MSG_GAME_START_RULES = FONT_CLASSIC.render("Clique sur les cases pour cacher mes insectes.", True, BLACK)
MSG_PLAYER_TURN = FONT_CLASSIC.render("C'est à mon tour de jouer. Aide moi à trouver les insectes que l'on m'a volé.", True, BLACK)
MSG_PLAYER_TURN_RULES = FONT_CLASSIC.render("Clique sur les cases de l'étang de l'adversaire pour chercher mes insectes.", True, BLACK)
MSG_OPPONNENT_TURN = FONT_CLASSIC.render("C'est au tour de mon adversaire de jouer. J'espère qu'il ne trouvera pas mes insectes.", True, BLACK)
NUMBER_1 = FONT_CLASSIC.render("1", True, BLACK)
NUMBER_2 = FONT_CLASSIC.render("2", True, BLACK)
NUMBER_3 = FONT_CLASSIC.render("3", True, BLACK)
BUGS_NUMBER_TO_HIDE = FONT_CLASSIC.render("Insectes à cacher", True, BLACK)
ETANG_JOUEUR = FONT_CLASSIC.render("Etang du joueur", True, WHITE)
ETANG_ADVERSAIRE = FONT_CLASSIC.render("Etang de l adversaire", True, WHITE)
MSG_SUPER = FONT_CLASSIC.render("Super", True, BLACK)
MSG_END_GAME = FONT_CLASSIC.render("La partie est finie !", True, BLACK)
MSG_END_LOSE = FONT_CLASSIC.render("Saperlipopette, la méchante grenouille a volé tous mes insectes. Je ne te remercie pas pour ton aide", True, BLACK)
MSG_END_WIN = FONT_CLASSIC.render("Hourra, j'ai bien mange. Merci pour ton aide.", True, BLACK)

# Pour calculer la taille que prend le texte et le centrer
TITLE_RECT = TITLE.get_rect(center=(600, 200))

####
#
#	Initialiser les images
#
####

FROG_GREEN = pygame.image.load("Pictures/Frog_green.png").convert_alpha()
FROG_YELLOW = pygame.image.load("Pictures/Frog_yellow.png").convert_alpha()
FROG_RED = pygame.image.load("Pictures/Frog_red.png").convert_alpha()
PICTURE_BUG = pygame.image.load("Pictures/Bug.png").convert_alpha()
PICTURE_BUG = pygame.transform.scale(PICTURE_BUG, (75, 75))
LOGO_FROG = pygame.image.load("Pictures/Frog_green.png").convert_alpha()

#	Utiliser un logo pour la fenêtre 
pygame.display.set_icon(LOGO_FROG)

####
#
#	Initialiser les bruitages
#
####

pygame.mixer.init()
PLOUF_SOUND = pygame.mixer.Sound("Sounds/Plouf.mp3")
ERROR_SOUND = pygame.mixer.Sound("Sounds/Error.mp3")
SUCCES_SOUND = pygame.mixer.Sound("Sounds/Succes.mp3")

####
#
#	Variables à initialiser en début de partie
#
####

page = "menu"
continuer = True

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
        for i in (0, 1, 2, 3, 4):
            for j in (0, 1, 2, 3, 4):
                checkerboard_player.insert(position, "Empty")
            position +=1
    return True

def initialisation_checkerboard_opponent():
    position = 0
    global initialisation_opponent
    global checkerboard_opponent
    if initialisation_opponent == False:
        for i in (0, 1, 2, 3, 4):
            for j in (0, 1, 2, 3, 4):
                checkerboard_opponent.insert(position, "Empty")
            position +=1
    return True

def display_checkerboard(perso, pos_x, pos_y):
    position = 0
    global checkerboard_player
    pos_x_initial = pos_x
    for i in (0, 1, 2, 3, 4):
        for j in (0, 1, 2, 3, 4):
            if perso[position] == "Empty" or perso[position] == "Bugs_opponent":
                pygame.draw.rect(fen, BLUE, (pos_x, pos_y, 75, 75))
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
    for i in (0, 1, 2, 3, 4):
        if pos_y+(i*100) < y < (75+pos_y)+(i*100):
            for j in (0, 1, 2, 3, 4):
                if pos_x+(j*100) < x < (75+pos_x)+(j*100):
                    #	Calculer le numéro de la case
                    case = i*5+(j+1)
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
        #   Choisir un nombre entre 0 et 24
        nb_aleatoire = random.randrange(0,24,1)
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

#	Fonction pour changer de tour
def end_of_turn(perso):
    if perso == "player":
        return False
    elif perso == "opponent":
        return True

#	Action lorsque le joueur clique sur une case de l'étang adverse
def player_search_action():
    global checkerboard_opponent
    global opponent_bugs
    global player_turn
    if event.type == pygame.MOUSEBUTTONDOWN and find_position(OPPONENT_POS_X,OPPONENT_POS_Y) != None and checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] != "Empty_cliked" and checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] != "Bugs_opponent_cliked":
        if checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] == "Empty":
            checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] = "Empty_cliked"
            PLOUF_SOUND.play()
            display_checkerboard(checkerboard_opponent, OPPONENT_POS_X, OPPONENT_POS_Y)
        elif checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] == "Bugs_opponent":
            checkerboard_opponent[find_position(OPPONENT_POS_X,OPPONENT_POS_Y)-1] = "Bugs_opponent_cliked"
            SUCCES_SOUND.play()
            opponent_bugs -= 1
        player_turn = end_of_turn("player")

#	Réinitialiser les variables
def initialisation_of_variables():
    global checkerboard_player
    global checkerboard_opponent
    global initialisation_player
    global initialisation_opponent
    global player_bugs
    global opponent_bugs
    global bugs_to_hide
    global BUGS_HIDDEN
    global opponent_bugs_hidden
    global PLAYER_POS_X
    global PLAYER_POS_Y
    global OPPONENT_POS_X
    global OPPONENT_POS_Y
    global player_turn

    checkerboard_player = []
    checkerboard_opponent = []
    initialisation_player = False
    initialisation_opponent = False
    player_bugs = 3
    opponent_bugs = 3
    bugs_to_hide = 3
    BUGS_HIDDEN = False
    opponent_bugs_hidden = False
    PLAYER_POS_X = 25
    PLAYER_POS_Y = 75
    OPPONENT_POS_X = 700
    OPPONENT_POS_Y = 75
    player_turn = True

####
#
#	Lancer la partie
#
####

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
            
    if page == "menu":
        fen.fill(GREEN_LIGHT)
        fen.blit(TITLE, TITLE_RECT)
        RECT_MENU_PLAY = fen.blit(MENU_PLAY, (500, 400))
        RECT_MENU_QUIT = fen.blit(MENU_QUIT, (500, 600))
        initialisation_of_variables()
        # Get mouse position
        mpos = pygame.mouse.get_pos()
        # Check if position is in the rect
        if RECT_MENU_PLAY.collidepoint(mpos) and event.type == pygame.MOUSEBUTTONDOWN:
            page = "niveau1"
        elif RECT_MENU_QUIT.collidepoint(mpos) and event.type == pygame.MOUSEBUTTONDOWN:
            continuer = False
            
    elif page == "niveau1":
        #	Création des listes correspondantes aux damiers
        initialisation_player = initialisation_checkerboard_player()
        initialisation_opponent = initialisation_checkerboard_opponent()   
        #   Affichage de l'arrière plan   
        fen.fill(GREEN_LIGHT)
        display_checkerboard(checkerboard_player, PLAYER_POS_X, PLAYER_POS_Y)
        pygame.draw.rect(fen, WHITE, (0, 600, 1200, 200))
        fen.blit(ETANG_JOUEUR, (200, 25))
        if BUGS_HIDDEN == False:
            fen.blit(FROG_GREEN, (0,600))
            fen.blit(MSG_GAME_START, (225, 650))
            fen.blit(MSG_GAME_START_RULES, (225, 700))
            show_bugs_number_to_hide()
            hide_bugs()
            if bugs_to_hide == 0:
                BUGS_HIDDEN = True
        elif BUGS_HIDDEN == True:
            fen.blit(ETANG_ADVERSAIRE, (850, 25))
            display_checkerboard(checkerboard_opponent, OPPONENT_POS_X, OPPONENT_POS_Y)
            opponent_bugs_hidden = opponent_hide_bugs(3)
            if player_bugs > 0 and opponent_bugs > 0:
                if player_turn == True:
                    fen.blit(FROG_GREEN, (0,600))
                    fen.blit(MSG_PLAYER_TURN, (225, 650))
                    fen.blit(MSG_PLAYER_TURN_RULES, (225, 700))
                    #   Afficher une image pour indiquer que c'est au joueur de jouer
                    #	Action lorsque l'on clique sur une case de l'adversaire
                    player_search_action()
                else:
                    fen.blit(FROG_YELLOW, (0,600))
                    fen.blit(MSG_OPPONNENT_TURN, (225, 650))
                    #   Afficher une image pour indiquer que c'est à l'adversaire de jouer
                    pygame.display.update()
                    pygame.time.wait(2000)
                    random_number = random.randrange(0,24,1)
                    while checkerboard_player[random_number] == "Empty_cliked" or checkerboard_player[random_number] == "Bugs_cliked":
                        random_number = random.randrange(0,24,1)
                    if checkerboard_player[random_number] == "Empty":
                        checkerboard_player[random_number] = "Empty_cliked"
                        PLOUF_SOUND.play()
                    elif checkerboard_player[random_number] == "Bugs":
                        checkerboard_player[random_number] = "Bugs_player_cliked"
                        player_bugs -= 1
                        ERROR_SOUND.play()
                    player_turn = end_of_turn("opponent")
            elif player_bugs == 0 or opponent_bugs == 0:
                if player_bugs == 0:
                    fen.blit(FROG_RED, (0,600))
                    fen.blit(MSG_END_LOSE, (225, 650))
                else:
                    fen.blit(FROG_GREEN, (0,600))
                    fen.blit(MSG_END_WIN, (225, 650))
                RECT_RETURN_MENU = fen.blit(RETURN_MENU, (225, 750))
                mpos = pygame.mouse.get_pos()
                if RECT_RETURN_MENU.collidepoint(mpos) and event.type == pygame.MOUSEBUTTONDOWN:
                    page = "menu"

    #	Mise à jour de l'écran        
    pygame.display.update()
    horloge.tick(FPS)