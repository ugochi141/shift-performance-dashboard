class ShiftPerformanceAnalyzer:
    def __init__(self):
        self.critical_staff = ["Person2_Sam"]  # Anonymized
        self.shift_targets = {
            "first": {"tat": 30, "wait": 15},
            "second": {"tat": 20, "wait": 15},  # Stricter for problem shift
            "third": {"tat": 35, "wait": 20}
        }
    
    def analyze_individual_performance(self, staff_id, shift):
        """Track individual staff member performance"""
        # Would connect to real data
        performance = {
            "staff_id": staff_id,
            "avg_tat": 71,  # Based on your real data
            "days_above_target": 5,
            "improvement_needed": True,
            "action_plan": "Immediate retraining required"
        }
        return performance
    
    def generate_alerts(self, performance_data):
        """Generate management alerts for poor performance"""
        alerts = []
        if performance_data["avg_tat"] > 65:
            alerts.append({
                "level": "CRITICAL",
                "message": f"Staff {performance_data['staff_id']} TAT critically high",
                "action": "Immediate supervisor intervention required"
            })
        return alerts
