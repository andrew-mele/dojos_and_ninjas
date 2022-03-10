from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
    
    @classmethod #select all 
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod #select one
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod #create one
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod #update one
    def update(cls, data):
        query = "UPDATE dojos SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod #delete one
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)