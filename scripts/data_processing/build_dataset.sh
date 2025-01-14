#!/bin/bash
source activate harbinger

echo "Starting reformat_arizona_cm_dataset.py..."
python3 reformat_arizona_cm_dataset.py
echo "Completed reformat_arizona_cm_dataset.py"

echo "Starting reformat_arizona_met_dataset.py..."
python3 reformat_arizona_met_dataset.py
echo "Completed reformat_arizona_met_dataset.py"

echo "Starting reformat_arizona_pop_estimates.py..."
python3 reformat_arizona_pop_estimates.py
echo "Completed reformat_arizona_pop_estimates.py"

# echo "Starting combine_arizona_cm_and_met.py..."
# python3 combine_arizona_cm_and_met.py
# echo "Completed combine_arizona_cm_and_met.py"

# echo "Starting combine_arizona_cmmet_and_rates.py..."
# python3 combine_arizona_cmmet_and_rates.py
# echo "Completed combine_arizona_cmmet_and_rates.py"

echo "Starting reformat_cali_cm_dataset.py..."
python3 reformat_cali_cm_dataset.py
echo "Completed reformat_cali_cm_dataset.py"

echo "Starting reformat_cali_met_dataset.py..."
python3 reformat_cali_met_dataset.py
echo "Completed reformat_cali_met_dataset.py"

echo "Starting reformat_cali_pop_estimates.py..."
python3 reformat_cali_pop_estimates.py
echo "Completed reformat_cali_pop_estimates.py"

# echo "Starting combine_cali_cm_and_met.py..."
# python3 combine_cali_cm_and_met.py
# echo "Completed combine_cali_cm_and_met.py"

# echo "Starting combine_cali_cmmet_and_cases.py..."
# python3 combine_cali_cmmet_and_cases.py
# echo "Completed combine_cali_cmmet_and_cases.py"

echo "Starting reformat_cali_pesticides_dataset.py.py..."
python3 reformat_cali_pesticides_dataset.py.py
echo "Completed reformat_cali_pesticides_dataset.py.py"

echo "All scripts completed!"
