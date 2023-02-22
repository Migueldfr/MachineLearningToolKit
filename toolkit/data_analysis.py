import pandas as pd

def read_url(url):

    '''
    This function reads a CSV file from a URL using the pandas library in Python. 
    The CSV file is read using different delimiters and encodings to handle different file types.

    Parameters
    ----------
    url : is a valid url.

    
    Return
    ----------
        df : is the dataframe with the data already loaded into memory.
    '''

    sep=[',', ';', '|', ':','\t','\s+']
    encoding=['utf-8', 'latin-1', 'latin1', 'iso-8859-1', 'iso8859-1', 'ascii', 'us-ascii', 'utf-16', 'utf16', 'utf-32', 'utf32']
    
    for s in sep:
        for e in encoding:

                df = pd.read_csv(url, sep=s, encoding=e)

                if df.shape[1] == 1:
                    continue
                else:
                    return df
                

def read_csv_zip(zip_file, csv_file, sep=';'):

    import pickle
    import zipfile
    """
    Upload a CSV file from a zip file with custom separation.

    Parameters
    ----------
         zip_file: The name of the zip file that contains the CSV file.
         csv_file: The name of the CSV file to upload.
         sep: The separator to use when reading the CSV file. the default value is ';'

    Returns:
    ----------
        A pandas DataFrame object that contains the data from the CSV file.
    """
    with zipfile.ZipFile(zip_file, 'r') as zip:
        with zip.open(csv_file, 'r') as file:
            # Read CSV file with custom separator
            df = pd.read_csv(file, sep=sep)

    return df

