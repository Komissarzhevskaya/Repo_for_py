from requests import get, utils
from collections import Counter

response = get('https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt')
encodings = utils.get_encoding_from_headers(response.headers)
txt = response.content.decode(encoding=encodings)

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('pars_file.txt', 'w', encoding='utf-8') as g:
        logs_gen = ((i.split(' ')[0], i.split(' ')[5][1:], i.split(' ')[6]) for i in f.read().split('\n'))
        for i in logs_gen:
            g.write(str(i) + '\n')

with open('pars_file.txt', 'r', encoding='utf-8') as k:
    req = Counter()
    for i in k:
        ip_add = i.split(',')[0].strip("('")
        req[ip_add] += 1
    print(f'IP: {req.most_common(1)[0][0]} , number of requests: {req.most_common(1)[0][1]}')
