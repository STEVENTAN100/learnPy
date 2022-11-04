def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _: #通配符，必定匹配成功
            return "Something's wrong with the internet"

#point is an (x,y) tuple
match point:
    case (0,0):
        print("Origin")
    case (0,y):
        print(f"Y={y}")
    case (x,0):
        print(f"X={x}")
    case (x,y):
        print(f"X={x},Y={y}")
    case _:
        raise ValueError("Not a point")

from enum import Enum
class Color(Enum):
    RED='red'
    GREEN='green'
    BLUE='blue'

color=Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

