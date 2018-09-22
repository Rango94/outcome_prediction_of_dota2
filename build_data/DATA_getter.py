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

k=np.load('matches_ids.npy')
print(k)


# get_teammate(168028715,5000)


