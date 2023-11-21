# Introduction

Analyzing stock tick data in SingleStoreDB using LangChain and OpenAI's Whisper. Following this, we aim to build GenAI Text-to-Speech Apps.

# Loading data
- [load_stock_tick_data_from_kafka_into_singlestoredb](notebook/load_stock_tick_data_from_kafka_into_singlestoredb.ipynb)

# Analysing data
- [quick_tip_analysing_stock_tick_data_in_singlestoredb_using_langchain](notebook/quick_tip_analysing_stock_tick_data_in_singlestoredb_using_langchain.ipynb)

# Setting
```
cd python
bash install.sh
python3 -m venv env
source env/bin/activate
```
# Running
```
python3 record-transcribe.py
```
![Alt text](python/data/record-transcribe.png)

```
python3 record-transcribe-visualise.py
```
![Alt text](python/data/record-transcribe-visualise.png)


```
python3 record-transcribe-visualise-speak.py
```
![Alt text](python/data/record-transcribe-visualise-speak.png)


# References
[Quick tip: Analysing Stock Tick Data in SingleStoreDB using LangChain and OpenAI's Whisper](https://medium.com/@VeryFatBoy/quick-tip-analysing-stock-tick-data-in-singlestoredb-using-langchain-and-openais-whisper-5c5516fc0443)