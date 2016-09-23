import sqlite3

class Database():

    class __Database():

        def __init__(self):
            self.connection = sqlite3.connect('data.db')
            self.cursor = self.connection.cursor()

        def query(self, query, sequence=None):
            if sequence == None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, sequence)
            self.connection.commit()

        def fetch_one(self):
            return self.cursor.fetchone()

        def fetch_all(self):
            return self.cursor.fetchall()
            

    instance = None

    def __new__(cls):
        if Database.instance == None:
            Database.instance = Database.__Database()
        return Database.instance

    def __getattr__(self, name):
        return getattr(Database.instance, name)

    def __setattr__(self, name):
        return setattr(Database.instance, name)

