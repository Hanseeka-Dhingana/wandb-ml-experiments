import wandb
run = wandb.init()
artifact = run.use_artifact('hanseeka-dhingana-sukkur-iba-university/sklearn-iris/random_forest_iris_model:v0', type='model')
artifact_dir = artifact.download()