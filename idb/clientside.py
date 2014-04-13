from django.shortcuts import render
import requests
import operator
from collections import OrderedDict

def clientside(request):
    money_per_win = {}
    total_wins = {}
    playoff_apps = {}
    for x in range(1,12):
        temp = {}
        wins = 0
        playoffs = 1
        r = requests.get('http://frozen-plateau-5382.herokuapp.com/api/teams/'+str(x)+'/years')
        years = r.json()
        for i in range(0,10):
            temp[str(years[i]["fields"]["year"])] = int(round(float(years[i]["fields"]["payroll"])/float(years[i]["fields"]["wins"])))
            wins += years[i]["fields"]["wins"]
            if years[i]["fields"]["playoffs"] != "":
                playoffs += 1
        name = requests.get('http://frozen-plateau-5382.herokuapp.com/api/teams/'+str(x)).json()[0]["fields"]["name"]
        money_per_win[name] = temp
        total_wins[name] = wins
        playoff_apps[name] = playoffs

    averages = {}
    for x in money_per_win.keys():
        team = money_per_win[x]
        avg = float(sum([num for num in team.values()]))/10.0
        averages[x] = int(round(avg))

    efficiency = {}
    for x in averages.keys():
        efficiency[x] = int(round(float(averages[x])/float(total_wins[x])))

    playoff_efficiency = {}
    for x in efficiency.keys():
        playoff_efficiency[x] = float(efficiency[x])/float(playoff_apps[x])
        playoff_apps[x] -= 1

    for x in money_per_win:
        money_per_win[x]["avg"] = averages[str(x)]
        money_per_win[x]["eff"] = playoff_efficiency[str(x)]
        money_per_win[x]["wins"] = total_wins[str(x)]
        money_per_win[x]["playoffs"] = playoff_apps[str(x)]

    sortedmoney_per_win = OrderedDict(sorted(money_per_win.iteritems(), key=lambda x: x[1]['eff']))
    return render(request, "efficiency.html", {'result': sortedmoney_per_win})
