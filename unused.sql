/* CREATE OR REPLACE FUNCTION add_logs (_tbl regclass, action_type varchar                       ) AS 
        RETURNS TRIGGER AS
$BODY$
BEGIN
    select array_to_string(avals(hstore(_tbl)), ', ')
    into rowString from OLD;
    select concat (_tbl, "_logs") into log_table_name;
    insert into log_table_name values ()
END
$BODY$

CREATE TRIGGER logs_trigger
 */

 /* 
put this in a loop for deleting more than 3 days old logs.

ALTER TABLE measurement DETACH PARTITION measurement_y2006m02;
 */

 /*
 phone number and ssn moved to backend because it didn't work!
 */


/*  ALTER TABLE "customers" ADD (CONSTRAINT "iran_phone" CHECK ("phone" ~* $$^(\+98|0)?9\d{9}$$));
ALTER TABLE "customers" ADD (CONSTRAINT "numeric_ssn" CHECK ("ssn" ~ $$^[0-9]+$$));

ALTER TABLE "deliveries" ADD (CONSTRAINT "iran_phone" CHECK ("phone" ~* $$^(\+98|0)?9\d{9}$$));
ALTER TABLE "deliveries" ADD (CONSTRAINT "numeric_ssn" CHECK ("ssn" ~ $$^[0-9]+$$));
 */

/*  CREATE FUNCTION valid_food()
    RETURNS TRIGGER AS
$BODY$
BEGIN  
    SELECT name into food_list from "menu_foods"; 
    IF NEW.name NOT IN food_list then
        RAISE EXCEPTION 'foods not in the menu';
    END IF;
END;
language plpgsql;
$BODY$

CREATE TRIGGER "no_invalid_food"
    BEFORE INSERT 
    ON "user_factors_items"
    FOR EACH ROW 
    EXECUTE PROCEDURE valid_food();

 */