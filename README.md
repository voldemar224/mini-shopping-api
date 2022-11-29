#user
GET user by user_id\
curl http://127.0.0.1:5000/user/{{user_id}}

GET all users in a database\
curl http://127.0.0.1:5000/users

POST user by name\
curl http://127.0.0.1:5000/register -d "username=name"

PUT user by id (edit user's name)\
curl -X PUT http://127.0.0.1:5000/user/{{user_id}} -d "username=name"

DELETE user by user_id\
curl -X DELETE http://127.0.0.1:5000/user/{{user_id}}

#Product
GET product by product_id\
curl http://127.0.0.1:5000/product/{{product_id}}

GET all products in a database\
curl http://127.0.0.1:5000/products

POST product by name and price\
curl http://127.0.0.1:5000/create-product -d "name=str" -d "price=float"

PUT product by product_id (edit product's name or price or together)\
curl -X PUT http://127.0.0.1:5000/product/{{product_id}} -d "price=float"
curl -X PUT http://127.0.0.1:5000/product/{{product_id}} -d "name=str"
curl -X PUT http://127.0.0.1:5000/product/{{product_id}} -d "name=str" -d "price=float"

DELETE product by product_id\
curl -X DELETE http://127.0.0.1:5000/product/{{product_id}}
!ATTENTION! if you delete a product from products, not from order, all products of this type will be deleted from orders

#Order
GET order by order_id\
curl http://127.0.0.1:5000/order/{{order_id}}

POST order by order_id (order is connected to user) \
curl http://127.0.0.1:5000/create-order -d "user_id=int"

PUT order by order_id (to add there a product you have to enter product_id)\
curl -X PUT http://127.0.0.1:5000/order/{{order_id}} -d "product_id=int"
it will add just one product

if you want to add a few products which are already in order or not in order yet:
curl -X PUT http://127.0.0.1:5000/order/{{order_id}} -d "product_id=int" -d "quantity=int"

DELETE order by order_id\
curl -X DELETE http://127.0.0.1:5000/order/{{order_id}}

if you want to delete a product of some type from order
curl -X DELETE http://127.0.0.1:5000/order/{{order_id}} -d "product_id=int"
it will delete just one product

if you want to delete a few products which are already in order:
curl -X DELETE http://127.0.0.1:5000/order/{{order_id}} -d "product_id=int" -d "quantity=int"