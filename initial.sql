
CREATE TABLE "log" (
  "id" SERIAL PRIMARY KEY,
  "changed_data" varchar NOT NULL,
  "changed_table" varchar NOT NULL,
  "changed_date" timestamp NOT NULL
);

CREATE TABLE "user_factor" (
  "id" SERIAL PRIMARY KEY,
  "user" varchar,
  "address" varchar,
  "delivery" varchar,
  "total_price" int DEFAULT 0,
  "date" timestamp NOT NULL
);

CREATE TABLE "user_factors_log" (
) inherits ("log");

CREATE TABLE "user_factors_item" (
  "id" SERIAL PRIMARY KEY,
  "factor" int NOT NULL,
  "item" varchar NOT NULL,
  "price_per" int NOT NULL,
  "count" int NOT NULL,
);

CREATE TABLE "user_factors_items_log" (
) inherits ("log");

CREATE TABLE "delivery" (
  "ssn" varchar PRIMARY KEY,
  "name" varchar NOT NULL,
  "surname" varchar NOT NULL,
  "phone" varchar NOT NULL
);

CREATE TABLE "delivery_log" (
) inherits ("log");

CREATE TABLE "customer" (
  "ssn" varchar PRIMARY KEY,
  "name" varchar NOT NULL,
  "surname" varchar NOT NULL,
  "phone" varchar NOT NULL,
  "age" int NOT NULL
);

CREATE TABLE "customer_log" (
) inherits ("log");

CREATE TABLE "address" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "address" varchar NOT NULL,
  "phone" varchar NOT NULL
);

CREATE TABLE "address_log" (
) inherits ("log");


CREATE TABLE "menu_food" (
  "name" varchar PRIMARY KEY,
  "price" int NOT NULL
);

CREATE TABLE "menu_food_log" (
) inherits ("log");

CREATE TABLE "store" (
  "name" varchar PRIMARY KEY,
  "is_active" boolean NOT NULL
);

CREATE TABLE "store_log" (
) inherits ("log");

CREATE TABLE "shopping_factor" (
  "id" int PRIMARY KEY,
  "store" varchar NOT NULL,
  "item" varchar NOT NULL,
  "price" int NOT NULL
);

CREATE TABLE "shopping_factor_log" (
) inherits ("log");

ALTER TABLE "user_factor" ADD FOREIGN KEY ("user") REFERENCES "customer" ("ssn") ON DELETE CASCADE;

ALTER TABLE "user_factor" ADD FOREIGN KEY ("delivery") REFERENCES "delivery" ("ssn");

ALTER TABLE "user_factors_item" ADD FOREIGN KEY ("factor") REFERENCES "user_factor" ("id");

ALTER TABLE "shopping_factor" ADD FOREIGN KEY ("store") REFERENCES "store" ("name");

CREATE PROCEDURE remove_old_log()
AS $$
BEGIN
    DELETE FROM "log"
    WHERE "changed_date" < now () - interval '3 days';
END;
$$
LANGUAGE plpgsql;

/*
Create trigger to disable store and disable it instead.
*/