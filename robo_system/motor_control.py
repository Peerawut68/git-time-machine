# robo_system/motor_control.py
"""
Motor Control Module - ระบบควบคุมมอเตอร์และทิศทางการเคลื่อนที่ของหุ่นยนต์
"""

def calculate_wheel_speed(target_speed: int, terrain: str = "flat") -> int:
    """
    คำนวณความเร็วล้อตามสภาพพื้นผิว
    :param target_speed: ความเร็วเป้าหมาย (0-100)
    :param terrain: สภาพพื้นผิว ("flat", "gravel", "mud")
    :return: ความเร็วจริงหลังปรับสภาพ
    """
    if target_speed < 0:
        return 0
    if target_speed > 100:
        target_speed = 100

    if terrain == "mud":
        # พื้นโคลน ความเร็วลดลง 50%
        return target_speed // 2
    elif terrain == "gravel":
        # พื้นกรวด ความเร็วลดลง 20%
        return int(target_speed * 0.8)
    else:
        # พื้นเรียบ วิ่งได้เต็มความเร็ว
        return target_speed

def get_steering_angle(direction: str) -> int:
    """
    คืนค่ามุมเลี้ยวของล้อหน้าตามทิศทาง
    :param direction: "left", "right", "straight"
    :return: องศาการเลี้ยว (-45 ถึง +45)
    """
    if direction == "left":
        return -45
    elif direction == "right":
        return 45
    else:
        return 0

if __name__ == "__main__":
    # Test cases ตรวจสอบความถูกต้องของระบบมอเตอร์
    assert calculate_wheel_speed(80, "flat") == 80
    assert calculate_wheel_speed(80, "mud") == 40
    assert calculate_wheel_speed(100, "gravel") == 80
    assert calculate_wheel_speed(-10) == 0
    assert get_steering_angle("left") == -45
    assert get_steering_angle("straight") == 0
    print("✅ Motor Control: ผ่านการทดสอบทั้งหมด!")

def activate_turbo():
    print("Turbo charge...incomplete")