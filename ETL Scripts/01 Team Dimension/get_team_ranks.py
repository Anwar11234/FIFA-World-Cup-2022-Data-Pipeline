from  bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.sportingnews.com/us/soccer/news/fifa-world-cup-rankings-2022-final-list-teams-record-finish/yvwh7l1urgugycsmmxqflp7y'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
ranks_table = soup.find('table')
ranks = []

for row in ranks_table.find_all('tr')[1:]:
    row_data = [tag.text for tag in row.find_all('td')]
    ranks.append({
        "team_name": row_data[1].lower(),
        "rank": int(row_data[0].replace('.',''))
    })

ranks_df = pd.DataFrame(ranks)
ranks_df.loc[ranks_df['team_name'] == 'south korea' , 'team_name'] = 'korea republic'
ranks_df.loc[ranks_df['team_name'] == 'usa' , 'team_name'] = 'united states'