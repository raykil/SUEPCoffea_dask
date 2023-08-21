import uproot as up
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.optimize import curve_fit
from scipy import interpolate

def polynomial(x, y, a, b, c, d, e, f, g, h, i, j, k): #Decent
    z = a*(x**5) + b*(x**4) + c*(x**3) + d*(x**2) + e*x + f + g*(y**5)  + h*(y**4) + i*(y**3) + j*(y**2) + k*y
    return z

def joint_polynomial(x, y, a, b, c, d): #Terrible
    z = a*(b*x-c*y)**5 + d
    return z

def exp(x, y, a, b, c, d, e): #Doesnt Converge
    z = a*np.exp(x*b) + c*np.exp(y*d) + e
    return z

def fit_contour(M, *args):
    x, y = M
    arr = np.zeros(x.shape)
    arr = polynomial(x, y, *args)
    return arr

sideband = str(sys.argv[1])
#file = up.open('/eos/user/c/cericeci/www/SUEP/UL18/SR_cards/leadclustertracks_'+sideband+'.root')
file = up.open('C:/Users/slatt/Downloads/leadclustertracks_'+sideband+'_SR.root')
branches = file.keys()

#Divide into Leptonic, Hadronic, Generic Branches
leptonic_branches, hadronic_branches, generic_branches = [], [], []
for i in branches:
    if "SUEP" in i and "Up" not in i and "Dn" not in i:
        if "leptonic" in i:
            leptonic_branches.append(i)
        if "hadronic" in i:
            hadronic_branches.append(i)
        if "generic" in i:
            generic_branches.append(i)

#Build all combinations of Generic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_generic_mS125_mDX_TY'
generic_mD = [2, 3, 4, 8]
multiples = [0.25, 0.5, 2, 4]
generic_TD = []
plotting_TD = np.log(multiples)
temp_T = []
for i in generic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    generic_TD.append(temp_T)
#print(generic_TD)
#print(plotting_TD)

#Construct arrays showing yields in mD and log(T/mD) for each NCluster Bin
temp_name = basename.replace('X', format(generic_mD[0], '.2f'))
temp_name = temp_name.replace('Y', format(generic_mD[0], '.2f'))
generic_bins = file[temp_name].axis().edges()

for i in range(len(generic_bins)):
    if i < len(generic_bins)-1:
        generic_vals = []
        for m in range(len(generic_mD)):
            for t in generic_TD[m]:
                temp_name = basename.replace('X', format(generic_mD[m], '.2f'))
                temp_name = temp_name.replace('Y', format(t, '.2f'))
                #print(temp_name)
                #print(file[temp_name].values()[i])
                #print(file[temp_name].axis().edges())
                generic_vals.append(file[temp_name].values()[i])
        x, y = np.meshgrid(generic_mD, plotting_TD)
        z = np.array(generic_vals).reshape(len(generic_mD), len(plotting_TD)).transpose()
        
        
        #SANITY CHECK
        #print(x)
        #print(y)
        #print(z)
        plt.contourf(x,y,z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Generic Decay')
        plt.colorbar()
        #plt.show()
        plt.clf()
        
        ''' #Using scipy curveFit
        x_data = np.vstack((x.ravel(), y.ravel()))
        #print(x_data)
        flat_data = z.ravel()
        #print(flat_data)


        #p0 = [1,1,1,1,1]
        p0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #p0 = [1,1,1,1]
        
        popt, pcov = curve_fit(fit_contour, x_data, flat_data, p0)
        fit = polynomial(x, y, *popt)
        print(popt)
        print(fit)
        print(z)
        print(z-fit)
        '''

        tck = interpolate.bisplrep(x.transpose(),y.transpose(),z.transpose(),s=3)
        xNew = np.linspace(x.T[:,0][0], x.T[:,0][len(x.T[:,0])-1], 12)
        yNew = np.linspace(y.T[0,:][0], y.T[0,:][len(y.T[0,:])-1], 12)
        fit = interpolate.bisplev(xNew, yNew,tck)

        plt.contourf(xNew,yNew,fit.T)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Fitted Contour of '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Generic Decay')
        plt.colorbar()
        plt.savefig('signalInterpolation/'+sideband+'/Generic_Int/Generic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

#Build all combinations of Hadronic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_hadronic_mS125_mDX_TY'
Hadronic_mD = [1.4, 2, 3, 4, 8]
multiples = [0.25, 0.5, 2, 4]
Hadronic_TD = []
plotting_TD = np.log(multiples)
temp_T = []
for i in Hadronic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    Hadronic_TD.append(temp_T)
#print(Hadronic_TD)
#print(plotting_TD)

#Construct arrays showing yields in mD and log(T/mD) for each NCluster Bin
temp_name = basename.replace('X', format(Hadronic_mD[0], '.2f'))
temp_name = temp_name.replace('Y', format(Hadronic_mD[0], '.2f'))
Hadronic_bins = file[temp_name].axis().edges()

for i in range(len(Hadronic_bins)):
    if i < len(Hadronic_bins)-1:
        Hadronic_vals = []
        for m in range(len(Hadronic_mD)):
            for t in Hadronic_TD[m]:
                temp_name = basename.replace('X', format(Hadronic_mD[m], '.2f'))
                temp_name = temp_name.replace('Y', format(t, '.2f'))
                #print(temp_name)
                #print(file[temp_name].values()[i])
                #print(file[temp_name].axis().edges())
                Hadronic_vals.append(file[temp_name].values()[i])
        x, y = np.meshgrid(Hadronic_mD, plotting_TD)
        z = np.array(Hadronic_vals).reshape(len(Hadronic_mD), len(plotting_TD)).transpose()
        
        
        #SANITY CHECK
        #print(x)
        #print(y)
        #print(z)
        plt.contourf(x,y,z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(Hadronic_bins[i])+','+str(Hadronic_bins[i+1])+']'+' - Hadronic Decay')
        plt.colorbar()
        #plt.show()
        plt.clf()
        
        ''' #Using scipy curveFit
        x_data = np.vstack((x.ravel(), y.ravel()))
        #print(x_data)
        flat_data = z.ravel()
        #print(flat_data)


        #p0 = [1,1,1,1,1]
        p0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #p0 = [1,1,1,1]
        
        popt, pcov = curve_fit(fit_contour, x_data, flat_data, p0)
        fit = polynomial(x, y, *popt)
        print(popt)
        print(fit)
        print(z)
        print(z-fit)
        '''

        tck = interpolate.bisplrep(x.transpose(),y.transpose(),z.transpose(),s=3)
        xNew = np.linspace(x.T[:,0][0], x.T[:,0][len(x.T[:,0])-1], 12)
        yNew = np.linspace(y.T[0,:][0], y.T[0,:][len(y.T[0,:])-1], 12)
        fit = interpolate.bisplev(xNew, yNew,tck)

        plt.contourf(xNew,yNew,fit.T)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Fitted Contour of '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(Hadronic_bins[i])+','+str(Hadronic_bins[i+1])+']'+' - Hadronic Decay')
        plt.colorbar()
        plt.savefig('signalInterpolation/'+sideband+'/Hadronic_Int/Hadronic_'+sideband+'_'+str(Hadronic_bins[i])+'_'+str(Hadronic_bins[i+1])+'.pdf')
        plt.clf()


#Build all combinations of Leptonic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_leptonic_mS125_mDX_TY'
Leptonic_mD = [1, 2, 3, 4, 8]
multiples = [0.25, 0.5, 2, 4]
Leptonic_TD = []
plotting_TD = np.log(multiples)
temp_T = []
for i in Leptonic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    Leptonic_TD.append(temp_T)
#print(Leptonic_TD)
#print(plotting_TD)

#Construct arrays showing yields in mD and log(T/mD) for each NCluster Bin
temp_name = basename.replace('X', format(Leptonic_mD[0], '.2f'))
temp_name = temp_name.replace('Y', format(Leptonic_mD[0], '.2f'))
Leptonic_bins = file[temp_name].axis().edges()

for i in range(len(Leptonic_bins)):
    if i < len(Leptonic_bins)-1:
        Leptonic_vals = []
        for m in range(len(Leptonic_mD)):
            for t in Leptonic_TD[m]:
                temp_name = basename.replace('X', format(Leptonic_mD[m], '.2f'))
                temp_name = temp_name.replace('Y', format(t, '.2f'))
                #print(temp_name)
                #print(file[temp_name].values()[i])
                #print(file[temp_name].axis().edges())
                Leptonic_vals.append(file[temp_name].values()[i])
        x, y = np.meshgrid(Leptonic_mD, plotting_TD)
        z = np.array(Leptonic_vals).reshape(len(Leptonic_mD), len(plotting_TD)).transpose()
        
        
        #SANITY CHECK
        #print(x)
        #print(y)
        #print(z)
        plt.contourf(x,y,z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(Leptonic_bins[i])+','+str(Leptonic_bins[i+1])+']'+' - Leptonic Decay')
        plt.colorbar()
        #plt.show()
        plt.clf()
        
        ''' #Using scipy curveFit
        x_data = np.vstack((x.ravel(), y.ravel()))
        #print(x_data)
        flat_data = z.ravel()
        #print(flat_data)


        #p0 = [1,1,1,1,1]
        p0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #p0 = [1,1,1,1]
        
        popt, pcov = curve_fit(fit_contour, x_data, flat_data, p0)
        fit = polynomial(x, y, *popt)
        print(popt)
        print(fit)
        print(z)
        print(z-fit)
        '''

        tck = interpolate.bisplrep(x.transpose(),y.transpose(),z.transpose(),s=3)
        xNew = np.linspace(x.T[:,0][0], x.T[:,0][len(x.T[:,0])-1], 12)
        yNew = np.linspace(y.T[0,:][0], y.T[0,:][len(y.T[0,:])-1], 12)
        fit = interpolate.bisplev(xNew, yNew,tck)

        plt.contourf(xNew,yNew,fit.T)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Fitted Contour of '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(Leptonic_bins[i])+','+str(Leptonic_bins[i+1])+']'+' - Leptonic Decay')
        plt.colorbar()
        plt.savefig('signalInterpolation/'+sideband+'/Leptonic_Int/Leptonic_'+sideband+'_'+str(Leptonic_bins[i])+'_'+str(Leptonic_bins[i+1])+'.pdf')
        plt.clf()

        

