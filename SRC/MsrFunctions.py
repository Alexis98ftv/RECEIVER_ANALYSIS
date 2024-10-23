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


# Plot STEC vs TIME figures
def PlotCodeMeas(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Pseudo range C1C/A vs Time from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "Pseudo-range [Km]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'
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
    PlotConf["yData"][Label] = LosData[LOS_IDX["MEAS[m]"]] / GnssConstants.M_IN_KM
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_CODE_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot tau figures
def PlotTauMeas(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "tau=Rho/c from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "tau [ms]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0

    rho_m = np.array(LosData[LOS_IDX["MEAS[m]"]])
    tau = rho_m/GnssConstants.LIGHT_SPEED_M_S

    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = tau*GnssConstants.MS_IN_S
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_TAU_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot TOF figures
def PlotTofMeas(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Time of Flight from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "ToF [ms]"

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
    PlotConf["yData"][Label] = LosData[LOS_IDX["TOF[ms]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_TOF_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Residuals figures
def PlotResidualsMeas(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Residuals C1C/A from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "Residuals [Km]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(1, 25)
    PlotConf["xLim"] = [0, 24]

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

    MEAS = np.array(LosData[LOS_IDX["MEAS[m]"]])
    RANGE = np.array(LosData[LOS_IDX["RANGE[m]"]])
    IONO = np.array(LosData[LOS_IDX["STEC[m]"]])
    TROPO = np.array(LosData[LOS_IDX["TROPO[m]"]])

    SV_CLK = np.array(LosData[LOS_IDX["SV-CLK[m]"]])
    DTR = np.array(LosData[LOS_IDX["DTR[m]"]])
    TGD = np.array(LosData[LOS_IDX["TGD[m]"]])
    CLK_P1 = SV_CLK - TGD + DTR

    RESIDUALS = MEAS - (RANGE - CLK_P1 + IONO + TROPO)


    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = RESIDUALS / GnssConstants.M_IN_KM
    PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_RESIDUALS_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

# Plot Doppler figures
def PlotDopplerMeas(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,7.6)
    PlotConf["Title"] = "Doppler effect from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "Doppler [KHz]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(1, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 1.5

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "GPS-PRN"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    
    # rLOS
    rx = LosData[LOS_IDX["SAT-X[m]"]] - GnssConstants.WGS84_REF_X
    ry = LosData[LOS_IDX["SAT-Y[m]"]] - GnssConstants.WGS84_REF_Y
    rz = LosData[LOS_IDX["SAT-Z[m]"]] - GnssConstants.WGS84_REF_Z
    rLOS = np.array([rx, ry, rz])
    
    # SAT velocity
    vSATX = LosData[LOS_IDX["VEL-X[m/s]"]]
    vSATY = LosData[LOS_IDX["VEL-Y[m/s]"]]
    vSATZ = LosData[LOS_IDX["VEL-Z[m/s]"]]
    vSAT = np.array([vSATX, vSATY, vSATZ])

    # Calc uLOS(unitary vector) and vLOS(velocity in uLOS direction)
    uLOS = rLOS / np.linalg.norm(rLOS, axis=0)
    vLOS = uLOS * vSAT

    vLOS = np.sum(vLOS, axis=0)

    fd = - (vLOS/GnssConstants.LIGHT_SPEED_M_S) * GnssConstants.FREQ_L1_MHz * GnssConstants.KHz_IN_MHz

    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = fd
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_DOPPLER_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)