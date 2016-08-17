## views for plotFitting
from django.shortcuts import render
from django.http import HttpResponse
import os

##it is imporant that matplotlib is called before sloppyCell
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from SloppyCell.ReactionNetworks import *
from photoperiodMaker import *
from data_plotter import *
from Full_TiMet_single_point_data_displaced import *
import numpy as np

## This dictionaty will contain the models to be used 
base_model_list={}
model_names = ['P2011','F2014','U2017']   ##This is going to be a more general thing such that wil help to generate model list automatically
for i in model_names:
    base_model_list[i] = 0


def sloppyCellReports(request):
    return render(request, 'plotFitting/sloppyCellReports.html')


def P2011_load(request):  ## this has to be a general name
    if not base_model_list['P2011']: 
        base_model_list['P2011'] = IO.from_SBML_file('P2011'+'.xml', 'base', duplicate_rxn_params=True)
        base_model_list['P2011'] = LD_into_LL(base_model_list['P2011'],10,'light') #This function takes a model and dya number
        base_model_list['P2011'].compile()
        return render(request, 'plotFitting/sloppyCellReports.html')
    else:
        return render(request, 'plotFitting/sloppyCellReports.html')

def plotFitting(request):
    
    #model_name='P2011'  ## This variable will deleted in the next commit selecting model will be 
    ## chosen by the user 
    ##Here we decide the type of model to use
    if base_model_list['P2011']:
        p  = Dynamics.integrate(base_model_list['P2011'],(0,24*15))
        x=p.timepoints
        y=p.get_var_traj('cL_m')
        light = p.get_var_traj('light')
        fig = plt.figure()
        ax = fig.add_subplot(211)
        plot_sp_data(ax,data,'col_0_LL','log_cL_m','red')
        ax.plot(x,np.log(y))
        ax2=fig.add_subplot(212)
        ax2.plot(x,light)
        ## the ploting file should required the name of the app
        #data_ploted = plot_sp_data(data,'col_0_LL','log_cL_m','red')
        #plt.data_ploted 
        fig.savefig('plotFitting/static/images/temp/x.png', format='png', dpi=300)
        return render(request, 'plotFitting/plot.html')
    else:
        return render(request, 'plotFitting/sloppyCellReports.html')


