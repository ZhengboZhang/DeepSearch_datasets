from datasets import load_dataset, load_from_disk, Dataset
import json
import jsonlines
import os
from tqdm import tqdm

dataset = load_from_disk('/4T/fengyue/MMSearch-Plus_decrypt')
image_dir = '/4T/fengyue/MMSearch-Plus_decrypt/images'

res = []
for idx, data in tqdm(enumerate(dataset)):
    # question = data['question']
    # answer = data['answer']
    images = [data[f'img_{i+1}'] for i in range(5)]
    # difficulty = data['difficulty']
    # video_url = data['video_url']
    # arxiv_id = data['arxiv_id']
    # category = data['category']
    # subtask = data['subtask']

    image_name = []
    for i, image in enumerate(images):
        if image:
            # image.save(os.path.join(image_dir, f"{idx+1}_{i+1}.png"))
            image_name.append(f"{idx+1}_{i+1}.png")

    for i in range(5):
        del data[f'img_{i+1}']

    data['images'] = image_name
    res.append(data)

with open('/4T/fengyue/MMSearch-Plus_decrypt/mmsearch_plus.jsonl', 'w', encoding='utf-8') as f:
    for item in res:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        