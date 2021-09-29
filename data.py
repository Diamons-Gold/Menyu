import random as r
import csv
import os

class Data:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_scores = f'{self.path}/assets/scores.csv'

        self.scores_data = self.import_cards_csv(self.path_scores)

    def import_cards_csv(self, fichier, separateur = ';'):
            '''
            Préconditions : fichier est au format str et correspond au chemin du fichier à importer 
                            separateur est au format str et correspond au caractère de délimitation du fichier csv
            Postcondition : retourne une table de dictionnaires
            '''

            data = []
            with open(fichier, newline='', encoding="utf8") as csvfile:
                spamreader = csv.DictReader(csvfile, delimiter = separateur)
                for row in spamreader:
                    data.append(dict(row))
            return data

    def sauv_table_dico_vers_csv(self, data, fichier, separateur = ';'):
        '''
        Préconditions : data est une table de dictionnaires
                        fichier est au format str et correspond au chemin du fichier à importer 
                        separateur est au format str et correspond au caractère de délimitation du fichier csv
        Postcondition : Sauvegarde le fichier csv correspondant aux données
        '''
        en_tetes = list(data[0].keys())
        with open(fichier, 'w') as csvfile:
            csvfile = csv.DictWriter(csvfile, en_tetes, delimiter = separateur)
            csvfile.writeheader()
            csvfile.writerows(data)
        return None

    def name(self):
        num = f'{r.randint(1, 9999)}'

        if len(num) < 4:
             

        name = f'palyer {num}'
        for i in range(len(self.scores_data)-1):
            if self.scores_data[i]['name'] != name:
                return name
        self.name()



    def score_append(self, name, score):
        if name == '':
            name = self.name()
             
        self.scores_data.append({'name': name,'score': score})
        self.sauv_table_dico_vers_csv(self.scores_data, self.path_scores)
