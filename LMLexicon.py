'''
Contains the following classes:
LMLexicon
'''

import os

import requests
import pandas
class LMLexicon:
    '''This can only be used for non-commerical purposes only see the following
    website for details:
    http://sraf.nd.edu/
    '''


    def __init__(self):
        data_path = os.path.abspath(os.path.join('data', 'finance',
                                                 'loughran_list.csv'))
        if not os.path.exists(data_path):
            os.makedirs(os.sep + os.path.join(*data_path.split(os.sep)[:-1])),
                        exist_ok=True)
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '\
                                    'Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get('https://drive.google.com/uc?id=0B4niqV00F'\
                                    '3msaFZGUEZNTGtBblU&export=download',
                                    headers=headers)
            with open(data_path, 'w') as fp:
                fp.write(response.text)
        self.lexicon = LMLexicon._load_lexicon(data_path)

    @staticmethod
    def _load_lexicon(data_path):
        with open(data_path, 'r', encoding='ISO-8859-1', newline='') as fp:
            data = pandas.read_csv(fp)
            pos_words = data.loc[data['Positive'] != 0]['Word']
            neg_words = data.loc[data['Negative'] != 0]['Word']
        lexicon = {word.lower().strip() : 1 for word in pos_words}
        lexicon.update({word.lower().strip() : -1 for word in neg_words})
        return lexicon
