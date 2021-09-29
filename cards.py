import random as r
from PIL import Image, ImageFont, ImageDraw
import os

class Card:
    def __init__(self, dict_cards):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.card_data = self.select_cards(dict_cards)

        self.background_data_img = Image.open(f'{self.path}/assets/texture/cards/cardBackground.png')
        self.framework_data_img = Image.open(f'{self.path}/assets/texture/cards/cardFramework.png')
        self.bar_data_img = Image.open(f'{self.path}/assets/texture/cards/cardBar.png')

        self.font_data = ImageFont.truetype(f'{self.path}/assets/fonts/m5x7.ttf', 16)

        self.name = self.card_data['name']
        self.type = self.card_data['type']
        self.pts_effect = int(self.card_data['pts_effect'])
        self.mana_price = int(self.card_data['mana_price'])
        self.rarity = int(self.card_data['rarity'])
        self.description = self.card_data['description']

        if self.card_data['img'].isdigit():
            self.img = self.card_data['img']
        else:
            self.img = r.randint(1, len(os.listdir(self.path + '/assets/texture/skills_texture')))

    def select_cards(self, dict_cards):
        card = dict_cards[r.randint(0, len(dict_cards)-1)]
        
        if r.randint(0,100) <= int(card['rarity']):
            return card
        
        return self.select_cards(dict_cards)

    def price_mana(self):
        return self.pts_effect, self.mana_price

    def card_background(self):
        if self.type == 'damage':
            return 0
        elif self.type == 'curse':
            return 1
        elif self.type == 'heal':
            return 2
        return 3

    def img_rarity(self):
        if self.rarity >= 50:
            return 0
        elif self.rarity > 10:
            return 1
        return 2

    def clear_background(self, img, del_color):
        img = img.convert("RGBA")
        data = img.getdata()
        new_data = []

        for items in data:
            if items[0] == del_color[0] and items[1] == del_color[1] and items[2] == del_color[2]:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(items)
        
        img.putdata(new_data)
        img.save('img.png')
        return img

    def text_center(self):
        return 50 - (len(self.name)*5)/2

    def make_card(self):
        i = self.card_background()
        background = self.background_data_img.crop((i*110, 0, (i+1)*100 + i*10, 128)).convert("RGBA")

        i = self.img_rarity()
        framework = self.framework_data_img.crop((i*96, 0, (i+1)*86 + i*10, 72)).convert("RGBA")
        framework = framework.resize((60,60))

        skill = Image.open(f'{self.path}/assets/texture/skills_texture/skill_icons{self.img}.png')
        skill = skill.crop((3, 3, 90 ,90))
        skill = skill.resize((54, 54))
        
        bar = self.bar_data_img.crop((i*106, 0, (i+1)*96 + i*10, 29)).convert("RGBA")
        bar = bar.resize((86, 26))

        small_bar = self.bar_data_img.crop((i*106, 39, (i+1)*96 + i*10, 57)).convert("RGBA")
        small_bar = small_bar.resize((86, 16))

        background.paste(skill, (23, 13), skill)
        background.paste(framework, (20, 10), framework)
        background.paste(bar, (7, 95), bar)
        background.paste(small_bar, (7, 75), small_bar)

        background_draw = ImageDraw.Draw(background)
        background_draw.text((10, 75), f'- {self.name}', font=self.font_data)

        return background

from data import Data
data = Data()

# card = Card(data.import_cards_csv('/assets/cards.csv'))
# card_img = card.make_card()
# card_img.save('image.png')
# card_img.show()

data.score_append('blele', r.randint(0,45542245))