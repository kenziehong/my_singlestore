import os
import openai

s2_password = ""
s2_host = ""
s2_db = "timeseries_db"
os.environ["OPENAI_API_KEY"] = ""
openai.api_key = os.environ["OPENAI_API_KEY"]