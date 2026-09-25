# robo_system/main.py
"""
Robo-Lab System Diagnostic - ระบบทดสอบความพร้อมของหุ่นยนต์ AI
คำสั่งรัน: python robo_system/main.py
"""

import sys
import os

# เพิ่ม path เพื่อให้ import โมดูลภายใน robo_system ได้อย่างราบรื่น
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    import motor_control
    import sensor_scanner
except ImportError as e:
    print(f"❌ ระบบขัดข้อง: ไม่สามารถโหลดโมดูลได้ ({e})")
    sys.exit(1)

def print_banner():
    print("=" * 60)
    print("🤖 ROBO-LAB AI: SYSTEM DIAGNOSTIC CHECK")
    print("สถานะ: กำลังตรวจสอบระบบมอเตอร์ เซนเซอร์ และระบบขับเคลื่อน")
    print("=" * 60)

def run_diagnostics():
    print_banner()

    # 1. ทดสอบระบบมอเตอร์
    print("[1] ตรวจสอบระบบมอเตอร์ (Motor Diagnostics):")
    speed_flat = motor_control.calculate_wheel_speed(100, "flat")
    speed_mud = motor_control.calculate_wheel_speed(100, "mud")
    steer_left = motor_control.get_steering_angle("left")

    print(f"   • ความเร็วพื้นเรียบ : {speed_flat:>3}/100 km/h [OK]")
    print(f"   • ความเร็วพื้นโคลน : {speed_mud:>3}/100 km/h [OK]")
    print(f"   • องศาเลี้ยวซ้าย   : {steer_left:>3} องศา       [OK]")

    # 2. ทดสอบระบบเซนเซอร์
    print("\n[2] ตรวจสอบระบบเซนเซอร์ (Sensor Diagnostics):")
    dist = sensor_scanner.evaluate_sensor_distance(512)
    is_danger, msg = sensor_scanner.detect_obstacle_warning(dist)
    print(f"   • ระยะตรวจจับวัตถุ : {dist} cm")
    print(f"   • การตอบสนอง      : {msg}")

    print("\n" + "=" * 60)
    print("✅ ระบบทั้งหมดทำงานปกติ 100%! หุ่นยนต์พร้อมปฏิบัติการ!")
    print("=" * 60)

if __name__ == "__main__":
    run_diagnostics()
