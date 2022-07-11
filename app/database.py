from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.notes

collection = db.notes



class Data:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.notes
        self.collection = self.db.notes


    def get_all_by_username(self,username:str):

        res = self.collection.find_one({"username": username},{'_id':0,'password':0})
        return res



 #   def create_account(self,username:str,email:str,password:str):




  #  def delete_account(self,username,password):




  #  def get_notes(self,username,password):




   # def create_notes(self,username,password):




