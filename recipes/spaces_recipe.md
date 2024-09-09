## 1. Extract nouns from the user stories or specification

As a user, when I create a space I want to be able to give it a name, a description and it’s price per night


Nouns:


## 2. Infer the Table Name and Columns

| Record                | Properties        |
| --------------------- | ------------------|
| space                 | name, description, price, user_id
| user


Table name: 'spaces'
Column names: name, description, price, user_id

Table name 'users'

## 3. Decide the column types
Spaces:

id: SERIAL
name: VARCHAR(255)
description: VARCHAR(255)
price: DECIMAL(10, 2)
user_id: int

Users:
id: SERIAL
name: VARCHAR(255)
email: VARCHAR(255)
password: VARCHAR(255)

## 4. Decide on The Tables Relationship

1. Can one space have many users? NO
2. Can one user have many spaces? YES

Therefore,

A user HAS MANY spaces
A space BELONGS TO a user

Therefore, the foreign key is on the spaces table.


## 5. Write the SQL
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
);
```
-- Then the table with the foreign key second.
```sql
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,`
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(10, 2),
    
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);
```

## 6. Create the tables

```bash
psql -h 127.0.0.1 makers_bnb_air_db < seeds/spaces_test.sql