#!/bin/bash
source activate harbinger

# echo "Starting ..."
# python3 
# echo "Completed "

echo "Starting general_data_analysis_info.py..."
python3 general_data_analysis_info.py
echo "Completed general_data_analysis_info.py"

echo "Starting calculate_missing_values_percentages.py..."
python3 calculate_missing_values_percentages.py
echo "Completed calculate_missing_values_percentages.py"


echo "All scripts completed!"
