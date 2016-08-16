
def LD_into_LL(model,days, light_variable):
    flag=1
    for i in range(0,24*(days)+12,12):
        if flag:
            model.add_event('on_'+str(i), 'gt(time,'+str(i)+')', {light_variable: 1.})
            flag = 0
        else:
            model.add_event('off_'+str(i), 'gt(time,'+str(i)+')', {light_variable: 0.})
            flag = 1
    return model
    
def LD_into_DD(model,days, light_variable):
    flag=1
    for i in range(0,24*(days)+12,12):
        if flag:
            model.add_event('on_'+str(i), 'gt(time,'+str(i)+')', {light_variable: 1.})
            flag = 0
        else:
            model.add_event('off_'+str(i), 'gt(time,'+str(i)+')', {light_variable: 0.})
            flag = 1
    return model