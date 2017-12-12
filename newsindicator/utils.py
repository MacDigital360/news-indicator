import json
import os


def print_json_object(obj):
    print 'Printing JSON object'
    print (json.dumps(obj, indent=4))


def get_asset(asset='sources'):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    print 'get_asset'
    print absolute_path

    if asset is not 'sources':
        print os.path.abspath(os.path.join(absolute_path, '..', 'assets/news_icon.png'))
        return os.path.abspath(os.path.join(absolute_path, '..', 'assets/news_icon.png'))
    print 'finished get_asset'
    print os.path.abspath(os.path.join(absolute_path, '..', 'assets/news_sources.txt'))
    return os.path.abspath(os.path.join(absolute_path, '..', 'assets/news_sources.txt'))


def get_news_sources_from_file():
    source_file = get_asset()

    with open(source_file, 'r') as f:
        news_sources = dict()
        for line in f:
            if not line.startswith('#') and line.split():
                split_line = line.split(' = ')
                news_sources[split_line[0]] = split_line[1].rstrip('\n')

    return news_sources


def delete_redundant_items(json_news, keys_to_del):
    for item in keys_to_del:
        del json_news[item]

    return json_news

