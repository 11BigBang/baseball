from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Scrape:
    def __init__(self):
        self.b_results, self.p_results = {}, {}
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.service = Service('C:\Program Files (x86)\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        time.sleep(5)

    def team_batting_scrape(self, metric_list, year):
        """ Argument must be a list of valid strings and a year.

        Valid metrics:  batters_used, age_bat, runs_per_game, G, PA, AB, R, H, 2B, 3B, HR, RBI, SB, CS, BB,
                        SO, batting_avg, onbase_perc, slugging_perc, onbase_plus_slugging,
                        onbase_plus_slugging_plus, TB, GDP, HBP, SH, SF, IBB, LOB

        Example:  team_batting_scrape(['G', 'TB', 'R'], 2021)

        Returns list of lists starting with list of team names followed by list in that order of each metric.
        """
        team_list, all_metrics = [], []
        tm_url = f'https://www.baseball-reference.com/leagues/majors/{str(year)}.shtml'
        self.driver.get(tm_url)
        team_path = f"//th[@data-stat='team_name']"
        team_elements = self.driver.find_elements(By.XPATH, team_path)

        for k in range(1, 31):
            team_list.append(team_elements[k].text)

        for metric in metric_list:
            temp = []
            xpath = f"//td[@data-stat='{metric}']"
            elements = self.driver.find_elements(By.XPATH, xpath)

            for i in range(30):
                temp.append(float(elements[i].text))

            all_metrics.append(temp)

        self.driver.quit()

        for ct in range(30):
            metric_dict = {}
            for k in range(len(metric_list)):
                metric_dict[metric_list[k]] = all_metrics[k][ct]
            self.b_results[team_list[ct]] = metric_dict

        return self.b_results

    def pitcher_scrape(self, year):
        """ Returns dictionary of dictionaries for all qualified pitchers.

        Qualified: A minimum of 100 plate appearances.

        Example:
            {
                'John Smith': {'G': 10, 'IP': 70, 'TB': 140},
                'Joe Snuffy': {'G': 11, 'IP': 77, 'TB': 154}
            }

        """
        nm_list, g_list, ip_list, tb_list, ct1, ct2 = [], [], [], [], 1, 0
        metric_list = ['G', 'IP', 'TB']
        p_url = f'https://baseballsavant.mlb.com/leaderboard/custom?year={str(year)}&type=pitcher&filter= \
        &sort=1&sortDir=asc&min=100&selections=p_game,p_formatted_ip,p_total_bases,&chart=false \
        &x=p_total_bases&y=p_total_bases&r=no&chartType=beeswarm'
        self.driver.get(p_url)
        time.sleep(10)
        p_elements = self.driver.find_elements(By.TAG_NAME, 'td')

        for data in p_elements:
            if ct1 == 6:
                tb_list.append(data.text)
            elif ct1 == 5:
                ip_list.append(data.text)
            elif ct1 == 4:
                g_list.append(data.text)
            elif ct1 == 2:
                nm_list.append(data.text)
            else:
                pass
            ct1 += 1

            if ct1 == 7:
                ct1 = 1

        self.driver.quit()

        for p in nm_list:
            self.p_results[p] = {'G': g_list[ct2], 'IP': ip_list[ct2], 'TB': tb_list[ct2]}
            ct2 += 1

        return self.p_results

    def get_matchups(self):
        """ Retrieves the teams in each matchup and the starting pitchers from mlb.com.

        #TODO: This part will need to be completed during the regular season.
        """
        matchups = [
            {
                'a_team': {
                    'name': 'Cardinals',  # name of team
                    'sp': 'Wainwright, Adam'  # name of starting pitcher
                },
                'h_team': {
                    'name': 'Pirates',  # name of team
                    'sp': 'Brubaker, JT'  # name of starting pitcher
                }
            },
            {
                'a_team': {
                    'name': 'Nationals',  # name of team
                    'sp': 'Corbin, Patrick'  # name of starting pitcher
                },
                'h_team': {
                    'name': 'Mets',  # name of team
                    'sp': 'Stroman, Marcus',  # name of starting pitcher
                }
            },
            {
                'a_team': {
                    'name': 'D-backs',  # name of team
                    'sp': 'Kelly, Merrill'  # name of starting pitcher
                },
                'h_team': {
                    'name': 'Brewers',  # name of team
                    'sp': 'Burnes, Corbin',  # name of starting pitcher
                }
            },
            {
                'a_team': {
                    'name': 'Yankees',  # name of team
                    'sp': 'Kluber, Corey'  # name of starting pitcher
                },
                'h_team': {
                    'name': 'Rangers',  # name of team
                    'sp': 'Lyles, Jordan',  # name of starting pitcher
                }
            }
        ]

        return matchups
