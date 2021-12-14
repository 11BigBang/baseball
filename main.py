from scrape import Scrape

yr_to_scrape = 2021
scrape = Scrape()
# team_scrape = scrape.team_batting_scrape(['TB','G','R'], yr_to_scrape)
p_scrape = scrape.pitcher_scrape(yr_to_scrape)
# matchups = scrape.get_matchups()

# print(team_scrape)
print(p_scrape)

def compile():
    data = []
    for game in matchups:
        data.append(
            {
                'a_team': {
                    'tm': game['a_team']['name'],  # name of team
                    'g': team_scrape[game['a_team']['name']]['G'],  # games played for team
                    'tb': team_scrape[game['a_team']['name']]['TB'],  # total bases for offense
                    'o_tm': game['h_team']['name'],  # opposing team
                    'op': game['h_team']['sp'],  # name of opposing starting pitcher
                    'op_g': 10, #TODO: needs a validation function to ensure the right team  # opposing starting pitcher total games
                    'op_ip': 70,  # opposing starting pitcher total innings pitched
                    'op_tb': 200,  # opposing starting pitcher total bases allowed
                    'obp_ip': 300,  # opposing bullpen innings pitched
                    'obp_tb': 600  # opposing bullpen total bases allowed
                },
                'h_team': {
                    'tm': 'Royals',  # name of team
                    'g': 100,  # games played for team
                    'tb': 1000,  # total bases for offense
                    'o_tm': 'Rays',  # opposing team
                    'op': 'Smith',  # name of opposing starting pitcher
                    'op_g': 10,  # opposing starting pitcher total games
                    'op_ip': 70,  # opposing starting pitcher total innings pitched
                    'op_tb': 200,  # opposing starting pitcher total bases allowed
                    'obp_ip': 300,  # opposing bullpen innings pitched
                    'obp_tb': 600  # opposing bullpen total bases allowed
                }
            }
        )

day_ex = [
    {
    'a_team': {
        'tm': 'Royals', # name of team
        'g': 100, # games played for team
        'tb': 1000, # total bases for offense
        'o_tm': 'Rays', # opposing team
        'op': 'Smith', # name of opposing starting pitcher
        'op_g': 10, # opposing starting pitcher total games
        'op_ip': 70, # opposing starting pitcher total innings pitched
        'op_tb': 200, # opposing starting pitcher total bases allowed
        'obp_ip': 300, # opposing bullpen innings pitched
        'obp_tb': 600 # opposing bullpen total bases allowed
        },
    'h_team': {
        'tm': 'Royals', # name of team
        'g': 100, # games played for team
        'tb': 1000, # total bases for offense
        'o_tm': 'Rays', # opposing team
        'op': 'Smith', # name of opposing starting pitcher
        'op_g': 10, # opposing starting pitcher total games
        'op_ip': 70, # opposing starting pitcher total innings pitched
        'op_tb': 200, # opposing starting pitcher total bases allowed
        'obp_ip': 300, # opposing bullpen innings pitched
        'obp_tb': 600 # opposing bullpen total bases allowed
        }
    },
    {
    'a_team': {
        'tm': 'Royals', # name of team
        'g': 100, # games played for team
        'tb': 1000, # total bases for offense
        'o_tm': 'Rays', # opposing team
        'op': 'Smith', # name of opposing starting pitcher
        'op_g': 10, # opposing starting pitcher total games
        'op_ip': 70, # opposing starting pitcher total innings pitched
        'op_tb': 200, # opposing starting pitcher total bases allowed
        'obp_ip': 300, # opposing bullpen innings pitched
        'obp_tb': 600 # opposing bullpen total bases allowed
        },
    'h_team': {
        'tm': 'Royals', # name of team
        'g': 100, # games played for team
        'tb': 1000, # total bases for offense
        'o_tm': 'Rays', # opposing team
        'op': 'Smith', # name of opposing starting pitcher
        'op_g': 10, # opposing starting pitcher total games
        'op_ip': 70, # opposing starting pitcher total innings pitched
        'op_tb': 200, # opposing starting pitcher total bases allowed
        'obp_ip': 300, # opposing bullpen innings pitched
        'obp_tb': 600 # opposing bullpen total bases allowed
        }
    }
    ]