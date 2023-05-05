import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from shop.models import Customer, Product, Order, OrderItem, ShippingAddress

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        ShippingAddress.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(_file_).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/ShoppingProject/CSV/BigBasketCSV.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                Customertable = Customer.objects.create(
                name = row[0],
                customer_id = [4]
                )
                Customertable.save()
        

        with open(str(base_dir) + '/ShoppingProject/CSV/BigBasketCSV.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                Producttable = Product.objects.create(
                name = row[5]
                price = row[7]
                brand = row[8]
                product_id = row[12]
                )
                Producttable.save()


        with open(str(base_dir) + '/ShoppingProject/CSV/BigBasketCSV.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                Ordertable = Order.objects.create(
                date_ordered = row[9]
	            order_id = row[6]
                )
                Ordertable.save()


        with open(str(base_dir) + '/ShoppingProject/CSV/BigBasketCSV.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                Ordertable = Order.objects.create(
                date_ordered = row[9]
	            order_id = row[6]
                )
                Ordertable.save()

        print("data parsed successfully")

