#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:47:36 2019

@author: Rohit Swami
"""

import requests 
from bs4 import BeautifulSoup
import time
from plyer import notification

prev_ball_status = 0

def sys_notification(title, commentary, current_score):
    notification.notify(
        title=title,
        message=commentary+" "+current_score,
        timeout=30
        )

while True:
    URL = "https://demo.entitysport.com/matches/rajasthan-royals-vs-royal-challengers-bangalore-40294/"
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html.content, 'html5lib')

    # Getting the match title
    title = soup.find('h1', attrs={'id': 'heading'}).text.split(',')[0]
        
    # Getting the update from last ball
    last_ball = soup.find('div', attrs={'class': 'live-info4'}).span.text.strip()

    # Getting the current score
    current_score = soup.find('div', attrs={'class': 'teamaScore'}).text.strip()

    # Current ball of the over
    current_ball_status = soup.find('div', attrs={'class': 'ovb'}).text.strip()
    if current_ball_status != prev_ball_status:
        if (last_ball == 'W'):
            last_wicket_commmentary = soup.find('div', attrs={'class': 'comment-wicket'})
            last_wicket_commmentary = last_wicket_commmentary.find('div', attrs={'class':'text'}).text.strip()
            print("Last Wicket Commentary: "+ last_wicket_commmentary + " " + current_score)
            sys_notification(title, last_wicket_commmentary, current_score)
            time.sleep(60)
            continue
        elif (last_ball == '4') or (last_ball == '6'):
            last_hit_commmentary = soup.find('div', attrs={'class': 'comment-ball'})
            last_hit_commmentary = last_hit_commmentary.find('div', attrs={'class':'text'}).text.strip()
            print("Last Hit Commentary: "+ last_hit_commmentary + " " + current_score)
            sys_notification(title, last_hit_commmentary, current_score)
        elif current_ball_status == '19.6':
            current_score = soup.find('div', attrs={'class': 'teamaScore'}).text.strip()
        print(current_score)
        prev_ball_status = current_ball_status