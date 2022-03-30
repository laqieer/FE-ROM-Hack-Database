#!/usr/bin/env python3

import sys
import requests
from xml.etree.ElementTree import ElementTree, dump

inputXML = 'OfflineList/datas/laqieer - Fire Emblem - Game Boy Advance.xml'
templateXML = 'Scripts/FEUProjectTemplate.xml'
FEUTopicURLPrefix = 'https://feuniverse.us/t/'
FEUTopProjectsURL = 'https://feuniverse.us/c/projects/17/l/top.json?ascending=false&page=%d&period=all'
PagesLimit = 50
ExcludeTags = ('snesfe', '3dsfe', 'dsfe', 'lt_engine', 'nesfe', 'other_engine', 'srpgstudio_engine', 'tactile_engine', 'tactile')

existedProjects = set()

def loadExistedProjects():
    tree = ElementTree()
    tree.parse(inputXML)
    games = tree.findall('./games/game')
    for game in games:
        comment = game[12].text
        if comment is not None and comment.startswith(FEUTopicURLPrefix):
            existedProjects.add(int(comment.split('/')[5]))

def saveMissingProjects():
    print('<games>')
    tree = ElementTree()
    tree.parse(templateXML)
    game = tree.getroot()
    for page in range(PagesLimit):
        response = requests.get(FEUTopProjectsURL % page).json()
        users = {}
        for user in response['users']:
            users[user['id']] = user['username']
        for topic in response['topic_list']['topics']:
            if topic['id'] not in existedProjects:
                valid = True
                game[3].text = 'Sram_F_v103'
                for tag in topic['tags']:
                    if tag in ExcludeTags:
                        valid = False
                        break
                    if tag in ('fe7', 'fe7_base', 'fe6_base'):
                        game[3].text = 'Sram_F_v102'
                        if tag == 'fe6_base':
                            game[6].txt = '7'
                if valid:
                    game[2].text = topic['fancy_title'].replace(':', ' -')
                    game[7].text = users[topic['posters'][0]['user_id']]
                    game[12].text = FEUTopicURLPrefix + topic['slug'] + '/' + str(topic['id'])
                    dump(game)
        if response['topic_list'].get('more_topics_url', '') == '':
            break
    print('</games>')

def main():
    loadExistedProjects()
    saveMissingProjects()

if __name__ == '__main__':
    main()
