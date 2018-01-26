import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import datetime

def sky_data():
    """Import star data from HYG table and output data for the brightest stars in list format."""
    
    f=open('hygdata_v3.csv','r')
    reader=csv.reader(f)

    star_data=[] 
    
    for row in reader: #list of data for all stars
        star_data.append(row)

    f.close()

    star_data=star_data[2:]
    bright_star_data=[]
    
    for star in range(len(star_data)):
        if float(star_data[star][13])<=4.0: #choosing brightest stars only
            bright_star_data.append(star_data[star])
            #columns 7 and 8 are ra and dec, column 13 is magnitude
            #note that the lower the magnitude, the brighter the star
    for star in range(len(star_data)):
        if star_data[star][29]=='Gem' and float(star_data[star][13])<=4.42:
            bright_star_data.append(star_data[star])
    for star in range(len(star_data)):
        if star_data[star][29]=='Per' and float(star_data[star][13])<=4.1 and float(star_data[star][13])>4.0:
            bright_star_data.append(star_data[star])
    for star in range(len(star_data)):
        if star_data[star][29]=='Lyr' and float(star_data[star][13])<=4.4 and float(star_data[star][13])>4.0:
            bright_star_data.append(star_data[star])

    return bright_star_data

def north_plot(year=2018,month=1,day=1,limited_view='true'):
    """Plots all stars visible in northern hemisphere with constellations. 
    Input format: year, month, day. 
    Leave limited_view at its default value to see only the stars that would be visible on the given date; 
    set it to something else to see the whole map."""
    
    stars=sky_data()
    north_data=[]

    for star in range(len(stars)):#only using northern hemisphere stars
        if float(stars[star][8])>=-30:
            if float(stars[star][8])<=90:
                north_data.append(stars[star])

    plt.style.use('dark_background')
    ax = plt.subplot(111, projection='polar')

    #setting origin based on input date
    ny=datetime.date(2018,1,1)
    current_date=datetime.date(year,month,day)
    days=(current_date-ny).days
    z_centre=35*np.exp(1j*(2+(days/365.)*2*np.pi))
    print np.abs(z_centre)
    
    #create arrays of ra and dec in polar coords as well as magnitude
    ra=np.zeros(len(north_data))
    dec=np.zeros(len(north_data))
    mag=np.zeros(len(north_data))
    full_con_list=[]
    
    for star in range(len(north_data)):
        ra[star]=float(north_data[star][7])*(np.pi/12.0)#ra in radians
        dec[star]=90-float(north_data[star][8])#dec all positive
        mag[star]=4.42-float(north_data[star][13])#mag all positive and on increasing scale
        full_con_list.append(north_data[star][29])#column 29 is constellation name
        if limited_view is 'true':
            z=dec[star]*np.exp(1j*ra[star])
            z=-np.conj(z)
            z=z-z_centre
            ra[star]=np.angle(z)
            dec[star]=np.abs(z)

    unique_con_list=list(set(full_con_list))
    #print this to see all the abbreviated constellation names
    #print unique_con_list



    #Lines for Cygnus
    Cygnus_ra=np.array([])
    Cygnus_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Cyg':
            if float(north_data[star][13])<=3.5:
                Cygnus_ra=np.append(Cygnus_ra,ra[star])
                Cygnus_dec=np.append(Cygnus_dec,dec[star])

    Cyg_line_0_ra=np.array([Cygnus_ra[0],Cygnus_ra[2]])
    Cyg_line_0_dec=np.array([Cygnus_dec[0],Cygnus_dec[2]])
    ax.plot(Cyg_line_0_ra,Cyg_line_0_dec,'r')

    Cyg_line_1_ra=np.array([Cygnus_ra[3],Cygnus_ra[2]])
    Cyg_line_1_dec=np.array([Cygnus_dec[3],Cygnus_dec[2]])
    ax.plot(Cyg_line_1_ra,Cyg_line_1_dec,'r')

    Cyg_line_2_ra=np.array([Cygnus_ra[4],Cygnus_ra[2]])
    Cyg_line_2_dec=np.array([Cygnus_dec[4],Cygnus_dec[2]])
    ax.plot(Cyg_line_2_ra,Cyg_line_2_dec,'r')

    Cyg_line_3_ra=np.array([Cygnus_ra[1],Cygnus_ra[2]])
    Cyg_line_3_dec=np.array([Cygnus_dec[1],Cygnus_dec[2]])
    ax.plot(Cyg_line_3_ra,Cyg_line_3_dec,'r')

    Cyg_line_4_ra=np.array([Cygnus_ra[4],Cygnus_ra[5]])
    Cyg_line_4_dec=np.array([Cygnus_dec[4],Cygnus_dec[5]])
    ax.plot(Cyg_line_4_ra,Cyg_line_4_dec,'r')

    #Lines for Orion
    Orion_ra=np.array([])
    Orion_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Ori':
            if float(north_data[star][13])<=3.4:
                Orion_ra=np.append(Orion_ra,ra[star])
                Orion_dec=np.append(Orion_dec,dec[star])

    Ori_line_0_ra=np.array([Orion_ra[8],Orion_ra[9]])
    Ori_line_0_dec=np.array([Orion_dec[8],Orion_dec[9]])
    ax.plot(Ori_line_0_ra,Ori_line_0_dec,'r')
    
    Ori_line_1_ra=np.array([Orion_ra[0],Orion_ra[3]])
    Ori_line_1_dec=np.array([Orion_dec[0],Orion_dec[3]])
    ax.plot(Ori_line_1_ra,Ori_line_1_dec,'r')

    Ori_line_2_ra=np.array([Orion_ra[4],Orion_ra[3]])
    Ori_line_2_dec=np.array([Orion_dec[4],Orion_dec[3]])
    ax.plot(Ori_line_2_ra,Ori_line_2_dec,'r')

    Ori_line_3_ra=np.array([Orion_ra[5],Orion_ra[3]])
    Ori_line_3_dec=np.array([Orion_dec[5],Orion_dec[3]])
    ax.plot(Ori_line_3_ra,Ori_line_3_dec,'r')

    Ori_line_4_ra=np.array([Orion_ra[10],Orion_ra[3]])
    Ori_line_4_dec=np.array([Orion_dec[10],Orion_dec[3]])
    ax.plot(Ori_line_4_ra,Ori_line_4_dec,'r')

    Ori_line_5_ra=np.array([Orion_ra[10],Orion_ra[5]])
    Ori_line_5_dec=np.array([Orion_dec[10],Orion_dec[5]])
    ax.plot(Ori_line_5_ra,Ori_line_5_dec,'r')

    Ori_line_6_ra=np.array([Orion_ra[4],Orion_ra[1]])
    Ori_line_6_dec=np.array([Orion_dec[4],Orion_dec[1]])
    ax.plot(Ori_line_6_ra,Ori_line_6_dec,'r')

    Ori_line_7_ra=np.array([Orion_ra[10],Orion_ra[8]])
    Ori_line_7_dec=np.array([Orion_dec[10],Orion_dec[8]])
    ax.plot(Ori_line_7_ra,Ori_line_7_dec,'r')

    Ori_line_8_ra=np.array([Orion_ra[7],Orion_ra[8]])
    Ori_line_8_dec=np.array([Orion_dec[7],Orion_dec[8]])
    ax.plot(Ori_line_8_ra,Ori_line_8_dec,'r')

    Ori_line_9_ra=np.array([Orion_ra[7],Orion_ra[4]])
    Ori_line_9_dec=np.array([Orion_dec[7],Orion_dec[4]])
    ax.plot(Ori_line_9_ra,Ori_line_9_dec,'r')

    #Lines for Ursa Major
    UMa_ra=np.array([])
    UMa_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'UMa':
            if float(north_data[star][13])<=3.8:
                UMa_ra=np.append(UMa_ra,ra[star])
                UMa_dec=np.append(UMa_dec,dec[star])

    UMa_line_0_ra=np.array([UMa_ra[12],UMa_ra[13]])
    UMa_line_0_dec=np.array([UMa_dec[12],UMa_dec[13]])
    ax.plot(UMa_line_0_ra,UMa_line_0_dec,'r')

    UMa_line_1_ra=np.array([UMa_ra[8],UMa_ra[9]])
    UMa_line_1_dec=np.array([UMa_dec[8],UMa_dec[9]])
    ax.plot(UMa_line_1_ra,UMa_line_1_dec,'r')
    
    UMa_line_2_ra=np.array([UMa_ra[8],UMa_ra[13]])
    UMa_line_2_dec=np.array([UMa_dec[8],UMa_dec[13]])
    ax.plot(UMa_line_2_ra,UMa_line_2_dec,'r')
    
    UMa_line_3_ra=np.array([UMa_ra[14],UMa_ra[13]])
    UMa_line_3_dec=np.array([UMa_dec[14],UMa_dec[13]])
    ax.plot(UMa_line_3_ra,UMa_line_3_dec,'r')
    
    UMa_line_4_ra=np.array([UMa_ra[9],UMa_ra[14]])
    UMa_line_4_dec=np.array([UMa_dec[9],UMa_dec[14]])
    ax.plot(UMa_line_4_ra,UMa_line_4_dec,'r')
    
    UMa_line_5_ra=np.array([UMa_ra[15],UMa_ra[14]])
    UMa_line_5_dec=np.array([UMa_dec[15],UMa_dec[14]])
    ax.plot(UMa_line_5_ra,UMa_line_5_dec,'r')
    
    UMa_line_6_ra=np.array([UMa_ra[15],UMa_ra[16]])
    UMa_line_6_dec=np.array([UMa_dec[15],UMa_dec[16]])
    ax.plot(UMa_line_6_ra,UMa_line_6_dec,'r')

    UMa_line_7_ra=np.array([UMa_ra[17],UMa_ra[16]])
    UMa_line_7_dec=np.array([UMa_dec[17],UMa_dec[16]])
    ax.plot(UMa_line_7_ra,UMa_line_7_dec,'r')

    UMa_line_8_ra=np.array([UMa_ra[0],UMa_ra[3]])
    UMa_line_8_dec=np.array([UMa_dec[0],UMa_dec[3]])
    ax.plot(UMa_line_8_ra,UMa_line_8_dec,'r')

    UMa_line_9_ra=np.array([UMa_ra[3],UMa_ra[9]])
    UMa_line_9_dec=np.array([UMa_dec[3],UMa_dec[9]])
    ax.plot(UMa_line_9_ra,UMa_line_9_dec,'r')

    UMa_line_10_ra=np.array([UMa_ra[0],UMa_ra[5]])
    UMa_line_10_dec=np.array([UMa_dec[0],UMa_dec[5]])
    ax.plot(UMa_line_10_ra,UMa_line_10_dec,'r')

    UMa_line_11_ra=np.array([UMa_ra[4],UMa_ra[5]])
    UMa_line_11_dec=np.array([UMa_dec[4],UMa_dec[5]])
    ax.plot(UMa_line_11_ra,UMa_line_11_dec,'r')

    UMa_line_12_ra=np.array([UMa_ra[4],UMa_ra[1]])
    UMa_line_12_dec=np.array([UMa_dec[4],UMa_dec[1]])
    ax.plot(UMa_line_12_ra,UMa_line_12_dec,'r')

    UMa_line_13_ra=np.array([UMa_ra[4],UMa_ra[2]])
    UMa_line_13_dec=np.array([UMa_dec[4],UMa_dec[2]])
    ax.plot(UMa_line_13_ra,UMa_line_13_dec,'r')

    UMa_line_14_ra=np.array([UMa_ra[4],UMa_ra[10]])
    UMa_line_14_dec=np.array([UMa_dec[4],UMa_dec[10]])
    ax.plot(UMa_line_14_ra,UMa_line_14_dec,'r')

    UMa_line_15_ra=np.array([UMa_ra[6],UMa_ra[10]])
    UMa_line_15_dec=np.array([UMa_dec[6],UMa_dec[10]])
    ax.plot(UMa_line_15_ra,UMa_line_15_dec,'r')

    UMa_line_16_ra=np.array([UMa_ra[7],UMa_ra[10]])
    UMa_line_16_dec=np.array([UMa_dec[7],UMa_dec[10]])
    ax.plot(UMa_line_16_ra,UMa_line_16_dec,'r')

    UMa_line_17_ra=np.array([UMa_ra[12],UMa_ra[10]])
    UMa_line_17_dec=np.array([UMa_dec[12],UMa_dec[10]])
    ax.plot(UMa_line_17_ra,UMa_line_17_dec,'r')

    #Lines for Auriga
    Aur_ra=np.array([])
    Aur_dec=np.array([])

    for star in range(len(north_data)):
        if north_data[star][29] == 'Aur':
            if float(north_data[star][13])<=3:
                Aur_ra=np.append(Aur_ra,ra[star])
                Aur_dec=np.append(Aur_dec,dec[star])
        if north_data[star][29] == 'Tau':
            if float(north_data[star][13])<=2 and float(north_data[star][13])>=1:
                Aur_ra=np.append(Aur_ra,ra[star])
                Aur_dec=np.append(Aur_dec,dec[star])

    Aur_line_1_ra=np.array([Aur_ra[0],Aur_ra[1]])
    Aur_line_1_dec=np.array([Aur_dec[0],Aur_dec[1]])
    ax.plot(Aur_line_1_ra,Aur_line_1_dec,'r')

    Aur_line_2_ra=np.array([Aur_ra[2],Aur_ra[0]])
    Aur_line_2_dec=np.array([Aur_dec[2],Aur_dec[0]])
    ax.plot(Aur_line_2_ra,Aur_line_2_dec,'r')

    Aur_line_3_ra=np.array([Aur_ra[2],Aur_ra[4]])
    Aur_line_3_dec=np.array([Aur_dec[2],Aur_dec[4]])
    ax.plot(Aur_line_3_ra,Aur_line_3_dec,'r')

    Aur_line_4_ra=np.array([Aur_ra[3],Aur_ra[4]])
    Aur_line_4_dec=np.array([Aur_dec[3],Aur_dec[4]])
    ax.plot(Aur_line_4_ra,Aur_line_4_dec,'r')

    Aur_line_5_ra=np.array([Aur_ra[1],Aur_ra[3]])
    Aur_line_5_dec=np.array([Aur_dec[1],Aur_dec[3]])
    ax.plot(Aur_line_5_ra,Aur_line_5_dec,'r')

    #Lines for Gemini
    Gem_ra=np.array([])
    Gem_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Gem':
            if float(north_data[star][13])<=5:
                Gem_ra=np.append(Gem_ra,ra[star])
                Gem_dec=np.append(Gem_dec,dec[star])

    Gem_line_1_ra=np.array([Gem_ra[3],Gem_ra[1]])
    Gem_line_1_dec=np.array([Gem_dec[3],Gem_dec[1]])
    ax.plot(Gem_line_1_ra,Gem_line_1_dec,'r')

    Gem_line_2_ra=np.array([Gem_ra[3],Gem_ra[16]])
    Gem_line_2_dec=np.array([Gem_dec[3],Gem_dec[16]])
    ax.plot(Gem_line_2_ra,Gem_line_2_dec,'r')

    Gem_line_3_ra=np.array([Gem_ra[8],Gem_ra[22]])
    Gem_line_3_dec=np.array([Gem_dec[8],Gem_dec[22]])
    ax.plot(Gem_line_3_ra,Gem_line_3_dec,'r')

    Gem_line_4_ra=np.array([Gem_ra[8],Gem_ra[28]])
    Gem_line_4_dec=np.array([Gem_dec[8],Gem_dec[28]])
    ax.plot(Gem_line_4_ra,Gem_line_4_dec,'r')

    Gem_line_5_ra=np.array([Gem_ra[11],Gem_ra[28]])
    Gem_line_5_dec=np.array([Gem_dec[11],Gem_dec[28]])
    ax.plot(Gem_line_5_ra,Gem_line_5_dec,'r')

    Gem_line_6_ra=np.array([Gem_ra[10],Gem_ra[28]])
    Gem_line_6_dec=np.array([Gem_dec[10],Gem_dec[28]])
    ax.plot(Gem_line_6_ra,Gem_line_6_dec,'r')

    Gem_line_7_ra=np.array([Gem_ra[7],Gem_ra[28]])
    Gem_line_7_dec=np.array([Gem_dec[7],Gem_dec[28]])
    ax.plot(Gem_line_7_ra,Gem_line_7_dec,'r')

    Gem_line_8_ra=np.array([Gem_ra[7],Gem_ra[6]])
    Gem_line_8_dec=np.array([Gem_dec[7],Gem_dec[6]])
    ax.plot(Gem_line_8_ra,Gem_line_8_dec,'r')

    Gem_line_9_ra=np.array([Gem_ra[7],Gem_ra[21]])
    Gem_line_9_dec=np.array([Gem_dec[7],Gem_dec[21]])
    ax.plot(Gem_line_9_ra,Gem_line_9_dec,'r')

    Gem_line_10_ra=np.array([Gem_ra[6],Gem_ra[4]])
    Gem_line_10_dec=np.array([Gem_dec[6],Gem_dec[4]])
    ax.plot(Gem_line_10_ra,Gem_line_10_dec,'r')

    Gem_line_11_ra=np.array([Gem_ra[2],Gem_ra[21]])
    Gem_line_11_dec=np.array([Gem_dec[2],Gem_dec[21]])
    ax.plot(Gem_line_11_ra,Gem_line_11_dec,'r')

    Gem_line_12_ra=np.array([Gem_ra[22],Gem_ra[9]])
    Gem_line_12_dec=np.array([Gem_dec[22],Gem_dec[9]])
    ax.plot(Gem_line_12_ra,Gem_line_12_dec,'r')

    Gem_line_13_ra=np.array([Gem_ra[22],Gem_ra[5]])
    Gem_line_13_dec=np.array([Gem_dec[22],Gem_dec[5]])
    ax.plot(Gem_line_13_ra,Gem_line_13_dec,'r')

    Gem_line_14_ra=np.array([Gem_ra[22],Gem_ra[3]])
    Gem_line_14_dec=np.array([Gem_dec[22],Gem_dec[3]])
    ax.plot(Gem_line_14_ra,Gem_line_14_dec,'r')

    Gem_line_15_ra=np.array([Gem_ra[1],Gem_ra[14]])
    Gem_line_15_dec=np.array([Gem_dec[1],Gem_dec[14]])
    ax.plot(Gem_line_15_ra,Gem_line_15_dec,'r')

    Gem_line_16_ra=np.array([Gem_ra[14],Gem_ra[13]])
    Gem_line_16_dec=np.array([Gem_dec[14],Gem_dec[13]])
    ax.plot(Gem_line_16_ra,Gem_line_16_dec,'r')

    #Lines for Taurus
    Tau_ra=np.array([])
    Tau_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Tau':
            if float(north_data[star][13])<=3.6:
                Tau_ra=np.append(Tau_ra,ra[star])
                Tau_dec=np.append(Tau_dec,dec[star])

    Tau_line_1_ra=np.array([Tau_ra[0],Tau_ra[2]])
    Tau_line_1_dec=np.array([Tau_dec[0],Tau_dec[2]])
    ax.plot(Tau_line_1_ra,Tau_line_1_dec,'r')

    Tau_line_2_ra=np.array([Tau_ra[3],Tau_ra[2]])
    Tau_line_2_dec=np.array([Tau_dec[3],Tau_dec[2]])
    ax.plot(Tau_line_2_ra,Tau_line_2_dec,'r')

    Tau_line_3_ra=np.array([Tau_ra[3],Tau_ra[4]])
    Tau_line_3_dec=np.array([Tau_dec[3],Tau_dec[4]])
    ax.plot(Tau_line_3_ra,Tau_line_3_dec,'r')

    Tau_line_4_ra=np.array([Tau_ra[3],Tau_ra[1]])
    Tau_line_4_dec=np.array([Tau_dec[3],Tau_dec[1]])
    ax.plot(Tau_line_4_ra,Tau_line_4_dec,'r')

    Tau_line_5_ra=np.array([Tau_ra[6],Tau_ra[4]])
    Tau_line_5_dec=np.array([Tau_dec[6],Tau_dec[4]])
    ax.plot(Tau_line_5_ra,Tau_line_5_dec,'r')

    Tau_line_6_ra=np.array([Tau_ra[5],Tau_ra[2]])
    Tau_line_6_dec=np.array([Tau_dec[5],Tau_dec[2]])
    ax.plot(Tau_line_6_ra,Tau_line_6_dec,'r')

    #Lines for Andromeda
    And_ra=np.array([])
    And_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'And':
            if float(north_data[star][13])<=4:
                And_ra=np.append(And_ra,ra[star])
                And_dec=np.append(And_dec,dec[star])

    And_line_1_ra=np.array([And_ra[0],And_ra[1]])
    And_line_1_dec=np.array([And_dec[0],And_dec[1]])
    ax.plot(And_line_1_ra,And_line_1_dec,'r')

    And_line_2_ra=np.array([And_ra[0],And_ra[2]])
    And_line_2_dec=np.array([And_dec[0],And_dec[2]])
    ax.plot(And_line_2_ra,And_line_2_dec,'r')

    And_line_3_ra=np.array([And_ra[3],And_ra[1]])
    And_line_3_dec=np.array([And_dec[3],And_dec[1]])
    ax.plot(And_line_3_ra,And_line_3_dec,'r')

    And_line_4_ra=np.array([And_ra[2],And_ra[4]])
    And_line_4_dec=np.array([And_dec[2],And_dec[4]])
    ax.plot(And_line_4_ra,And_line_4_dec,'r')

    And_line_5_ra=np.array([And_ra[3],And_ra[5]])
    And_line_5_dec=np.array([And_dec[3],And_dec[5]])
    ax.plot(And_line_5_ra,And_line_5_dec,'r')

    And_line_6_ra=np.array([And_ra[2],And_ra[7]])
    And_line_6_dec=np.array([And_dec[2],And_dec[7]])
    ax.plot(And_line_6_ra,And_line_6_dec,'r')

    And_line_7_ra=np.array([And_ra[6],And_ra[7]])
    And_line_7_dec=np.array([And_dec[6],And_dec[7]])
    ax.plot(And_line_7_ra,And_line_7_dec,'r')

    #Lines for Cassiopeia
    Cas_ra=np.array([])
    Cas_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Cas':
            if float(north_data[star][13])<=3.4:
                Cas_ra=np.append(Cas_ra,ra[star])
                Cas_dec=np.append(Cas_dec,dec[star])

    Cas_line_1_ra=np.array([Cas_ra[0],Cas_ra[1]])
    Cas_line_1_dec=np.array([Cas_dec[0],Cas_dec[1]])
    ax.plot(Cas_line_1_ra,Cas_line_1_dec,'r')

    Cas_line_2_ra=np.array([Cas_ra[2],Cas_ra[1]])
    Cas_line_2_dec=np.array([Cas_dec[2],Cas_dec[1]])
    ax.plot(Cas_line_2_ra,Cas_line_2_dec,'r')

    Cas_line_3_ra=np.array([Cas_ra[2],Cas_ra[3]])
    Cas_line_3_dec=np.array([Cas_dec[2],Cas_dec[3]])
    ax.plot(Cas_line_3_ra,Cas_line_3_dec,'r')

    Cas_line_4_ra=np.array([Cas_ra[4],Cas_ra[3]])
    Cas_line_4_dec=np.array([Cas_dec[4],Cas_dec[3]])
    ax.plot(Cas_line_4_ra,Cas_line_4_dec,'r')

    #Lines for Perseus
    Per_ra=np.array([])
    Per_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Per':
            if float(north_data[star][13])<=4.1:
                Per_ra=np.append(Per_ra,ra[star])
                Per_dec=np.append(Per_dec,dec[star])

    Per_line_1_ra=np.array([Per_ra[0],Per_ra[1]])
    Per_line_1_dec=np.array([Per_dec[0],Per_dec[1]])
    ax.plot(Per_line_1_ra,Per_line_1_dec,'r')

    Per_line_2_ra=np.array([Per_ra[0],Per_ra[2]])
    Per_line_2_dec=np.array([Per_dec[0],Per_dec[2]])
    ax.plot(Per_line_2_ra,Per_line_2_dec,'r')

    Per_line_3_ra=np.array([Per_ra[1],Per_ra[2]])
    Per_line_3_dec=np.array([Per_dec[1],Per_dec[2]])
    ax.plot(Per_line_3_ra,Per_line_3_dec,'r')

    Per_line_4_ra=np.array([Per_ra[1],Per_ra[16]])
    Per_line_4_dec=np.array([Per_dec[1],Per_dec[16]])
    ax.plot(Per_line_4_ra,Per_line_4_dec,'r')

    Per_line_5_ra=np.array([Per_ra[2],Per_ra[6]])
    Per_line_5_dec=np.array([Per_dec[2],Per_dec[6]])
    ax.plot(Per_line_5_ra,Per_line_5_dec,'r')

    Per_line_6_ra=np.array([Per_ra[6],Per_ra[16]])
    Per_line_6_dec=np.array([Per_dec[6],Per_dec[16]])
    ax.plot(Per_line_6_ra,Per_line_6_dec,'r')

    Per_line_7_ra=np.array([Per_ra[15],Per_ra[16]])
    Per_line_7_dec=np.array([Per_dec[15],Per_dec[16]])
    ax.plot(Per_line_7_ra,Per_line_7_dec,'r')

    Per_line_8_ra=np.array([Per_ra[15],Per_ra[14]])
    Per_line_8_dec=np.array([Per_dec[15],Per_dec[14]])
    ax.plot(Per_line_8_ra,Per_line_8_dec,'r')

    Per_line_9_ra=np.array([Per_ra[7],Per_ra[6]])
    Per_line_9_dec=np.array([Per_dec[7],Per_dec[6]])
    ax.plot(Per_line_9_ra,Per_line_9_dec,'r')

    Per_line_10_ra=np.array([Per_ra[7],Per_ra[11]])
    Per_line_10_dec=np.array([Per_dec[7],Per_dec[11]])
    ax.plot(Per_line_10_ra,Per_line_10_dec,'r')

    Per_line_11_ra=np.array([Per_ra[7],Per_ra[13]])
    Per_line_11_dec=np.array([Per_dec[7],Per_dec[13]])
    ax.plot(Per_line_11_ra,Per_line_11_dec,'r')

    Per_line_12_ra=np.array([Per_ra[12],Per_ra[11]])
    Per_line_12_dec=np.array([Per_dec[12],Per_dec[11]])
    ax.plot(Per_line_12_ra,Per_line_12_dec,'r')

    Per_line_13_ra=np.array([Per_ra[12],Per_ra[10]])
    Per_line_13_dec=np.array([Per_dec[12],Per_dec[10]])
    ax.plot(Per_line_13_ra,Per_line_13_dec,'r')

    Per_line_14_ra=np.array([Per_ra[8],Per_ra[10]])
    Per_line_14_dec=np.array([Per_dec[8],Per_dec[10]])
    ax.plot(Per_line_14_ra,Per_line_14_dec,'r')

    Per_line_15_ra=np.array([Per_ra[4],Per_ra[11]])
    Per_line_15_dec=np.array([Per_dec[4],Per_dec[11]])
    ax.plot(Per_line_15_ra,Per_line_15_dec,'r')

    Per_line_16_ra=np.array([Per_ra[4],Per_ra[3]])
    Per_line_16_dec=np.array([Per_dec[4],Per_dec[3]])
    ax.plot(Per_line_16_ra,Per_line_16_dec,'r')

    Per_line_17_ra=np.array([Per_ra[4],Per_ra[5]])
    Per_line_17_dec=np.array([Per_dec[4],Per_dec[5]])
    ax.plot(Per_line_17_ra,Per_line_17_dec,'r')

    Per_line_18_ra=np.array([Per_ra[16],Per_ra[5]])
    Per_line_18_dec=np.array([Per_dec[16],Per_dec[5]])
    ax.plot(Per_line_18_ra,Per_line_18_dec,'r')

    #Lines for Cepheus
    Cep_ra=np.array([])
    Cep_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Cep':
            if float(north_data[star][13])<=3.5:
                Cep_ra=np.append(Cep_ra,ra[star])
                Cep_dec=np.append(Cep_dec,dec[star])

    Cep_line_1_ra=np.array([Cep_ra[1],Cep_ra[2]])
    Cep_line_1_dec=np.array([Cep_dec[1],Cep_dec[2]])
    ax.plot(Cep_line_1_ra,Cep_line_1_dec,'r')

    Cep_line_2_ra=np.array([Cep_ra[3],Cep_ra[1]])
    Cep_line_2_dec=np.array([Cep_dec[3],Cep_dec[1]])
    ax.plot(Cep_line_2_ra,Cep_line_2_dec,'r')

    Cep_line_3_ra=np.array([Cep_ra[3],Cep_ra[4]])
    Cep_line_3_dec=np.array([Cep_dec[3],Cep_dec[4]])
    ax.plot(Cep_line_3_ra,Cep_line_3_dec,'r')

    Cep_line_4_ra=np.array([Cep_ra[2],Cep_ra[4]])
    Cep_line_4_dec=np.array([Cep_dec[2],Cep_dec[4]])
    ax.plot(Cep_line_4_ra,Cep_line_4_dec,'r')

    Cep_line_5_ra=np.array([Cep_ra[2],Cep_ra[5]])
    Cep_line_5_dec=np.array([Cep_dec[2],Cep_dec[5]])
    ax.plot(Cep_line_5_ra,Cep_line_5_dec,'r')

    Cep_line_6_ra=np.array([Cep_ra[5],Cep_ra[4]])
    Cep_line_6_dec=np.array([Cep_dec[5],Cep_dec[4]])
    ax.plot(Cep_line_6_ra,Cep_line_6_dec,'r')

    #Lines for Bootes
    Boo_ra=np.array([])
    Boo_dec=np.array([])

    for star in range(len(north_data)):
        if north_data[star][29] == 'Boo':
            if float(north_data[star][13])<=4:
                Boo_ra=np.append(Boo_ra,ra[star])
                Boo_dec=np.append(Boo_dec,dec[star])

    Boo_line_1_ra=np.array([Boo_ra[0],Boo_ra[1]])
    Boo_line_1_dec=np.array([Boo_dec[0],Boo_dec[1]])
    ax.plot(Boo_line_1_ra,Boo_line_1_dec,'r')

    Boo_line_2_ra=np.array([Boo_ra[1],Boo_ra[2]])
    Boo_line_2_dec=np.array([Boo_dec[1],Boo_dec[2]])
    ax.plot(Boo_line_2_ra,Boo_line_2_dec,'r')

    Boo_line_3_ra=np.array([Boo_ra[2],Boo_ra[3]])
    Boo_line_3_dec=np.array([Boo_dec[2],Boo_dec[3]])
    ax.plot(Boo_line_3_ra,Boo_line_3_dec,'r')

    Boo_line_4_ra=np.array([Boo_ra[4],Boo_ra[1]])
    Boo_line_4_dec=np.array([Boo_dec[4],Boo_dec[1]])
    ax.plot(Boo_line_4_ra,Boo_line_4_dec,'r')

    Boo_line_5_ra=np.array([Boo_ra[1],Boo_ra[5]])
    Boo_line_5_dec=np.array([Boo_dec[1],Boo_dec[5]])
    ax.plot(Boo_line_5_ra,Boo_line_5_dec,'r')

    Boo_line_6_ra=np.array([Boo_ra[6],Boo_ra[3]])
    Boo_line_6_dec=np.array([Boo_dec[6],Boo_dec[3]])
    ax.plot(Boo_line_6_ra,Boo_line_6_dec,'r')

    Boo_line_7_ra=np.array([Boo_ra[6],Boo_ra[7]])
    Boo_line_7_dec=np.array([Boo_dec[6],Boo_dec[7]])
    ax.plot(Boo_line_7_ra,Boo_line_7_dec,'r')

    Boo_line_8_ra=np.array([Boo_ra[5],Boo_ra[7]])
    Boo_line_8_dec=np.array([Boo_dec[5],Boo_dec[7]])
    ax.plot(Boo_line_8_ra,Boo_line_8_dec,'r')

    #Lines for Draco
    Dra_ra=np.array([])
    Dra_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Dra':
            if float(north_data[star][13])<=4:
                Dra_ra=np.append(Dra_ra,ra[star])
                Dra_dec=np.append(Dra_dec,dec[star])

    Dra_line_1_ra=np.array([Dra_ra[0],Dra_ra[1]])
    Dra_line_1_dec=np.array([Dra_dec[0],Dra_dec[1]])
    ax.plot(Dra_line_1_ra,Dra_line_1_dec,'r')

    Dra_line_2_ra=np.array([Dra_ra[2],Dra_ra[1]])
    Dra_line_2_dec=np.array([Dra_dec[2],Dra_dec[1]])
    ax.plot(Dra_line_2_ra,Dra_line_2_dec,'r')

    Dra_line_3_ra=np.array([Dra_ra[2],Dra_ra[3]])
    Dra_line_3_dec=np.array([Dra_dec[2],Dra_dec[3]])
    ax.plot(Dra_line_3_ra,Dra_line_3_dec,'r')

    Dra_line_4_ra=np.array([Dra_ra[4],Dra_ra[3]])
    Dra_line_4_dec=np.array([Dra_dec[4],Dra_dec[3]])
    ax.plot(Dra_line_4_ra,Dra_line_4_dec,'r')

    Dra_line_5_ra=np.array([Dra_ra[4],Dra_ra[5]])
    Dra_line_5_dec=np.array([Dra_dec[4],Dra_dec[5]])
    ax.plot(Dra_line_5_ra,Dra_line_5_dec,'r')

    Dra_line_6_ra=np.array([Dra_ra[9],Dra_ra[5]])
    Dra_line_6_dec=np.array([Dra_dec[9],Dra_dec[5]])
    ax.plot(Dra_line_6_ra,Dra_line_6_dec,'r')

    Dra_line_7_ra=np.array([Dra_ra[6],Dra_ra[7]])
    Dra_line_7_dec=np.array([Dra_dec[6],Dra_dec[7]])
    ax.plot(Dra_line_7_ra,Dra_line_7_dec,'r')

    Dra_line_8_ra=np.array([Dra_ra[6],Dra_ra[8]])
    Dra_line_8_dec=np.array([Dra_dec[6],Dra_dec[8]])
    ax.plot(Dra_line_8_ra,Dra_line_8_dec,'r')

    Dra_line_9_ra=np.array([Dra_ra[8],Dra_ra[7]])
    Dra_line_9_dec=np.array([Dra_dec[8],Dra_dec[7]])
    ax.plot(Dra_line_9_ra,Dra_line_9_dec,'r')

    Dra_line_10_ra=np.array([Dra_ra[6],Dra_ra[10]])
    Dra_line_10_dec=np.array([Dra_dec[6],Dra_dec[10]])
    ax.plot(Dra_line_10_ra,Dra_line_10_dec,'r')

    Dra_line_11_ra=np.array([Dra_ra[11],Dra_ra[9]])
    Dra_line_11_dec=np.array([Dra_dec[11],Dra_dec[9]])
    ax.plot(Dra_line_11_ra,Dra_line_11_dec,'r')

    Dra_line_12_ra=np.array([Dra_ra[11],Dra_ra[10]])
    Dra_line_12_dec=np.array([Dra_dec[11],Dra_dec[10]])
    ax.plot(Dra_line_12_ra,Dra_line_12_dec,'r')

    #Lines for Aquila
    Aql_ra=np.array([])
    Aql_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Aql':
            if float(north_data[star][13])<=3.5:
                Aql_ra=np.append(Aql_ra,ra[star])
                Aql_dec=np.append(Aql_dec,dec[star])

    Aql_line_1_ra=np.array([Aql_ra[0],Aql_ra[2]])
    Aql_line_1_dec=np.array([Aql_dec[0],Aql_dec[2]])
    ax.plot(Aql_line_1_ra,Aql_line_1_dec,'r')

    Aql_line_2_ra=np.array([Aql_ra[1],Aql_ra[2]])
    Aql_line_2_dec=np.array([Aql_dec[1],Aql_dec[2]])
    ax.plot(Aql_line_2_ra,Aql_line_2_dec,'r')

    Aql_line_3_ra=np.array([Aql_ra[4],Aql_ra[0]])
    Aql_line_3_dec=np.array([Aql_dec[4],Aql_dec[0]])
    ax.plot(Aql_line_3_ra,Aql_line_3_dec,'r')

    Aql_line_4_ra=np.array([Aql_ra[4],Aql_ra[5]])
    Aql_line_4_dec=np.array([Aql_dec[4],Aql_dec[5]])
    ax.plot(Aql_line_4_ra,Aql_line_4_dec,'r')

    Aql_line_5_ra=np.array([Aql_ra[2],Aql_ra[5]])
    Aql_line_5_dec=np.array([Aql_dec[2],Aql_dec[5]])
    ax.plot(Aql_line_5_ra,Aql_line_5_dec,'r')

    #Lines for Canis Major
    CMa_ra=np.array([])
    CMa_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'CMa':
            if float(north_data[star][13])<=4:
                CMa_ra=np.append(CMa_ra,ra[star])
                CMa_dec=np.append(CMa_dec,dec[star])



    ax.plot(CMa_ra,CMa_dec,'wo',markersize=1)

    
    #Plotting all stars
    #for i in range(len(ra)):
     #   ax.plot(ra[i],dec[i],'wo',markersize=mag[i])
        
    if limited_view is 'true':
        ax.set_rmax(85)
    else:
        ax.set_rmax(120)

    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
        
    #plt.savefig('north_hemi.eps', format='eps', dpi=1000)
    
    plt.show()

    return len(north_data)
