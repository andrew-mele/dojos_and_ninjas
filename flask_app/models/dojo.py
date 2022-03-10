from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
    @classmethod #select all
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos


    @classmethod #select one
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod #create one
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod #selecting one ninja of the associated Dojo
    def get_one_dojo_all_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo

    @classmethod #update one
    def update(cls, data):
        query = "UPDATE dojos SET name=%(name)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod #delete one
    def update(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)