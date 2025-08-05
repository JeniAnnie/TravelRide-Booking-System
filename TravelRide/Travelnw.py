import os
import platform
import mysql.connector

def mysqlconnection():
    global mySqlDb
    mySqlDb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306,
        database='travel_booking',  # NEW database
    )
    return mySqlDb.cursor()

def registerTravelerDetails():
    try:
        mycursor = mysqlconnection()

        travelerList = []

        traveler_no = int(input('Enter traveler number: '))
        travelerList.append(traveler_no)

        traveler_name = input('Enter traveler name: ')
        travelerList.append(traveler_name)

        address = input('Enter address: ')
        travelerList.append(address)

        travel_date = input('Enter travel date (YYYY-MM-DD): ')
        travelerList.append(travel_date)

        sql = 'INSERT INTO traveler_data(travelerno, travelername, address, traveldate) VALUES (%s, %s, %s, %s)'
        mycursor.execute(sql, tuple(travelerList))
        mySqlDb.commit()
        mycursor.close()

    except Exception as e:
        print(e)
    finally:
        mySqlDb.close()

def rideFareCalculation():
    try:
        mycursor = mysqlconnection()
        fareList = []

        tno = int(input('Enter traveler number: '))
        fareList.append(tno)

        print('We offer the following rides:')
        print('1. Sedan - Rs. 6000 per trip')
        print('2. SUV - Rs. 4000 per trip')
        print('3. Hatchback - Rs. 2000 per trip')

        choice = int(input('Choose ride type: '))
        num_rides = int(input('Enter number of rides: '))

        if choice == 1:
            print('You selected Sedan.')
            base_fare = 6000 * num_rides
        elif choice == 2:
            print('You selected SUV.')
            base_fare = 4000 * num_rides
        elif choice == 3:
            print('You selected Hatchback.')
            base_fare = 2000 * num_rides
        else:
            print('Invalid choice.')
            return

        fareList.append(base_fare)

        print('Additional charge per extra passenger: Rs. 500')
        extra_passengers = int(input('Enter number of extra passengers: '))
        extra_fare = extra_passengers * 500
        fareList.append(extra_fare)

        total_fare = base_fare + extra_fare
        print(f'Total Fare: Rs. {total_fare}')

        sql = "INSERT INTO ridefare(travelerno, basefare, extrafare, totalfare) VALUES (%s, %s, %s, %s)"
        fareList.append(total_fare)
        mycursor.execute(sql, tuple(fareList))
        mySqlDb.commit()
        mycursor.close()

    except Exception as e:
        print(e)
    finally:
        mySqlDb.close()

def displayTravelerBill():
    try:
        mycursor = mysqlconnection()
        traveler_no = int(input("Enter traveler number to view bill: "))
        sql = """SELECT traveler_data.travelerno, traveler_data.travelername, 
                        ridefare.basefare, ridefare.extrafare, ridefare.totalfare 
                 FROM traveler_data 
                 INNER JOIN ridefare ON traveler_data.travelerno = ridefare.travelerno 
                 WHERE ridefare.travelerno = %s"""
        mycursor.execute(sql, (traveler_no,))
        results = mycursor.fetchall()

        for row in results:
            print(row)
        mycursor.close()
    except Exception as e:
        print(e)
    finally:
        mySqlDb.close()

def displayAllTravelerDetails():
    try:
        mycursor = mysqlconnection()
        sql = """SELECT traveler_data.travelerno, traveler_data.travelername, traveler_data.address, 
                        ridefare.basefare, ridefare.extrafare, ridefare.totalfare 
                 FROM traveler_data 
                 INNER JOIN ridefare ON traveler_data.travelerno = ridefare.travelerno"""
        mycursor.execute(sql)
        results = mycursor.fetchall()
        print("All traveler details:")
        for row in results:
            print(row)
        mycursor.close()
    except Exception as e:
        print(e)
    finally:
        mySqlDb.close()

def menu():
    print('\n=== Travel Ride Booking System ===')
    print('1. Register Traveler')
    print('2. Calculate Ride Fare')
    print('3. Display Bill by Traveler')
    print('4. Display All Traveler Details')
    print('5. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        registerTravelerDetails()
    elif choice == 2:
        rideFareCalculation()
    elif choice == 3:
        displayTravelerBill()
    elif choice == 4:
        displayAllTravelerDetails()
    elif choice == 5:
        quit()
    else:
        print('Invalid choice.')

def runagain():
    run = input('\nRun again? (y/n): ')
    while run.lower() == 'y':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        menu()
        run = input('\nRun again? (y/n): ')

menu()
runagain()