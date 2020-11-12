#utility functions

def test():
    print("Connected to Utility Functions")

    
def cell_filter(threshold, sample):
    ms = sample.sum(axis = 1) #library size 
    use_cells = ms.index[np.log10(ms) > threshold]
    sample = sample.loc[use_cells]
    print(sample.shape)
    return sample

def graph_patients(df_list, names_list):
    fig = plt.figure(figsize=[4 * len(df_list), 4])
    for i, sample in enumerate(df_list):
        ms = np.log10(sample.sum(axis=1)) #library size
        # Figure
        ax = fig.add_subplot(1, len(df_list), i+1)
        ax.hist(ms,50)
        ax.set_title(names_list[i])
        ax.set_xlabel('log10 of library size')

def gene_filter(sample):
    before = sample.shape[1]
    use_genes = sample.columns[sample.sum(axis=0) > 0]
    sample = sample[use_genes]
    print(before - sample.shape[1] , "genes removed")
    return sample