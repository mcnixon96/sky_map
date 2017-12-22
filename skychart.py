import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

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

    return bright_star_data

def north_plot():
    """Plots all stars visible in northern hemisphere with constellations."""
    
    stars=sky_data()
    north_data=[]

    for star in range(len(stars)):#only using northern hemisphere stars
        if float(stars[star][8])>=-30:
            if float(stars[star][8])<=90:
                north_data.append(stars[star])


    #create arrays of ra and dec in polar coords as well as magnitude
    ra=np.zeros(len(north_data))
    dec=np.zeros(len(north_data))
    mag=np.zeros(len(north_data))
    full_con_list=[]
    
    for star in range(len(north_data)):
        ra[star]=float(north_data[star][7])*(np.pi/12.0)#ra in radians
        dec[star]=90-float(north_data[star][8])#dec all positive
        mag[star]=4-float(north_data[star][13])#mag all positive and on increasing scale
        full_con_list.append(north_data[star][29])#column 29 is constellation name

    unique_con_list=list(set(full_con_list))
    #print this to see all the abbreviated constellation names
    print unique_con_list

    #Lines for Cygnus
    Cygnus_ra=np.array([])
    Cygnus_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Cyg':
            if float(north_data[star][13])<=3.5:
                Cygnus_ra=np.append(Cygnus_ra,ra[star])
                Cygnus_dec=np.append(Cygnus_dec,dec[star])

    Cyg_line_1_ra=np.array([Cygnus_ra[0],Cygnus_ra[2]])
    Cyg_line_1_dec=np.array([Cygnus_dec[0],Cygnus_dec[2]])

    Cyg_line_2_ra=np.array([Cygnus_ra[3],Cygnus_ra[2]])
    Cyg_line_2_dec=np.array([Cygnus_dec[3],Cygnus_dec[2]])

    Cyg_line_3_ra=np.array([Cygnus_ra[4],Cygnus_ra[2]])
    Cyg_line_3_dec=np.array([Cygnus_dec[4],Cygnus_dec[2]])

    Cyg_line_4_ra=np.array([Cygnus_ra[1],Cygnus_ra[2]])
    Cyg_line_4_dec=np.array([Cygnus_dec[1],Cygnus_dec[2]])

    Cyg_line_5_ra=np.array([Cygnus_ra[4],Cygnus_ra[5]])
    Cyg_line_5_dec=np.array([Cygnus_dec[4],Cygnus_dec[5]])

    #Lines for Orion
    Orion_ra=np.array([])
    Orion_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'Ori':
            if float(north_data[star][13])<=3.4:
                Orion_ra=np.append(Orion_ra,ra[star])
                Orion_dec=np.append(Orion_dec,dec[star])
    
    Ori_line_1_ra=np.array([Orion_ra[0],Orion_ra[3]])
    Ori_line_1_dec=np.array([Orion_dec[0],Orion_dec[3]])

    Ori_line_2_ra=np.array([Orion_ra[4],Orion_ra[3]])
    Ori_line_2_dec=np.array([Orion_dec[4],Orion_dec[3]])

    Ori_line_3_ra=np.array([Orion_ra[5],Orion_ra[3]])
    Ori_line_3_dec=np.array([Orion_dec[5],Orion_dec[3]])

    Ori_line_4_ra=np.array([Orion_ra[10],Orion_ra[3]])
    Ori_line_4_dec=np.array([Orion_dec[10],Orion_dec[3]])

    Ori_line_5_ra=np.array([Orion_ra[10],Orion_ra[5]])
    Ori_line_5_dec=np.array([Orion_dec[10],Orion_dec[5]])

    Ori_line_6_ra=np.array([Orion_ra[4],Orion_ra[1]])
    Ori_line_6_dec=np.array([Orion_dec[4],Orion_dec[1]])

    Ori_line_7_ra=np.array([Orion_ra[10],Orion_ra[8]])
    Ori_line_7_dec=np.array([Orion_dec[10],Orion_dec[8]])

    Ori_line_8_ra=np.array([Orion_ra[7],Orion_ra[8]])
    Ori_line_8_dec=np.array([Orion_dec[7],Orion_dec[8]])

    Ori_line_9_ra=np.array([Orion_ra[7],Orion_ra[4]])
    Ori_line_9_dec=np.array([Orion_dec[7],Orion_dec[4]])

    Ori_line_10_ra=np.array([Orion_ra[8],Orion_ra[9]])
    Ori_line_10_dec=np.array([Orion_dec[8],Orion_dec[9]])

    #Lines for Ursa Major
    UMa_ra=np.array([])
    UMa_dec=np.array([])
    
    for star in range(len(north_data)):
        if north_data[star][29] == 'UMa':
            if float(north_data[star][13])<=3.8:
                UMa_ra=np.append(UMa_ra,ra[star])
                UMa_dec=np.append(UMa_dec,dec[star])

    UMa_line_1_ra=np.array([UMa_ra[8],UMa_ra[9]])
    UMa_line_1_dec=np.array([UMa_dec[8],UMa_dec[9]])
    
    UMa_line_2_ra=np.array([UMa_ra[8],UMa_ra[13]])
    UMa_line_2_dec=np.array([UMa_dec[8],UMa_dec[13]])
    
    UMa_line_3_ra=np.array([UMa_ra[14],UMa_ra[13]])
    UMa_line_3_dec=np.array([UMa_dec[14],UMa_dec[13]])
    
    UMa_line_4_ra=np.array([UMa_ra[9],UMa_ra[14]])
    UMa_line_4_dec=np.array([UMa_dec[9],UMa_dec[14]])
    
    UMa_line_5_ra=np.array([UMa_ra[15],UMa_ra[14]])
    UMa_line_5_dec=np.array([UMa_dec[15],UMa_dec[14]])
    
    UMa_line_6_ra=np.array([UMa_ra[15],UMa_ra[16]])
    UMa_line_6_dec=np.array([UMa_dec[15],UMa_dec[16]])

    UMa_line_7_ra=np.array([UMa_ra[17],UMa_ra[16]])
    UMa_line_7_dec=np.array([UMa_dec[17],UMa_dec[16]])

    UMa_line_8_ra=np.array([UMa_ra[0],UMa_ra[3]])
    UMa_line_8_dec=np.array([UMa_dec[0],UMa_dec[3]])

    UMa_line_9_ra=np.array([UMa_ra[3],UMa_ra[9]])
    UMa_line_9_dec=np.array([UMa_dec[3],UMa_dec[9]])

    UMa_line_10_ra=np.array([UMa_ra[0],UMa_ra[5]])
    UMa_line_10_dec=np.array([UMa_dec[0],UMa_dec[5]])

    UMa_line_11_ra=np.array([UMa_ra[4],UMa_ra[5]])
    UMa_line_11_dec=np.array([UMa_dec[4],UMa_dec[5]])

    UMa_line_12_ra=np.array([UMa_ra[4],UMa_ra[1]])
    UMa_line_12_dec=np.array([UMa_dec[4],UMa_dec[1]])

    UMa_line_13_ra=np.array([UMa_ra[4],UMa_ra[2]])
    UMa_line_13_dec=np.array([UMa_dec[4],UMa_dec[2]])

    UMa_line_14_ra=np.array([UMa_ra[4],UMa_ra[10]])
    UMa_line_14_dec=np.array([UMa_dec[4],UMa_dec[10]])

    UMa_line_15_ra=np.array([UMa_ra[6],UMa_ra[10]])
    UMa_line_15_dec=np.array([UMa_dec[6],UMa_dec[10]])

    UMa_line_16_ra=np.array([UMa_ra[7],UMa_ra[10]])
    UMa_line_16_dec=np.array([UMa_dec[7],UMa_dec[10]])

    UMa_line_17_ra=np.array([UMa_ra[12],UMa_ra[10]])
    UMa_line_17_dec=np.array([UMa_dec[12],UMa_dec[10]])

    UMa_line_18_ra=np.array([UMa_ra[12],UMa_ra[13]])
    UMa_line_18_dec=np.array([UMa_dec[12],UMa_dec[13]])
    
    plt.style.use('dark_background')
    ax = plt.subplot(111, projection='polar')

    #Plotting Cygnus
    ax.plot(Cyg_line_1_ra,Cyg_line_1_dec,'r')
    ax.plot(Cyg_line_2_ra,Cyg_line_2_dec,'r')
    ax.plot(Cyg_line_3_ra,Cyg_line_3_dec,'r')
    ax.plot(Cyg_line_4_ra,Cyg_line_4_dec,'r')
    ax.plot(Cyg_line_5_ra,Cyg_line_5_dec,'r')

    #Plotting Orion
    ax.plot(Ori_line_1_ra,Ori_line_1_dec,'r')
    ax.plot(Ori_line_2_ra,Ori_line_2_dec,'r')
    ax.plot(Ori_line_3_ra,Ori_line_3_dec,'r')
    ax.plot(Ori_line_4_ra,Ori_line_4_dec,'r')
    ax.plot(Ori_line_5_ra,Ori_line_5_dec,'r')
    ax.plot(Ori_line_6_ra,Ori_line_6_dec,'r')
    ax.plot(Ori_line_7_ra,Ori_line_7_dec,'r')
    ax.plot(Ori_line_8_ra,Ori_line_8_dec,'r')
    ax.plot(Ori_line_9_ra,Ori_line_9_dec,'r')
    ax.plot(Ori_line_10_ra,Ori_line_10_dec,'r')

    #Plotting Ursa Major
    ax.plot(UMa_line_1_ra,UMa_line_1_dec,'r')
    ax.plot(UMa_line_2_ra,UMa_line_2_dec,'r')
    ax.plot(UMa_line_3_ra,UMa_line_3_dec,'r')
    ax.plot(UMa_line_4_ra,UMa_line_4_dec,'r')
    ax.plot(UMa_line_5_ra,UMa_line_5_dec,'r')
    ax.plot(UMa_line_6_ra,UMa_line_6_dec,'r')
    ax.plot(UMa_line_7_ra,UMa_line_7_dec,'r')
    ax.plot(UMa_line_8_ra,UMa_line_8_dec,'r')
    ax.plot(UMa_line_9_ra,UMa_line_9_dec,'r')
    ax.plot(UMa_line_10_ra,UMa_line_10_dec,'r')
    ax.plot(UMa_line_11_ra,UMa_line_11_dec,'r')
    ax.plot(UMa_line_12_ra,UMa_line_12_dec,'r')
    ax.plot(UMa_line_13_ra,UMa_line_13_dec,'r')
    ax.plot(UMa_line_14_ra,UMa_line_14_dec,'r')
    ax.plot(UMa_line_15_ra,UMa_line_15_dec,'r')
    ax.plot(UMa_line_16_ra,UMa_line_16_dec,'r')
    ax.plot(UMa_line_17_ra,UMa_line_17_dec,'r')
    ax.plot(UMa_line_18_ra,UMa_line_18_dec,'r')

    
    #Plotting all stars
    for i in range(len(ra)):
        ax.plot(ra[i],dec[i],'wo',markersize=mag[i])

    ax.set_rmax(120)
    plt.show()

    return len(north_data)
