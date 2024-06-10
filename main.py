from fastapi import FastAPI, HTTPException
import random
import json
import math
import secrets
import string
import faker

app = FastAPI()


def generate_random_int(left: int = 0, right: int = math.inf) -> int:
    """Generate a random integer within the given range."""
    return random.randint(left, right)


@app.get("/")
def get_home() -> dict:
    """Return the API home page with available routes."""
    routes = {
        "/": "Description of the api",
        "/random": "Get a random float between 0 and 1.",
        "/random/int": "Get a random integer",
        "/random/range/{left}/{right}": "Get a random integer within the specified range.",
        "/random/char": "Get a random ASCII character.",
        "/random/coinflip": "Simulate a coin toss and get the result.",
        "/random/choice/{options}": "Select a random option from the given list.",
        "/random/color": "Select a random hex color.",
        "/random/user": "Generate a random user with name, email, and password.",
        "/random/password/{length}": "Generate a random password of a specified length.",
    }
    meta = {
        "api_version": "1.0",
        "docs": "https://github.com/MahirSalahin/random_api"
    }
    return {"routes": routes, "meta": meta}


@app.get("/random")
def get_root() -> dict:
    """Return a random float between 0 and 1."""
    return {"float": random.random()}


@app.get("random/int")
def get_random_int() -> dict:
    """Return a random integer."""
    return {"int": generate_random_int()}


@app.get("/random/range/{left}/{right}")
def get_random_in_range(left: int, right: int) -> dict:
    """Return a random integer within the given range."""
    if left > right:
        raise HTTPException(status_code=400, detail="Invalid range")
    return {"int": generate_random_int(left, right)}


@app.get("/random/char")
def generate_random_char() -> dict:
    """Get a random ASCII character."""
    return {"char": random.choice(string.ascii_letters)}


@app.get("/random/coinflip")
def toss_coin() -> dict:
    """Simulate a coin toss and return the result."""
    return {"result": random.choice(["Heads", "Tails"])}


@app.get("/random/choice/{options}")
def select_randomly(options: str) -> dict:
    """Select a random option from the given list."""
    options_list = json.loads(options)
    if not options_list:
        raise HTTPException(status_code=400, detail="Invalid options")
    return {"selected": random.choice(options_list)}


@app.get("/random/color")
def get_color() -> dict:
    """Select a random hex color."""
    hex_colors = [
        "#" + "".join([random.choice('0123456789ABCDEF') for _ in range(6)])]
    return {"color": hex_colors[0]}


@app.get("/random/user")
def generate_user() -> dict:
    """Generate a random user with name, email, and password."""
    fake = faker.Faker()
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=12)
    }
    return user


@app.get("/random/password/{length}")
def generate_password(length: int) -> dict:
    """Generate a random password of a specified length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return {"password": password}
