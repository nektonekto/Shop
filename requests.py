create_shop_table_query = """
CREATE TABLE IF NOT EXISTS product(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    image VARCHAR(200),
    url VARCHAR(200)
)
"""
show_table_query = "DESCRIBE product"

insert_product_query = """
INSERT INTO product(name, price, image, url)
VALUES
    ("Adidas boost", 12000, "image1", "url1"),
    ("Adidas EP", 7000, "image2", "url2")
"""
insert_product_query2 = """
INSERT INTO product(name, price, image, url)
VALUES 
    ("Nike", 9000, "image3", "url3")
"""

check_table_query = """
SELECT * FROM product;
"""
fields_table_query = """
SHOW FIELDS FROM product;"""