
CREATE DATABASE travel_booking_db;
USE travel_booking_db;

CREATE TABLE traveler_data (
    travelerno INT PRIMARY KEY,
    travelername VARCHAR(100),
    address VARCHAR(255),
    traveldate DATE
);

CREATE TABLE ridefare (
    id INT AUTO_INCREMENT PRIMARY KEY,
    travelerno INT,
    basefare INT,
    extrafare INT,
    totalfare INT,
    FOREIGN KEY (travelerno) REFERENCES traveler_data(travelerno)
);
ALTER TABLE traveler_data MODIFY travelerno INT;
ALTER TABLE ridefare MODIFY travelerno INT;





































CREATE TABLE traveler_data (
    travelerno VARCHAR(50),
    travelername VARCHAR(50),
    address VARCHAR(100),
    traveldate DATE
);

-- Ride fare details
CREATE TABLE ridefare (
    travelerno VARCHAR(50),
    basefare DECIMAL(10,2),
    extrafare DECIMAL(10,2),
    totalfare DECIMAL(10,2)
);
show tables;
SELECT 
    traveler_data.travelerno,
    traveler_data.travelername,
    traveler_data.address,
    traveler_data.traveldate,
    ridefare.basefare,
    ridefare.extrafare,
    ridefare.totalfare
FROM traveler_data
INNER JOIN ridefare ON traveler_data.travelerno = ridefare.travelerno;


