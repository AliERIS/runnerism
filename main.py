# runners will race and earn points need division to add

from math import *
from random import *


class Runner:
    def __init__(self, name, speed, acc):
        self.name = name
        self.speed = speed
        self.acc = acc
        self.maxspeedtime = speed/acc
        self.time = 0
        self.points = 0
        self.seasonpoints = 0
        self.age = randint(11, 26)
        self.reputation = randint(0, 10)
        self.luck = randint(0, 10)
        self.logic = randint(0, 10+self.age)
        self.value = speed*acc
        self.level = 1
        self.xp = 0
        self.expneedtonextlevel = pow(self. level, 2)  # i know so ugly
        self.manager = [] # you can call it with number of manager then call them ex managers etc.


class Track:
    def __init__(self, track_name, track_length):
        self.track_name = track_name
        self.track_length = track_length
        self.track_best = ""  # by name i presume
        self.track_best_time = 99999


class Manager:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.runners = []


me = Manager("ali", 100)
runner1 = Runner("ali", 10, 2)
runner2 = Runner("veli", 7, 3)
runner3 = Runner("mert", 15, 1)
runner4 = Runner("Bolt", 20, 4)
runner5 = Runner("Slo-mo", 1, 1)
runner6 = Runner("Oliver", 12, 7)
runner7 = Runner("Horauf", 15, 3)
runner8 = Runner("Memo", 9, 3)

meter100track = Track("100 meters track", 100)
meter200track = Track("200 meters track", 200)
meter60track = Track("60 meters track", 60)
meter1000track = Track("1000 meters track", 1000)
meter300track = Track("300 meters track", 300)


racerlist = [runner1, runner2, runner3, runner4, runner5, runner6, runner7, runner8]
tracklist = [meter100track, meter200track, meter60track, meter1000track, meter300track]


def race(racerlist, track):
    track_length = track.track_length
    for racer in racerlist:

        racerprespeed = 0.5*racer.acc*pow(racer.maxspeedtime, 2)
        if racerprespeed > track_length:
            racer.time = sqrt(2 * track_length / racer.acc)
        else:
            racer.time = (track_length - racerprespeed) / racer.speed + racer.maxspeedtime

    if racerlist[0].time > racerlist[1].time:
        print(racerlist[1].name, " wins")
        racerlist[1].points += 1
        if len(racerlist[1].manager) != 0:
            racerlist[1].manager[len(racerlist[1].manager)-1].money += 1

    elif racerlist[0].time == racerlist[1].time:
        print("tie")
    else:
        print(racerlist[0].name, "wins")
        racerlist[0].points += 1

    print(racerlist[0].time, " ", racerlist[1].time)


standinglist = []


def getracerlist():
    if len(standinglist) == 0:
        return racerlist
    else:
        return standinglist


def menu():
    mcount = 0
    while True:
        if mcount == 0:  #if it is first run
            racerlist = getracerlist()

        else:
            racerlist = standinglist  # no a ş
        secim1 = int(input(
"""1-Race
2-Standing
3-League
4-Managerial Menu    
5-Improve Runner
6-Create Runner 
x-Exit
"""))
        if secim1 == 1:
            newracelist = []
            print("choose first runner")
            for i in range(0, len(racerlist)):
                print(i+1, racerlist[i].name)
            secim11 = int(input())
            newracelist.append(racerlist[secim11-1])

            print("choose second runner")
            for i in range(0, len(racerlist)):
                print(i + 1, racerlist[i].name)
            secim11 = int(input())
            newracelist.append(racerlist[secim11-1])
            print("choose track ")
            for i in range(0, len(tracklist)):
                print(i + 1, tracklist[i].track_name)
            secim11 = int(input())
            track = tracklist[secim11-1]
            race(newracelist, track)
        elif secim1 == 2 :
            standinglist = []
            stando = racerlist

            while True:
                for i in stando:
                    count = 0
                    for b in stando:
                        if i.points >= b.points:
                           count += 1
                        if count == len(stando):
                            standinglist.append(i)
                            stando.remove(i)
                if len(stando) == 0:
                    for zep in range(0, len(standinglist)):
                        print(zep + 1, ")", standinglist[zep].name, " ", standinglist[zep].points)
                    stando = standinglist
                    racerlist = stando

                    print(standinglist[0].name)
                    mcount += 1
                    break

        elif secim1 == 3:

            for i in range(0, len(racerlist)):
                for z in range(0, len(racerlist)):
                    leaguelist = []
                    leaguelist.append(racerlist[i])
                    leaguelist.append(racerlist[z])
                    for k in range(0, len(tracklist)):
                        race(leaguelist, tracklist[k])

        elif secim1 == 4:
            secim11 = int(input("""
            1-)Buy Runner
            2-)İnfo"""))
            if secim11 == 1:
                for i in range(0, len(racerlist)):
                    print(i + 1, ")", racerlist[i].name)
                secim111 = int(input())
                me.runners.append(racerlist[secim111 - 1])
                me.money -= racerlist[secim111-1].value  # if racer.value > me.money -> insufficent funds
                racerlist[secim111 - 1].manager.append(me)
            elif secim11 == 2:
                print("name of you ", me.name)
                print("money of you", me.money)
                for i in me.runners:
                    print(i.name, " speed=", i.speed, " acc=", i.acc, " value=", i.value)

        elif secim1 == 5:
            print("choose runner")
            for i in range(0, len(racerlist)):
                print(i + 1, racerlist[i].name)
            secim11 = int(input())
            stro = racerlist[secim11-1].name, " un hangi özelliği geliştirilecek?", """
            1-Speed
            2-Acc"""
            secim111 = int(input(stro))

            if secim111 == 1:
                racerlist[secim11-1].speed += 1
            elif secim111 == 2:
                racerlist[secim11-1].acc += 1
        elif secim1 == 6:  # create runner
            print("create your runner")
            name = input("name of your runner")
            weight = int(input("weight of your runner"))
            height = int(input("height of your runner"))
            speed = (height - weight) / 10
            acc = speed / 5
            newplayer = Runner(name, speed, acc)
            racerlist.append(newplayer)

        elif secim1 == "x" or secim1 == "X" or "99":
            break


menu()
