db_config = {
    'host': 'your-rds-endpoint.amazonaws.com',  
    # e.g., flaskdb-instance.xxxxxx.ap-south-1.rds.amazonaws.com
    'user': 'admin',                            # master username created in RDS
    'password': 'YourPasswordHere',             # master password created in RDS
    'database': 'flaskdb'                       # database name created in MySQL
}
