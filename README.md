# Pizza Restaurant API Challenge

A RESTful API for managing a pizza restaurant, built with Flask and SQLAlchemy.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JosephNgugi254/pizza-api-challenge.git
cd pizza-api-challenge
```

### 2. Set Up Virtual Environment

```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

### 3. Initialize the Database

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Seed the Database

```bash
python3 -m server.seed
```

### 5. Run the Application

```bash
flask run
```

The server runs at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Endpoints

| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/restaurants`            | List all restaurants               |
| GET    | `/restaurants/<id>`       | Get a restaurant and its pizzas    |
| DELETE | `/restaurants/<id>`       | Delete a restaurant and its pizzas |
| GET    | `/pizzas`                 | List all pizzas                    |
| POST   | `/restaurant_pizzas`      | Create a restaurant-pizza association |

