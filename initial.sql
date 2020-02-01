
CREATE TABLE "log" (
  "id" SERIAL PRIMARY KEY,
  "changed_data" varchar NOT NULL,
  "change_type" varchar NOT NULL,
  "changed_date" timestamp NOT NULL
);

CREATE TABLE "user_factor" (
  "id" SERIAL PRIMARY KEY,
  "user" INT,
  "address" INT,
  "delivery" INT,
  "total_price" int NOT NULL DEFAULT 0,
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
  UNIQUE("factor", "item")
);

CREATE TABLE "user_factors_items_log" (
) inherits ("log");

CREATE TABLE "delivery" (
  "id" SERIAL PRIMARY KEY, 
  "ssn" varchar NOT NULL,
  "name" varchar NOT NULL,
  "surname" varchar NOT NULL,
  "phone" varchar NOT NULL,
  UNIQUE("ssn")
);

CREATE TABLE "delivery_log" (
) inherits ("log");

CREATE TABLE "customer" (
  "id" SERIAL PRIMARY KEY, 
  "ssn" varchar NOT NULL,
  "name" varchar NOT NULL,
  "surname" varchar NOT NULL,
  "phone" varchar NOT NULL,
  "age" INT NOT NULL,
  UNIQUE("ssn")
);

CREATE TABLE "customer_log" (
) inherits ("log");

CREATE TABLE "address" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "address" varchar NOT NULL,
  "phone" varchar NOT NULL,
  "user" INT NOT NULL
);

CREATE TABLE "address_log" (
) inherits ("log");


CREATE TABLE "menu_food" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "price" int NOT NULL,
  UNIQUE("name")
);

CREATE TABLE "menu_food_log" (
) inherits ("log");

CREATE TABLE "store" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "is_active" boolean NOT NULL DEFAULT TRUE,
  UNIQUE("name")
);

CREATE TABLE "store_log" (
) inherits ("log");

CREATE TABLE "shopping_factor" (
  "id" SERIAL PRIMARY KEY,
  "store" INT NOT NULL,
  "item" varchar NOT NULL,
  "price" int NOT NULL,
  "date" timestamp NOT NULL
);

CREATE TABLE "shopping_factor_log" (
) inherits ("log");

ALTER TABLE "user_factor" ADD FOREIGN KEY ("user") REFERENCES "customer" ("id") ON DELETE CASCADE;

ALTER TABLE "user_factor" ADD FOREIGN KEY ("delivery") REFERENCES "delivery" ("id") ON DELETE SET NULL;

ALTER TABLE "user_factor" ADD FOREIGN KEY ("address") REFERENCES "address" ("id") ON DELETE SET NULL;

ALTER TABLE "address" ADD FOREIGN KEY ("user") REFERENCES "customer" ("id") ON DELETE CASCADE;

ALTER TABLE "user_factors_item" ADD FOREIGN KEY ("factor") REFERENCES "user_factor" ("id") ON DELETE CASCADE;

ALTER TABLE "shopping_factor" ADD FOREIGN KEY ("store") REFERENCES "store" ("id");

CREATE PROCEDURE remove_old_logs()
AS $$
BEGIN
    DELETE FROM "log"
    WHERE "changed_date" < now () - interval '3 days';
END;
$$
LANGUAGE plpgsql;
