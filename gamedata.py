import random
import datetime

def gamedata(level, healpoint, endtime, cash, mode):

    #==================================================INVITEM

    EstusFlask = "Estus Flask"
    tangoboost = "Tango"
    
    ChaosBlade = "Chaos Blade"
    DChaosBlade = "Dual Chaos Blade"
    FChaosBlades = "Furi Chaos Blade"
    
    NKShield = "Nameless Knight Shield"
    NKSet = "Nameless Knight Set"

    DemonsScar = "Demons Scar" 
    DarkHand = "Dark Hand"
    
    VampiricMask = "Vampiric Mask"
    RegRing = "Regeneration Ring"

    shopinv = [RegRing,VampiricMask]
    # DemonsScar, DarkHand, NKShield, NKSet, FChaosBlades, DChaosBlade, ChaosBlade

    #==================================================MAIN

    inventory = []

    hp = healpoint
   
    enemy = healpoint
    enemystart = True
    enemykill = 0

    lvlexp = 0
    lvl = 1 
    hplvl = hp
    
    lvlcheck = False
    if level >= 2:
        lvlcheck = True
    
    elvlexp = 0
    elvl = 1 
    ehplvl = enemy
    enemykillboost = 10

    money = cash * 1.2
    
    enemyboost = 0

    #typepower = ("Dark", "Lightning", "Fire", "Aqua", "Crystal", "Chaos", "Poison", "Blessed")

    endTime = endtime

    start = True

    datetimeStart = datetime.datetime.now()

    while start:

        #==================================================LEVEL UP AND HP LOCK

        if lvlcheck == True:
            for i in range(round(level)):
                hplvl += 15
                hp += hplvl
                lvl += 1

                ehplvl += 15
                enemy += ehplvl
                elvl += 1
                
                lvlcheck = False

        if lvlexp >= 100:

            hplvl += 15
            hp += hplvl
            lvlexp = 0
            lvl += 1

        if elvlexp >= 100:

            ehplvl += 15 
            enemy += ehplvl
            elvlexp = 0
            elvl += 1  

        if hp >= hplvl:
            hp = hplvl  

        if enemy >= ehplvl:
            enemy = ehplvl

        #==================================================USER MAIN

        damage = 1 + (lvl // 2)
        defenserandom = random.uniform(1,1.5)
        defense = (5 * defenserandom) + (lvl // 3)

        attack = random.randint(5,10)
        attackboost = random.uniform(1,2)

        accuracy = random.uniform(0.85,1)

        hpboost = random.randint(20,25)
        hpultraboost = random.uniform(1,2)

        lvlexp += 0.1
        money += 0.0008

        numb = random.randint(0,300)
        agility = random.randint(0,500)
        invnumb = random.randint(0,1000)

        #typedamage = random.choice(typepower)
        #typedefense = random.choice(typepower)

        #==================================================INVENTORY

        if invnumb <= 10:
            if numb >= 200:
                inventory.append(EstusFlask)
                print(f"Estus Flask add to inventory ({inventory.count(EstusFlask)})")
            if numb <= 200:
                inventory.append(tangoboost)
                print(f'Tango add to inventory ({inventory.count(tangoboost)})')

        if ChaosBlade in inventory:
            damage += 5
        
        if inventory.count(ChaosBlade) == 2:
            inventory.remove(ChaosBlade)
            inventory.remove(ChaosBlade)
            inventory.append(DChaosBlade)
            print("Dual Chaos Blade")
        
        if DChaosBlade in inventory:
            damage += 15

        if NKSet in inventory:
            defense += 5

        #==================================================MODE

        if mode == "Test":

            damagedell = -int((defense - (attack + damage)) // accuracy)

        if mode == "Versus" or "Enemy":

            #======================ENEMY MAIN

            edamage = ((1 + (elvl // 2)) + enemyboost)
            edefenserandom = random.uniform(1,1.5)
            edefense = ((5 * edefenserandom) + (elvl // 3) + enemyboost)
         
            if enemykill >= enemykillboost:
                enemyboost += 2
                enemykillboost += 10

            #print(f"{edamage}")

            eattack = random.randint(5,10)
            eattackboost = random.uniform(1,2)

            eaccuracy = random.uniform(0.85,1)

            ehpboost = random.randint(20,25)
            ehpultraboost = random.uniform(1,2)

            elvlexp += 0.15

            enumb = random.randint(0,300)
            eagility = random.randint(0,500)

            #etypedamage = random.choice(typepower)
            #etypedefense = random.choice(typepower)

            if mode == "Versus":

                damagedell = -int((defense - (eattack + edamage)) // eaccuracy)
                edamagedell = -int((edefense - (attack + damage)) // accuracy)
            
            if mode == "Enemy":
                
                damagedell = -int((defense - (eattack + edamage)) // eaccuracy)
                edamagedell = -int((edefense - (attack + damage)) // accuracy) 

            #======================DAMAGE AND HPBOOST

            if eagility >= 250:     
                enemy = enemy - edamagedell

            if eagility >= 350:
                enemy = enemy - ((edamagedell * eattackboost) // 2)

            if enemy <= 100 and enumb <= 100:
                enemy += 5

            elif enemy <= 35 and enumb <= 50:
                enemy += ehpboost

            elif enemy <= 35 and enumb <= 25:
                enemy += (ehpboost // eaccuracy)

        #==================================================ENEMY DEAD 

        if enemystart and mode == "Versus" or "Enemy":
            
            if enemy <= 0:

                print("enemy is dead")
                money += 50
                lvlexp += 20
                hp += 50
                #enemystart = False

                if mode == "Versus":
                    
                    datetimeEnd = datetime.datetime.now()
                    datetimeDelta = datetimeEnd - datetimeStart
                    money = (round(((lvl // 2) + money) * defenserandom))

                    print(f"You Win \nYou stay alive: {datetimeDelta} \nYour level: {lvl}")
                    print(f"You save money: {money}")
                    start = False

                elif mode == "Enemy":
                    enemy = ehplvl
                    enemykill += 1 
                    hp += hplvl
                    print(f"Enemy kill : {enemykill}")
                    itemnumb = random.randint(0,100)  

                    if enemykill == enemykillboost and money >= 750 and str(shopinv) != "[]":
                        
                        choiceM = str(input(f""" "Hi it's magic shop \n1. Regeneration Ring = 750$ 
                        \n2. Vampiric Mask = 1000$ \nYour money: {money} \nBuy or leave!  " """))

                        if money >= 750 and choiceM == "1" and RegRing not in inventory:
                            money -= 750
                            inventory.append(RegRing)
                            print("You Buy a Regeneration Ring")
                            shopinv.remove(RegRing)

                        if money >= 1000 and choiceM == "2" and VampiricMask not in inventory:
                            money -= 1000
                            inventory.append(VampiricMask)
                            print("You Buy a Vampiric Mask")
                            shopinv.remove(VampiricMask)

                        else:
                            print("goodbye!")

                    if NKSet not in inventory and itemnumb >= 95: 
                        inventory.append(NKSet)
                        print(f"Nameless Knight Set add to inventory")
                        
                    elif not inventory.count(ChaosBlade) == 2 and DChaosBlade not in inventory and itemnumb <= 5: 
                        inventory.append(ChaosBlade)
                        print(f"Chaos Blade add to inventory")
                    
                    elif invnumb <= 10:
                        inventory.append(EstusFlask)
                        print(f"EstusFlask add to inventory {inventory.count(EstusFlask)}")
                
                else:
                    enemystart = False

            elif enemy <= 10:
                print(f"Enemy heartpoint: {round(enemy)}")
              
        #==================================================USER > DAMAGE AND HPBOOST 

        if agility >= 150: 
            
            hp = hp - damagedell

        elif agility >= 250: 

            hp = hp - ((damagedell * attackboost) // 2)

        if hp <= 100 and numb <= 100:
            hp += 5

        if VampiricMask in inventory:
            hp += (damagedell // 2) 

        if RegRing in inventory:
            hp += 5

        if hp <= 50 and "Estus Flask" in inventory:
            #print(f"Estus Flask:{inventory.count(EstusFlask)} \nhp = {hp}")
            hp += 25
            inventory.remove(EstusFlask)
            print(f"Estus Flask:{inventory.count(EstusFlask)} Heartpoint = {hp}")
        
        if hp <= 75 and "Tango" in inventory:

            hp += 5
            inventory.remove(tangoboost)
            print(f"Tango:{inventory.count(tangoboost)} Heartpoint = {hp}")
        
        #==================================================USER DEAD

        if hp <= 0:
            
            datetimeEnd = datetime.datetime.now()
            datetimeDelta = datetimeEnd - datetimeStart
            money = (round(((lvl // 2) + money) * defenserandom))
            
            print(f"You are dead \nYou stay alive: {datetimeDelta} \nYour level: {lvl} \nMoney lose: {money}")
            if str(inventory) == "[]":
                pass
            if str(inventory) != "[]":
                print(f"Your inventory: {','.join(inventory)}")

            start = False
        
        elif hp <= 10:
            print(f"heartpoint: {round(hp)}")

        #==================================================USER NOT DEAD
        
        endTime = endTime - 1

        if endTime <= 0:

            datetimeEnd = datetime.datetime.now()
            datetimeDelta = datetimeEnd - datetimeStart

            lvlexp += 100
            elvlexp += 100

            hp += 100
            enemy += 100 

            money += 10
            endTime += endtime * (round(lvl))

            print(f"You stay alive: {datetimeDelta} \nYour level: {lvl} \nHeartpoint: {round(hp)} \nYour money: {round(money)}")
                
            continue

        if mode == "Enemy" and enemykill >= 100:
            datetimeEnd = datetime.datetime.now()
            datetimeDelta = datetimeEnd - datetimeStart
            money = (round(((lvl // 2) + money) * defenserandom))

            print(f"You Win \nYou stay alive: {datetimeDelta} \nYour level: {lvl}")
            print(f"You save money: {money}")
            if str(inventory) == "[]":
                pass
            if str(inventory) != "[]":
                print(f"Your inventory: {','.join(inventory)}")

            start = False

gamedata(level= 1, healpoint= 100, endtime= 100000, cash= 100, mode= "Enemy")
#mode = Versus / Test / Enemy