import curses
import traitement_image
import sys

#  type_of_display=

grid = traitement_image.make_grid("/mnt/c/Users/DPVR5455/OneDrive - orange.com/Bureau/anniv_memorial.jpg")
regle_ligne, regle_colonne = traitement_image.make_info(grid)
playgame = traitement_image.make_empty(grid)
a_afficher = playgame
#  print(type(playgame))
#  print(playgame[0])
#  print(playgame)
for l in regle_ligne:
	print("stdscr.addstr(",len(l),"+max_regle_taille_y, 0, "+" ".join([str(b) for b in l])+")")
print(max([len(a) for a in regle_colonne]))

def make_affichage(stdscr, curr_x=0, curr_y=0):
	max_regle_taille_y = max([len(" ".join([str(b) for b in a])) for a in regle_ligne])
	max_regle_taille_x = max([len(a) for a in regle_colonne])
	#  affiche les regles pour chaques lignes
	for l in range(len(regle_ligne)):
		stdscr.addstr(l+max_regle_taille_x+1, 0, " ".join([str(b) for b in regle_ligne[l]]))
	#  affiche les regles pour chaques colonnes
	for c in range(len(regle_colonne)):
		for element in range(1, len(regle_colonne[c])+1):
			stdscr.addstr(max_regle_taille_x-element, max_regle_taille_y+1+c*2, str(regle_colonne[c][-element]))

	#  affiche la grille a afficher
	for x in range(a_afficher.shape[0]):
		for y in range(len(a_afficher)):
			if (a_afficher[y][x] == 255):
				s = "x "
			else:
				s = ". "
			if (curr_x == x and curr_y == y):
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y+max_regle_taille_x+1, (x*2)+max_regle_taille_y+1, s)
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.addstr(y+max_regle_taille_x+1, (x*2)+max_regle_taille_y+1, s)
	stdscr.refresh()

def main(stdscr):
	global a_afficher
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
	h, w = stdscr.getmaxyx()
	x=5
	y=5

	make_affichage(stdscr)
	
	curr_x = 0
	curr_y = 0
	while 1:
		key = stdscr.getch()
		if key == ord('h'):
			curr_x -= 1
		elif key == ord('j'):
			curr_y += 1
		elif key == ord('k'):
			curr_y -= 1
		elif key == ord('l'):
			curr_x += 1
		elif key == ord('a'):
			if traitement_image.compare_grille(a_afficher, playgame):
				a_afficher = grid
			else:
				a_afficher = playgame
		elif key == ord('q'):
			curses.endwin()
		elif key == ord(' '):
			playgame[curr_y][curr_x] = 255 - playgame[curr_y][curr_x]
		if curr_y < 0: curr_y = len(grid)-1
		if curr_y >= len(grid): curr_y = 0
		if curr_x < 0: curr_x = len(grid[0])-1
		if curr_x >= len(grid[0]): curr_x = 0
		make_affichage(stdscr, curr_x, curr_y)
		stdscr.refresh()

curses.wrapper(main)
