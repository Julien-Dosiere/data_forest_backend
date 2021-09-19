# Data Forest - Backend

Data forest is a web app designed to ease the management of a real forest by providing data analysis regarding trees populating the forest.

This backend part allows the input of new data and provides statistics that would be visualized in the frontend app.

It is built on the Django Rest Framework and uses Pandas for data processing.

Deployed version (with frontend app) available __[here](https://data-forest-e79ed.web.app/)__


## API endpoints:

#### GET /admin
Access to Django admin interface (for deployed version username: admin, password: password)

#### POST /seeds
Generates a new random forest and populates with a maximum of 10 000 trees. 
Requires a "name" parameter (form-data) to set the newly generated forest name.
It should return the id of the newly created forest.

#### GET /drop
Delete all forests, destroying all associated data.

#### POST /analytics
Returns a pivot table containing trees related data. The table is generated according the specified parameters (form-data):
- forest_id: the id of the forest to select, must be a number.
- columns: the type of data that would be used as columns in the pivot table. 
Accepted value are "species", "area", "age", "size", "state", "alive".
- rows: the type of data that would be used as rows in the pivot table. 
Accepted value are "species", "area", "age", "size", "state", "alive".
- format: the format of the return pivot table. 
Accepted value is "html", default is json.


### REST API
#### GET | POST | UPDATE | DELETE /forests/<id?>
#### GET | POST | UPDATE | DELETE /trees/<id?>
#### GET | POST | UPDATE | DELETE /events/<id?>


