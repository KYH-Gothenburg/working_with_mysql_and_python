from mysql import connector


def main():
    connection = connector.connect(user='root', password='s3cr37', host='127.0.0.1', database='classicmodels')
    cursor = connection.cursor()

    sql = """SELECT e.firstName, e.lastName FROM employees e
            JOIN customers c ON e.employeeNumber=c.salesRepEmployeeNumber
            JOIN orders o ON c.customerNumber=o.customerNumber
            JOIN orderdetails od ON o.orderNumber=od.orderNumber
            JOIN products p ON od.productCode=p.productCode
            WHERE p.productName='Collectable Wooden Train'
            GROUP BY  e.firstName, e.lastName
            ORDER BY e.lastName"""

    cursor.execute(sql)
    for row in cursor:
        first_name, last_name = row
        #customerNumber, customerName, contactLast, contactFirst, phone, address1, address2, city, state, postalCode, country, salesRepNo, creditLimit = row
        print(first_name, last_name)
    connection.close()


if __name__ == '__main__':
    main()
