"""
 This game resembles the “Jetpac” arcade game from Donkey Kong 64. In this game, an astronaut needs to collect
 fuel boxes that appear at random spots and place them by his spaceship 10 times in order to escape. While he does this,
 there are enemies that fly in random directions. If the astronaut gets hit, he loses one life. The astronaut has three
 lives. Also, there are collectibles that fall along the way, which can be collected to boost the player’s score. In
 our game, we will also include a timer, and when it runs out, the player loses.

    The optional features our game includes are enemies, collectibles, timer and health meter.
"""

import gamebox
import pygame
import random

Height = 600
Width = 800

camera = gamebox.Camera(800, 600)
Player = gamebox.from_image(100, -40, 'RightAstronaut.png')
platforms = [gamebox.from_image(200, 270, 'Platform.png'), gamebox.from_image(450, 320, 'Platform.png'),
             gamebox.from_image(670, 150, 'Platform.png'), gamebox.from_image(400, 575, 'Ground.png')]
originalenemies = [gamebox.from_image(20, 50, 'RedEnemy.png'), 5, 0, gamebox.from_image(20, 300, 'RedEnemy.png'),
                   5, 0, gamebox.from_image(600, 200, 'RedEnemy.png'), 5, 3,
                   gamebox.from_image(700, 100, 'RedEnemy.png'), -4, 4, gamebox.from_image(400, 350, 'RedEnemy.png'),
                   -5, 0]
enemies = []
collectibles = [gamebox.from_image(450, -20, 'Collectible.png')]
fuelboxes = [gamebox.from_image(200, -20, 'Fuelbox.png')]
leftbullets = []
rightbullets = []
rocketship = gamebox.from_image(600, 400, 'Rocketship.png')
game_start = 0
timeremaining = 150
count = 0
lives = 3
score = 0
fuelboxcount = 0
stars = []
delay = 7
sprite_list = []
counter = 0


def tick(keys):
    camera.clear('black')

    global Player, platforms, originalenemies, enemies, collectibles, fuelboxes, leftbullets, rightbullets, rocketship
    global game_start, timeremaining, count, lives, score, fuelboxcount

    if game_start == 0:
        global counter, stars, Height, Width
        counter += 1  # counter increments at tick speed (30 per sec)
        if counter % 5 == 0:  # approx 1/6 sec
            numstars = random.randint(0, 7)
            for i in range(numstars):
                stars.append(gamebox.from_color(random.randint(5, Width - 5), 0, "light blue", 3, 3))
        for star in stars:
            star.y += 5
            if star.y > Height:
                stars.remove(star)
            camera.draw(star)
        if counter > ticks_per_second:
            for sprite in sprite_list:
                # boundary_action(sprite)
                sprite[0].move_speed()
                camera.draw(sprite[0])
        Player = gamebox.from_image(100, 350, 'RightAstronaut.png')
        platforms = [gamebox.from_image(200, 270, 'Platform.png'), gamebox.from_image(450, 320, 'Platform.png'),
                     gamebox.from_image(670, 150, 'Platform.png'), gamebox.from_image(400, 575, 'Ground.png')]
        platforms[0].width = 150
        platforms[1].width = 150
        platforms[2].width = 150
        platforms[3].width = 800
        originalenemies = [gamebox.from_image(-20, 50, 'RedEnemy.png'), 5, 0,
                           gamebox.from_image(-20, 300, 'RedEnemy.png'),
                           5, 0, gamebox.from_image(600, 200, 'RedEnemy.png'), 5, 3,
                           gamebox.from_image(700, 100, 'RedEnemy.png'), -4, 4,
                           gamebox.from_image(400, 350, 'RedEnemy.png'),
                           -5, 0]
        enemies = []
        collectibles = [gamebox.from_image(450, -20, 'Collectible.png')]
        fuelboxes = [gamebox.from_image(200, -25, 'Fuelbox.png')]
        fuelboxes[0].height = 25
        leftbullets = []
        rightbullets = []
        rocketship = gamebox.from_image(600, 400, 'Rocketship.png')
        rocketship.height = 150
        game_start = 0
        timeremaining = 150
        count = 0
        lives = 3
        score = 0
        fuelboxcount = 0
        title = gamebox.from_text(camera.x, camera.y-100, "Jetpac", 100, 'white')
        game_instructions_8 = gamebox.from_text(camera.x, camera.y-10, " *** Instructions *** ", 30, "white")
        game_instructions = gamebox.from_text(camera.x, camera.y+10, " UP key: move up", 25, "white")
        game_instructions_1 = gamebox.from_text(camera.x, camera.y+30, " LEFT key: move left", 25, "white")
        game_instructions_2 = gamebox.from_text(camera.x, camera.y + 50, " RIGHT key: move right", 25, "white")
        game_instructions_3 = gamebox.from_text(camera.x, camera.y + 70, " A: shoots left", 25, "white")
        game_instructions_4 = gamebox.from_text(camera.x, camera.y + 90, " S: shoots right", 25, "white")
        game_instructions_5 = gamebox.from_text(camera.x, camera.y + 110, " You have 3 lives. Each time you hit enemy,"
                                                                          "you lose one.", 25, "white")
        game_instructions_6 = gamebox.from_text(camera.x, camera.y + 130, " Collect the 10 fuel boxes.", 25,
                                                "white")
        game_instructions_7 = gamebox.from_text(camera.x, camera.y + 150, "The last item to collect will be the Rareware coin.", 25,
                                                "white")
        game_instructions_9 = gamebox.from_text(camera.x, camera.y + 170, "Collecting the blue diamonds will boost your score "
                                                                          "by 100 each time.", 25, 'white')
        game_instructions_10 = gamebox.from_text(camera.x, camera.y + 190, "You have 150 seconds to finish the game.", 25, 'white')
        instructions = gamebox.from_text(camera.x, camera.y-50, "Press q to start", 50, 'white')
        camera.draw(game_instructions)
        camera.draw(game_instructions_1)
        camera.draw(game_instructions_2)
        camera.draw(game_instructions_3)
        camera.draw(game_instructions_4)
        camera.draw(game_instructions_5)
        camera.draw(game_instructions_6)
        camera.draw(game_instructions_7)
        camera.draw(game_instructions_8)
        camera.draw(game_instructions_9)
        camera.draw(game_instructions_10)
        camera.draw(title)
        camera.draw(instructions)
        if pygame.K_q in keys:
            game_start = 1

    if game_start == 1:
        count += 1
        camera.draw(rocketship)
        Player.move_speed()
        Player.yspeed += 0.75
        Player.xspeed = 0

        if lives == 3:
            threelivesremaining = gamebox.from_image(250, 25, '3LivesRemaining.png')
            camera.draw(threelivesremaining)

        if lives == 2:
            twolivesremaining = gamebox.from_image(250, 25, '2LivesRemaining.png')
            camera.draw(twolivesremaining)

        if lives == 1:
            oneliferemaining = gamebox.from_image(250, 25, '1LifeRemaining.png')
            camera.draw(oneliferemaining)

        if Player.touches(rocketship):
            Player.move_to_stop_overlapping(rocketship)
        if pygame.K_UP in keys:
            Player.yspeed -= 1.5
        if pygame.K_LEFT in keys:
            Player.image = "LeftAstronaut.png"
            Player.xspeed = -5
        if pygame.K_RIGHT in keys:
            Player.image = 'RightAstronaut.png'
            Player.xspeed = 5

        if Player.x > Width:
            Player.x = 0
        if Player.x < 0:
            Player.x = Width
        if Player.y <= 0:
            Player.yspeed = 0
            Player.y = 1

        for platform in platforms:
            camera.draw(platform)
            if Player.touches(platform):
                Player.move_to_stop_overlapping(platform)
            for fuelbox in fuelboxes:
                if fuelbox.touches(platform):
                    fuelbox.move_to_stop_overlapping(platform)
            for leftbullet in leftbullets:
                if leftbullet.touches(platform):
                    leftbullets.remove(leftbullet)
            for rightbullet in rightbullets:
                if rightbullet.touches(platform):
                    rightbullets.remove(rightbullet)
            for enemy in enemies:
                if enemy.touches(platform):
                    enemies.remove(enemy)
            for collectible in collectibles:
                if collectible.touches(platform):
                    collectible.move_to_stop_overlapping(platform)
            if rocketship.touches(platform):
                rocketship.move_to_stop_overlapping(platform)

        if pygame.K_a in keys:
            keys.remove(97)
            newleftbullet = gamebox.from_image(Player.x, Player.y, 'Bullet.png')
            newleftbullet.height = 10
            leftbullets.append(newleftbullet)

        for leftbullet in leftbullets:
            leftbullet.move_speed()
            leftbullet.xspeed = -9
            if leftbullet.x < 0:
                leftbullets.remove(leftbullet)
            camera.draw(leftbullet)

        if pygame.K_s in keys:
            keys.remove(115)
            newrightbullet = gamebox.from_image(Player.x, Player.y, 'Bullet.png')
            newrightbullet.height = 10
            rightbullets.append(newrightbullet)

        for rightbullet in rightbullets:
            rightbullet.move_speed()
            rightbullet.xspeed = 9
            if rightbullet.x > Width:
                rightbullets.remove(rightbullet)
            camera.draw(rightbullet)

        if count == 1:
            for thirdnumber in range(0, 15, 3):
                originalenemies[thirdnumber].xspeed = originalenemies[thirdnumber + 1]
                originalenemies[thirdnumber].yspeed = originalenemies[thirdnumber + 2]
                originalenemies[thirdnumber].move_speed()
                enemies.append(originalenemies[thirdnumber])

        for enemy in enemies:
            for leftbullet in leftbullets:
                if leftbullet.touches(enemy):
                    if enemy in enemies:
                        enemies.remove(enemy)
                        leftbullets.remove(leftbullet)

        for enemy in enemies:
            for rightbullet in rightbullets:
                if rightbullet.touches(enemy):
                    if enemy in enemies:
                        enemies.remove(enemy)
                        rightbullets.remove(rightbullet)

        for fuelbox in fuelboxes:
            for secondfuelbox in fuelboxes:
                if secondfuelbox.touches(fuelbox) and secondfuelbox != fuelbox and (secondfuelbox.x > rocketship.x - 25
                                                                                    or secondfuelbox.x < rocketship.x +
                                                                                    25):
                    secondfuelbox.move_to_stop_overlapping(fuelbox)
            fuelbox.move_speed()
            fuelbox.yspeed += 0.1
            if Player.touches(fuelbox) and fuelbox.x == rocketship.x:
                Player.move_to_stop_overlapping(fuelbox)
            if Player.touches(fuelbox) and fuelbox.x != rocketship.x and fuelboxcount < 10:
                fuelboxcount += 1
                fuelbox.x = rocketship.x
                fuelbox.y = rocketship.y - 100
                if fuelboxcount == 9:
                    newfuelbox = gamebox.from_image(random.randrange(25, 776, 2), -25, 'RarewareCoin.png')
                    newfuelbox.width = 100
                else:
                    newfuelbox = gamebox.from_image(random.randrange(25, 776, 2), -25, 'Fuelbox.png')
                    newfuelbox.height = 25
                fuelboxes.append(newfuelbox)
            camera.draw(fuelbox)

        for collectible in collectibles:
            collectible.move_speed()
            collectible.yspeed += 0.1
            if collectible.touches(rocketship):
                collectible.move_to_stop_overlapping(rocketship)
            if Player.touches(collectible):
                score += 100
                collectibles.remove(collectible)
                newcollectible = gamebox.from_image(random.randint(15, 785), -15, 'Collectible.png')
                collectibles.append(newcollectible)
            camera.draw(collectible)

        for enemy in enemies:
            if Player.touches(enemy):
                lives -= 1
                enemies.remove(enemy)
                Player.x = 100
                Player.y = -40

        while len(enemies) < 7:
            location = random.randint(1, 2)
            if location == 1:
                newenemy = gamebox.from_image(-15, random.randint(75, 500), 'RedEnemy.png')
                newenemy.move_speed()
                newenemy.xspeed = random.randint(4, 8)
                newenemy.yspeed = random.randint(-7, 7)
                enemies.append(newenemy)
            if location == 2:
                newenemy = gamebox.from_image(815, random.randint(75, 500), 'RedEnemy.png')
                newenemy.move_speed()
                newenemy.xspeed = random.randint(-5, -1)
                newenemy.yspeed = random.randint(-5, 5)
                enemies.append(newenemy)

        for enemy in enemies:
            if enemy.x < -15:
                enemies.remove(enemy)
            if enemy.x > 815:
                if enemy in enemies:
                    enemies.remove(enemy)
            if enemy.y < 0:
                if enemy in enemies:
                    enemies.remove(enemy)
            enemy.move_speed()
            camera.draw(enemy)

        camera.draw(Player)
        rocketship.move_speed()
        rocketship.yspeed += 1

        if count % 30 == 0:
            timeremaining -= 1

        timer = gamebox.from_text(700, 25, 'Time Remaining: ' + str(timeremaining), 25, 'white')
        scorebox = gamebox.from_text(100, 25, "Score: " + str(score), 25, 'white')
        camera.draw(timer)
        camera.draw(scorebox)

        if lives == 0 or timeremaining == 0:
            game_start = 2

        if fuelboxcount == 10:
            game_start = 3

    if game_start == 2:
        counter += 1  # counter increments at tick speed (30 per sec)
        if counter % 5 == 0:  # approx 1/6 sec
            numstars = random.randint(0, 7)
            for i in range(numstars):
                stars.append(gamebox.from_color(random.randint(5, Width - 5), 0, "light blue", 3, 3))
        for star in stars:
            star.y += 5
            if star.y > Height:
                stars.remove(star)
            camera.draw(star)
        if counter > ticks_per_second:
            for sprite in sprite_list:
                # boundary_action(sprite)
                sprite[0].move_speed()
                camera.draw(sprite[0])
        losedtext = gamebox.from_text(camera.x, camera.y - 50, "You lost!", 50, 'white')
        finalscore = gamebox.from_text(camera.x, camera.y, "Your score is: " + str(score), 25, 'white')
        buttontopress = gamebox.from_text(camera.x, camera.y + 50, "Press SPACE to return to title screen", 25, 'white')
        camera.draw(losedtext)
        camera.draw(finalscore)
        camera.draw(buttontopress)
        if pygame.K_SPACE in keys:
            game_start = 0

    if game_start == 3:
        counter += 1  # counter increments at tick speed (30 per sec)
        if counter % 5 == 0:  # approx 1/6 sec
            numstars = random.randint(0, 7)
            for i in range(numstars):
                stars.append(gamebox.from_color(random.randint(5, Width - 5), 0, "light blue", 3, 3))
        for star in stars:
            star.y += 5
            if star.y > Height:
                stars.remove(star)
            camera.draw(star)
        if counter > ticks_per_second:
            for sprite in sprite_list:
                # boundary_action(sprite)
                sprite[0].move_speed()
                camera.draw(sprite[0])
        wontext = gamebox.from_text(camera.x, camera.y - 50, "You won!", 50, 'white')
        finalscore = gamebox.from_text(camera.x, camera.y, "Your score is: " + str(score), 25, 'white')
        buttontopress = gamebox.from_text(camera.x, camera.y + 50, "Press SPACE to return to title screen", 25, 'white')
        camera.draw(wontext)
        camera.draw(finalscore)
        camera.draw(buttontopress)
        if pygame.K_SPACE in keys:
            game_start = 0

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
