from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

client = MongoClient(
    "172.28.1.3", port=27017, username="root", password="example", authSource="admin"
)
# client = MongoClient("mongodb://root:example@172.28.1.3/", 27017)
try:
    # The ismaster command is cheap and does not require auth.
    client.admin.command("ismaster")
    print("Database server connected")
except ConnectionFailure:
    print("Server not available")

db = client["projectfinder"]
msg = [data["title"] for data in db.itproject.find({})]


@app.route("/")
def index():
    print(len(msg))
    return msg[0]


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

