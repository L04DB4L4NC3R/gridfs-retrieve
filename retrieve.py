from pymongo import MongoClient
import gridfs
import base64
import sys
import bson
import json
import os.path

save_path = "./files"

fs_file = sys.argv[1]
fs_chunks = sys.argv[2]

db = MongoClient("YOUR_DB_URI").test
fs = gridfs.GridFS(db)


filemeta = []

with open(fs_file) as f:
  data = bson.decode_all(f.read())
for i in data:
    filemeta.append({"_id": i["_id"], "filename": i["filename"]})
    print(filemeta[-1])
    fileData = fs.get(i["_id"]).read()
    completeName = os.path.join(save_path, i["filename"])
    ff = open(completeName, "w")
    ff.write(fileData)
    ff.close()

