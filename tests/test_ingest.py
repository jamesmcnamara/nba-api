import json
import pickle
import requests

from nba.ingest import *

class TestGamelogIngester(object):
    def setup(self):
        url = ('http://www.basketball-reference.com/players/d/duranke01/'
               'gamelog/2014/')
        self.g = GamelogIngester(collection='gamelogs', url=url)
        player_combination = ('Kevin Durant', 'LeBron James')
        self.h = GamelogIngester(collection='headtoheads',
                                 player_combination=player_combination)

    def teardown(self):
        pass

    def test_class_attributes(self):
        assert self.g.collection == 'gamelogs'
        assert self.g.output is False
        assert self.g.url == ('http://www.basketball-reference.com/players/d/'
                             'duranke01/gamelog/2014/')
        assert self.g.reg_table_id == 'pgl_basic'
        assert self.g.playoff_table_id == 'pgl_basic_playoffs'
        assert self.g.header == [
            u'Player', u'PlayerCode', u'Year', u'Season', u'Rk', u'G',
            u'Date', u'Age', u'Tm', u'Home', u'Opp', u'WinLoss', u'GS', u'MP',
            u'FG', u'FGA', u'TP', u'TPA', u'FT', u'FTA', u'ORB', u'DRB',
            u'TRB', u'AST', u'STL', u'BLK', u'TOV', u'PF', u'PTS', u'GmSc',
            u'PlusMinus'
        ]


class TestCollectionCreator(object):
    def setup(self):
        self.g = CollectionCreator('gamelogs')
        self.h = CollectionCreator('headtoheads')
        self.p = CollectionCreator('players')

    def teardown(self):
        pass

    def test_find_options_gamelogs(self):
        with open('files/gamelogs_options.json', 'r') as f:
            gamelogs_options = json.load(f)
        assert self.g.find_options() == gamelogs_options

    def test_find_options_headtoheads(self):
        with open('files/headtoheads_options.p', 'r') as f:
            headtoheads_options = pickle.load(f)
        assert self.h.find_options() == headtoheads_options

    def test_find_options_players(self):
        assert self.p.find_options() == 'abcdefghijklmnopqrstuvwxyz'

