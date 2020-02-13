
import time,random
player_score=0
enemy_score=0
while True:

    for i in range(3):
        time.sleep(1.5)  # 让局与局之间有较明显的有时间间隔
        print(' \n~~~~~~~~~~现在是第'+str(i+1)+'局，ready go!~~~~~~~~~~') 
#生成随机属性
        player_life = random.randint(100,150) 
        player_attack = random.randint(30,50) 
        enemy_life = random.randint(100,150) 
        enemy_attack = random.randint(30,50) 

#展示双方属性

        print('游戏开始，【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
        print('------------------------')
        time.sleep(1)
        print('游戏开始，【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
        print('------------------------')
        time.sleep(1)

#双方PK


        while True:
            player_life = player_life - enemy_attack
            enemy_life  = enemy_life - player_attack
            if player_life <= 0 or enemy_life <= 0:
                print('本局游戏结束！！！')
                break
            else:
                print(' 敌人进攻,  玩家血量 :'+str(player_life))
                time.sleep(1)
                print(' 玩家进攻,   敌人血量 :'+str(enemy_life))
                time.sleep(1)
                print('------------')
        print(' 最后玩家血量 :'+str(player_life))
        time.sleep(1)
        print(' 最后敌人血量 :'+str(enemy_life))
        print('-------------')
        if enemy_life>0 and player_life<=0:
            print('第'+str(i+1)+'局: '+'敌人赢了')
            print('====================================')
            enemy_score=enemy_score+1
        elif enemy_life<=0 and player_life>0:
            print('第'+str(i+1)+'局: '+'玩家赢了')
            print('====================================')
            player_score=player_score+1
        elif enemy_life<=0 and player_life<=0:
            print('第'+str(i+1)+'局: '+'平局')
            print('====================================')
            pass
    print('******* ******** *******')
    time.sleep(1)
    if player_score > enemy_score:
        print('三局之后，'+'玩家和敌人的比分是：'+str(player_score)+' VS '+str(enemy_score)+'\n玩家获得最终胜利')
    elif player_life == enemy_life:
        print('三局之后，'+'玩家和敌人的比分是：'+str(player_score)+' VS '+str(enemy_score)+'\n打成平手')
    else:
        print('三局之后，'+'玩家和敌人的比分是：'+str(player_score)+' VS '+str(enemy_score)+'\n玩家输掉比赛')
    
    gamechoose = input('再玩一遍吗?y or n: \n')
    if gamechoose == 'y':
        continue
    else:
        print('好吧，游戏彻底结束')
        break