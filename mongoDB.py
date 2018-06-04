import pymongo



def readFromMongoDB(_dataBaseName, _tableName, ID):
    
    ID = int(ID)
    client = MongoClient(CONNSTRING)
    mydb = client[_dataBaseName]
    qry = {"ID": ID}
    obj = mydb[_tableName].find_one(qry,{'_id': False}) # the second parameter {'_id': False} causes the objectID not to be returned
    #print('Mongo obj:', obj)
    client.close()
    return obj

def writeToMongoDB(_dataBaseName, _tableName, ID, value):

    ID = int(ID)
    #client = pymongo.MongoClient(CONNSTRING)
    client = MongoClient(CONNSTRING)

    # Connect to DB:
    # mydb = client.heroku_dgltjp2d
    mydb = client[_dataBaseName]

    obj = json.loads(value)

    doc = { "ID":ID, "value" : obj }
    
    
    # if this ID doesnt exist yet, insert a new one
    #mydb[_tableName].insert_one(doc)
    
    # if this ID already exists, we will need to update it with a new value
    # mycollection.update({'_id':mongo_id}, {"$set": post}, upsert=False)
    mydb[_tableName].update({ 'ID':ID }, doc, upsert=True )
    
    client.close()

    return