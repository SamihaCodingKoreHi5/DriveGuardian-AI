from vehicle_analyzer import VehicleAnalyzer

analyzer = VehicleAnalyzer()

print("=" * 60)
print("🚗 DRIVEGUARDIAN AI")
print("Vehicle Health Monitoring System")
print("=" * 60)

engine_temp = float(input("Engine Temperature (°C): "))
brake_wear = float(input("Brake Wear (%): "))
battery_health = float(input("Battery Health (%): "))
tire_health = float(input("Tire Health (%): "))
mileage = float(input("Mileage (km): "))

result = analyzer.analyze_vehicle(
    engine_temp,
    brake_wear,
    battery_health,
    tire_health,
    mileage
)

print("\n📊 VEHICLE HEALTH REPORT")
print("-" * 50)

print(f"Health Score: {result['score']}/100")
print(f"Risk Level: {result['risk']}")

print("\n🔧 Recommendations:")

if result["recommendations"]:
    for rec in result["recommendations"]:
        print(f"• {rec}")
else:
    print("• No immediate maintenance required.")

print("\n✅ Analysis Complete")
