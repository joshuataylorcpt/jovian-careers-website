#this file contains the details to connect to the database
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://sql7752023:aFwF9KDMxH@sql7.freemysqlhosting.net/sql7752023?charset=utf8mb4"
#created an engine to connect to the database
ssl_ca_path = "/path/to/mysql-ssl-ca-cert.pem"

engine = create_engine(db_connection_string)
#we can use that connection to execute commands
with engine.connect() as conn:
  # Execute the query
  result = conn.execute(text("SELECT * FROM salesrequest"))

  # Print the type of the result object
  print("Type of result:", type(result))

  # Fetch all rows as a list of tuples
  result_all = result.all()

  # Print the type of result_all
  print("Type of result.all():", type(result_all))

  # Print the first row from the result
  print("First row of result:", result_all[0])
  