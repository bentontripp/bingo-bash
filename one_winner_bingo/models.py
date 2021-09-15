from django.db import models
import numpy as np
import random
import textwrap

# Create your models here.
def bingo_text_wrap(item):
    lines = textwrap.fill(item, 12, break_long_words=True, break_on_hyphens=True)
    hyphen_indices = []
    for l in range(0, len(lines)):
        try:
            if lines[l] not in [' ','-','\n'] and lines[l + 1] == '\n':
                hyphen_indices.append(l + len(hyphen_indices))
        except:
            pass
    if len(lines) > 60:
        lines = lines[:57] + '...'
    return lines

def get_dict(user_input):
    d = {}
    for i in range(1, len(user_input) + 1):
        d.update({i: user_input[i - 1]})
    return d

def map_custom_input(card, user_input):
    d = get_dict(user_input)
    for row in range(1, len(card)):
        try:
            card[row] = [d[j] for j in card[row]]
        except:
            card[row].pop(2)
            card[row] = [d[j] for j in card[row]]
            card[row][2:2] = ['FREE']
    return card

def get_arangements(arr, free_space):
    if free_space is True:
        try:
            arr[12] = 0
        except:
            arr[2][2] = 0
    arr = arr.reshape(5, 5)
    diag_lr = set(np.diagonal(arr)) # diagonal left to right
    diag_rl = set(np.fliplr(arr).diagonal()) # diagonal right to left
    r1 = set(arr[0])
    r2 = set(arr[1])
    r3 = set(arr[2])
    r4 = set(arr[3])
    r5 = set(arr[4])
    c1 = set(arr[:, 0])
    c2 = set(arr[:, 1])
    c3 = set(arr[:, 2])
    c4 = set(arr[:, 3])
    c5 = set(arr[:, 4])
    return arr, [diag_lr, diag_rl, r1, r2, r3, r4, r5, c1, c2, c3, c4, c5]

# custom bingo cards
def custom_shuff(user_input, total_cards, free_space = True):
    for item in range(0, len(user_input)):
        user_input[item] = bingo_text_wrap(user_input[item])
    one_winner_arrs = []
    one_winner_bingos = []
    unique_tiles = len(user_input)
    while len(one_winner_arrs) < total_cards:
        rand = np.array(random.sample(range(1, unique_tiles + 1), 25))
        arr, bingos = get_arangements(rand, free_space)
        check =  any(item in bingos for item in one_winner_bingos)
        if check is False:
            arr = arr.tolist()
            if free_space is True:
                arr[2][2] = 'FREE'
            arr.insert(0, ['B','I','N','G','O'])
            arr = map_custom_input(arr, user_input)
            one_winner_arrs.append(arr)
            for bingo in bingos:
                one_winner_bingos.append(bingo)  
    
    return one_winner_arrs

# official bingo cards
def get_official_arr():
    B = np.array(random.sample(range(1, 16), 5))
    I = np.array(random.sample(range(17, 31), 5))
    N = np.array(random.sample(range(31, 46), 5))
    G = np.array(random.sample(range(46, 61), 5))
    O = np.array(random.sample(range(61, 76), 5))
    arr = np.vstack((B,I,N,G,O)).T
    return arr

def official_shuff(total_cards, free_space = True):
    one_winner_arrs = []
    one_winner_bingos = []
    while len(one_winner_arrs) < total_cards:
        off_arr = get_official_arr()
        arr, bingos = get_arangements(off_arr, free_space)
        check =  any(item in bingos for item in one_winner_bingos)
        if check is False:
            arr = arr.tolist()
            if free_space is True:
                arr[2][2] = 'FREE'
            arr.insert(0, ['B','I','N','G','O'])
            one_winner_arrs.append(arr)
            for bingo in bingos:
                one_winner_bingos.append(bingo)  
    return one_winner_arrs