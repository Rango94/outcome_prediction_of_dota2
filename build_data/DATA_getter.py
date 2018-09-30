import dota2api
import random as rd
import numpy as np
import os

#懒姐：A62B39CB8B51A0494A8E08A2DC69E0DB
api=dota2api.Initialise('A62B39CB8B51A0494A8E08A2DC69E0DB')
# api=dota2api.Initialise('EFB29011FFD46B347C9E9DEE8A1F4252')

# his=api.get_match_history(account_id=168028715,start_at_match_id=4059082885,matches_requested=100)
# for key in his:
#     print(key)
#
# for key in his['matches']:
#     print(key)
# {'match_id': 4059082885, 'match_seq_num': 3521473250, 'start_time': 1534220133, 'lobby_type': 7, 'radiant_team_id': 0, 'dire_team_id': 0, 'players': }
# print(his)
# print(len(his['matches']))

class data_getter:

    def __init__(self,area):
        self.area=area
        if area=='CN':
            self.account_id=168028715
        elif area=='SEA':
            self.account_id=181716137
        elif area=='EU':
            self.account_id=77490514
        elif area=='US':
            self.account_id=12231202


    def get(self):
        self.get_teammate()
        self.get_matches()
        self.get_matches_detail()

    def get_teammate(self,num=5000,account_id=0):
        if os.path.exists(self.area+'/account_ids.npy'):
            return 0
        if account_id==0:
            account_id=self.account_id
        out={}
        start_at_match_id=None
        while True:
            his = api.get_match_history(account_id=account_id,start_at_match_id=start_at_match_id, matches_requested=100)
            for match in his['matches']:
                for player in match['players']:
                    try:
                        out[player['account_id']]=1
                    except:
                        continue
                    if len(out) >= num:
                        break
                if len(out) >= num:
                    break
            if len(out) >= num:
                break
            account_id=list(out)[rd.randint(0,len(out)-1)]

        np.save(self.area+'/account_ids',np.array(list(out)))

    def get_matches(self):
        if os.path.exists(self.area+'/matches_ids.npy'):
            return 0
        dic={}
        account_ids=np.load(self.area+'/account_ids.npy')
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
        np.save(self.area+'/matches_ids', np.array(list(dic)))

    def get_matches_detail(self):
        try:
            with open(self.area+'/matches_detail','r',encoding='utf-8') as fo:
                all=fo.readlines()
                match_ids_flag=int(all[-1].split(' ')[0])
        except:
            match_ids_flag=False

        matches=np.load(self.area+'/matches_ids.npy')
        num=len(matches)
        for idx,match_id in enumerate(matches):
            if match_ids_flag:
                print(match_id)
                if match_id == match_ids_flag:
                    match_ids_flag=False
                continue
            try:
                try:
                    match = api.get_match_details(match_id=match_id)
                except:
                    print("\033[0;31m%s\033[0m" % (str(match_id) + 'timeout'))
                    continue
                if match['duration']<1500:
                    print("\033[0;31m%s\033[0m" % (str(match_id)+':duration='+str(match['duration'])))
                    continue
                if match['human_players']!=10:
                    print("\033[0;31m%s\033[0m" % (str(match_id)+ ':human_players='+str(match['human_players'])))
                    continue
                if match['game_mode'] not in [1,3,2,22]:
                    print("\033[0;31m%s\033[0m" % (str(match_id)+':game_mode='+str(match['game_mode'])))
                    continue
                if match['lobby_type'] not in [0,7,2]:
                    print("\033[0;31m%s\033[0m" % (str(match_id)+':lobby_type='+str(match['lobby_type'])))
                    continue
                # if match['skill'] != 3:
                #     print("\033[0;31m%s\033[0m" % (str(match_id) + ':skill=' + str(match['skill'])))
                #     continue
            except:
                print("\033[0;31m%s\033[0m" % ('maybe key error'))
                continue
            players=match['players']
            leave_flag=False
            for player in players:
                try:
                    if player['leaver_status']!=0:
                        leave_flag=True
                        print("\033[0;31m%s\033[0m" % ('someone has AFK'))
                        continue
                except:
                    print("\033[0;31m%s\033[0m" % ('key error "leaver_status"'))
                    leave_flag = True
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

                    radiant=[str(i[0]) for i in sorted(zip(radiant,radiant_prior),key=lambda x:x[1])]
                    dire =[str(i[0]) for i in  sorted(zip(dire, dire_prior), key=lambda x: x[1])]
                    if len(radiant)!=5 or len(dire)!=5:
                        continue

                    with open(self.area+'/matches_detail', 'a', encoding='utf-8') as fo:
                        fo.write(' '.join([str(match_id),' '.join(radiant),' '.join(dire),str(radiant_win)])+'\n')
                    print(match_id,'%.6f'%(idx/num))
                except:
                    print('match error')
                    pass

# get_teammate(168028715,5000)
if __name__=='__main__':
    data_getter=data_getter('US')
    data_getter.get()




