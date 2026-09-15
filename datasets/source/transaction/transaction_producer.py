import json
import time
import pandas as pd

from azure.eventhub import EventHubProducerClient, EventData
from azure.eventhub.exceptions import EventDataSendError


# ============================================
# CONFIGURATION
# ============================================

CONNECTION_STRING = "PASTE THE CONNECTION STRING HERE"

EVENT_HUB_NAME = "banking-transactions"

CSV_FILE = "TRANSACTION_MASTER.csv"


# ============================================
# BATCH CONFIGURATION
# ============================================

# Change this for each run
START_RECORD = 70000

RECORDS_TO_SEND = 30000

END_RECORD = START_RECORD + RECORDS_TO_SEND


# ============================================
# THROTTLING CONTROL
# ============================================

CHUNK_SIZE = 5000

DELAY_BETWEEN_CHUNKS = 1

MAX_RETRIES = 10


# ============================================
# CREATE PRODUCER
# ============================================

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING,
    eventhub_name=EVENT_HUB_NAME
)


# ============================================
# SEND BATCH WITH RETRY
# ============================================

def send_with_retry(batch):

    for retry in range(MAX_RETRIES):

        try:

            producer.send_batch(batch)

            return True

        except EventDataSendError:

            wait_time = 4 + retry

            print(
                f"Event Hub throttling detected. "
                f"Waiting {wait_time} seconds..."
            )

            time.sleep(wait_time)

    return False


# ============================================
# START PROCESSING
# ============================================

print("=" * 60)

print(
    f"Sending records {START_RECORD + 1:,} "
    f"to {END_RECORD:,}"
)

print("=" * 60)


records_read = 0
records_sent = 0


try:

    for chunk in pd.read_csv(
        CSV_FILE,
        dtype=str,
        chunksize=CHUNK_SIZE
    ):

        batch = producer.create_batch()


        for _, row in chunk.iterrows():

            # ----------------------------------------
            # Skip records before our required batch
            # ----------------------------------------

            if records_read < START_RECORD:

                records_read += 1

                continue


            # ----------------------------------------
            # Stop after reaching batch end
            # ----------------------------------------

            if records_read >= END_RECORD:

                break


            # ----------------------------------------
            # Convert record to JSON
            # ----------------------------------------

            message = json.dumps(
                row.to_dict()
            )


            event = EventData(message)


            # ----------------------------------------
            # Add to Event Hub batch
            # ----------------------------------------

            try:

                batch.add(event)


            except ValueError:

                # Batch reached size limit
                success = send_with_retry(batch)

                if not success:

                    raise RuntimeError(
                        "Failed to send Event Hub batch "
                        "after maximum retries."
                    )


                batch = producer.create_batch()

                batch.add(event)


            records_read += 1
            records_sent += 1


        # ========================================
        # SEND REMAINING EVENTS
        # ========================================

        if len(batch) > 0:

            success = send_with_retry(batch)

            if not success:

                raise RuntimeError(
                    "Failed to send Event Hub batch "
                    "after maximum retries."
                )


        # ========================================
        # PROGRESS
        # ========================================

        print(
            f"Records sent in this run: "
            f"{records_sent:,} / "
            f"{RECORDS_TO_SEND:,}"
        )


        # ========================================
        # THROTTLING PROTECTION
        # ========================================

        time.sleep(
            DELAY_BETWEEN_CHUNKS
        )


        # ========================================
        # STOP CONDITION
        # ========================================

        if records_read >= END_RECORD:

            break


finally:

    producer.close()


# ============================================
# COMPLETED
# ============================================

print("=" * 60)

print(
    f"Batch completed successfully."
)

print(
    f"Records sent: {records_sent:,}"
)

print("=" * 60)