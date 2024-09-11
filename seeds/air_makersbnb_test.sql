DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  email text,
  password text
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(10, 2),
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date_booked DATE,
    booking_status VARCHAR(255), 
    CONSTRAINT chk_booking_status CHECK (booking_status IN ('pending', 'confirmed')),

    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade,

    space_id int,
    constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
);

INSERT INTO users (username, email, password) VALUES ('Sam', 'sam@example.com', '5751a44782594819e4cb8aa27c2c9d87a420af82bc6a5a05bc7f19c3bb00452b');
-- original password before is password123! 
INSERT INTO users (username, email, password) VALUES ('Rob', 'rob@example.com', '588de65968beb9699bca6d4c59e842fedd42715fa25ca72751eab4c200986f89');
-- original password before is password45%6
INSERT INTO users (username, email, password) VALUES ('Alex', 'alex@example.com', '6df39f96b4be04ab9fb801b461967c5b4761b92af7624af4901c08ae49fbd1e3');
-- original password before is password£7£89 
INSERT INTO users (username, email, password) VALUES ('Avnita', 'avnita@example.com', '31a99a735d4a59d1d15e9cc7e992401c169ae01115550c1348a2ce00c46d7ef5');
-- original password before is passwor$d321
INSERT INTO users (username, email, password) VALUES ('Tom', 'tom@example.com', 'ae62d1f9b0d68b63cb4e6a6e2fa7594578c8fd95325195055b812f0259e67c60');
-- original password before is password65^4
INSERT INTO users (username, email, password) VALUES ('Khari', 'khari@example.com', '038ad83b9e0dbc76bfefdce8b037e00aef5a5337cf6466763d412c621dd08250');
-- original password before is passwo!r^^d987

INSERT INTO spaces (name, description, price, user_id) VALUES ('Cozy Apartment', 'A small, comfortable apartment in the city center', 120, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Modern Office', 'A sleek office space with a view', 250, 4);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Warehouse', 'Spacious warehouse near the docks', 300.00, 3);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Studio Loft', 'An open loft with lots of natural light', 150.00, 5);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Private Office', 'A compact office space for individual work', 18.00, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Garden Den', 'A shed in my garden', 180.00, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Cupboard', 'A crappy cupboard underneath the stairs', 150.00, 2);

INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES ('2024-09-25', 'confirmed', 1, 3);
INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES ('2024-11-23', 'confirmed', 1, 5);
INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES ('2025-09-20', 'pending', 2, 1);
INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES ('2024-10-15', 'pending', 2, 4);
INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES ('2024-12-30', 'pending', 1, 2);