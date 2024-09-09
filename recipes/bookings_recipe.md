## 1. Extract nouns from the user stories or specification




Nouns:






## 2. Infer the Table Name and Columns

| Record                | Properties        |
| --------------------- | ------------------|

| Bookings               | ID, date_booked, bookings_status, user_id, space_id

1. Name of the first table (always plural): `bookings` 

    Column names: `ID`, `date_booked`, `booking_status`, `user_id`, `space_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: bookings
id: SERIAL
date_booked: DATE
booking_status: BIT (boolean 1 for True 0 for False)
user_id: int
space_id: int



## 4. Decide on The Tables Relationship

N/A

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

N/A

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: bookings.sql

-- Replace the table name, columm names and types.





Table: bookings
id: SERIAL
date_booked: DATE
booking_status: VARCHAR(255) (boolean 1 for True 0 for False)
user_id: int
space_id: int


-- Then the table with the foreign key second.
CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  date_booked DATE,
  booking_status VARCHAR(255), 
  CONSTRAINT chk_booking_status CHECK (booking_status IN ('pending', 'confirmed'))

-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
-- The foreign key name is always {other_table_singular}_id
  space_id int,
  constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 bookings < bookings_table.sql
```