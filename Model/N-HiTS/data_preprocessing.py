import argparse
import os
import pandas as pd

def read_dataset(dataset_name):
    file_path = './data/Raw_Stock_Data/Data_01_03_2019'
    full_file_path = os.path.join(file_path, f'{dataset_name}.csv')
    assert os.path.exists(full_file_path), f"File '{dataset_name}.csv' does not exist."
    return pd.read_csv(full_file_path)

def save_processed_data(dataset_name, data):
    processed_path = f'./data/{dataset_name}/'
    os.makedirs(processed_path, exist_ok=True)
    output_file = os.path.join(processed_path, 'df_y.csv')
    with open(output_file, 'w') as f:
        data.to_csv(f, index=False)

def process_data(stock_data):
    df = pd.DataFrame({
        'ds': pd.to_datetime(stock_data['Date']),
        'unique_id': 1,
        'y': stock_data['Close']
    })

    df.sort_values(by=['ds'], inplace=True, ascending=True)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # handle missing data
    start_date = df['ds'].min()
    end_date = df['ds'].max()
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    filtered_dates = [date for date in date_range if date.weekday() < 5]  # 0-4: Monday-Friday
    full_date = pd.DataFrame({'ds': filtered_dates})

    df = pd.merge(full_date,df,on='ds',how='left')
    df.ffill(inplace=True)

    return df

def main(args):
    dataset_names = args.dataset_names

    for dataset_name in dataset_names:
        # read data
        stock_data = read_dataset(dataset_name)
        processed_data = process_data(stock_data)

        # save data
        save_processed_data(dataset_name, processed_data)
        print(f'./data/{dataset_name}/df_y.csv')

def parse_args():
    desc = "Data Preprocessing"
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('--dataset_name', type=str, help='Dataset name (CSV)')
    parser.add_argument('--dataset_names', nargs='+', type=str, help='Dataset names (CSV)')
    return parser.parse_args()

if __name__ == '__main__':

    # parse arguments
    args = parse_args()
    if args is None:
        exit()

    main(args)