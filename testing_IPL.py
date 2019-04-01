#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:47:36 2019

@author: Rohit Swami
"""

import requests 
from bs4 import BeautifulSoup 
URL = "https://demo.entitysport.com/matches/kings-xi-punjab-vs-delhi-capitals-40293/"


while True:
    URL = "https://demo.entitysport.com/matches/kings-xi-punjab-vs-delhi-capitals-40293/"
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(URL, headers=headers) 
    soup = BeautifulSoup(html.content, 'html5lib')
        
    # Getting the update from last ball
    last_ball = soup.find('div', attrs={'class': 'live-info4'})
    last_ball = last_ball.span.text.strip()
    if current_status != prev_status:
        if last_ball == 'W':
            last_ball_commmentary = soup.find('div', attrs={'class': 'comment-wicket'})
            last_ball_commmentary = last_ball_commmentary.find('div', attrs={'class':'text'}).text.strip()
            print(last_ball_commmentary)
        elif (last_ball == '4') or (last_ball == '6'):
            last_ball_commmentary = soup.find('div', attrs={'class': 'comment-ball'})
            last_ball_commmentary = last_ball_commmentary.find('div', attrs={'class':'text'}).text.strip()
            print("Last Ball Commentary: ", last_ball_commmentary)
        prev_status = current_status