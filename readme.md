# Data Forest - Backend

Data forest is a web app designed to ease the management of a real forest by providing data analysis regarding trees populating the forest.

This backend part allows the input of new data and provides statistics that would be visualized in the frontend app.

It is built on the Django Rest Framework and uses Pandas for data processing.



## API endpoints:

#### GET /seeds
Generates a new random forest and populates with a maximum of 10 000 trees. 
It should return the id of the newly created forest.

#### POST /analytics
Returns a pivot table containing trees related data. The table is generated according the specified parameters:
- forest_id: the id of the forest to select, must be a number.
- columns: the type of data that would be used as columns in the pivot table. 
Accepted value are "species", "area", "age", "size", "state", "alive".
- rows: the type of data that would be used as rows in the pivot table. 
Accepted value are "species", "area", "age", "size", "state", "alive".

### REST API
#### GET | POST | UPDATE | DELETE /forests/<id?>
#### GET | POST | UPDATE | DELETE /trees/<id?>
#### GET | POST | UPDATE | DELETE /events/<id?>


