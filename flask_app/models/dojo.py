from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        # Retrieve all dojos from the database
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create a Dojo object for each result and return the list of Dojo objects
        return [cls(d) for d in results]

    @classmethod
    def save(cls, data):
        # Save a new dojo to the database
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data):
        # Retrieve a dojo with its associated ninjas from the database
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            # Create a Ninja object for each associated ninja and add it to the dojo's ninjas list
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo
