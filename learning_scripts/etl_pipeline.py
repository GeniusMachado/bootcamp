import time

# In a real job, you would import these:
# from airflow import DAG
# from airflow.operators.python import PythonOperator

def extract_from_kafka():
    print("[Task 1] Extracting data from Kafka topic 'user-clicks'...")
    time.sleep(1)
    print(" -> Extracted 5,000 records.")
    return "raw_data.json"

def transform_with_glue(file_name):
    print(f"[Task 2] Triggering AWS Glue job for {file_name}...")
    # Simulation of cleaning data
    time.sleep(1)
    print(" -> Cleaning data... Removing duplicates...")
    print(" -> Transformation complete.")
    return "clean_data.csv"

def load_into_redshift(file_name):
    print(f"[Task 3] Loading {file_name} into AWS Redshift...")
    time.sleep(1)
    print(" -> COPY command executed.")
    print(" -> Data is now live in the Analytics Dashboard.")

# This function simulates what Airflow does: ensuring Order of Operations
def run_airflow_dag():
    print("--- AIRFLOW SCHEDULER STARTING ---")

    try:
        # Step 1
        raw_file = extract_from_kafka()

        # Step 2 (Only runs if Step 1 succeeds)
        clean_file = transform_with_glue(raw_file)

        # Step 3 (Only runs if Step 2 succeeds)
        load_into_redshift(clean_file)

        print("--- DAG COMPLETED SUCCESSFULLY ---")

    except Exception as e:
        print(f"!!! DAG FAILED: {e} !!!")
        print("Sending Alert to PagerDuty...")

if __name__ == "__main__":
    run_airflow_dag()
