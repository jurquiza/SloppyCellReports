## views for plotFitting
from django.shortcuts import render
from django.http import HttpResponse
import os

##it is imporant that matplotlib is called before sloppyCell
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from SloppyCell.ReactionNetworks import *

#plt.ioff()
#plt.plot([1.6, 2.7])
#plt.savefig('/images/t.png',format='png')


#net_base = IO.from_SBML_file(model_name+'.xml', 'base', duplicate_rxn_params=True)
#net_base.compile()
P2011_flag=0
def P2011_load(request):
    net_base = IO.from_SBML_file(model_name+'.xml', 'base', duplicate_rxn_params=True)
    net_base.compile()
    P2011_flag=1
    return render(request, 'plotFitting/plotFitting.html')

def plotFitting(request):
    
    #model_name='P2011'  ## This variable will deleted in the next commit selecting model will be 
    ## chosen by the user 
    ##Here we decide the type of model to use
    
    if P2011_flag:
        p  = Dynamics.integrate(net_base,(0,24*10))
        x=p.timepoints
        y=p.get_var_traj('cL_m')
        plt.figure()
        plt.plot(x,y)
        ## the ploting file should required the name of the app 
        plt.savefig('plotFitting/static/images/temp/x.png', format='png', dpi=300)
        return render(request, 'plotFitting/plot.html')
    else:
        p = 1
        return render(request, 'plotFitting/plotFitting.html', {'p':p})


