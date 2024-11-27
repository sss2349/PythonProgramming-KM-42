import json
t = []
with open('image_info_test-dev2017.json') as f:
    s = json.load(f)
    print(f"Кількість картиинок: {len(s['images'])}")
    print(f"Кількість категорій: {len(s['categories'])}")
    for x in s['images']:
        t.append(x['file_name'].replace('.jpg', ''))
        if x['file_name'] == '000000000001.jpg':
            print('height: '+str(x['height']), 'width:', x['width'], 'id: ', x['id'])
    print(f"Максимальний номер: {max(t)}")