import csv
import os

from gensim.models import Word2Vec

class IMDB:
    '''
    Number of words = 25,630,633
    '''

    def __init__(self):

        word2vec_path = os.path.abspath(os.path.join('word2vec_models',
                                                     'movies', 'imdb'))
        if os.path.exists(word2vec_path):
            self.vectors = Word2Vec.load(word2vec_path)
        else:
            word2vec_model = Word2Vec(self, size=300, workers=4)
            word2vec_model.save(word2vec_path)
            self.vectors = word2vec_model


    def __iter__(self, sentence_tokens=True):
        '''Will iterate through every line in the IMDB training corpus at the
        following URL:
        http://ir.hit.edu.cn/~dytang/paper/acl2015/dataset.7z
        paper - http://aclweb.org/anthology/P15-1098
        and Generate the sentences/String from each review in the corpus seperated
        by <sssss>.

        default argument:
        sentence_tokens - True when set to True instead of generating sentences/
        String it generates a list of tokens of that sentence.

        Return String/list of Strings.
        '''

        data_path = os.path.abspath(os.path.join('data', 'imdb',
                                                 'imdb.train.txt.ss'))
        with open(data_path, 'r', newline='') as fp:
            tsv_reader = csv.reader(fp, delimiter='\t')
            for row in tsv_reader:
                sentences = row[-1].split('<sssss>')
                for sentence in sentences:
                    if sentence_tokens:
                        yield sentence.split()
                    else:
                        yield sentence
