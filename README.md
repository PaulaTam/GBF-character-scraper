# GBF-character-scraper
Web scraper for GBFwiki to get basic information about the characters.

Granblue Fantasy content and materials are trademarks and copyrights of Cygames, Inc. or its licensors. All rights reserved.

## Use the dataset on Kaggle!
This dataset is currently public on [Kaggle](https://www.kaggle.com/datasets/nyaronya/gbf-character-dataset/data)! However you can also download the .csv here on GitHub too.

## Built with
- jupyter notebook
- python 3.10.0
  **IMPORTANT** (because otherwise the match statements will not work)

## Overview
This dataset includes the basic information for every character in the mobile / browser jrpg Granblue Fantasy. The data is scraped from [GBFwiki](https://gbf.wiki/Character_Tier_List/Gamewith/Ratings).

Information includes:

- **Rarity:** Rarity of character (SSR, SR, R)
- **Element:** Element of character
- **Name:** The name of the character
- **Series:** What series the character is part of (ex. "Summer" for summer limited characters.) Some characters are part of multiple series (ex. A character can be both "Summer" and "Zodiac"), which is what the **2nd Series** column is for.
- **Weapon:** What weapon category the character uses. Some characters are considered to be using 2 weapons (ex. "Katana" and "Melee"), which is what the **2nd Weapon** column is for.
- **Race:** What race the character is. (Human, Erune, Draph, etc.)
- **Type:** The character's play style. (Attack, Defense, etc.)

Any values with "-" are considered as empty or none.

Please note: This dataset was made with the intention of web scraping practice, but also with a curiosity with how weapon types and elements correlate or the race distribution per element.
