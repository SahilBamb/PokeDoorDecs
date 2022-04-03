import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os.path


def DrawID(fn, ln, count, fileName):
	template = Image.open('pokeTemplate.jpg').convert("RGBA")
	draw = ImageDraw.Draw(template)

	#Name of the Institution
	font = ImageFont.truetype("Font/DAYROM__.ttf", size=180)
	draw.text((1100,70), 'Pokedex', font = font, fill='black')

	#Name of the Institutio
	font = ImageFont.truetype("Font/DAYROM__.ttf", size=120)
	draw.text((1300,240), 'Entry', font = font, fill='black')

	x1 = 1167
	y1 = 460
	x2 = 1793
	y2 = 1094

	#Profile Pasted
	pic = Image.open(fileName).resize((x2-x1, y2-y1), Image.ANTIALIAS).convert("RGBA")
	template.paste(pic, (x1, y1, x2, y2), mask=pic)
	
	#Writing the Name
	font = ImageFont.truetype("Font/University.otf", size=70)
	lname=ln[0] if len(fn)+len(ln)>18 else ln
	draw.text((70,815), fn+' '+lname, font = font, fill='black')

	#Writing the Title (Student)
	font = ImageFont.truetype("Font/University.otf", size=140)
	draw.text((200,966), 'Pokemon', font = font, fill='white')

	#Save the Image
	finalFileName = f'{fn} {ln}.png'
	template.save(finalFileName)
	print(f'Wrote the ID for {fn}')

df = pd.read_csv("students.csv",index_col='ID')

count = 1
for index, row in df.iterrows():
	fn = row['First Name'].strip()
	ln = row['Last Name'].strip()
	fileName = f'PKMN.NET Sprite Resource 4/Pokemon/BW/{count}.png'
	if os.path.exists(fileName): DrawID(fn, ln, count, fileName)
	else: DrawID(fn, ln, count, f'PKMN.NET Sprite Resource 4/Pokemon/BW/{0}.png')
	count+=1
	if count==10: exit()

	
