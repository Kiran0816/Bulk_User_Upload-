import psycopg2

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="{DBName}",
        user="postgres",
        password="{PASSWORD}"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Read and execute SQL commands from a file
    with open('create_tables.sql', 'r') as sql_file:
        sql_commands = sql_file.read()
        cursor.execute(sql_commands)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database setup complete.")

except Exception as e:
    print(f"Error during database setup: {str(e)}")
