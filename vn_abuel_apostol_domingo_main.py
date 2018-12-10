from practice import *

if random.randint(0,100)>STD_CHANCE:
    STD_CHANCE=True
if random.randint(0,100)>CHOSEN_GIRL_PREGNANCY_CHANCE:
    CHOSEN_GIRL_PREGNANCY_CHANCE=True
if random.randint(0,100)>EXTRA_GIRL_ONE_PREGNANCY_CHANCE:
    EXTRA_GIRL_ONE_PREGNANCY_CHANCE=True
if random.randint(0,100)>EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
    EXTRA_GIRL_TWO_PREGNANCY_CHANCE=True


def good_ending():
    disp.fill(black)
    while True:
        a = 'Congratulations!'
        b = 'You had sex and no one got pregnant or an STD!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def std_cg_eo():
    disp.fill(black)
    while True:
        a = 'You\'re lucky this is just a game'
        b = 'You got an STD and ' +CHOSEN_GIRL+ ' & '+ EXTRA_GIRL_TWO+ 'are pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def std_cg_et():
    disp.fill(black)
    while True:
        a = 'You\'re lucky this is just a game'
        b = 'You got an STD and ' +CHOSEN_GIRL+ ' & '+ EXTRA_GIRL_ONE+ 'are pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def std_eo_et():
    disp.fill(black)
    while True:
        a = 'You\'re lucky this is just a game'
        b = 'You got an STD and ' +EXTRA_GIRL_TWO+ ' & '+ EXTRA_GIRL_ONE+ 'are pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def std_eo():
    disp.fill(black)
    while True:
        a = 'Don\'t have sex in real life please'
        b = 'You got an STD and ' + EXTRA_GIRL_ONE + ' is pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def std_et():
    disp.fill(black)
    while True:
        a = 'Don\'t have sex in real life please'
        b = 'You got an STD and ' + EXTRA_GIRL_TWO + ' is pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def std_cg():
    disp.fill(black)
    while True:
        a = 'Don\'t have sex in real life please'
        b = 'You got an STD and ' + CHOSEN_GIRL + ' is pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def std():
    disp.fill(black)
    while True:
        a = 'At least no one\'s pregnant'
        b = 'You got an STD.'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def cg_eo():
    disp.fill(black)
    while True:
        a = 'DOBOL TROBOL!'
        b = 'You got ' + CHOSEN_GIRL+ ' and '+ EXTRA_GIRL_ONE + ' pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def cg_et():
    disp.fill(black)
    while True:
        a = 'DOBOL TROBOL!'
        b = 'You got ' + CHOSEN_GIRL+ ' and '+ EXTRA_GIRL_TWO + ' pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def eo_et():
    disp.fill(black)
    while True:
        a = 'DOBOL TROBOL!'
        b = 'You got ' + EXTRA_GIRL_TWO+ ' and '+ EXTRA_GIRL_ONE + 'pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def cg():
    disp.fill(black)
    while True:
        a = 'Coulda been worse!'
        b = 'You got ' + CHOSEN_GIRL + ' pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def eo():
    disp.fill(black)
    while True:
        a = 'Coulda been worse!'
        b = 'You got ' + CHOSEN_GIRL + ' pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()

def et():
    disp.fill(black)
    while True:
        a = 'Coulda been worse!'
        b = 'You got ' + CHOSEN_GIRL + ' pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def super_bad_ending():
    disp.fill(black)
    while True:
        a = 'MAJOR OOFF!'
        b = 'You got an STD, and everyone (except you) is pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def cg_eo_et():
    disp.fill(black)
    while True:
        a = 'OOOF!'
        b = 'You got everyone (except you!) pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


def no_sex():
    disp.fill(black)
    while True:
        a = 'Not good, but not bad either!'
        b = 'No sex. But at least you didn\'t get anyone pregnant!'
        while ctr == 0:
            mainframe_two(a,b)
            ctr +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                credit()
        pygame.display.update()


lol=runmain()

if lol==1 or lol=='convo_negative_one':
    convo_negative_one()

if lol=='convo_one':
    convo_one()

if lol=='convo_two':
    convo_two()

if lol=='convo_three':
    convo_three()

if lol=='convo_four':
    convo_four()

if lol=='convo_five':
    convo_five()

if lol=='sofa_scene':
    sofa_scene()

if lol=='drink_scene_ctr()':
    drink_scene_ctr()

if lol=='drink_scene':
    drink_scene()

if lol=='drink_convo_one':
    drink_convo_one()

if lol=='drink_convo_two':
    drink_convo_two()
    
if lol=='drink_tut':
    drink_tut()

if lol=='drink_tut_one':
    drink_tut_one()

if lol=='drink_tut_two':
    drink_tut_two()

if lol=='drink_tut_tri':
    drink_tut_tri()

if lol=='drink_tut_por':
    drink_tut_por()

if lol=='drink_tut_pyb':
    drink_tut_pyb()

if lol=='drink_tut_six':
    drink_tut_six()

if lol=='drink_tut_svn':
    drink_tut_svn()

if lol=='drink_tut_ate':
    drink_tut_ate()

if lol=='drink_no':
    drink_tut_nyn()

if lol=='drink_scene_tri_one':
    drink_scene_tri_one()

if lol=='drink_scene_tri_two':
    drink_scene_tri_two()

if lol=='drink_scene_tri_tri':
    drink_scene_tri_tri()

if lol=='drink_scene_tri_por':
    drink_scene_tri_por()

if lol=='drink_scene_tri_pyb':
    drink_scene_tri_pyb()

if lol=='drink_scene_tri_six':
    drink_scene_tri_six()

if lol=='drink_scene_tri_svn':
    drink_scene_tri_svn()

if lol=='drink_scene_tri_ate':
    drink_scene_tri_ate()

if lol=='drink_scene_tri_nyn':
    drink_scene_tri_nyn()

if lol=='drink_scene_tri_ten':
    drink_scene_tri_ten()

if lol=='drink_scene_tri_lvn':
    drink_scene_tri_lvn()

if lol=='drink_scene_pyb_one':
    drink_scene_pyb_one()

if lol=='drink_scene_pyb_two':
    drink_scene_pyb_two()

if lol=='drink_scene_pyb_tri':
    drink_scene_pyb_tri()

if lol=='drink_scene_pyb_por':
    drink_scene_pyb_por()

if lol=='drink_scene_two_one':
    drink_scene_two_one()

if lol=='drink_scene_two_two':
    drink_scene_two_two()

if lol=='drink_scene_two_tri':
    drink_scene_two_tri()

if lol=='drink_scene_two_por':
    drink_scene_two_por()

if lol=='drink_scene_two_pyb':
    drink_scene_two_pyb()

if lol=='drink_scene_two_six':
    drink_scene_two_six()

if lol=='drink_scene_two_svn':
    drink_scene_two_svn()

if lol=='drink_scene_two_ate':
    drink_scene_two_ate()

if lol=='drink_scene_two_nyn':
    drink_scene_two_nyn()

if lol=='drink_scene_six_one':
    drink_scene_six_one()

if lol=='drink_scene_six_two':
    drink_scene_six_two()

if lol=='drink_scene_six_tri':
    drink_scene_six_tri()

if lol=='drink_scene_six_por':
    drink_scene_six_por()

if lol=='drink_scene_six_pyb':
    drink_scene_six_pyb()

if lol=='drink_scene_six_six':
    drink_scene_six_six()

if lol=='drink_scene_six_svn':
    drink_scene_six_svn()

if lol=='drink_scene_six_ate':
    drink_scene_six_ate()

if lol=='drink_scene_six_nyn':
    drink_scene_six_nyn()

if lol=='drink_scene_six_paris':
    drink_scene_six_paris()

if lol=='drink_scene_six_korea':
    drink_scene_six_korea()

if lol=='drink_scene_six_uranus':
    drink_scene_six_uranus()

if lol=='drink_scene_six_antartica':
    drink_scene_six_antartica()
    
if lol=='drink_scene_lvn':
    drink_scene_lvn()

if lol=='drink_scene_six_twv':
    drink_scene_six_twv()

if lol=='drink_scene_six_trn':
    drink_scene_six_trn()

if lol=='drink_scene_six_porten':
    drink_scene_six_porten()

if lol=='drink_scene_six_pipten':
    drink_scene_six_pipten()

if lol=='dance_scene':
    dance_scene()

if lol=='dance_scene_one':
    dance_scene_one()

if lol=='dance_scene_two':
    dance_scene_two()

if lol=='dance_scene_tri':
    dance_scene_tri()

if lol=='dance_scene_por':
    dance_scene_por()

if lol=='dance_scene_pyb':
    dance_scene_pyb()

if lol=='dance_scene_grind':
    dance_scene_grind()

if lol=='dance_scene_svn':
    dance_scene_svn()

if lol=='dance_scene_ate':
    dance_scene_ate()

if lol=='dance_she_leaves':
    dance_she_leaves()
    
if lol=='dance_dj_over':
    dance_dj_over()

if lol=='dance_scene_ask':
    dance_scene_ask()

if lol=='dance_scene_ask_two':
    dance_scene_ask_two()

if lol=='dance_scene_ask_tri':
    dance_scene_ask_tri()

if lol=='dance_scene_ew':
    dance_scene_ew()

if lol=='dance_scene_woah':
    dance_scene_woah()

if lol=='dance_scene_woah_two':
    dance_scene_woah_two()

if lol=='dance_scene_ew_two':
    dance_scene_ew_two()

if lol=='smoke_zero':
    smoke_zero()

if lol=='smoke_one':
    smoke_one()

if lol=='smoke_two':
    smoke_two()

if lol=='smoke_tri':
    smoke_tri()

if lol=='smoke_por':
    smoke_por()

if lol=='smoke_pyb':
    smoke_pyb()

if lol=='smoke_six':
    smoke_six()

if lol=='smoke_svn':
    smoke_svn()

if lol=='smoke_nyn':
    smoke_nyn()

if lol=='smoke_ten':
    smoke_ten()

if lol=='smoke_twv':
    smoke_twv()

if lol=='smoke_trn':
    smoke_trn()

if lol=='smoke_rtn':
    smoke_rtn()

if lol=='smoke_ptn':
    smoke_ptn()

if lol=='smoke_stn':
    smoke_stn()

if lol=='smoke_svtn':
    smoke_svtn()

if lol=='smoke_aten':
    smoke_aten()

if lol=='smoke_nytn':
    smoke_nytn()

if lol=='smoke_twty':
    smoke_twty()

if lol=='smoke_twtu':
    smoke_twtu()

if lol=='smoke_twto':
    smoke_twto()

if lol=='smoke_thank_you':
    smoke__thank_you()

if lol=='smoke_twpor':
    smoke_twpor()

if lol=='smoke_twpyb':
    smoke_twpyb()

if lol=='smoke_twsix':
    smoke_twsix()

if lol=='smoke_twsvn':
    smoke_twsvn()

if lol=='smoke_twate':
    smoke_twate()

if lol=='smoke_twnyn':
    smoke_twnyn()

if lol=='smoke_trty':
    smoke_trty()

if lol=='smoke_trto':
    smoke_()

if lol=='smoke_empty':
    smoke_()

##if lol=='sex':
##    sex()
##
##if lol=='foreplay':
##    foreplay()
##
##if lol=='knock_knock':
##    knock_knock()
##
##if lol=='whos_there':
##    whos_there()
##
##if lol=='stop_knocking':
##    stop_knocking()
##
##if lol=='solo':
##    solo()
##
##if lol=='solo_one':
##    solo_two()
##
##if lol=='where_to_put':
##    where_to_put(who) ####tama ba 'to
##
##if lol=='who_to_put':
##    who_two_put()
##
##if lol=='two':
##    two()
##
##if lol=='tri':
##    tri()
##
##if lol=='anal':
##    anal(who)
##
##if lol=='vagene':
##    vagene(who)
##
##if lol=='hand':
##    hand()
##
##if lol=='mouth':
##    mouth(who)
##
##if lol=='exhausted':
##    exhausted()


#copy this for every functio/scene na may savegame:
#if lol=='scene/function':
    #scenefunction()

if cash == 0 and GIRLS == []:
    no_sex()
else:
    if CONDOMS:
        good_ending()
    else:
        if STD_CHANCE and CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            super_bad_ending()
        elif STD_CHANCE and CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE:
            std_cg_eo()  
        elif STD_CHANCE and CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            std_cg_et()
        elif STD_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            std_eo_et()
        elif STD_CHANCE and CHOSEN_GIRL_PREGNANCY_CHANCE:
            std_cg()
        elif STD_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE:
            std_eo()
        elif STD_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            std_et()
        elif STD_CHANCE:
            std()
        elif CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            cg_eo_et()
        elif CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_ONE_PREGNANCY_CHANCE:
            cg_eo() 
        elif CHOSEN_GIRL_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            cg_et()
        elif EXTRA_GIRL_ONE_PREGNANCY_CHANCE and EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            eo_et()
        elif CHOSEN_GIRL_PREGNANCY_CHANCE:
            cg()
        elif EXTRA_GIRL_ONE_PREGNANCY_CHANCE:
            eo()
        elif EXTRA_GIRL_TWO_PREGNANCY_CHANCE:
            et()
        else:
            good_ending()