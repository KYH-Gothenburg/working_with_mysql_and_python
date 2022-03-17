import json

import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:s3cr37@localhost:3306/eshop")

# Base är basklass för våra modeller
Base = declarative_base()

# Session är den klass vi använder för att kommunicera med databasen
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(150), nullable=False)
    product_in_stock = Column(Integer)
    product_sell_price = Column(Float, nullable=False)
    product_description = Column(Text)
    order_lines = relationship('OrderLines', back_populates='product')

    def __repr__(self):
        return self.product_name


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_first_name = Column(String(45), nullable=False)
    customer_last_name = Column(String(45), nullable=False)
    customer_email = Column(String(45), nullable=False)
    customer_mobile_phone = Column(String(45))
    orders = relationship('Order', back_populates='customer')

    def __repr__(self):
        return self.customer_first_name + ' ' + self.customer_last_name


class OrderStatus(Base):
    __tablename__ = 'order_status'

    order_status_id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(45), nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    order_status_id = Column(Integer, ForeignKey('order_status.order_status_id'), nullable=False)
    order_status = relationship('OrderStatus')
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    customer = relationship('Customer', back_populates='orders')
    order_lines = relationship('OrderLines', back_populates='order')


class OrderLines(Base):
    __tablename__ = 'order_lines'

    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    amount_ordered = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_lines')
    product = relationship('Product', back_populates='order_lines')


def main():
    #product = Product(product_name="Hoppborg", product_in_stock=67, product_sell_price=567.90, product_description="En hoppborg")

    #session.add(product)
    #session.commit()

    #products = session.query(Product).all()

    #print(products)

    #customers = session.query(Customer).all()
    #print(customers)

    customer = session.query(Customer).get(2)
    item1 = session.query(Product).get(1)
    item2 = session.query(Product).get(2)
    order_status = session.query(OrderStatus).get(3)
    order_lines = [OrderLines(product=item1, amount_ordered=3), OrderLines(product=item2, amount_ordered=1)]
    order = Order(order_date='2022-03-17', order_status=order_status, customer=customer, order_lines=order_lines)
    session.add(order)
    session.commit()
    print()


if __name__ == '__main__':
    main()
