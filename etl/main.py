from prometheus_client import start_http_server, Summary, Counter
import time
from extract import extract_orders
from transform import transform_orders
from load import load_orders


ETL_DURATION = Summary("etl_duration_seconds", "Time spent running ETL job")
RECORDS_PROCESSED = Counter("records_processed_total", "Total number of records processed")

@ETL_DURATION.time()
def run_etl():
    data = extract_orders("data/sample_orders.csv")
    transformed = transform_orders(data)
    load_orders(transformed)
    RECORDS_PROCESSED.inc(len(transformed))

if __name__ == "__main__":
    start_http_server(8000)
    run_etl()
