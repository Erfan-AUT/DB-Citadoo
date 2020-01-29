/* Relayed deleting old logs to the GUI system. */

CREATE TABLE "logs" (
  "change_type" varchar NOT NULL,
  "date" timestamp NOT NULL
);

CREATE TABLE "user_factors" (
  "id" SERIAL PRIMARY KEY,
  "user" varchar,
  "address" varchar,
  "delivery" varchar,
  "total_price" int DEFAULT 0,
  "date" timestamp NOT NULL
);

/* CREATE TABLE "user_factors_logs" (
  "id" PRIMARY KEY
); */

CREATE TABLE "user_factors_items" (
  "factor" int,
  "item" varchar NOT NULL,
  "price_per" int,
  "count" int,
  PRIMARY KEY ("factor", "item")
);

CREATE TABLE "human" (
  "ssn" varchar PRIMARY KEY,
  "name" varchar NOT NULL,
  "surname" varchar NOT NULL,
  "phone" varchar NOT NULL
);

CREATE TABLE "deliveries" (
) inherits ("human");

CREATE TABLE "customers" (
  "age" int NOT NULL
) inherits ("human");

CREATE TABLE "addresses" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "str" varchar NOT NULL,
  "phone" varchar NOT NULL
);

/* ‌Need to check if user's desired food exists in food items or not. */

CREATE TABLE "item" (
  "name" varchar PRIMARY KEY,
  "price" int
);

CREATE TABLE "store" (
  "name" varchar PRIMARY KEY,
  "is_active" boolean
);

CREATE TABLE "shopping_factor" (
  "id" int PRIMARY KEY,
  "store" varchar,
  "item" varchar NOT NULL,
  "price" int NOT NULL
);

ALTER TABLE "user_factors" ADD FOREIGN KEY ("user") REFERENCES "customers" ("ssn");

ALTER TABLE "user_factors" ADD FOREIGN KEY ("delivery") REFERENCES "deliveries" ("ssn");

ALTER TABLE "user_factors_logs" ADD FOREIGN KEY ("id") REFERENCES "user_factors" ("id");

ALTER TABLE "user_factors_items" ADD FOREIGN KEY ("factor") REFERENCES "user_factors" ("id");

ALTER TABLE "shopping_factor" ADD FOREIGN KEY ("store") REFERENCES "store" ("name");

ALTER TABLE "human" ADD (CONSTRAINT "iran_phone" CHECK ("phone" ~ $$^(\+98|0)?9\d{9}$$));
ALTER TABLE "human" ADD (CONSTRAINT "numeric_ssn" CHECK ("ssn" ~ $$^[0-9]+$$));