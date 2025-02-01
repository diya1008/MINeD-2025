import pandas as pd

# Create Shipments Data
shipments_data = {
    'Shipment ID': [1, 2, 3, 4, 5],
    'Details': ['Grocery Delivery', 'Electronics', 'Furniture', 'Clothing', 'Books'],
    'Weight': [10, 5, 20, 8, 3],
    'Timeslot': ['09:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 13:00', '13:00 - 14:00'],
    'Latitude': [40.7128, 40.7306, 40.7580, 40.6892, 40.748817],
    'Longitude': [-74.0060, -73.9352, -73.9855, -74.0445, -73.985428]
}

# Create Vehicle Information
vehicle_data = {
    'Vehicle ID': [1, 2, 3, 4, 5],
    'Type': ['3W', '4W-EV', '4W', '2W', '3W'],
    'Capacity': [30, 50, 40, 15, 25],
    'Availability': ['Available', 'Available', 'Not Available', 'Available', 'Available']
}

# Create DataFrames
shipments_df = pd.DataFrame(shipments_data)
vehicles_df = pd.DataFrame(vehicle_data)

# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter('SmartRoute_Optimizer.xlsx', engine='xlsxwriter') as writer:
    shipments_df.to_excel(writer, sheet_name='Shipments Data', index=False)
    vehicles_df.to_excel(writer, sheet_name='Vehicle Information', index=False)

print("SmartRoute_Optimizer.xlsx has been created successfully.")
