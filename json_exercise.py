
import pandas as pd
import numpy as np

import json
from pandas.io.json import json_normalize


def get_top_ten_countries():
    projects = pd.read_json('data/world_bank_projects.json')
    return projects.groupby('countryname').size().sort_values(ascending=False).head(10)


def get_top_ten_major_project_themes():
    projects = json.load((open('data/world_bank_projects.json')))
    projects_themes = json_normalize(projects, 'mjtheme_namecode').sort_values('code')
    projects_themes.name.replace('', np.nan, inplace=True)
    projects_themes['name'] = projects_themes.name.bfill()
    return projects_themes.groupby('name').size().sort_values(ascending=False).head(10)


def main():
    print(f'Top Ten Countries by Number of Projects\n{get_top_ten_countries()}\n')
    print(f'Top Ten Major Project Themes by Number of Projects\n{get_top_ten_major_project_themes()}')


if __name__ == '__main__':
    main()
