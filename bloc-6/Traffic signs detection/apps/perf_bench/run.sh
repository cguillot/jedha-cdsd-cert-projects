#!/bin/bash
set -e

source /opt/conda/etc/profile.d/conda.sh
conda activate docker-env


#if [ $var -gt 0 -a $var -lt 10 ]
if [ -n "$1" -a $1 = "dev" ]; then
    echo 'Running dev mode...'
    exec streamlit run --browser.gatherUsageStats false --server.port 7866 --server.address "0.0.0.0" --server.fileWatcherType poll --server.runOnSave true src/model-tester/main.py
else
    echo 'Running production mode...'
    exec streamlit run --browser.gatherUsageStats false --server.port $SERVER_PORT --server.enableXsrfProtection false --server.enableCORS false src/model-tester/main.py
fi

#exec streamlit run --browser.gatherUsageStats false --server.port $SERVER_PORT src/model-tester/main.py

