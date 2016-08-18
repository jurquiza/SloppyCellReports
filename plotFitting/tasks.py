from __future__ import absolute_import

from celery import shared_task
import numpy as np
from SloppyCell.ReactionNetworks import *
from .photoperiodMaker import *
from .models import ModelProfile
from .Full_TiMet_single_point_data_displaced import *

@shared_task
def test(model, profile):
    q1=ModelProfile.objects.get(pk=profile)
    model_base = IO.from_SBML_file(model+'.xml', 'col_0_LL', duplicate_rxn_params=True)
    
    colnames = ['cL_m','cP9_m','cP7_m','cP5_m','cT_m','cLUX_m','cG_m','cE3_m','cE4_m']
    for i in range(len(colnames)):
        model_base.add_species('log_'+colnames[i],'compartment_')
        model_base.add_assignment_rule('log_'+colnames[i],'log('+colnames[i]+')')
    
    model_base= LD_into_LL(model_base,q1.number_of_LD_cycles,'light')
    model_base.compile()
    m = Model([expt],[model_base])
    params = m.get_params()
    params = Optimization.fmin_lm_log_params_fd(m,params,maxiter=2,disp=True, avegtol=1e3)
    print "compiled"
    return 'Test for SloppyCell "%s" ' % model
    
#@shared_task
#def run_fitting(model):
#    return 'Test for SloppyCell "%s" ' % model
#    params = m.get_params()
#    params = Optimization.fmin_lm_log_params_fd(m,params,maxiter=2,disp=True, avegtol=1e3)
#    params = np.asarray(params)
    
#    return params
