## SQL for new table:
```sh
CREATE TABLE people (
    'ID' INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY, 
    'Name' TEXT NOT NULL,
    'Age' INTEGER NOT NULL,
    'Address' TEXT
) PRIMARY KEY (ID);
```
_GENERATED ALWAYS AS IDENTITY - is optional._