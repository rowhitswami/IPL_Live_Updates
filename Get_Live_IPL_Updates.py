#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:47:36 2019

@author: Rohit Swami
"""

import requests 
from bs4 import BeautifulSoup
import time
from plyer import notification
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--team', action='store', dest='team', default='A', choices={"A", "B"}, help='Team A or B', required=False)
results = parser.parse_args()
team = results.team

# Swapping Team name
if team == 'A':
    team = 'teamaScore'
else:
    team = 'teambScore'
prev_ball_status = 0

def sys_notification(title, commentary, current_score):
    notification.notify(
        title=title,
        message=commentary+" "+current_score,
        timeout=30
        )

def get_html(request_URL = "https://demo.entitysport.com/"):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(request_URL, headers=headers)
    soup = BeautifulSoup(html.content, 'html5lib')
    return soup

def get_match_URL(soup):
    match_URL = soup.find('a', attrs={'class': 'match-status-3'})['href']
    return match_URL

def get_live_updates(live_match_URL):
    global prev_ball_status
    while True:
        time.sleep(5)
        soup = get_html(live_match_URL)

        # Getting the match title
        title = soup.find('h1', attrs={'id': 'heading'}).text.split(',')[0]
            
        # Getting the update from last ball
        last_ball = soup.find('div', attrs={'class': 'live-info4'}).span.text.strip()

        # Getting the current score
        current_score = soup.find('div', attrs={'class': team}).text.strip()

        # Current ball of the over
        current_ball_status = soup.find('div', attrs={'class': 'ovb'}).text.strip()
        if current_ball_status != prev_ball_status:
            if (last_ball == 'W'):
                last_wicket_commentary = soup.find('div', attrs={'class': 'comment-wicket'})
                last_wicket_commentary = last_wicket_commentary.find('div', attrs={'class':'text'}).text.strip()
                print("Last Wicket Commentary: "+ last_wicket_commentary + " " + current_score)
                sys_notification(title, last_wicket_commentary, current_score)
                time.sleep(60)
            elif (last_ball == '4') or (last_ball == '6'):
                last_hit_commentary = soup.find('div', attrs={'class': 'comment-ball'})
                last_hit_commentary = last_hit_commentary.find('div', attrs={'class':'text'}).text.strip()
                print("Last Hit Commentary: "+ last_hit_commentary + " " + current_score)
                sys_notification(title, last_hit_commentary, current_score)
            prev_ball_status = current_ball_status

if __name__ == "__main__":
    soup = get_html()
    live_match_URL = get_match_URL(soup)
    get_live_updates(live_match_URL)