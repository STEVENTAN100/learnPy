from json import JSONEncoder
import json

person = {"name": "John", "age": 30, "city": "New York",
          "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# convert back
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

# customize encode


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


def encode_user(o):
    if isinstance(o, User):
        # trick of class name
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, default=encode_user)
userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

# decode


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name, user.age)
