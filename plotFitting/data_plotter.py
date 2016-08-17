def plot_sp_data(ax,data,network,species, colour):
    time = []
    data_mean = []
    data_std= []
    for i in data[network][species]:
        time.append(i)
        data_mean.append(data[network][species][i][0])
        data_std.append(data[network][species][i][1])
    return ax.errorbar(time,data_mean,yerr=data_std, fmt='o', color=colour)  