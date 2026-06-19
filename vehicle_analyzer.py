class VehicleAnalyzer:

    def analyze_vehicle(
        self,
        engine_temp,
        brake_wear,
        battery_health,
        tire_health,
        mileage
    ):

        score = 100

        recommendations = []

        # Engine
        if engine_temp > 105:
            score -= 25
            recommendations.append(
                "Check engine cooling system immediately."
            )

        elif engine_temp > 95:
            score -= 15
            recommendations.append(
                "Monitor engine temperature regularly."
            )

        # Brake
        if brake_wear > 70:
            score -= 25
            recommendations.append(
                "Brake replacement recommended."
            )

        elif brake_wear > 50:
            score -= 15
            recommendations.append(
                "Inspect brake pads soon."
            )

        # Battery
        if battery_health < 60:
            score -= 20
            recommendations.append(
                "Battery replacement may be required."
            )

        elif battery_health < 80:
            score -= 10
            recommendations.append(
                "Battery performance is declining."
            )

        # Tire
        if tire_health < 60:
            score -= 15
            recommendations.append(
                "Replace tires for safety."
            )

        elif tire_health < 75:
            score -= 8
            recommendations.append(
                "Tire inspection recommended."
            )

        # Mileage
        if mileage > 100000:
            score -= 15

        elif mileage > 70000:
            score -= 8

        score = max(score, 0)

        if score >= 80:
            risk = "Low"

        elif score >= 60:
            risk = "Medium"

        else:
            risk = "High"

        return {
            "score": score,
            "risk": risk,
            "recommendations": recommendations
        }
