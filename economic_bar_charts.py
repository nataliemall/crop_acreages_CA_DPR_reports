### Create bar chart from crop_loss_calcs ###  

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
import unittest



# overall_ID_table =pd.read_csv('overall_irrigation_district_revenue_loss_estimates.csv', index_col = [0])  # import data 
overall_ID_table =pd.read_csv('overall_irrigation_district_revenue_loss_estimates_to_graph.csv', index_col = [0])  # import data 



def plot_dollar_losses():
	n_groups = len(overall_ID_table)

	bars_in_group = len(overall_ID_table.columns) / 2   # number of clumps  

	baseline_curtailment_rev_loss = overall_ID_table.total_revenue_lost_baseline

	curtailment_at_75_af_rev_loss = overall_ID_table.total_revenue_lost_75 - baseline_curtailment_rev_loss

	curtailment_at_50_af_rev_loss = overall_ID_table.total_revenue_lost_50 - baseline_curtailment_rev_loss

	curtailment_at_25_af_rev_loss = overall_ID_table.total_revenue_lost_25 - baseline_curtailment_rev_loss


	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
 
	rects_75_af = plt.barh(index, (curtailment_at_75_af_rev_loss / 1000000), bar_width / 1.5,   # /1000000 for millions of dollars
	                 alpha=opacity,
	                 color='b',
	                 label='Revenue loss with 75% of dry year GW use')

	rects_50_af = plt.barh(index + bar_width, (curtailment_at_50_af_rev_loss / 1000000) , bar_width / 1.5,  # /1000000 for millions of dollars
	                 alpha=opacity,
	                 color='g',
	                 label='Revenue loss with 50% of dry year GW use')

	rects_20_af = plt.barh(index + 2 * bar_width, (curtailment_at_25_af_rev_loss / 1000000) , bar_width / 1.5,  # /1000000 for millions of dollars
	                 alpha=opacity,
	                 color='r',
	                 label='Revenue loss with 25% of dry year GW use')


	 
	# plt.ylabel('Irrigation District')
	plt.xlabel('Revenue loss, millions of dollars')
	plt.title('Economic Analysis of Revenue Loss for Irrigation Districts')
	plt.yticks(index + bar_width, (overall_ID_table.index))
	# pdb.set_trace()
	plt.legend()
	 
	plt.tight_layout()
	plt.show()


def plot_losses_as_percent_total_revenue():
	n_groups = len(overall_ID_table)

	# bars_in_group = len(overall_ID_table.columns) / 2   # number of clumps  

	baseline_curtailment_rev_loss = overall_ID_table.total_revenue_lost_baseline
	curtailment_at_75_af_rev_loss = overall_ID_table.total_revenue_lost_75 - baseline_curtailment_rev_loss
	curtailment_at_50_af_rev_loss = overall_ID_table.total_revenue_lost_50 - baseline_curtailment_rev_loss
	curtailment_at_25_af_rev_loss = overall_ID_table.total_revenue_lost_25 - baseline_curtailment_rev_loss


	# percentages 
	pdb.set_trace()
	percent_rev_loss_at_75 = curtailment_at_75_af_rev_loss / overall_ID_table.baseline_revenue * 100
	percent_rev_loss_at_50 = curtailment_at_50_af_rev_loss / overall_ID_table.baseline_revenue * 100
	percent_rev_loss_at_25 = curtailment_at_25_af_rev_loss / overall_ID_table.baseline_revenue * 100

	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
 
	rects_75_af = plt.barh(index + 2* bar_width, percent_rev_loss_at_75, bar_width / 1.5,   # percent of total ag revenue
	                 alpha=opacity,
	                 color='orange',
	                 label='Percent Revenue loss with 75% of dry year GW use')

	rects_50_af = plt.barh(index + bar_width, percent_rev_loss_at_50 , bar_width / 1.5,  # percent of total ag revenue
	                 alpha=opacity,
	                 color='r',
	                 label='Percent Revenue loss with 50% of dry year GW use')

	# rects_20_af = plt.barh(index, percent_rev_loss_at_25 , bar_width / 1.5,  # percent of total ag revenue
	#                  alpha=opacity,
	#                  color='r',
	#                  label='Percent Revenue loss with 25% of dry year GW use')


	 
	# plt.ylabel('Irrigation District')
	plt.xlabel('Percent revenue loss')
	plt.title('Economic Analysis of Revenue Loss for Irrigation Districts')
	plt.yticks(index + bar_width, (overall_ID_table.index))
	# pdb.set_trace()
	plt.legend()
	 
	plt.tight_layout()
	plt.show()






plot_dollar_losses()
plot_losses_as_percent_total_revenue()








pdb.set_trace()