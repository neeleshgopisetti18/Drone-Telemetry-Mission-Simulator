import time
import random
# Initial Values
altitude = 0
speed = 0
battery = 100.0
latitude = 17.3850
longitude = 78.4867

print("========================================")
print("      AUTONOMOUS DRONE MISSION MODE     ")
print("========================================\n")

for second in range(1, 31):

    # ---- MISSION PHASE LOGIC ----
    
    # Takeoff Phase
    if second <= 5:
        altitude += 15
        speed = 10
    
    # Cruising Phase
    elif second <= 15:
        altitude += random.uniform(-2, 2)
        speed = 25
    
    # Surveillance Phase
    elif second <= 25:
        altitude += random.uniform(-1, 1)
        speed = 12
    
    # Landing Phase
    else:
        altitude -= 20
        speed = 8

    # GPS Movement
    latitude += 0.0001
    longitude += 0.0001

    # Battery Drain (realistic logic)
    battery -= speed * 0.05

    # Safety Checks
    warning = ""
    if battery < 20:
        warning = "⚠ LOW BATTERY – RETURNING HOME"
    if altitude > 120:
        warning = "⚠ MAX SAFE ALTITUDE REACHED"

    # Display Telemetry
    print(f"Time: {second}s")
    print(f"Altitude: {round(altitude,2)} m")
    print(f"Speed: {speed} m/s")
    print(f"Battery: {round(battery,2)} %")
    print(f"GPS: ({round(latitude,6)}, {round(longitude,6)})")

    if warning:
        print(warning)

    print("----------------------------------------")

    time.sleep(1)

print("\nMission Completed Successfully")
print(f"Remaining Battery: {round(battery,2)} %")
