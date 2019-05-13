import pymongo
host = "localhost"
port = 27017
online = "mongodb://root:root@cluster0-shard-00-00-npoou.mongodb.net:27017,cluster0-shard-00-01-npoou.mongodb.net:27017,cluster0-shard-00-02-npoou.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
client = pymongo.MongoClient(host , port)
db = client["whatsApp"]
userCol = db["users"]
messageCol = db["messages"]
