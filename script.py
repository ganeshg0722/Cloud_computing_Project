import pandas as pd
import tensorflow_decision_forests as tfdf
import numpy as np


def predict_sale_price(desired_id, train_file_path, test_file_path):
    dataset_df = pd.read_csv(train_file_path)
    dataset_df = dataset_df.drop('Id', axis=1)

    train_ds_pd, valid_ds_pd = split_dataset(dataset_df)
    label = 'SalePrice'
    train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=label, task=tfdf.keras.Task.REGRESSION)
    valid_ds = tfdf.keras.pd_dataframe_to_tf_dataset(valid_ds_pd, label=label, task=tfdf.keras.Task.REGRESSION)

    rf = tfdf.keras.RandomForestModel(task=tfdf.keras.Task.REGRESSION)
    rf.compile(metrics=["mse"])
    rf.fit(x=train_ds)

    test_data = pd.read_csv(test_file_path)
    desired_row = test_data[test_data['Id'] == desired_id]
    if not desired_row.empty:
        features_for_prediction = desired_row.drop('Id', axis=1)
        predicted_price = rf.predict(tfdf.keras.pd_dataframe_to_tf_dataset(
            features_for_prediction, task=tfdf.keras.Task.REGRESSION)).squeeze()
        return predicted_price
    else:
        return f"No data found for ID {desired_id}"

def split_dataset(dataset, test_ratio=0.30):
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]