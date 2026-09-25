# robo_system/sensor_scanner.py
"""
Sensor Scanner Module - ระบบสแกนเนอร์และตรวจจับสิ่งกีดขวาง
"""

def evaluate_sensor_distance(raw_signal: int) -> int:
    """
    แปลงสัญญาณดิบจากเรดาร์ (0-1023) เป็นระยะทางเซนติเมตร (0-500 cm)
    """
    if raw_signal < 0:
        return 0
    # แปลงสัญญาณสเกล
    distance_cm = int((raw_signal / 1023.0) * 500)
    return min(500, distance_cm)

def detect_obstacle_warning(distance_cm: int) -> tuple[bool, str]:
    """
    ตรวจจับความปลอดภัยตามระยะห่างสิ่งกีดขวาง
    :param distance_cm: ระยะห่างเป็นเซนติเมตร
    :return: (is_danger: bool, alert_message: str)
    """
    if distance_cm < 30:
        return True, "🚨 DANGER: สิ่งกีดขวางประชิดตัว! หยุดฉุกเฉิน!"
    elif distance_cm < 100:
        return True, "⚠️ WARNING: ตรวจพบวัตถุด้านหน้า ชะลอความเร็ว"
    else:
        return False, "🟢 CLEAR: ทางสะดวก ปลอดภัย"

if __name__ == "__main__":
    assert evaluate_sensor_distance(0) == 0
    assert evaluate_sensor_distance(1023) == 500
    assert detect_obstacle_warning(20)[0] is True
    assert detect_obstacle_warning(50)[0] is True
    assert detect_obstacle_warning(150)[0] is False
    print("✅ Sensor Scanner: ผ่านการทดสอบทั้งหมด!")
