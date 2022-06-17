# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:46:22 2022

@author: charl
"""
import requests
import random
import time
from jikanpy import Jikan

def randomAnime():
    jikan=Jikan()
    # or anime['genres'][0]!='mystery'
    goodtype=0
    while goodtype==0:
        #print('reset1')
        time.sleep(0.1)
        anime=0
        while(anime==0):
            #print('reset2')
            try:
                anime=jikan.anime(random.randint(1,1000))
            except:
                anime=0
            if(anime!=0):
                for i in range(0,len(anime["genres"])):
                    #print(anime['genres'][i]['name'])
                    if anime['genres'][i]['name']=='Action':
                        goodtype+=1
                #print(goodtype)
    return anime
def randomAnimeGenre(genre):
    jikan=Jikan()
    #print(genre)
    # or anime['genres'][0]!='mystery'
    goodtype=0
    while goodtype==0:
        #print('reset1')
        time.sleep(0.1)
        anime=0
        while(anime==0):
            #print('reset2')
            try:
                anime=jikan.anime(random.randint(1,1000))
            except:
                anime=0
            if(anime!=0):
                for i in range(0,len(anime["genres"])):
                    print(anime['genres'][i]['name'])
                    if anime['genres'][i]['name']==genre:
                        goodtype+=1
                #print(goodtype)
    return anime

genres=['Action','Supernatural','Comedy','Drama','Slice of Life',
        'Fantasy','Adventure','Sci-Fi','Mystery','Boys Love','Horror',
        'Avant Garde','Girls Love','Sports','Romance','Suspense']
#anime=randomAnime()
taille=0

for i in range(0,len(genres)):
    print(genres[i]," | ",end="")
    taille+=1
    if taille%6==0:
        print()
x=int(input("\nQuel genre souhaitez vous ?"))-1
anime=randomAnimeGenre(genres[x])


print(anime['title'])
print("Synopsis :\n",anime['synopsis'])
print("Episodes : ",anime['episodes'])
#response =requests.get('http://randomfox.ca/floof')

