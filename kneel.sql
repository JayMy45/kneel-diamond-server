--Create All Tables
CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `metal_id` INTEGER NOT NULL,
    `price` NUMERIC(5,2) NOT NULL,
    `timestamp`TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
);

CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

--INSERT DATA
--Data for Orders
INSERT INTO `Orders` VALUES (null, 1, 3, 2, 6712.42, 1665087278);
INSERT INTO `Orders` VALUES (null, 2, 1, 1, 2536.4, 1665087278 );
INSERT INTO `Orders` VALUES (null, 5, 3, 3, 5341, 1665087278 );
INSERT INTO `Orders` VALUES (null, 5, 1, 2, 6941, 1665087278 );
INSERT INTO `Orders` VALUES (null, 4, 3, 2, 7495.45, 1665087278 );
INSERT INTO `Orders` VALUES (null, 3, 3, 2, 7958.9, 1665087278 );
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 1812.42, 1665087278 );
INSERT INTO `Orders` VALUES (null, 4, 1, 1, 2595.45, 1665087278 );
INSERT INTO `Orders` VALUES (null, 3, 3, 3, 5258.90, 1665087278 );
INSERT INTO `Orders` VALUES (null, 2, 3, 1, 3536.4, 1665087278 );
INSERT INTO `Orders` VALUES (null, 1, 1, 3, 1812.42, 1665087278 );
INSERT INTO `Orders` VALUES (null, 4, 3, 2, 7495.45, 1665087278 );


--Data for Metals
INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.40);
INSERT INTO `Metals` VALUES (null, '24K Gold', 1258.9);
INSERT INTO `Metals` VALUES (null, 'Platinumm', 795.45);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241);

--Data for Styles
INSERT INTO `Styles` VALUES (null, 'Solitaire', 500);
INSERT INTO `Styles` VALUES (null, 'Princess', 1000);
INSERT INTO `Styles` VALUES (null, 'Emerald', 1500);

--Data for Sizes
INSERT INTO `Sizes` VALUES (null, 1, 1300);
INSERT INTO `Sizes` VALUES (null, 4, 5200);
INSERT INTO `Sizes` VALUES (null, 2, 2600);

--Delet Tables (if neeeded)
DROP TABLE Orders;
DROP TABLE Metals;
DROP TABLE Styles;
DROP TABLE Sizes;