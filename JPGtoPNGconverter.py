import sys
import os
from PIL import Image
image_folder=sys.argv[1]
output_folder=sys.argv[2]
#print(image_folder,output_folder)
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
for filename in os.listdir(image_folder):
	img=Image.open('f{image_folder}{filename}')
	#img.save(f'{output_folder}{filename}.png','png')
	clean_name=os.path.splittext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')
	print('all done')

#python JPGtoPNGconverter.py Pokedex\ new\   (to run)