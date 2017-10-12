from Scraper.SoupSquads import SquadsSoup
from Scraper.SoupPlayerHeading import PlayerHeadingSoup
from Scraper.SoupMatchDetails import MatchDetailsSoup
# from Scraper.SoupMatchEvents import MatchEventsSoup
from Scraper.SoupMatchEvents import MatchEventsHeadingSoup
from Scraper.SoupMatchHeading import MatchHeadingSoup
from Tests.DataForTests import *

# soup = SquadsSoup(squads_text)
# soup2 = PlayerHeadingSoup(player_heading_text)
# soup = MatchEventsSoup(match_events_text)

# print soup.extract_all_events()[0].prettify()

soup2 = MatchEventsHeadingSoup(match_event_heading_text)
print soup2.get_event_player_id()
print soup2.get_event_time()

soup = MatchHeadingSoup(match_heading_text)
print soup.get_date_of_match()
print soup.get_match_detail_url()


