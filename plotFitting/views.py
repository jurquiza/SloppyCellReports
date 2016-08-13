## views for plotFitting
from django.shortcuts import render
import os
from SloppyCell.ReactionNetworks import *

def plotFitting(request):
    model_name='P2011'
    ##Here we decide the type of model to use
    
    if model_name=='P2011':
        net_base = IO.from_SBML_file('BIOMD055-noceil.xml', 'base', duplicate_rxn_params=True)
        net_base.compile()
        p  = Dynamics.integrate(net_base,(0,25)).timepoints
        
    else:
        p = 1
    return render(request, 'plotFitting/plotFitting.html', {'p':p})



