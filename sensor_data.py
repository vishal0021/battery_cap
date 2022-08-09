start_time = "Fri Aug 05 2022 13:44:51 GMT+0530"
end_time = "Sun Aug 07 2022 13:44:51 GMT+0530"

battery_cap = getBatteryCapacity(start_time, end_time)

sun_position = getSunPositions(start_time, end_time, [sensor_no])

power_consumption = getPowerConsumption(start_time, end_time)

#store data in Csv 