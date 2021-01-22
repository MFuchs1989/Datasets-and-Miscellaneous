import pandas as pd
import numpy as np
import os


class DataPreprocessor:
    def __init__(self, path_folder = "path/to/data"):

        self.path_folder = path_folder
        
        # Path to input
        self.path_input_folder = "{}/input/".format(path_folder)
        self.path_input_countries = self.path_input_folder + 'Countries.csv'
        self.path_input_countries_metadata = self.path_input_folder + 'Countries_metadata.csv'

        # Path to modified input
        self.path_input_modified_folder = "{}/input_modified/".format(path_folder)
        self.path_input_modified_countries = self.path_input_modified_folder + 'Countries.csv'
        self.path_input_modified_countries_metadata = self.path_input_modified_folder + 'Countries_metadata.csv'

        # Path on which output tables are saved
        self.path_output_folder = "{}/output/".format(path_folder)
        self.path_output_countries = self.path_output_folder + 'Countries.csv'
        self.path_output_countries_metadata = self.path_output_folder + 'Countries_metadata.csv'

        # create dictionaries for read dtypes
        self.read_dtypes_countries = {'Countries':'category'}
        self.read_dtypes_countries_metadata = {'country_names':'category'}

        # create folders for output if not existent yet
        if not os.path.exists(self.path_input_modified_folder):
            os.makedirs(self.path_input_modified_folder)
        if not os.path.exists(self.path_output_folder):
            os.makedirs(self.path_output_folder) 


    def read_data_from_raw_input(self, save_countries=True, save_countries_metadata=True):

        print("Start:\tRead in countries Dataset")
        self.countries = pd.read_csv(self.path_input_countries, dtype=self.read_dtypes_countries)
        self.countries.Population = self.countries.Population.map(lambda x: x.split(':')[1])
        self.countries['Population'] = self.countries['Population'].astype('int64')
        print("Finish:\tRead in countries Dataset")

        print("Start:\tRead in countries_metadata Dataset")       
        self.countries_metadata = pd.read_csv(self.path_input_countries_metadata, dtype=self.read_dtypes_countries_metadata)
        self.countries_metadata.Land_Area = self.countries_metadata.Land_Area.map(lambda x: x.split(':')[1])
        self.countries_metadata['Land_Area'] = self.countries_metadata['Land_Area'].astype('int64')
        print("Finish:\tRead in countries_metadata Dataset")

        if save_countries:
            print("Start:\tSave countries Dataset to disc")
            self.countries.to_csv(self.path_input_modified_countries, index=False)
            print("Finish:\tSave countries Dataset to disc")
 
        if save_countries_metadata:
            print("Start:\tSave countries_metadata Dataset to disc")
            self.countries_metadata.to_csv(self.path_input_modified_countries_metadata, index=False)
            print("Finish:\tSave countries_metadata Dataset to disc")


    def read_data_from_modified_input(self):

        self.countries = pd.read_csv(self.path_input_modified_countries, dtype=self.read_dtypes_countries)
        self.countries_metadata = pd.read_csv(self.path_input_modified_countries_metadata, dtype=self.read_dtypes_countries_metadata)


    def preprocess_data(self, save_preprocess_countries=True, save_preprocess_countries_metadata=True):

        print("Start:\tPreprocessing countries Dataset")
        self.preprocess_countries()
        print("Finish:\tPreprocessing countries Dataset")

        print("Start:\tPreprocessing countries_metadata Dataset")
        self.preprocess_countries_metadata()
        print("Finish:\tPreprocessing countries_metadata Dataset")

        if save_preprocess_countries:
            print("Start:\tSave countries Dataset to disc")
            self.countries.to_csv(self.path_output_countries, index=False)
            print("Finish:\tSave countries Dataset to disc")

        if save_preprocess_countries_metadata:
            print("Start:\tSave countries_metadata Dataset to disc")
            self.countries_metadata.to_csv(self.path_output_countries_metadata, index=False)
            print("Finish:\tSave countries_metadata Dataset to disc")

        return self.countries, self.countries_metadata


    def preprocess_countries(self):
        
        self.countries['Population'] = self.countries['Population']/1000
        self.countries = self.countries.rename(columns={'Population':'Population_per_k'})


    def preprocess_countries_metadata(self):
        
        self.countries_metadata['Land_Area'] = self.countries_metadata['Land_Area']/1000
        self.countries_metadata = self.countries_metadata.rename(columns={'Land_Area':'Land_Area_per_k'})


    def read_preprocessed_tables(self):
        
        print("Start:\tRead in modified countries Dataset")
        self.countries = pd.read_csv(self.path_output_countries, dtype=self.read_dtypes_countries)
        print("Finish:\tRead in modified countries Dataset")

        print("Start:\tRead in modified countries_metadata Dataset")       
        self.countries_metadata = pd.read_csv(self.path_output_countries_metadata, dtype=self.read_dtypes_countries_metadata)
        print("Finish:\tRead in modified countries_metadata Dataset")

        return self.countries, self.countries_metadata


def main():

    datapreprocesssor = DataPreprocessor()
    datapreprocesssor.read_data_from_raw_input()
    datapreprocesssor.read_data_from_modified_input()
    datapreprocesssor.preprocess_data()
    print('ETL has been successfully completed !!')

if __name__ == '__main__':
    main()

