
def get_genes(infile,outfile):
    gene_lst = []                             
    with open(infile) as  g:
        check = False                         
        for item in g:
            if item.startswith('name'):       
                check = True                  
                pass                          
            if check:                          
                new = item.split()
                if len(new) > 0:
                    gene_lst.append(new[0])   
                
    gene_lst = gene_lst[2:-7]                 
    with open(outfile, 'w') as outfile:       
        for i in gene_lst:
            outfile.write(i+'\n')