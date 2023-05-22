from Attendance import myconn


def main():
    try:
        connection = myconn.myconn()
        cursor = connection.cursor()

        queries = ['create database eventide04',

                   'use eventide04',

                   'create table user (username varchar(20), userID int auto_increment , admin char(1), \
                  password varchar(50), primary key (userID))',

                   'alter table user auto_increment = 101',

                   'create table events( eventID int auto_increment , eventname varchar(100), primary key (eventID))',

                   'alter table events auto_increment = 501',

                   'create table participants(pname varchar(100), email varchar(100), ph_no char(10), eventid int, \
                  pID int, city varchar(100), college varchar(100), attendance char(1))',

                   'create table c_v(userid int,eventid int,  foreign key (userid) references user (userID), \
                  foreign key (eventid) references events (eventID))'
                   ]

        for query in queries:
            cursor.execute(query)

        name = input('Enter first username : ')
        password = input('Enter first password : ')

        cursor.execute(f"insert into user(username,admin,password) values('{name}','y','{password}')")

        print('Database and tables created successfully')
    except Exception as e:
        print("Error : ", e)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
