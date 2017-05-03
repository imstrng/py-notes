import csv, pickle


def pickle_space_csv(filename_in, filename_out):
    '''Pickled de CSV data van filename_in naar filename_out'''

    # Leest het csv bestand in een list met lists
    with open(filename_in) as f:
        csvobject = csv.reader(f, delimiter=' ')
        data = [row for row in csvobject]

    # Picle de list met lists naar een beststand.    
    with open(filename_out,'wb') as f:
        pickle.dump(data,f)



if __name__ == '__main__':
    # Leest een csv besand en Pickle deze
    pickle_space_csv('sample_sep_is_space_csv.txt','sample_sep_is_space_csv.pickled')

    # Ter contole, leest de data vanuit csv file en pickle file en vergelijk deze
    with open('sample_sep_is_space_csv.txt') as f:
        csvobject = csv.reader(f, delimiter=' ')
        csvdata = [row for row in csvobject]

    with open('sample_sep_is_space_csv.pickled','rb') as f:
        picledata = pickle.load(f)

    if csvdata == picledata:
        print('Ja het zelfde')    
    else:
        print('Nee, ze zijn niet het zelfde')