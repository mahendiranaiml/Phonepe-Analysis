import pandas as pd
import glob
import os

def merge_csv_files(input_dir, output_file):
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
    
    # We want to exclude the output file just in case it already exists
    csv_files = [f for f in csv_files if os.path.basename(f) != output_file]
    
    print(f"Found {len(csv_files)} CSV files to merge.")
    
    dfs = []
    for file in csv_files:
        print(f"Reading {os.path.basename(file)}...")
        df = pd.read_csv(file)
        # Add a column to identify the source file if it doesn't already exist or to be explicit
        df['origin_csv'] = os.path.basename(file)
        dfs.append(df)
        
    print("Concatenating all dataframes...")
    combined_df = pd.concat(dfs, axis=0, ignore_index=True, sort=False)
    
    print(f"Total rows in combined file: {len(combined_df)}")
    print(f"Total columns in combined file: {len(combined_df.columns)}")
    
    print(f"Saving to {output_file}...")
    out_path = os.path.join(input_dir, output_file)
    combined_df.to_csv(out_path, index=False)
    print(f"Done! File saved to {out_path}")

if __name__ == "__main__":
    input_directory = "."
    output_filename = "master_phonepe_data.csv"
    merge_csv_files(input_directory, output_filename)
