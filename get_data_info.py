import json
import os
import tqdm
import nltk
from nltk.tokenize import word_tokenize

root = '/home/peixixio/diffusion_dataset/story2img'
annotation_root = os.path.join(root, 'annotations')
train_save_file = os.path.join(root, 'annotations', 'captions_train2014.json')
val_save_file = os.path.join(root, 'annotations', 'captions_val2014.json')
test_save_file = os.path.join(root, 'annotations', 'captions_test2014.json')
rel_label = {'positional':0, 'verb':0, 'conjunction':0, 'comparative':0, 'pronoun':0}
max_len = 0
total_len = 0
max_rel = 0

#avg rel, max rel, max len, avg len,
train_data = json.load(open(train_save_file))['annotations']
val_data = json.load(open(val_save_file))['annotations']
test_data = json.load(open(test_save_file))['annotations']

for data in [train_data, val_data, test_data]:
    for annotation in tqdm.tqdm(data):
        category = annotation['category']
        caption = word_tokenize(annotation['caption'])
        length = len(caption)
        max_rel = max(max_rel, len(category))
        for cat in category:
            rel_label[cat] += 1
        max_len = max(max_len, length)
        total_len += length

avg_rel = sum(rel_label.values())/float(len(train_data)+len(test_data)+len(val_data))
avg_len = total_len/float(len(train_data)+len(test_data)+len(val_data))

print('avg rel', avg_rel)
print('max rel', max_rel)
print('avg len', avg_len)
print('max len', max_len)
print('dist', rel_label)

# avg rel 3.4837176013496243
# max rel 5
# avg len 67.51735596339655
# max len 319
# dist {'positional': 19392, 'verb': 19442, 'conjunction': 16452, 'comparative': 1617, 'pronoun': 11242}