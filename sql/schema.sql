-- EEData Schema

-- Represents users that have created an account
CREATE TABLE "users" (
    "id" INTEGER,
    "username" TEXT NOT NULL UNIQUE,
    "email" TEXT NOT NULL,
    "address" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "date_account_created" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    "date_last_login" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    "date_recent_login" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id")
);

-- Represents items that have been listed for sale
CREATE TABLE "items" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "price" NUMERIC NOT NULL,
    "shipping_price" NUMERIC NOT NULL,
    "description_length" INTEGER NOT NULL,
    "reviews" INTEGER NOT NULL,
    "product_images" INTEGER NOT NULL,
    "product_videos" INTEGER NOT NULL,
    "advertisement" NUMERIC NOT NULL,
    "date_listed" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id")
);

-- Represents carts that users create after selecting an item
CREATE TABLE "carts" (
    "id" INTEGER,
    "user_id" INTEGER,
    "item_id" INTEGER,
    "date_created" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    "date_cart_transition" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    "became_order" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("item_id") REFERENCES "items"("id")
);

-- Represents orders of carts
CREATE TABLE "orders" (
    "id" INTEGER,
    "cart_id" INTEGER,
    "item_quantity" INTEGER NOT NULL,
    "total_amount" NUMERIC NOT NULL,
    "date_placed" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    "order_status" TEXT NOT NULL,
    "date_order_status" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id"),
    FOREIGN KEY("cart_id") REFERENCES "carts"("id")
);

-- Represents returns that have been made from orders
CREATE TABLE "returns" (
    "id" INTEGER,
    "order_id" INTEGER,
    "reason" TEXT NOT NULL,
    "date_returned" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("id")
);

-- Represents the account a user has deleted
CREATE TABLE "deleted_accounts" (
    "id" INTEGER,
    "username" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "address" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "date_deleted" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id")
);

-- Represents items that had their listing deleted
CREATE TABLE "deleted_items" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "price" NUMERIC NOT NULL,
    "shipping_price" NUMERIC NOT NULL,
    "description_length" INTEGER NOT NULL,
    "reviews" INTEGER NOT NULL,
    "product_images" INTEGER NOT NULL,
    "product_videos" INTEGER NOT NULL,
    "advertisement" NUMERIC NOT NULL,
    "date_listed" NUMERIC NOT NULL,
    "date_deleted" NUMERIC NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY("id")
);

-- Create trigger for moving deleted user accounts into the deleted_accounts table
CREATE TRIGGER "remove_user_account"
BEFORE DELETE ON "users"
FOR EACH ROW
BEGIN
    INSERT INTO "deleted_accounts"("username","email","address","state")
    VALUES (OLD."username", OLD."email", OLD."address", OLD."state");
END;

-- Create trigger for moving deleted items into the deleted_items table
CREATE TRIGGER "remove_item"
BEFORE DELETE ON "items"
FOR EACH ROW
BEGIN
    INSERT INTO "deleted_items"("name","type","price","shipping_price","description_length","reviews","product_images","product_videos","advertisement","date_listed")
    VALUES (OLD."name",OLD."type",OLD."price",OLD."shipping_price",OLD."description_length",OLD."reviews",OLD."product_images",OLD.product_videos,OLD."advertisement",OLD."date_listed");
END;

-- Create view for tracking key performance indicators
CREATE VIEW "order_statistics" AS 
SELECT
    "items"."name",
    "items"."type",
    ROUND(AVG("orders"."item_quantity"),0) AS "Average Quantity Ordered",
    MIN("orders"."item_quantity") AS "Minimum Quantity Ordered",
    MAX("orders"."item_quantity") AS "Maximum Quantity Ordered",
    ROUND(AVG("orders"."total_amount"),0) AS "Average Total Amount",
    MIN("orders"."total_amount") AS "Minimum Total Amount",
    MAX("orders"."total_amount") AS "Maximum Total Amount"
FROM "orders"
JOIN "carts" ON "orders"."cart_id" = "carts"."id"
JOIN "items" ON "carts"."item_id" = "items"."id"
WHERE "orders"."date_placed" = '2025-03-21'
GROUP BY "items"."name"
ORDER BY "items"."type";

-- Create view to access the dates when items were listed and how many users purchased items on the first day of March
CREATE VIEW "duration_items_listed" AS 
SELECT
    "items"."name",
    "items"."date_listed",
    "orders"."date_placed",
    JULIANDAY("orders"."date_placed") - JULIANDAY("items"."date_listed") AS "Total Days Listed Prior Order",
    RANK() OVER (ORDER BY JULIANDAY("orders"."date_placed") - JULIANDAY("items"."date_listed") DESC) AS "Rank"
FROM "items"
JOIN "carts" ON "items"."id" = "carts"."item_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
WHERE "orders"."date_placed" = '2025-03-21'
GROUP BY "items"."name"
ORDER BY "items"."date_listed", "orders"."date_placed" DESC;

-- Create view to simplify the access to frequently combined tables
CREATE VIEW "items_carts_orders" AS
SELECT 
    "items"."name",
    "items"."type",
    "items"."description_length",
    "items"."reviews",
    "items"."product_images",
    "items"."product_videos",
    "items"."date_listed",
    "carts"."user_id",
    "orders"."date_placed"
FROM "items"
JOIN "carts" ON "items"."id" = "carts"."item_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id";

-- Create index to speed up frequent searches
CREATE INDEX "date_placed_index" on "orders"("date_placed")
WHERE "date_placed" = '2025-03-20' OR "date_placed" = '2025-03-21';