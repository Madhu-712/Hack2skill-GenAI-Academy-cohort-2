import json
import pandas as pd
import requests

# --- CONFIGURATION ---
PROJECT_ID = "notebooklm-491108"
DATASET_ID = "your_legal_dataset"
TABLE_ID = "strova_direct_import"
HF_DATA_URL = "https://huggingface.co/datasets/strova-ai/legal_contract_dataset/resolve/main/legal-contract%20(2).jsonl"

def upload_hf_to_bigquery():
    print("Step 1: Fetching Strova dataset from Hugging Face via direct HTTP download...")
    try:
        response = requests.get(HF_DATA_URL)
        response.raise_for_status() 
        
        # Robust parsing: split lines, strip carriage returns (\r), and skip blank elements
        raw_lines = response.text.split('\n')
        data_dicts = []
        
        for line in raw_lines:
            cleaned_line = line.strip()
            if cleaned_line: # Skips empty lines completely
                data_dicts.append(json.loads(cleaned_line))
                
        print(f"Successfully downloaded and verified {len(data_dicts)} records.")
    except Exception as e:
        print(f"Error downloading file: {e}")
        return

    print("\nStep 2: Converting dataset to a structured DataFrame...")
    df = pd.DataFrame(data_dicts)
    
    # Check if df is truly empty before proceeding
    if df.empty:
        print("Error: DataFrame is empty after parsing data.")
        return
    else:
        print(f"DataFrame loaded with shapes: {df.shape}")

    print("\nStep 3: Processing and sanitizing column data types...")
    # Because BigQuery struggles with lists of dicts natively passed from pandas,
    # we convert 'messages' or any nested objects into a strict valid JSON string.
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if elements are actually nested objects (like arrays/lists/dicts)
            sample_elements = df[col].dropna()
            if not sample_elements.empty and isinstance(sample_elements.iloc[0], (dict, list)):
                print(f" -> Converting nested array/object column '{col}' to a clear JSON string...")
                df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x)

    destination_table = f"{DATASET_ID}.{TABLE_ID}"
    print(f"\nStep 4: Uploading data directly to BigQuery table: {destination_table}...")
    
    try:
        import pandas_gbq
        
        # We enforce a chunksize and check for chunk validation
        pandas_gbq.to_gbq(
            df,
            destination_table=destination_table,
            project_id=PROJECT_ID,
            if_exists='replace',
            chunksize=1000, # Push data in chunks to prevent memory/buffer overflow
            progress_bar=True
        )
        print("\nSuccess! The data is now a permanent table in your BigQuery dataset with populated rows.")
        
    except Exception as e:
        print(f"\nFailed to write to BigQuery: {e}")

if __name__ == "__main__":
    upload_hf_to_bigquery()