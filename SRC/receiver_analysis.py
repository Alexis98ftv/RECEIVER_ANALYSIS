#!/usr/bin/env python

## Copyright (C) GNSS ACADEMY 
##
## Name          : receiver_analysis.py
## Purpose       : WP0 Takss: Plot Receiver SPP Analyses
## Project       : WP0-JSNP
## Component     : 
## Author        : GNSS Academy
## Creation date : 2021
## File Version  : 1.0
##

import sys, os

# Add path to find all modules
Common = os.path.dirname(os.path.dirname(
    os.path.abspath(sys.argv[0]))) + '/COMMON'
sys.path.insert(0, Common)

from collections import OrderedDict
from interfaces import LOS_IDX, POS_IDX
from pandas import read_csv
from yaml import dump
import SatFunctions, AtmFunctions, MsrFunctions, PosFunctions

#######################################################
# INTERNAL FUNCTIONS 
#######################################################

def displayUsage():
    sys.stderr.write("ERROR: Please provide path to SCENARIO as a unique \nargument\n")

def readConf(CfgFile):
    Conf = OrderedDict({})
    with open(CfgFile, 'r') as f:
        # Read file
        Lines = f.readlines()

        # Read each configuration parameter which is compound of a key and a value
        for Line in Lines:
            if "#" in Line or Line.isspace(): continue
            LineSplit = Line.split('=')
            try:
                LineSplit = list(filter(None, LineSplit))
                Conf[LineSplit[0].strip()] = LineSplit[1].strip()

            except:
                sys.stderr.write("ERROR: Bad line in conf: %s\n" % Line)

    return Conf

#######################################################
# MAIN PROCESSING
#######################################################

print( '-----------------------------')
print( 'RUNNING RECEIVER ANALYSES ...')
print( '-----------------------------')

if len(sys.argv) != 2:
    displayUsage()
    sys.exit()

# Take the arguments
Scen = sys.argv[1]

# Path to conf
CfgFile = Scen + '/CFG/receiver_analysis.cfg'

# Read conf file
Conf = readConf(CfgFile)

# Print 
print('Reading Configuration file',CfgFile)

#print(dump(Conf))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>> LOS FILE ANALYSES
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get LOS file full path
LosFile = Scen + '/OUT/LOS/' + Conf["LOS_FILE"]

#-----------------------------------------------------------------------
# PLOT SATELLITE ANALYSES
#-----------------------------------------------------------------------

# Plot Satellite Visibility figures
if(Conf["PLOT_SATVIS"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["PRN"],LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Visibility Periods ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatVisibility(LosData)

# Plot Satellite Geometrical Ranges figures
if(Conf["PLOT_SATRNG"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["RANGE[m]"],LOS_IDX["ELEV"]])

    print( 'Plot Satellite Geometrical Ranges ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatGeomRnge(LosData)

# Plot Satellite Tracks figures
if(Conf["PLOT_SATTRK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["SAT-X[m]"],
    LOS_IDX["SAT-Y[m]"],
    LOS_IDX["SAT-Z[m]"],
    LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Tracks ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatTracks(LosData)

# Plot Satellite Velocity figures
if(Conf["PLOT_SATVEL"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["VEL-X[m/s]"],
    LOS_IDX["VEL-Y[m/s]"],
    LOS_IDX["VEL-Z[m/s]"],
    LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Velocity ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatVelocity(LosData)

# Plot Satellite Clock from NAV message figures
if(Conf["PLOT_NAVCLK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["SV-CLK[m]"],
    LOS_IDX["PRN"]])
    
    print( 'Plot Satellite Clock from NAV message ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatClkFromNav(LosData)

# Plot Satellite Clock Corrected figures
if(Conf["PLOT_CORCLK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["PRN"],
    LOS_IDX["SV-CLK[m]"],
    LOS_IDX["DTR[m]"],
    LOS_IDX["TGD[m]"]])
    
    print( 'Plot Satellite Clock Corrected ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatCorrectedClk(LosData)

# Plot Satellite TGD figures
if(Conf["PLOT_SATTGD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["PRN"],
    LOS_IDX["TGD[m]"]])
    
    print( 'Plot Satellite Total Group Delay ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatTGD(LosData)

# Plot Satellite DTR figures
if(Conf["PLOT_SATDTR"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["DTR[m]"]])
    
    print( 'Plot Satellite Relativistic Effect Correction ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatDTR(LosData)

#-----------------------------------------------------------------------
# PLOT ATMOSPHERIC ANALYSES
#-----------------------------------------------------------------------

# Plot STEC vs TIME figures
if(Conf["PLOT_STEC"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["STEC[m]"]])
    
    print( 'Plot Klobuchar Ionospheric Delay ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotSTEC(LosData)

# Plot STEC vs PRN figures
if(Conf["PLOT_STEC_PRN"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["PRN"],
    LOS_IDX["STEC[m]"]])
    
    print( 'Plot STEC during Visibility ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotSTECvsPRN(LosData)

# Plot VTEC figures
if(Conf["PLOT_VTEC"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["STEC[m]"]])
    
    print( 'Plot Klobuchar VTEC with Mapping Function ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotVTEC(LosData)

# Plot VTEC figures
if(Conf["PLOT_VTEC_PRN"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["PRN"],
    LOS_IDX["VTEC[m]"]])
    
    print( 'Plot VTEC during Visibility ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotVTECvsPRN(LosData)

# Plot STD figures
if(Conf["PLOT_STD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["TROPO[m]"]])
    
    print( 'Plot Slant Tropo Delay ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotSTD(LosData)

# Plot ZTD figures
if(Conf["PLOT_ZTD"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["TROPO[m]"]])
    
    print( 'Plot Zenith Tropo Delay ...')

    # Configure plot and call plot generation function
    AtmFunctions.plotZTD(LosData)

#-----------------------------------------------------------------------
# PLOT MEASUREMENT ANALYSES
#-----------------------------------------------------------------------

# Plot Code Measurement figures
if(Conf["PLOT_MEAS"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["MEAS[m]"]])
    
    print( 'Plot Code Measurement ...')

    # Configure plot and call plot generation function
    MsrFunctions.PlotCodeMeas(LosData)

# Plot tau figures
if(Conf["PLOT_TAU"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["MEAS[m]"]])
    
    print( 'Plot tau = Rho/c measurement ...')

    # Configure plot and call plot generation function
    MsrFunctions.PlotTauMeas(LosData)

# Plot TOF figures
if(Conf["PLOT_TOF"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["TOF[ms]"]])
    
    print( 'Plot Time of Flight measurement ...')

    # Configure plot and call plot generation function
    MsrFunctions.PlotTofMeas(LosData)

# Plot Residuals figures
if(Conf["PLOT_RES"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["PRN"],
    LOS_IDX["MEAS[m]"],
    LOS_IDX["RANGE[m]"],
    LOS_IDX["SV-CLK[m]"],
    LOS_IDX["DTR[m]"],
    LOS_IDX["TGD[m]"],
    LOS_IDX["TROPO[m]"],
    LOS_IDX["STEC[m]"]
    ])
    
    print( 'Plot Residuals measurement ...')

    # Configure plot and call plot generation function
    MsrFunctions.PlotResidualsMeas(LosData)

# Plot Doppler figures
if(Conf["PLOT_DOPPLER"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["ELEV"],
    LOS_IDX["SAT-X[m]"],
    LOS_IDX["SAT-Y[m]"],
    LOS_IDX["SAT-Z[m]"],
    LOS_IDX["VEL-X[m/s]"],
    LOS_IDX["VEL-Y[m/s]"],
    LOS_IDX["VEL-Z[m/s]"]
    ])
    
    print( 'Plot Doppler measurement ...')

    # Configure plot and call plot generation function
    MsrFunctions.PlotDopplerMeas(LosData)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>> LOS FILE ANALYSES
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get LOS file full path
PosFile = Scen + '/OUT/POS/' + Conf["POS_FILE"]

#-----------------------------------------------------------------------
# PLOT POSITION ANALYSES
#-----------------------------------------------------------------------

# Plot NSAT figures
if(Conf["PLOT_NSAT"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["NSATS"]
    ])
    
    print( 'Plot the number of satellites used in PVT ...')

    # Configure plot and call plot generation function
    PosFunctions.PlotNsatPos(PosData)

# Plot DOP figures
if(Conf["PLOT_DOP"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["GDOP"],
    POS_IDX["PDOP"],
    POS_IDX["TDOP"]
    ])
    
    print( 'Plot the GDOP, PDOP, TDOP ...')

    # Configure plot and call plot generation function
    PosFunctions.PlotDOP(PosData)

# Plot DOP figures
if(Conf["PLOT_DOPvsNSAT"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["NSATS"],
    POS_IDX["VDOP"],
    POS_IDX["HDOP"]
    ])
    
    print( 'Plot the DOP vs NSAT ...')

    # Configure plot and call plot generation function
    PosFunctions.PlotDOPvsNSAT(PosData)

# Plot ENU PE figures
if(Conf["PLOT_ENU_PE"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["UPE[m]"]
    ])
    
    print( 'Plot the PE in ENU ...')

    # Configure plot and call plot generation function
    PosFunctions.PlotENU_PE(PosData)

# Plot ENU PE figures
if(Conf["PLOT_XPE"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["UPE[m]"]
    ])
    
    print( 'Plot the VPE and HPE ...')

    # Configure plot and call plot generation function
    PosFunctions.PlotXPE(PosData)

# Plot ENU PE figures
if(Conf["PLOT_HPEvsHDOP"] == '1'):
    # Read the cols we need from LOS file
    PosData = read_csv(PosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[POS_IDX["SOD"],
    POS_IDX["EPE[m]"],
    POS_IDX["NPE[m]"],
    POS_IDX["HDOP"]
    ])
    
    print( 'Plot HPE vs HDOP ...')

    # Configure plot and call plot generation function
    PosFunctions.plotPosNPEEPE(PosData)