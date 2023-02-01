import pandas as pd

import matplotlib.pyplot as plt
# Load data
df = pd.read_excel("Data_for_Syed.xlsx", sheet_name=None)
df = pd.concat(df.values(), ignore_index=True)

print(df.head())

# Driver Behavior
# a. Frequency of rides/total number of rides
frequency = df.groupby("Kennzeichen").size().reset_index(name="frequency")

print(frequency)

print(frequency.max())

print(frequency.min())



# b. Duration of rides
df["ride_duration"] = (df["Fahrtende"] - df["Fahrtbeginn"]).dt.total_seconds()
duration = df.groupby("Kennzeichen")["ride_duration"].mean().reset_index(name="duration")

print(duration)





# c. Time of rides (in particular, at what time are the drivers active?)
df["hour"] = df["Fahrtbeginn"].dt.hour
activity = df.groupby(["Kennzeichen", "hour"]).size().reset_index(name="activity")
activity = activity.pivot(index="Kennzeichen", columns="hour", values="activity").reset_index()

print(activity)

# d. Cancellation
cancellation = df[df["Fahrtstatus"] == "storniert"].groupby("Kennzeichen").size().reset_index(name="cancellation")


print(cancellation)

print(len(df.index))



# Calculate the duration of each ride by subtracting the 'Fahrtbeginn' column from the 'Fahrtende' column
df['Duration'] = (df['Fahrtende'] - df['Fahrtbeginn']).dt.total_seconds()/60

# Group the data by Kennzeichen (car registration) and calculate the average duration for each driver
driver_average_duration = df.groupby('Kennzeichen')['Duration'].mean().reset_index(name='Average Duration')

# Sort the data in ascending order to get the drivers with the shortest average ride duration
driver_average_duration = driver_average_duration.sort_values('Average Duration', ascending=True)

# Print the top 5 drivers with the shortest average ride duration
print(driver_average_duration)


# Hotspots
# a. Which hotspots are there in Cologne?
pickup_hotspots = df.groupby("Abholort").size().reset_index(name="pickup_hotspots")
dropoff_hotspots = df.groupby("Zielort").size().reset_index(name="dropoff_hotspots")

print(pickup_hotspots.head())
# Plot the pickup and dropoff hotspots
# plt.figure(figsize=(15, 5))
# plt.subplot(1, 2, 1)
# plt.bar(pickup_hotspots['Abholort'], pickup_hotspots['pickup_hotspots'])
# plt.title('Pickup Hotspots')
# plt.xlabel('Location')
# plt.ylabel('Count')

# plt.subplot(1, 2, 2)
# plt.bar(dropoff_hotspots['Zielort'], dropoff_hotspots['dropoff_hotspots'])
# plt.title('Dropoff Hotspots')
# plt.xlabel('Location')
# plt.ylabel('Count')

#plt.show()
print("\n\nTop 10 pickup locaions:")
print(pickup_hotspots.sort_values(by=['pickup_hotspots'], ascending=False).head(10))
print("\n\nTop 10 dropoff locations:")
print(dropoff_hotspots.sort_values(by=['dropoff_hotspots'], ascending=False).head(10))

