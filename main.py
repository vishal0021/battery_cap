import csv
import numpy as np
import matplotlib.pyplot as plt
import julian
import datetime

# Input filename in .csv format
# Plot the logfile of the satellite (battery, MRP, angular rate, etc.) as functions of Julian Date
path = "SSD21_Sun-Pointing_Log_Results_2_Orbits_Start_IDLE.csv"
#path = "Old_SSD21_Sun-Pointing_Log_Results_2_Orbits_Start_IDLE.csv"

'''
mjd = 2459563.632858
dt = julian.from_jd(mjd, fmt='mjd')
print(dt)
'''


def Logs_Plotter( filename ):

    rt = open( filename , "r" )
    if rt.readable():
        data = csv.reader( rt )
        lst = []
        for line in data:
            #print("Rows:\n",line)
            lst.append( line )
            #print("List:\n",lst)
        ndata = len( lst ) - 1

        jd = np.zeros( ndata )
        pos = np.zeros( ( 3 , ndata ) )
        b_sat = np.zeros( ( 3 , ndata ) )
        mrp = np.zeros( ( 3 , ndata ) )
        om = np.zeros( ( 3 , ndata ) )
        opmode = np.zeros( ndata )
        batt_cap = np.zeros( ndata )
        n_sun = np.zeros( ( 3 , ndata ) )
        
        for i in range( 0 , ndata ):

            jd[ i ] = float( lst[ i + 1 ][ 0 ] )

            pos[ 0 ][ i ] = float( lst[ i + 1 ][ 1 ] )
            pos[ 1 ][ i ] = float( lst[ i + 1 ][ 2 ] )
            pos[ 2 ][ i ] = float( lst[ i + 1 ][ 3 ] )

            b_sat[ 0 ][ i ] = float( lst[ i + 1 ][ 4 ] )
            b_sat[ 1 ][ i ] = float( lst[ i + 1 ][ 5 ] )
            b_sat[ 2 ][ i ] = float( lst[ i + 1 ][ 6 ] )

            mrp[ 0 ][ i ] = float( lst[ i + 1 ][ 7 ] )
            mrp[ 1 ][ i ] = float( lst[ i + 1 ][ 8 ] )
            mrp[ 2 ][ i ] = float( lst[ i + 1 ][ 9 ] )

            om[ 0 ][ i ] = float( lst[ i + 1 ][ 10 ] )
            om[ 1 ][ i ] = float( lst[ i + 1 ][ 11 ] )
            om[ 2 ][ i ] = float( lst[ i + 1 ][ 12 ] )

            batt_cap[ i ] = float( lst[ i + 1 ][ 17 ] )

            n_sun[ 0 ][ i ] = float( lst[ i + 1 ][ 13 ] )
            n_sun[ 1 ][ i ] = float( lst[ i + 1 ][ 14 ] )
            n_sun[ 2 ][ i ] = float( lst[ i + 1 ][ 15 ] )
            
            if str( lst[ i + 1 ][ 16 ] ) == " Hell":
                opmode[ i ] = 0
            elif str( lst[ i + 1 ][ 16 ] ) == " Phoenix":
                opmode[ i ] = 1
            elif str( lst[ i + 1 ][ 16 ] ) == " Safe":
                opmode[ i ] = 2
            elif str( lst[ i ][ 16 ] ) == " IDLE":
                opmode[ i ] = 3
            elif str( lst[ i + 1 ][ 16 ] ) == " Detumbling":
                opmode[ i ] = 4
            elif str( lst[ i + 1 ][ 16 ] ) == " Downlink":
                opmode[ i ] = 5
            elif str( lst[ i + 1 ][ 16 ] ) == " Payload":
                opmode[ i ] = 6
            else:
                opmode[ i ] = -1

    else:
        print( "Unreadable data, there's something wrong with the output file " + filename )

    fig = plt.figure()

    ax1 = plt.subplot( 611 )
        
    # Plot all the lines
    ax1.plot(jd, pos[ 0 ] , color = "green" , linestyle = "solid" )
    ax1.plot( jd , pos[ 1 ] , color = "red" , linestyle = "solid" )
    ax1.plot( jd , pos[ 2 ] , color = "blue" , linestyle = "solid" )

    fig.subplots_adjust( wspace = 0 )
    
    ax2 = plt.subplot( 612 )
    
    # Plot all the lines
    ax2.plot(jd, mrp[ 0 ] , color = "green" , linestyle = "solid" )
    ax2.plot( jd , mrp[ 1 ] , color = "red" , linestyle = "solid" )
    ax2.plot( jd , mrp[ 2 ] , color = "blue" , linestyle = "solid" )

    ax3 = plt.subplot( 613 , sharex = ax1 )

    # Plot all the lines
    ax3.plot( jd , om[ 0 ] , color = "green" , linestyle = "solid" )
    ax3.plot( jd , om[ 1 ] , color = "red" , linestyle = "solid" )
    ax3.plot( jd , om[ 2 ] , color = "blue" , linestyle = "solid" )

    ax4 = plt.subplot( 614 , sharex = ax1 )

    # Plot all the lines
    ax4.plot( jd , batt_cap , color = "green" , linestyle = "solid" )

    ax5 = plt.subplot( 615 , sharex = ax1 )

    # Plot all the lines
    ax5.plot( jd , opmode , color = "green" , linestyle = "solid" )

    ax6 = plt.subplot( 616 , sharex = ax1 )

    # Plot all the lines
    ax6.plot( jd , n_sun[ 0 ] , color = "green" , linestyle = "solid" )
    ax6.plot( jd , n_sun[ 1 ] , color = "red" , linestyle = "solid" )
    ax6.plot( jd , n_sun[ 2 ] , color = "blue" , linestyle = "solid" )

    # Set Labels where needed
    ax1.set_ylabel( r"ECI XYZ Components [km]" )
    ax1.set_xlabel( r"Julian Date [days]" )
    ax2.set_ylabel( r"MRP components [-]" )
    ax3.set_ylabel( r"Angular Rate [rad/s]" )
    ax4.set_ylabel( r"Battery Capacity [Wh]" )
    ax5.set_ylabel( r"Operational Mode" )
    ax6.set_ylabel( r"Sun Normal Components [-]" )

    # Save the figure if you want
    plt.savefig( "Res_Logs.eps", format="eps" )

    plt.show()

Logs_Plotter(path)
