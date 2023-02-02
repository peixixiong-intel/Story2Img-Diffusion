import json
import os
import tqdm
import random
import shutil
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


ori_file = os.path.join('captions_train2014.json')


rel_list = [['IN'], #preposition/subordinating conjunction
            ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ'], #verb relation
            ['CC', 'RB'],  #however even  is RG and but is cc
            ['RBR', 'JJR', 'JJS'], #comparative
            ['PRP', ] #hers herself him ...
            ]
rel_label = {0: 'positional', 1: 'verb', 2: 'conjunction', 3: 'comparative', 4: 'pronoun'}
rel2label = {rel: rel_label[idx] for idx, rels in enumerate(rel_list) for rel in rels}





'''
text = word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)
'''
rel_label = {'positional':0, 'verb':0, 'conjunction':0, 'comparative':0, 'pronoun':0}
max_len = 0
total_len = 0
max_rel = 0

ori_data = json.load(open(ori_file))['annotations']
for idx, data in tqdm.tqdm(enumerate(ori_data)):
    sentence = data["caption"]
    text = word_tokenize(sentence)
    text_tags = [pos[1] for pos in nltk.pos_tag(text)]
    category = []
    for text_tag in text_tags:
        if text_tag in rel2label and rel2label[text_tag] not in category:
            category.append(rel2label[text_tag])
    length = len(text)
    max_rel = max(max_rel, len(category))
    for cat in category:
        rel_label[cat] += 1
    max_len = max(max_len, length)
    total_len += length


avg_rel = sum(rel_label.values())/float(len(ori_data))
avg_len = total_len/float(len(ori_data))

print('avg rel', avg_rel)
print('max rel', max_rel)
print('avg len', avg_len)
print('max len', max_len)
print('dist', rel_label)
