#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)

# 1. Create Algo Order
try:
    response = um_futures_client.new_algo_order(
        symbol="BTCUSDT",
        side="BUY",
        type="STOP_MARKET",
        quantity="0.001",
        triggerPrice="60000",
        positionSide="BOTH"
    )
    logging.info(response)
    # Save the returned algo order ID for subsequent operations
    algo_order_id = response.get("algoid")
    client_algo_id = response.get("clientAlgoId")
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# 2. Cancel Algo Order
try:
    response = um_futures_client.cancel_algo_order(
        algoid=algo_order_id  # Or use clientalgoid=client_algo_id
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# 3. Cancel All Algo Orders
try:
    response = um_futures_client.cancel_all_algo_open_orders(
        symbol="BTCUSDT"
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# 4. Query Algo Order
try:
    response = um_futures_client.query_algo_order(
        algoid=algo_order_id  # Or use clientAlgoId=client_algo_id
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# 5. Get All Algo Open Orders
try:
    response = um_futures_client.get_all_algo_open_orders(
        symbol="BTCUSDT"  # Optional parameter, query all symbols if not specified
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# 6. Query All Algo Orders
try:
    response = um_futures_client.query_all_algo_orders(
        symbol="BTCUSDT"  # Optional parameter, query all symbols if not specified
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
