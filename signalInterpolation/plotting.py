import uproot as up
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

sideband = str(sys.argv[1])
#file = up.open('/eos/user/c/cericeci/www/SUEP/UL18/SR_cards/leadclustertracks_'+sideband+'.root')
#file = up.open('C:/Users/slatt/Downloads/leadclustertracks_'+sideband+'_SR.root')
file = up.open('/eos/user/g/gdecastr/SUEPCoffea_dask/signalInterpolation/leadclustertracks_'+sideband+'_SR.root')
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


######################################################################################################### Generic


#Build all combinations of Generic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_generic_mS125_mDX_TY'
generic_mD = [2, 3, 4, 8]
multiples = [0.25, 0.5, 1, 2, 4]
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

totalMD = []
totaltD = []
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

        '''DEBUGGING
        print(x)
        print(y)
        z = np.array(generic_vals).reshape(len(generic_mD), len(plotting_TD)).transpose()
        print(z)
        #generic_vals = np.linspace(0,20,20)
        #z = np.array(generic_vals).reshape(len(generic_mD), len(plotting_TD)).transpose()
        #print(z)
        '''

        ###Save mD Projection for later
        mDproj_x = x[0]
        mDproj_y = z.sum(axis = 0)
        totalMD.append(mDproj_y)

        ###Save tD Projection for later
        tDproj_x = [item[0] for item in y]
        tDproj_y = z.sum(axis = 1)
        totaltD.append(tDproj_y)
        
        ###Plot contour
        plt.contourf(x, y, z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Generic Decay')
        plt.colorbar()            
        plt.savefig('plots/'+sideband+'/Generic/Generic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot(x[0], z[0], label = r'$log(T_D/m_D) \approx$ -1.39')
        plt.plot(x[0], z[1], label = r'$log(T_D/m_D) \approx$ -.69')
        plt.plot(x[0], z[2], label = r'$log(T_D/m_D) \approx$ 0')
        plt.plot(x[0], z[3], label = r'$log(T_D/m_D) \approx$ .69')
        plt.plot(x[0], z[4], label = r'$log(T_D/m_D) \approx$ 1.39')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Generic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Generic_1D_Projections/1DmD_Generic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot([s[0] for s in y], [s[0] for s in z], label = r'm = 2')
        plt.plot([s[0] for s in y], [s[1] for s in z], label = r'm = 3')
        plt.plot([s[0] for s in y], [s[2] for s in z], label = r'm = 4')
        plt.plot([s[0] for s in y], [s[3] for s in z], label = r'm = 8')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Generic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Generic_1D_Projections/1DTD_Generic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

if not os.path.isdir('plots/'+sideband+'/Generic_1D_Projections/'):
    os.makedirs('plots/'+sideband+'/Generic_1D_Projections/')

###Plot tD Projections
for i in range(len(generic_bins)):
    if i < len(generic_bins)-1:
        plt.plot(tDproj_x, totaltD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']')
plt.xlabel(r'$log(T_D/m_D)$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Generic Decay')
plt.savefig('plots/'+sideband+'/Generic_1D_Projections/TDTotal.pdf')

plt.clf()

###Plot mD Projections
for i in range(len(generic_bins)):
    if i < len(generic_bins)-1:
        plt.plot(mDproj_x, totalMD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']')
plt.xlabel(r'$m_D$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Generic Decay')
plt.savefig('plots/'+sideband+'/Generic_1D_Projections/mDTotal.pdf')

plt.clf()

######################################################################################################### Hadronic

#Build all combinations of Hadronic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_hadronic_mS125_mDX_TY'
hadronic_mD = [1.40, 2, 3, 4, 8]
multiples = [0.25, 0.5, 1, 2, 4]
hadronic_TD = []
plotting_TD = np.log(multiples)
temp_T = []
for i in hadronic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    hadronic_TD.append(temp_T)
#print(hadronic_TD)
#print(plotting_TD)

#Construct arrays showing yields in mD and log(T/mD) for each NCluster Bin
temp_name = basename.replace('X', format(hadronic_mD[0], '.2f'))
temp_name = temp_name.replace('Y', format(hadronic_mD[0], '.2f'))
hadronic_bins = file[temp_name].axis().edges()
#print(hadronic_bins)

totalMD = []
totaltD = []
for i in range(len(hadronic_bins)):
    if i < len(hadronic_bins)-1:
        hadronic_vals = []
        for m in range(len(hadronic_mD)):
            for t in hadronic_TD[m]:
                temp_name = basename.replace('X', format(hadronic_mD[m], '.2f'))
                temp_name = temp_name.replace('Y', format(t, '.2f'))
                #print(temp_name)
                #print(file[temp_name].axis().edges())
                hadronic_vals.append(file[temp_name].values()[i])
        x, y = np.meshgrid(hadronic_mD, plotting_TD)
        z = np.array(hadronic_vals).reshape(len(hadronic_mD), len(plotting_TD)).transpose()

        ###Save mD Projection for later
        mDproj_x = x[0]
        mDproj_y = z.sum(axis = 0)
        totalMD.append(mDproj_y)

        ###Save tD Projection for later
        tDproj_x = [item[0] for item in y]
        tDproj_y = z.sum(axis = 1)
        totaltD.append(tDproj_y)

        plt.contourf(x, y, z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(hadronic_bins[i])+','+str(hadronic_bins[i+1])+']'+' - Hadronic Decay')
        plt.colorbar()            
        plt.savefig('plots/'+sideband+'/Hadronic/Hadronic_'+sideband+'_'+str(hadronic_bins[i])+'_'+str(hadronic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot(x[0], z[0], label = r'$log(T_D/m_D) \approx$ -1.39')
        plt.plot(x[0], z[1], label = r'$log(T_D/m_D) \approx$ -.69')
        plt.plot(x[0], z[2], label = r'$log(T_D/m_D) \approx$ 0')
        plt.plot(x[0], z[3], label = r'$log(T_D/m_D) \approx$ .69')
        plt.plot(x[0], z[4], label = r'$log(T_D/m_D) \approx$ 1.39')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Hadronic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Hadronic_1D_Projections/1DmD_Hadronic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot([s[0] for s in y], [s[0] for s in z], label = r'm = 1.4')
        plt.plot([s[0] for s in y], [s[1] for s in z], label = r'm = 2')
        plt.plot([s[0] for s in y], [s[2] for s in z], label = r'm = 3')
        plt.plot([s[0] for s in y], [s[3] for s in z], label = r'm = 4')
        plt.plot([s[0] for s in y], [s[4] for s in z], label = r'm = 8')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Hadronic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Hadronic_1D_Projections/1DTD_Hadronic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

if not os.path.isdir('plots/'+sideband+'/Hadronic_1D_Projections/'):
    os.makedirs('plots/'+sideband+'/Hadronic_1D_Projections/')

###Plot tD Projections
for i in range(len(hadronic_bins)):
    if i < len(hadronic_bins)-1:
        plt.plot(tDproj_x, totaltD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(hadronic_bins[i])+','+str(hadronic_bins[i+1])+']')
plt.xlabel(r'$T_D$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Hadronic Decay')
plt.savefig('plots/'+sideband+'/Hadronic_1D_Projections/TDTotal.pdf')

plt.clf()

###Plot mD Projections
for i in range(len(hadronic_bins)):
    if i < len(hadronic_bins)-1:
        plt.plot(mDproj_x, totalMD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(hadronic_bins[i])+','+str(hadronic_bins[i+1])+']')
plt.xlabel(r'$m_D$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Hadronic Decay')
plt.savefig('plots/'+sideband+'/Hadronic_1D_Projections/mDTotal.pdf')

plt.clf()

######################################################################################################### Leptonic


#Build all combinations of Leptonic Branch mD and TD for plotting
basename = 'leadclustertracks_'+sideband+'_SUEP_leptonic_mS125_mDX_TY'
leptonic_mD = [1, 2, 3, 4, 8]
multiples = [0.25, 0.5, 1, 2, 4]
leptonic_TD = []
plotting_TD = np.log(multiples)
temp_T = []
for i in leptonic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    leptonic_TD.append(temp_T)
#print(leptonic_TD)
#print(plotting_TD)

#Construct arrays showing yields in mD and log(T/mD) for each NCluster Bin
temp_name = basename.replace('X', format(leptonic_mD[0], '.2f'))
temp_name = temp_name.replace('Y', format(leptonic_mD[0], '.2f'))
leptonic_bins = file[temp_name].axis().edges()
#print(leptonic_bins)

totalMD = []
totaltD = []
for i in range(len(leptonic_bins)):
    if i < len(leptonic_bins)-1:
        leptonic_vals = []
        for m in range(len(leptonic_mD)):
            for t in leptonic_TD[m]:
                temp_name = basename.replace('X', format(leptonic_mD[m], '.2f'))
                temp_name = temp_name.replace('Y', format(t, '.2f'))
                #print(temp_name)
                #print(file[temp_name].axis().edges())
                leptonic_vals.append(file[temp_name].values()[i])
        x, y = np.meshgrid(leptonic_mD, plotting_TD)
        z = np.array(leptonic_vals).reshape(len(leptonic_mD), len(plotting_TD)).transpose()

        ###Save mD Projection for later
        mDproj_x = x[0]
        mDproj_y = z.sum(axis = 0)
        totalMD.append(mDproj_y)

        ###Save tD Projection for later
        tDproj_x = [item[0] for item in y]
        tDproj_y = z.sum(axis = 1)
        totaltD.append(tDproj_y)

        plt.contourf(x, y, z)
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'$log(T_D/m_D)$')
        plt.title(r'Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(leptonic_bins[i])+','+str(leptonic_bins[i+1])+']'+' - Leptonic Decay')
        plt.colorbar()            
        plt.savefig('plots/'+sideband+'/Leptonic/Leptonic_'+sideband+'_'+str(leptonic_bins[i])+'_'+str(leptonic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot(x[0], z[0], label = r'$log(T_D/m_D) \approx$ -1.39')
        plt.plot(x[0], z[1], label = r'$log(T_D/m_D) \approx$ -.69')
        plt.plot(x[0], z[2], label = r'$log(T_D/m_D) \approx$ 0')
        plt.plot(x[0], z[3], label = r'$log(T_D/m_D) \approx$ .69')
        plt.plot(x[0], z[4], label = r'$log(T_D/m_D) \approx$ 1.39')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Leptonic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Leptonic_1D_Projections/1DmD_Leptonic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

        plt.plot([s[0] for s in y], [s[0] for s in z], label = r'm = 1')
        plt.plot([s[0] for s in y], [s[1] for s in z], label = r'm = 2')
        plt.plot([s[0] for s in y], [s[2] for s in z], label = r'm = 3')
        plt.plot([s[0] for s in y], [s[3] for s in z], label = r'm = 4')
        plt.plot([s[0] for s in y], [s[4] for s in z], label = r'm = 8')
        plt.xlabel(r'$m_D$')
        plt.ylabel(r'Yields')
        plt.title(r'1D Projection of Yields in '+sideband+' - $N^{SUEP}_{Tracks}$ ['+str(generic_bins[i])+','+str(generic_bins[i+1])+']'+' - Leptonic Decay')
        plt.legend()
        plt.savefig('plots/'+sideband+'/Leptonic_1D_Projections/1DTD_Leptonic_'+sideband+'_'+str(generic_bins[i])+'_'+str(generic_bins[i+1])+'.pdf')
        plt.clf()

if not os.path.isdir('plots/'+sideband+'/Leptonic_1D_Projections/'):
    os.makedirs('plots/'+sideband+'/Leptonic_1D_Projections/')

###Plot tD Projections
for i in range(len(leptonic_bins)):
    if i < len(leptonic_bins)-1:
        plt.plot(tDproj_x, totaltD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(leptonic_bins[i])+','+str(leptonic_bins[i+1])+']')
plt.xlabel(r'$T_D$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Leptonic Decay')
plt.savefig('plots/'+sideband+'/Leptonic_1D_Projections/TDTotal.pdf')

plt.clf()

###Plot mD Projections
for i in range(len(leptonic_bins)):
    if i < len(leptonic_bins)-1:
        plt.plot(mDproj_x, totalMD[i], label = r'$N^{SUEP}_{Tracks}$ ['+str(leptonic_bins[i])+','+str(leptonic_bins[i+1])+']')
plt.xlabel(r'$m_D$')
plt.ylabel(r'Count')
plt.legend(loc = 'upper left', prop={'size': 6})
plt.title(r'1D Projection of Yields in '+sideband+' - Leptonic Decay')
plt.savefig('plots/'+sideband+'/Leptonic_1D_Projections/mDTotal.pdf')

plt.clf()


















'''
#Get all Leptonic Branch names used for fitting (remove T = 1 for validation)
multiples = [0.25, 0.5, 2, 4]
leptonic_TD = []
temp_T = []
for i in leptonic_mD:
    temp_T = []
    for j in multiples:
        temp_T.append(i*j)
    leptonic_TD.append(temp_T)

leptonic_vals = []
temp_vals = []
for m in range(len(leptonic_mD)):
    temp_vals = []
    for t in leptonic_TD[m]:
        temp_name = basename.replace('X', format(leptonic_mD[m], '.2f'))
        temp_name = temp_name.replace('Y', format(t, '.2f'))
        #print(temp_name)
        #print(file[temp_name].axis().edges())
        temp_vals.append(file[temp_name].values())
    leptonic_vals.append(np.array(temp_vals))
leptonic_bins = file[temp_name].axis().edges()
print(leptonic_vals[0])

#Get all Leptonic Branch names used for validating fit
leptonic_vals_check = []
for m in range(len(leptonic_mD)):
    temp_name = basename.replace('X', format(leptonic_mD[m], '.2f'))
    temp_name = temp_name.replace('Y', format(leptonic_mD[m], '.2f'))
    #print(temp_name)
    leptonic_vals_check.append(file[temp_name].values())
#print(leptonic_vals_check)
'''

