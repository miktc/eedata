-- EEData Queries

-- Find the total number of accounts that placed an order on the same day the account was created
SELECT
    "users"."date_account_created",
    "orders"."date_placed",
    COUNT("orders"."date_placed") AS "Total Accounts per Date"
FROM "users"
JOIN "carts" ON "users"."id" = "carts"."user_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
WHERE "users"."date_account_created" = "orders"."date_placed"
GROUP BY "orders"."date_placed"
ORDER BY "orders"."date_placed";

-- Find the maximum number of days between a user creating an account and purchasing an item
SELECT
    "users"."date_account_created",
    "orders"."date_placed",
    JULIANDAY("orders"."date_placed") - JULIANDAY("users"."date_account_created") AS "Total Days"
FROM "users"
JOIN "carts" ON "users"."id" = "carts"."user_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
GROUP BY "Total Days"
ORDER BY "users"."date_account_created", "carts"."date_created" DESC
LIMIT 1;

-- Find the total number of Gmail, Yahoo, and Hotmail accounts
SELECT 'Gmail' AS "Domain", COUNT("email") AS "Total Accounts" FROM "users"
WHERE "email" LIKE '%gmail%'
UNION
SELECT 'Yahoo', COUNT("email") FROM "users"
WHERE "email" LIKE '%yahoo%'
UNION
SELECT 'Hotmail', COUNT("email") FROM "users"
WHERE "email" LIKE '%hotmail%'
ORDER BY "Total Accounts" DESC;

-- Find the top three most ordered items
SELECT
    "items"."name",
    "items"."type",
    COUNT("items"."name") AS "Total Items Ordered"
FROM "carts"
JOIN "items" ON "carts"."item_id" = "items"."id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
GROUP BY "items"."name"
ORDER BY "Total Items Ordered" DESC
LIMIT 3;

-- Find an item name given an item ID and a specific condition
SELECT "name" FROM "items"
WHERE "id" IN (
    SELECT "item_id" FROM (
        SELECT "item_id", COUNT("item_id") AS "Total Items" FROM "carts"
        WHERE "became_order" = 0
        GROUP BY "item_id"
        ORDER BY "Total Items" DESC
        LIMIT 1
    )
);

-- Find the maximum total orders placed for an item with the highest total sum of images, videos, and reviews
SELECT
    "items"."name",
    SUM("items"."product_images") + SUM("items"."product_videos") + SUM("items"."reviews") AS "Total Item Info",
    COUNT("orders"."id") AS "Total Orders Placed"
FROM "items"
JOIN "carts" ON "items"."id" = "carts"."item_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
GROUP BY "items"."name"
ORDER BY "Total Item Info" DESC
LIMIT 1;

-- Find the names and the number of reviews an item received with no product images posted
WITH "item_info" AS (
    SELECT
        "items"."name",
        "items"."type",
        "items"."reviews",
        "items"."product_images",
        "items"."product_videos",
        "items"."advertisement",
        SUM("orders"."total_amount") AS "Sum Orders Total Amount",
        COUNT("orders"."id") AS "Total Number of Orders"
    FROM "items"
    JOIN "carts" ON "items"."id" = "carts"."item_id"
    JOIN "orders" ON "carts"."id" = "orders"."cart_id"
    GROUP BY "items"."name"
)
SELECT "name","reviews" FROM "item_info"
WHERE "product_images" = 0;

-- Find and rank the total number of days items were listed before orders were placed for a given date
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

-- Find the names, types, prices, and advertisements of items, as well as the average item quantity purchased and the total number of orders
SELECT
    "items"."name",
    "items"."type",
    "items"."price",
    "items"."advertisement",
    ROUND(AVG("orders"."item_quantity"),0) AS "Average Quantity Purchased",
    COUNT("orders"."id") AS "Total Orders",
    ROW_NUMBER() OVER (ORDER BY COUNT("orders"."id")) AS "Row Number"
FROM "items"
JOIN "carts" ON "items"."id" = "carts"."item_id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
GROUP BY "items"."name"
ORDER BY "Total Orders";

-- Find the total cost of posted items and the total number of carts that discarded the item for a given shipping price
SELECT
    "items"."name",
    "items"."price",
    "items"."shipping_price",
    "items"."price" + "items"."shipping_price" AS "Total Cost per Item",
    COUNT("items"."id") AS "Total Carts Canceled"
FROM "carts"
JOIN "items" ON "carts"."item_id" = "items"."id"
WHERE "carts"."became_order" = 0 AND "items"."shipping_price" <> 0
GROUP BY "items"."name"
HAVING "carts"."date_created" = "carts"."date_cart_transition"
ORDER BY "Total Cost per Item" DESC;

-- Find the average, minimum, and maximum item quantity and the total amount ordered for a given date
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

-- Find the usernames of users that made an order for a given date
SELECT "username" FROM "users"
WHERE "id" IN (
    SELECT "user_id" FROM "carts"
    WHERE "id" IN (
        SELECT "cart_id" FROM "orders"
        WHERE "date_placed" = '2025-03-20' or "date_placed" = '2025-03-21'
    )
);

-- Find items and the total number of orders for a given minimum description length
SELECT 
    "items"."name",
    "items"."description_length",
    COUNT("items"."id") AS "Total Orders"
FROM "items"
JOIN "carts" ON "items"."id" = "carts"."item_id"
JOIN "users" ON "carts"."user_id" = "users"."id"
JOIN "orders" ON "carts"."id" = "orders"."cart_id"
GROUP BY "items"."id"
HAVING "items"."description_length" > 200
ORDER BY "Total Orders" DESC;

-- Find the usernames of users that submitted a return for a given reason and date
SELECT "username" FROM "users"
WHERE "id" IN (
    SELECT "user_id" FROM "carts"
    WHERE "id" IN (
        SELECT "cart_id" FROM "orders"
        WHERE "id" in (
            SELECT "order_id" FROM "returns"
            WHERE "reason" = 'damaged' AND "date_returned" = '2025-04-15'
        )
    )
);

-- Find the total number of returns for items along with their type, description length, number of images posted, and number of videos posted
SELECT
    "items"."name",
    "items"."type",
    "items"."description_length",
    "items"."product_images",
    "items"."product_videos",
    COUNT("returns"."id") AS "Total Returns",
    ROW_NUMBER() OVER (ORDER BY COUNT("returns"."id") DESC) AS "Row Number"
FROM "returns"
JOIN "orders" ON "returns"."order_id" = "orders"."id"
JOIN "carts" ON "orders"."cart_id" = "carts"."id"
JOIN "items" ON "carts"."item_id" = "items"."id"
GROUP BY "items"."name"
ORDER BY "Total Returns" DESC, "items"."description_length" DESC;

-- Insert new users
INSERT INTO "users"("id","username","email","address","state","date_account_created","date_last_login","date_recent_login")
VALUES
(100001,'freddyfred','freddyfred@gmail.com','4332 Lake Lane', 'California', '2025-03-31', '2025-03-31', '2025-03-31'),
(100002, 'anniev22', 'anniev22@yahoo.com', '1232 Tree Wood Park', 'Iowa', '2025-03-31', '2025-03-31', '2025-03-31');

-- Insert new items
INSERT INTO "items"("id","name","type","price","shipping_price","description_length","reviews","product_images","product_videos","advertisement","date_listed")
VALUES
(16,'jacket','clothing',200,14.99,351,8788,15,1,26000,'2025-02-01'),
(17,'hat','clothing',30,9.99,504,9088,35,5,15000,'2025-02-02');

-- Update the items price for a given item type
UPDATE "items" SET "price" = round("price" - ("price"*0.20),2)
WHERE "type" = 'software';

-- Update the items shipping price for a given item type
UPDATE "items" SET "shipping_price" = round("shipping_price" + ("shipping_price"*0.5),2)
WHERE "type" = 'technology';

-- Update the items advertisement for given item types
UPDATE "items" SET "advertisement" = round("advertisement" + ("advertisement"*0.45),2)
WHERE "type" = 'technology' AND "type" = 'software';

-- User account deletion trigger
DELETE FROM "users"
WHERE "username" = 'freddyfred';

DELETE FROM "users"
WHERE "username" = 'anniev22';

-- Item deletion trigger
DELETE FROM "items"
WHERE "name" = 'jacket';

DELETE FROM "items"
WHERE "name" = 'hat';