## Copyright (C) GNSS ACADEMY 
##
## Name          : SatFunctions.py
## Purpose       : Satellite Analyses functions
## Project       : WP0-JSNP
## Component     : 
## Author        : GNSS Academy
## Creation date : 2021
## File Version  : 1.0
## Version date  : 
##

import sys, os
from pandas import unique
from interfaces import LOS_IDX
sys.path.append(os.getcwd() + '/' + \
    os.path.dirname(sys.argv[0]) + '/' + 'COMMON')
from COMMON import GnssConstants
from COMMON.Plots import generatePlot
import numpy as np
# from pyproj import Transformer
from COMMON.Coordinates import xyz2llh


# Plot Satellite Visibility Figures
def plotSatVisibility(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,6.6)
    PlotConf["Title"] = "Satellite Visibility from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "GPS-PRN"
    PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yLim"] = [0, max(unique(LosData[LOS_IDX["PRN"]])) + 1]

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'
    PlotConf["LineWidth"] = 15

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    for prn in sorted(unique(LosData[LOS_IDX["PRN"]])):
        Label = "G" + ("%02d" % prn)
        FilterCond = LosData[LOS_IDX["PRN"]] == prn
        PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]][FilterCond] / GnssConstants.S_IN_H
        PlotConf["yData"][Label] = LosData[LOS_IDX["PRN"]][FilterCond]
        PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]][FilterCond]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_VISIBILITY_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)


# Plot Satellite Geometrical Range Figures
def plotSatGeomRnge(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Satellite Geometical Range from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "Range [km]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["RANGE[m]"]]/1000
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_GEOMETRICAL_RANGE_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)


# Plot Satellite Tracks Figures
def plotSatTracks(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (16.8,15.2)
    PlotConf["Title"] = "Satellite Tracks during visibility periods from "\
        "TLSA on Year 2015 DoY 006"

    PlotConf["LonMin"] = -135
    PlotConf["LonMax"] = 135
    PlotConf["LatMin"] = -35
    PlotConf["LatMax"] = 90
    PlotConf["LonStep"] = 15
    PlotConf["LatStep"] = 10

    # PlotConf["yLabel"] = "Latitude [deg]"
    PlotConf["yTicks"] = range(PlotConf["LatMin"],PlotConf["LatMax"]+1,10)
    PlotConf["yLim"] = [PlotConf["LatMin"], PlotConf["LatMax"]]

    # PlotConf["xLabel"] = "Longitude [deg]"
    PlotConf["xTicks"] = range(PlotConf["LonMin"],PlotConf["LonMax"]+1,15)
    PlotConf["xLim"] = [PlotConf["LonMin"], PlotConf["LonMax"]]

    PlotConf["Grid"] = True

    PlotConf["Map"] = True

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    # Transform ECEF to Geodetic
    LosData[LOS_IDX["SAT-X[m]"]].to_numpy()
    LosData[LOS_IDX["SAT-Y[m]"]].to_numpy()
    LosData[LOS_IDX["SAT-Z[m]"]].to_numpy()
    DataLen = len(LosData[LOS_IDX["SAT-X[m]"]])
    Longitude = np.zeros(DataLen)
    Latitude = np.zeros(DataLen)
    # transformer = Transformer.from_crs('epsg:4978', 'epsg:4326')
    for index in range(DataLen):
        x = LosData[LOS_IDX["SAT-X[m]"]][index]
        y = LosData[LOS_IDX["SAT-Y[m]"]][index]
        z = LosData[LOS_IDX["SAT-Z[m]"]][index]
        Longitude[index], Latitude[index], h = xyz2llh(x, y, z)
        # Latitude[index], Longitude[index], h = transformer.transform(x, y, z)

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = Longitude
    PlotConf["yData"][Label] = Latitude
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_TRACKS_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Satellite Velocity figures
def plotSatVelocity(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Satellite Absolute Velocity from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "Velocity [km/s]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    velX = np.array(LosData[LOS_IDX["VEL-X[m/s]"]])
    velY = np.array(LosData[LOS_IDX["VEL-Y[m/s]"]])
    velZ = np.array(LosData[LOS_IDX["VEL-Z[m/s]"]])

    absVelocity_kms = np.sqrt(velX**2+velY**2+velZ**2) / GnssConstants.M_IN_KM

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = absVelocity_kms
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_VELOCITY_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Satellite Clock from NAV message figures
def plotSatClkFromNav(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)

    PlotConf["yLabel"] = "Satellite Clock [Km]"

    PlotConf["xLabel"] = "Hour of DoY 006"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["Color"] = {}
    Label = 0
    PlotConf["Color"][Label] = "purple"

    for prn in sorted(unique(LosData[LOS_IDX["PRN"]])):
        FilterCond = LosData[LOS_IDX["PRN"]] == prn

        PlotConf["Title"] = "PRN" + str(prn) + " NAV CLK from TLSA on Year 2015"\
        " DoY 006"
        
        CLK_values = LosData[LOS_IDX["SV-CLK[m]"]][FilterCond]
        time_cond = LosData[LOS_IDX["SOD"]][FilterCond]

        PlotConf["xData"][Label] = time_cond / GnssConstants.S_IN_H
        PlotConf["yData"][Label] = CLK_values / GnssConstants.M_IN_KM

        PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/NAVCLK/' + 'SAT_CLK_PRN' + str(prn) + '_TLSA_D006Y15.png'

        # Call generatePlot from Plots library
        generatePlot(PlotConf)

# Plot Satellite Clock Corrected figures
def plotSatCorrectedClk(LosData):
    PlotConf = {}
    
    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)

    PlotConf["Title"] = "Satellite CLK + DTR - TGD from TLSA on Year 2015"\
    " DoY 006"
    
    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["yLabel"] = "CLK [Km]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "GPS-PRN"
    PlotConf["ColorBarTicks"] = range(1,33)

    NavClk = np.array(LosData[LOS_IDX["SV-CLK[m]"]])
    DTR = np.array(LosData[LOS_IDX["DTR[m]"]])
    TGD = np.array(LosData[LOS_IDX["TGD[m]"]])

    CorrectedClk = NavClk - TGD + DTR

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = CorrectedClk / GnssConstants.M_IN_KM
    PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_CORRECTED_CLK_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Satellite TGD figures
def plotSatTGD(LosData):
    PlotConf = {}
    
    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)

    PlotConf["Title"] = "Satellite Total Group Delay from TLSA on Year 2015"\
    " DoY 006"
    
    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["yLabel"] = "TGD [m]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "GPS-PRN"
    PlotConf["ColorBarTicks"] = range(1,33)

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = np.array(LosData[LOS_IDX["TGD[m]"]])
    PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_TGD_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Satellite DTR figures
def plotSatDTR(LosData):
    PlotConf = {}
    
    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)

    PlotConf["Title"] = "Satellite Relativistic Clock Correction (DTR) from TLSA on Year 2015"\
    " DoY 006"
    
    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["yLabel"] = "DTR [m]"

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [Deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = np.array(LosData[LOS_IDX["DTR[m]"]])
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/SAT/' + 'SAT_DTR_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)