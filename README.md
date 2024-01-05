# WineQuality-Prediction-Using-MLOPS---II

# Procedure of Creating a Environment

<!-- pip install virtualenv (if not installed)

virtualenv myenv  # Replace "myenv" with the name you want for your environment -->


# environment = wineq_env
# Activate the env by pasting this on gitbash => source wineq_env/Scripts/activate 

# __init__.py -> This file is everywhere in folders as we are using those folders as local packages and in order to import that we have to create __init__.py

# utils are the functions that we use in our code frequently

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml