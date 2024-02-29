import cv2
import numpy as np
import sys

def gray_to_bw(img):
	for ligne in img:
		ligne[ligne > 128] = 255
		ligne[ligne <= 128] = 0
	return img

def make_info(img):
	a_l = []
	a_c = []
	for l in img:
		in_ligne = False
		curr = 0
		info_ligne = []
		for pos in l:
			if (pos == 0):
				curr += 1
				in_ligne = True
			else:
				if in_ligne:
					info_ligne += [curr]
					curr = 0
					in_ligne = False
		if curr > 0:
			info_ligne += [curr]
		if ( info_ligne != [] ): a_l += [info_ligne]
	for x in range(len(img[0])):
		in_ligne = False
		curr = 0
		info_ligne = []
		for y in range(len(img)):
			if (img[y][x] == 0):
				curr += 1
				in_ligne = True
			else:
				if in_ligne:
					info_ligne += [curr]
					curr = 0
					in_ligne = False
		if curr > 0:
			info_ligne += [curr]
		if ( info_ligne != [] ): a_c += [info_ligne]
	return a_l, a_c




	

img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)

#  cv2.imshow("base", img)


height, width = img.shape[:2]
w, h = (30, 30)
output = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
#  output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

gray_to_bw(output)

#  cv2.imshow("noir et blanc", img_bw)

cv2.imshow('pixel', output)
k = cv2.waitKey(0)

#  for l in output:
#      for i in l:
#          print(type(i))
#          print(i == 255)

print(output.shape)

all_ligne, all_colonne = make_info(output)
for l in range(len(output)):
	#  print(all_ligne[l],"#",list(output[l]))
	print(list(output[l]))
#  for l in all_ligne:
#      print(l)

print()
for block in range(max([len(a) for a in all_colonne])):
	print("",", ".join([str(c[block]) if len(c) > block else "  " for c in all_colonne ]))
#  print(all_colonne)
#  print(max([len(a) for a in all_colonne]))
#  block=0
#  print([str(c[block]) if len(c) < block else "  " for c in all_colonne ])
#  print([c[block] for c in all_colonne if len(c) > block])
