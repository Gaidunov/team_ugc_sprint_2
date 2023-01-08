

load: 
	python -m data_load       

easy_get: 
	locust -f locustfile.py --tags mongo postgres --headless -u 100 -r 5

extreme_mongo_get: 
	locust -f locustfile.py --tags mongo --headless -u 1000 -r 20

extreme_pg_get: 
	locust -f locustfile.py --tags postgres --headless -u 1000 -r 20

easy_insert:
	locust -f locustfile.py --tags like_postgres like_mongo --headless -u 100 -r 20

extreme_insert_pg:
	locust -f locustfile.py --tags like_postgres --headless -u 1000 -r 20

extreme_insert_mongo:
	locust -f locustfile.py --tags like_mongo --headless -u 1000 -r 20

