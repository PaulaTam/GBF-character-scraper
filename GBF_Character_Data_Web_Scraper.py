#!/usr/bin/env python
# coding: utf-8

# ### Author: Paula Abigail Tam
# ### Project: GBF character dataset
# 
# This project is to scrape the character data from the tierlist on GBFwiki. End goal is to make a visualizer to make character statistics more digestible.
# 
# Example: To be able to compare the number of Dark SSR characters vs number of Light SSR characters.

#imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

#character data url
URL = "https://gbf.wiki/Character_Tier_List"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#get data from tierlist
table_tier = soup.find('table', class_ = "wikitable tierlist tierlist-multi")
td = table_tier.find_all('td')

#function to determine rarity of character
def chara_rarity(id_num):
    match id_num:
        case "4":
            return "SSR"
        case "3":
            return "SR"
        case "2":
            return "R"

#function to determine a character's element
def which_element(element_n):
    match element_n:
        case 1:
            return "Fire"
        case 2:
            return "Water"
        case 3:
            return "Earth"
        case 4:
            return "Wind"
        case 5:
            return "Light"
        case 6:
            return "Dark"
        case 7:
            return "Any"
        case 0:
            return "Rank"

#function to check if multiple series / weapons
def is_multiple(string):
    line = string.split(",")
    return line

#function to rename series
def which_series(series_name):
    match series_name:
        case "":
            return "-"
        case "none":
            return "Permanent"
        case "tie-in":
            return "Tie-In / Collab"
        case "12generals":
            return "Zodiac"
        case default:
            return series_name.capitalize()

def get_chara_page(short_id):
    table_detail = soup.find('table', class_ = "wikitable tierlist-details")
    tr = table_detail.find_all('tr', attrs={'data-short-id':short_id})
    for k in tr:
        a = k.find('a')
        return(a['href'])

#initliaize list of dicts
list_of_charas = []
n = 0

for i in td:
    item = i.find_all('span', attrs={"data-short-id": True})
    
    for j in item:            
        name = [title['title'] for title in j.find_all('a')]
        series = is_multiple(j['data-filter-series'])
        wep = is_multiple(j['data-filter-weapon'])
        race = is_multiple(j['data-filter-race'])
        
        chara_page = get_chara_page(j['data-short-id'])
        chara_url = "https://gbf.wiki" + chara_page
        
        chara_info = {}
        #populate the character's dictionary
        chara_info['Rarity'] = chara_rarity(j['data-short-id'][0])
        chara_info['Element'] = which_element(n) #call function to convert n to element
        chara_info['Name'] = name[0] #to just keep it as a string
        
        chara_info['Series'] = which_series(series[0]) #seasonal/grand/etc.
        if len(series) > 1:
            chara_info['2nd Series'] = which_series(series[1])
        else:
            chara_info['2nd Series'] = "-"
            
        chara_info['Weapon'] = wep[0].capitalize()
        if len(wep) > 1:
            chara_info['2nd Weapon'] = wep[1].capitalize()
        else:
            chara_info['2nd Weapon'] = "-"
            
        chara_info['Race'] = race[0].capitalize()
        if len(race) > 1:
            chara_info['2nd Race'] = race[1].capitalize()
        else:
            chara_info['2nd Race'] = "-"
            
        chara_info['Type'] = j['data-filter-style'].capitalize()
        chara_info['URL'] = chara_url
        
        list_of_charas.append(chara_info)
        
    if n != 7:
        n += 1
    else:
        n = 0

#dataframe of basic character data
df = pd.DataFrame(list_of_charas)
df.to_csv('GBF_character_dataset_test.csv', index=False)