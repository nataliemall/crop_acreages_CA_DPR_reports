# plot_gw_crop_type_comparison_exc.py

import numpy as np 
import matplotlib.colors as mplc
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import os 
import pdb
import pandas as pd
import seaborn as sns
import re 
from tqdm import tqdm  # for something in tqdm(something something):



def gw_crop_type_comparison_plot(irrigation_district_list):
    # irrigation_district_list = ['Tulare Irrigation District', 'Cawelo Water District',  'North Kern Water Storage District', 'Lost Hills Water District', 'Lower Tule River Irrigation District', 'Westlands Water District', 'Kern Delta Water District', 'Tulare Lake Basin Water Storage District', 'Delano - Earlimart Irrigation District', 'Wheeler Ridge - Maricopa Water Storage District', 'Semitropic Water Service District', 'Arvin - Edison Water Storage District', 'Shafter - Wasco Irrigation District' ]
    # pdb.set_trace()
    zero_fillers = np.zeros((len(irrigation_district_list), 5))

    district_matrix = pd.DataFrame(zero_fillers, columns = [ 'irrigation_district_name', 'irrigation_district_acronym', 'perennial_annual_ratio', 'gw_surface_percent', 'gw_surface_percent_wet'  ] )
    for num, irrigation_district in enumerate(irrigation_district_list):
        water_portfolios = pd.read_csv('irrigation_district_water_portfolios.csv', index_col = 'irrigation district')
        sum_crop_types_normalized = pd.read_csv(str(str(irrigation_district) + '/calPUR_data_normalized' + str(irrigation_district) + '.csv'), index_col = 'year')
        sum_crop_types_normalized.index = sum_crop_types_normalized.index.astype(int) # convert index years to integers

        perennial_annual_ratio = sum_crop_types_normalized.percent_tree_crops
        dry_year_surface_water = water_portfolios.dry_year_surface_water[irrigation_district]
        dry_year_gw = water_portfolios.dry_year_gw[irrigation_district]
        wet_year_surface_water = water_portfolios.wet_year_surface_water[irrigation_district]
        wet_year_gw = water_portfolios.wet_year_gw[irrigation_district]

        gw_surface_percent = dry_year_surface_water / ( dry_year_gw + dry_year_surface_water) * 100 # surface water as a percent of total, dry year
        gw_surface_percent_wet = wet_year_surface_water / (wet_year_gw + wet_year_surface_water) * 100 
        # pdb.set_trace()
        district_matrix.irrigation_district_name[num] = irrigation_district
        district_matrix.irrigation_district_acronym[num] = water_portfolios.irrigation_district_acronym[irrigation_district]
        district_matrix.perennial_annual_ratio[num] = perennial_annual_ratio[2016]
        district_matrix.gw_surface_percent[num] = gw_surface_percent
        district_matrix.gw_surface_percent_wet[num] = gw_surface_percent_wet

        point_size = np.sqrt((water_portfolios.irrigated_acreage.values) )  # square root since marker size is ^2
        # point_size
    # pdb.set_trace()        

    fig, ax = plt.subplots()
    ax.scatter(district_matrix.perennial_annual_ratio, district_matrix.gw_surface_percent, color = 'red', s = point_size, alpha = 0.7 )
    plt.hlines(50, 0, 100, colors = '#6baed6', label = 'test')
    plt.vlines(50, 0, 100, colors = '#08519c', label = 'test vline')
    plt.xlabel('Percentage of perennial crops in irrigation district')
    plt.ylabel('Surface water as a percent of total agricultural water use within the irrigation district')
    # pdb.set_trace()
    nn_old = irrigation_district_list
    nn = water_portfolios.irrigation_district_acronym.tolist()
    nn = district_matrix.irrigation_district_acronym.tolist()
    pdb.set_trace()

    for i, txt in enumerate(nn):
        text_x_coord = district_matrix.perennial_annual_ratio[i] - 3
        text_y_coord = district_matrix.gw_surface_percent[i] + 0.1
        ax.annotate(txt, (district_matrix.perennial_annual_ratio[i], district_matrix.gw_surface_percent[i] ), xycoords='data',
                  xytext=(text_x_coord, text_y_coord), textcoords='data',
                  size=10, va="center", ha="center",
                   ) # bbox=dict(boxstyle="round4", fc="w"),

    ax.scatter(district_matrix.perennial_annual_ratio, district_matrix.gw_surface_percent_wet, color = 'green' , s = point_size, alpha = 0.7 )
    
    for i, txt in enumerate(nn):
        text_x_coord = district_matrix.perennial_annual_ratio[i] - 3
        text_y_coord = district_matrix.gw_surface_percent_wet[i] + 0.1
        ax.annotate(txt, (district_matrix.perennial_annual_ratio[i], district_matrix.gw_surface_percent_wet[i] ), xycoords='data',
                  xytext=(text_x_coord, text_y_coord), textcoords='data',
                  size=10, va="center", ha="center",
                   ) # bbox=dict(boxstyle="round4", fc="w"),
        # pdb.set_trace()

    plt.show()
    pdb.set_trace()



irrigation_district_list = [
    'Tulare Irrigation District',
    'Cawelo Water District',
    'Lost Hills Water District',
    'Lower Tule River Irrigation District',
    'Westlands Water District',
    'Kern Delta Water District',
    'Tulare Lake Basin Water Storage District',
    'Delano - Earlimart Irrigation District',
    'Wheeler Ridge - Maricopa Water Storage District',
    'Semitropic Water Service District',
    'Arvin - Edison Water Storage District',
    'Shafter - Wasco Irrigation District',
    'North Kern Water Storage District',
    'Kern - Tulare Water District',
    'Buena Vista Water Storage District',
    'Alta Irrigation District',
    'Berrenda Mesa Water District',
    'Consolidated Irrigation District',
    'Corcoran Irrigation District',
    'Fresno Irrigation District'] 

gw_crop_type_comparison_plot(irrigation_district_list)


