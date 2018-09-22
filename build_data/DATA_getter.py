import dota2api
import random as rd
import numpy as np
api=dota2api.Initialise('EFB29011FFD46B347C9E9DEE8A1F4252')

his=api.get_match_history(account_id=168028715,start_at_match_id=4059082885,matches_requested=100)
# for key in his:
#     print(key)
#
# for key in his['matches']:
#     print(key)
# {'match_id': 4059082885, 'match_seq_num': 3521473250, 'start_time': 1534220133, 'lobby_type': 7, 'radiant_team_id': 0, 'dire_team_id': 0, 'players': }
# print(his)
# print(len(his['matches']))

def get_teammate(account_id,num):
    out={}
    start_at_match_id=None
    while True:
        his = api.get_match_history(account_id=account_id,start_at_match_id=start_at_match_id, matches_requested=100)
        for match in his['matches']:
            for player in match['players']:
                print(len(out),player)
                out[player['account_id']]=1
                if len(out) >= num:
                    break
            if len(out) >= num:
                break
        if len(out) >= num:
            break
        account_id=list(out)[rd.randint(0,len(out)-1)]
    np.save('account_ids',np.array(list(out)))

def get_matches():
    dic={}
    account_ids=np.load('account_ids.npy')
    for id in account_ids:
        try:
            print(len(dic),id)
            his = api.get_match_history(account_id=id, matches_requested=100)
            matches=his['matches']
            for match in matches:
                if int(match['start_time'])<1521693973:
                    continue
                dic[match['match_id']]=1
        except:
            pass
    np.save('matches_ids', np.array(list(dic)))

# players:[{'account_id': 149486894,
            #'player_slot': 0,
            #'hero_id': 7,
            # 'item_0': 1,
            # 'item_1': 180,
            # 'item_2': 34,
            # 'item_3': 81,
            # 'item_4': 86,
            # 'item_5': 0,
            # 'backpack_0': 0,
            # 'backpack_1': 0,
            # 'backpack_2': 0,
            # 'kills': 1,
            # 'deaths': 1,
            # 'assists': 13,
            # 'leaver_status': 0,
            # 'last_hits': 72,
            # 'denies': 7,
            # 'gold_per_min': 395,
            # 'xp_per_min': 405,
            # 'level': 13,
            # 'hero_damage': 5660,
            # 'tower_damage': 1187,
            # 'hero_healing': 206,
            # 'gold': 1054,
            # 'gold_spent': 8375,
            # 'scaled_hero_damage': 4833,
            # 'scaled_tower_damage': 782,
            # 'scaled_hero_healing': 116,
            # 'ability_upgrades': [{'ability': 5023, 'time': 262, 'level': 1}, {'ability': 5024, 'time': 473, 'level': 2}, {'ability': 5023, 'time': 621, 'level': 3}, {'ability': 5025, 'time': 730, 'level': 4}, {'ability': 5025, 'time': 819, 'level': 5}, {'ability': 5026, 'time': 891, 'level': 6}, {'ability': 5025, 'time': 968, 'level': 7}, {'ability': 5025, 'time': 1065, 'level': 8}, {'ability': 5023, 'time': 1241, 'level': 9}, {'ability': 6006, 'time': 1322, 'level': 10}, {'ability': 5023, 'time': 1404, 'level': 11}, {'ability': 5026, 'time': 1507, 'level': 12}, {'ability': 5024, 'time': 1568, 'level': 13}],
            # 'hero_name': 'Earthshaker',
            # 'item_0_name': 'Blink Dagger', 'item_1_name': 'Arcane Boots', 'item_2_name': 'Magic Stick', 'item_3_name': "Vladmir's Offering", 'item_4_name': 'Buckler',
            # 'leaver_status_name': 'NONE',
            # 'leaver_status_description':'finished match, no abandon'},
            # {'account_id': 339399766, 'player_slot': 1, 'hero_id': 9, 'item_0': 46, 'item_1': 36, 'item_2': 212, 'item_3': 170, 'item_4': 63, 'item_5': 166, 'backpack_0': 237, 'backpack_1': 0, 'backpack_2': 0, 'kills': 10, 'deaths': 1, 'assists': 10, 'leaver_status': 0, 'last_hits': 77, 'denies': 9, 'gold_per_min': 468, 'xp_per_min': 530, 'level': 15, 'hero_damage': 11992, 'tower_damage': 3972, 'hero_healing': 0, 'gold': 1694, 'gold_spent': 8890, 'scaled_hero_damage': 10738, 'scaled_tower_damage': 2451, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5048, 'time': 337, 'level': 1}, {'ability': 5050, 'time': 456, 'level': 2}, {'ability': 5051, 'time': 525, 'level': 3}, {'ability': 5051, 'time': 616, 'level': 4}, {'ability': 5051, 'time': 736, 'level': 5}, {'ability': 5049, 'time': 787, 'level': 6}, {'ability': 5051, 'time': 847, 'level': 7}, {'ability': 5050, 'time': 931, 'level': 8}, {'ability': 5050, 'time': 987, 'level': 9}, {'ability': 5938, 'time': 1111, 'level': 10}, {'ability': 5050, 'time': 1222, 'level': 11}, {'ability': 5049, 'time': 1272, 'level': 12}, {'ability': 5048, 'time': 1286, 'level': 13}, {'ability': 5048, 'time': 1433, 'level': 14}, {'ability': 6013, 'time': 1579, 'level': 15}], 'hero_name': 'Mirana', 'item_0_name': 'Town Portal Scroll', 'item_1_name': 'Magic Wand', 'item_2_name': 'Ring of Aquila', 'item_3_name': 'Yasha', 'item_4_name': 'Power Treads', 'item_5_name': 'Maelstrom', 'leaver_status_name': 'NONE', 'leaver_status_description': 'finished match, no abandon'}, {'account_id': 334050219, 'player_slot': 2, 'hero_id': 17, 'item_0': 36, 'item_1': 63, 'item_2': 259, 'item_3': 41, 'item_4': 69, 'item_5': 77, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 4, 'deaths': 2, 'assists': 9, 'leaver_status': 0, 'last_hits': 152, 'denies': 2, 'gold_per_min': 513, 'xp_per_min': 541, 'level': 16, 'hero_damage': 7597, 'tower_damage': 2255, 'hero_healing': 100, 'gold': 3707, 'gold_spent': 7635, 'scaled_hero_damage': 7151, 'scaled_tower_damage': 1460, 'scaled_hero_healing': 78, 'ability_upgrades': [{'ability': 5098, 'time': 258, 'level': 1}, {'ability': 5100, 'time': 425, 'level': 2}, {'ability': 5100, 'time': 460, 'level': 3}, {'ability': 5098, 'time': 536, 'level': 4}, {'ability': 5098, 'time': 627, 'level': 5}, {'ability': 5101, 'time': 710, 'level': 6}, {'ability': 5098, 'time': 809, 'level': 7}, {'ability': 5100, 'time': 877, 'level': 8}, {'ability': 5100, 'time': 944, 'level': 9}, {'ability': 6926, 'time': 1070, 'level': 10}, {'ability': 5099, 'time': 1139, 'level': 11}, {'ability': 5101, 'time': 1263, 'level': 12}, {'ability': 5099, 'time': 1298, 'level': 13}, {'ability': 5099, 'time': 1375, 'level': 14}, {'ability': 5976, 'time': 1510, 'level': 15}, {'ability': 5099, 'time': 1605, 'level': 16}], 'hero_name': 'Storm Spirit', 'item_0_name': 'Magic Wand', 'item_1_name': 'Power Treads', 'item_3_name': 'Bottle', 'item_4_name': 'Perseverance', 'item_5_name': 'Null Talisman', 'leaver_status_name': 'NONE', 'leaver_status_description': 'finished match, no abandon'}, {'account_id': 130921377, 'player_slot': 3, 'hero_id': 36, 'item_0': 1, 'item_1': 190, 'item_2': 100, 'item_3': 16, 'item_4': 29, 'item_5': 0, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 6, 'deaths': 0, 'assists': 4, 'leaver_status': 0, 'last_hits': 129, 'denies': 26, 'gold_per_min': 494, 'xp_per_min': 499, 'level': 15, 'hero_damage': 5072, 'tower_damage': 730, 'hero_healing': 593, 'gold': 2882, 'gold_spent': 8645, 'scaled_hero_damage': 4841, 'scaled_tower_damage': 449, 'scaled_hero_healing': 470, 'ability_upgrades': [{'ability': 5158, 'time': 330, 'level': 1}, {'ability': 5159, 'time': 425, 'level': 2}, {'ability': 5158, 'time': 475, 'level': 3}, {'ability': 5160, 'time': 575, 'level': 4}, {'ability': 5158, 'time': 634, 'level': 5}, {'ability': 5161, 'time': 714, 'level': 6}, {'ability': 5158, 'time': 834, 'level': 7}, {'ability': 5159, 'time': 934, 'level': 8}, {'ability': 5159, 'time': 1023, 'level': 9}, {'ability': 5940, 'time': 1109, 'level': 10}, {'ability': 5159, 'time': 1233, 'level': 11}, {'ability': 5161, 'time': 1267, 'level': 12}, {'ability': 5160, 'time': 1336, 'level': 13}, {'ability': 5160, 'time': 1496, 'level': 14}, {'ability': 7110, 'time': 1609, 'level': 15}], 'hero_name': 'Necrophos', 'item_0_name': 'Blink Dagger', 'item_1_name': 'Veil of Discord', 'item_2_name': "Eul's Scepter of Divinity", 'item_3_name': 'Iron Branch', 'item_4_name': 'Boots of Speed', 'leaver_status_name': 'NONE', 'leaver_status_description': 'finished match, no abandon'}, {'account_id': 318309669, 'player_slot': 4, 'hero_id': 75, 'item_0': 244, 'item_1': 0, 'item_2': 46, 'item_3': 29, 'item_4': 223, 'item_5': 43, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 1, 'deaths': 2, 'assists': 16, 'leaver_status': 0, 'last_hits': 7, 'denies': 1, 'gold_per_min': 270, 'xp_per_min': 356, 'level': 12, 'hero_damage': 5087, 'tower_damage': 1755, 'hero_healing': 0, 'gold': 84, 'gold_spent': 5835, 'scaled_hero_damage': 5808, 'scaled_tower_damage': 1112, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5377, 'time': 312, 'level': 1}, {'ability': 5379, 'time': 425, 'level': 2}, {'ability': 5377, 'time': 631, 'level': 3}, {'ability': 5379, 'time': 746, 'level': 4}, {'ability': 5377, 'time': 866, 'level': 5}, {'ability': 5380, 'time': 985, 'level': 6}, {'ability': 5377, 'time': 987, 'level': 7}, {'ability': 5379, 'time': 1086, 'level': 8}, {'ability': 5378, 'time': 1268, 'level': 9}, {'ability': 5379, 'time': 1381, 'level': 10}, {'ability': 6016, 'time': 1511, 'level': 11}, {'ability': 5380, 'time': 1523, 'level': 12}], 'hero_name': 'Silencer', 'item_0_name': 'Wind Lace', 'item_2_name': 'Town Portal Scroll', 'item_3_name': 'Boots of Speed', 'item_5_name': 'Sentry Ward', 'leaver_status_name': 'NONE', 'leaver_status_description': 'finished match, no abandon'}, {'account_id': 4294967295, 'player_slot': 128, 'hero_id': 79, 'item_0': 180, 'item_1': 36, 'item_2': 40, 'item_3': 0, 'item_4': 188, 'item_5': 0, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 1, 'deaths': 3, 'assists': 1, 'leaver_status': 1, 'last_hits': 38, 'denies': 0, 'gold_per_min': 184, 'xp_per_min': 185, 'level': 8, 'hero_damage': 2525, 'tower_damage': 0, 'hero_healing': 0, 'gold': 1, 'gold_spent': 3485, 'scaled_hero_damage': 2498, 'scaled_tower_damage': 0, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5423, 'time': 313, 'level': 1}, {'ability': 5421, 'time': 446, 'level': 2}, {'ability': 5423, 'time': 662, 'level': 3}, {'ability': 5422, 'time': 795, 'level': 4}, {'ability': 5423, 'time': 890, 'level': 5}, {'ability': 5425, 'time': 978, 'level': 6}, {'ability': 5423, 'time': 1084, 'level': 7}, {'ability': 5421, 'time': 1179, 'level': 8}], 'hero_name': 'Shadow Demon', 'item_0_name': 'Arcane Boots', 'item_1_name': 'Magic Wand', 'item_2_name': 'Dust of Appearance', 'item_4_name': 'Smoke of Deceit', 'leaver_status_name': 'DISCONNECTED', 'leaver_status_description': 'player DC, no abandon'}, {'account_id': 168028715, 'player_slot': 129, 'hero_id': 76, 'item_0': 1, 'item_1': 102, 'item_2': 36, 'item_3': 63, 'item_4': 212, 'item_5': 77, 'backpack_0': 46, 'backpack_1': 0, 'backpack_2': 0, 'kills': 1, 'deaths': 6, 'assists': 1, 'leaver_status': 0, 'last_hits': 112, 'denies': 19, 'gold_per_min': 437, 'xp_per_min': 391, 'level': 13, 'hero_damage': 7850, 'tower_damage': 773, 'hero_healing': 0, 'gold': 791, 'gold_spent': 8120, 'scaled_hero_damage': 6722, 'scaled_tower_damage': 502, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5392, 'time': 339, 'level': 1}, {'ability': 5391, 'time': 408, 'level': 2}, {'ability': 5392, 'time': 441, 'level': 3}, {'ability': 5393, 'time': 496, 'level': 4}, {'ability': 5392, 'time': 569, 'level': 5}, {'ability': 5393, 'time': 637, 'level': 6}, {'ability': 5392, 'time': 700, 'level': 7}, {'ability': 5393, 'time': 769, 'level': 8}, {'ability': 5393, 'time': 889, 'level': 9}, {'ability': 5391, 'time': 922, 'level': 10}, {'ability': 5394, 'time': 1009, 'level': 11}, {'ability': 5903, 'time': 1131, 'level': 12}, {'ability': 5391, 'time': 1220, 'level': 13}], 'hero_name': 'Outworld Devourer', 'item_0_name': 'Blink Dagger', 'item_1_name': 'Force Staff', 'item_2_name': 'Magic Wand', 'item_3_name': 'Power Treads', 'item_4_name': 'Ring of Aquila', 'item_5_name': 'Null Talisman', 'leaver_status_name': 'NONE', 'leaver_status_description': 'finished match, no abandon'}, {'account_id': 4294967295, 'player_slot': 130, 'hero_id': 63, 'item_0': 63, 'item_1': 36, 'item_2': 7, 'item_3': 16, 'item_4': 265, 'item_5': 75, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 1, 'deaths': 4, 'assists': 0, 'leaver_status': 1, 'last_hits': 58, 'denies': 8, 'gold_per_min': 313, 'xp_per_min': 256, 'level': 10, 'hero_damage': 2596, 'tower_damage': 0, 'hero_healing': 0, 'gold': 2568, 'gold_spent': 4850, 'scaled_hero_damage': 2006, 'scaled_tower_damage': 0, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5290, 'time': 265, 'level': 1}, {'ability': 5291, 'time': 524, 'level': 2}, {'ability': 5290, 'time': 632, 'level': 3}, {'ability': 5289, 'time': 772, 'level': 4}, {'ability': 5290, 'time': 918, 'level': 5}, {'ability': 5292, 'time': 1082, 'level': 6}, {'ability': 5290, 'time': 1172, 'level': 7}, {'ability': 5291, 'time': 1264, 'level': 8}], 'hero_name': 'Weaver', 'item_0_name': 'Power Treads', 'item_1_name': 'Magic Wand', 'item_2_name': 'Javelin', 'item_3_name': 'Iron Branch', 'item_4_name': 'Infused Raindrop', 'item_5_name': 'Wraith Band', 'leaver_status_name': 'DISCONNECTED', 'leaver_status_description': 'player DC, no abandon'}, {'account_id': 137515340, 'player_slot': 131, 'hero_id': 114, 'item_0': 63, 'item_1': 145, 'item_2': 212, 'item_3': 0, 'item_4': 0, 'item_5': 182, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 2, 'deaths': 5, 'assists': 0, 'leaver_status': 1, 'last_hits': 147, 'denies': 13, 'gold_per_min': 444, 'xp_per_min': 400, 'level': 13, 'hero_damage': 4104, 'tower_damage': 0, 'hero_healing': 0, 'gold': 0, 'gold_spent': 8235, 'scaled_hero_damage': 3389, 'scaled_tower_damage': 0, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5723, 'time': 374, 'level': 1}, {'ability': 5716, 'time': 417, 'level': 2}, {'ability': 5723, 'time': 518, 'level': 3}, {'ability': 5721, 'time': 581, 'level': 4}, {'ability': 5721, 'time': 681, 'level': 5}, {'ability': 5721, 'time': 740, 'level': 6}, {'ability': 5721, 'time': 803, 'level': 7}, {'ability': 5723, 'time': 874, 'level': 8}, {'ability': 5716, 'time': 941, 'level': 9}, {'ability': 5906, 'time': 1028, 'level': 10}, {'ability': 5725, 'time': 1069, 'level': 11}, {'ability': 5725, 'time': 1183, 'level': 12}, {'ability': 5716, 'time': 1314, 'level': 13}], 'hero_name': 'Monkey King', 'item_0_name': 'Power Treads', 'item_1_name': 'Battle Fury', 'item_2_name': 'Ring of Aquila', 'item_5_name': 'Stout Shield', 'leaver_status_name': 'DISCONNECTED', 'leaver_status_description': 'player DC, no abandon'}, {'account_id': 4294967295, 'player_slot': 132, 'hero_id': 86, 'item_0': 92, 'item_1': 36, 'item_2': 180, 'item_3': 0, 'item_4': 46, 'item_5': 0, 'backpack_0': 0, 'backpack_1': 0, 'backpack_2': 0, 'kills': 1, 'deaths': 5, 'assists': 2, 'leaver_status': 3, 'last_hits': 22, 'denies': 2, 'gold_per_min': 192, 'xp_per_min': 178, 'level': 8, 'hero_damage': 4631, 'tower_damage': 0, 'hero_healing': 0, 'gold': 1, 'gold_spent': 4285, 'scaled_hero_damage': 3624, 'scaled_tower_damage': 0, 'scaled_hero_healing': 0, 'ability_upgrades': [{'ability': 5450, 'time': 390, 'level': 1}, {'ability': 5448, 'time': 491, 'level': 2}, {'ability': 5450, 'time': 517, 'level': 3}, {'ability': 5448, 'time': 823, 'level': 4}, {'ability': 5450, 'time': 923, 'level': 5}, {'ability': 5452, 'time': 968, 'level': 6}, {'ability': 5450, 'time': 1085, 'level': 7}, {'ability': 5451, 'time': 1223, 'level': 8}], 'hero_name': 'Rubick', 'item_0_name': 'Urn of Shadows', 'item_1_name': 'Magic Wand', 'item_2_name': 'Arcane Boots', 'item_4_name': 'Town Portal Scroll', 'leaver_status_name': 'ABANDONED', 'leaver_status_description': 'player dc, clicked leave, abandon'}]
# radiant_win:True
# duration:1268
# pre_game_duration:90
# start_time:1537549363
# match_id:4129851075
# match_seq_num:3579193389
# tower_status_radiant:1983
# tower_status_dire:416
# barracks_status_radiant:63
# barracks_status_dire:60
# cluster:224
# first_blood_time:173
# lobby_type:7
# human_players:10
# leagueid:0
# positive_votes:0
# negative_votes:0
# game_mode:3
# flags:0
# engine:1
# radiant_score:22
# dire_score:6
# lobby_name:Ranked
# game_mode_name:Random Draft
# cluster_name:China



def get_matches_detail():
    fo=open('matches_detail','w',encoding='utf-8')
    matches=np.load('matches_ids.npy')
    for match_id in matches:
        match = api.get_match_details(match_id=match_id)
        try:
            if match['duration']<1500:
                continue
            if match['human_players']!=10:
                continue
            if match['game_mode'] not in [0,1,3]:
                continue
            if match['lobby_type'] not in [0,7,2]:
                continue
        except:
            print('key error')
            continue
        players=match['players']
        leave_flag=False
        for player in players:
            if player['leaver_status']!=0:
                leave_flag=True
                continue
        if leave_flag:
            continue
        else:
            try:
                radiant_gold=[player['gold_per_min'] for player in players[:5]]
                dire_gold=[player['gold_per_min'] for player in players[5:]]
                radiant_exp=[player['xp_per_min'] for player in players[:5]]
                dire_exp = [player['xp_per_min'] for player in players[5:]]

                radiant_prior=[(a+b)/2 for a,b in zip(radiant_gold,radiant_exp)]
                dire_prior = [(a + b) / 2 for a, b in zip(dire_gold, dire_exp)]

                radiant=[player['hero_id'] for player in players[:5]]
                dire=[player['hero_id'] for player in players[5:]]
                #1是radiant胜利 0是dire胜利
                radiant_win=int(match['radiant_win'])
                # print(radiant,dire,radiant_win)

                radiant=[str(i[0]) for i in sorted(zip(radiant,radiant_prior),key=lambda x:x[1])]
                dire =[str(i[0]) for i in  sorted(zip(dire, dire_prior), key=lambda x: x[1])]

                fo.write(' '.join([' '.join(radiant),' '.join(dire),str(radiant_win)]))
                # print(' '.join([' '.join(radiant),' '.join(dire),str(radiant_win)]))
            except:
                print('match error')
                pass



def bueaty_print(dic):
    for key in dic:
        print(key+':',end='')
        if isinstance(dic[key], dict):
            bueaty_print(dic[key])
        else:
            print(dic[key])

get_matches_detail()
# get_teammate(168028715,5000)


