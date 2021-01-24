from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields
from bson.objectid import ObjectId


class Transcriptions(MongoModel):
    _id = fields.ObjectIdField(primary_key=True, default=ObjectId)
    transcription = fields.CharField()
    createdAt = fields.DateTimeField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'FirstSource'
