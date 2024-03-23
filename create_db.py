import mysql.connector

def create_db(sql_user, sql_pass):

    conn = mysql.connector.connect(
        host='localhost',
        user=sql_user,
        password=sql_pass
    )
    cursor = conn.cursor()

    cursor.execute('''
        DROP DATABASE IF EXISTS reddit_tech;
        CREATE DATABASE reddit_tech;
    ''')
                
    conn = mysql.connector.connect(
        host='localhost',
        user=sql_user,
        password=sql_pass,
        database='reddit_tech'
    )

    cursor = conn.cursor()

    cursor.execute('''
        use reddit_tech;
    '''
    )
                
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id VARCHAR(255) PRIMARY KEY,
        content TEXT NOT NULL,
        username VARCHAR(512),
        url VARCHAR(512), 
        upvotes INT,
        comments INT,
        timestamp VARCHAR(255),
        subreddit VARCHAR(255),
        keywords VARCHAR(512),
        vec VARCHAR(512)
        )
    ''')

    conn.commit()
    conn.close()

