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


## This dictionaty will contain the models to be used 
model_list={}
list_of_models = ['P2011','F2014','U2017']
for i in list_of_models:
    model_list[i] = 0


def sloppyCellReports(request):
    return render(request, 'plotFitting/sloppyCellReports.html')


def P2011_load(request):  ## this has to be a general name
    if not model_list['P2011']: 
        model_list['P2011'] = IO.from_SBML_file('P2011'+'.xml', 'base', duplicate_rxn_params=True)
        model_list['P2011'] = LD_into_LL(model_list['P2011'],20,'light')
        model_list['P2011'].compile()
        return render(request, 'plotFitting/sloppyCellReports.html')
    else:
        return render(request, 'plotFitting/sloppyCellReports.html')

def plotFitting(request):
    
    #model_name='P2011'  ## This variable will deleted in the next commit selecting model will be 
    ## chosen by the user 
    ##Here we decide the type of model to use
    if model_list['P2011']:
        p  = Dynamics.integrate(model_list['P2011'],(0,24*25))
        x=p.timepoints
        y=p.get_var_traj('cL_m')
        plt.figure()
        plt.plot(x,y)
        ## the ploting file should required the name of the app 
        plt.savefig('plotFitting/static/images/temp/x.png', format='png', dpi=300)
        return render(request, 'plotFitting/plot.html')
    else:
        return render(request, 'plotFitting/sloppyCellReports.html')


