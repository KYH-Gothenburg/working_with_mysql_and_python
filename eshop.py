from mysql import connector


def main():
    connection = connector.connect(user='root', password='s3cr37', host='127.0.0.1', database='eshop')
    cursor = connection.cursor()

    sql = "INSERT INTO products (product_name, product_in_stock, product_sell_price, product_description)" \
          " VALUES ('Studsboll', 34, 54, 'En studsig boll som är fin')"

    cursor.execute(sql)

    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
