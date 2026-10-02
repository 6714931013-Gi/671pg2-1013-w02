
การเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming: OOP) ในภาษา Python ตามแนวทางของ W3Schools มุ่งเน้นการมองข้อมูลและพฤติกรรมของโปรแกรมให้อยู่ในรูปของ "วัตถุ (Object)" โดยมีหัวใจสำคัญดังนี้:

Class (คลาส): เปรียบเสมือนพิมพ์เขียว (Blueprint) หรือแม่แบบที่ใช้กำหนดโครงสร้าง ประกอบด้วยคุณลักษณะ (Attributes) และการทำงาน (Methods)

Object (วัตถุ): ชิ้นงานจริงที่ถูกสร้างขึ้นมาจากคลาส (Instance)

__init__() Function: ฟังก์ชันสร้าง (Constructor) ที่จะถูกเรียกใช้โดยอัตโนมัติเมื่อมีการสร้างวัตถุใหม่ ใช้สำหรับการตั้งค่าเริ่มต้นให้กับคุณลักษณะของวัตถุ

Self Parameter: ตัวแปรอ้างอิงถึงอินสแตนซ์ปัจจุบันของคลาส ใช้เพื่อเข้าถึงคุณลักษณะหรือเมธอดภายในคลาสนั้นๆ

Inheritance (การสืบทอด): การสร้างคลาสใหม่ (Child Class) โดยการรับถ่ายทอดคุณลักษณะและเมธอดมาจากคลาสเดิม (Parent Class) เพื่อลดการเขียนโค้ดซ้ำซ้อน

Encapsulation & Polymorphism: การซ่อนรายละเอียดข้อมูลภายในคลาส และการกำหนดให้เมธอดชื่อเดียวกันทำงานแตกต่างกันได้ตามคลาสที่เรียกใช้




class TouristAttraction:
    def __init__(self, name, province, category, rating, entry_fee=0):
        # คุณลักษณะ (Attributes) ของสถานที่ท่องเที่ยว
        self.name = name          # ชื่อสถานที่
        self.province = province  # จังหวัดที่ตั้ง
        self.category = category  # ประเภท (เช่น วัด, สวนสาธารณะ, ทะเล)
        self.rating = rating      # คะแนนรีวิว (0.0 - 5.0)
        self.entry_fee = entry_fee # ค่าเข้าชม (บาท)

    def display_info(self):
        """เมธอดสำหรับแสดงรายละเอียดของสถานที่ท่องเที่ยว"""
        print(f"=== ข้อมูลสถานที่ท่องเที่ยว ===")
        print(f"ชื่อสถานที่: {self.name}")
        print(f"จังหวัด: {self.province}")
        print(f"ประเภท: {self.category}")
        print(f"คะแนนรีวิว: {self.rating} / 5.0")
        fee_text = f"{self.entry_fee} บาท" if self.entry_fee > 0 else "เข้าชมฟรี"
        print(f"ค่าเข้าชม: {fee_text}")

# --- การสร้างวัตถุ (Object) จากคลาส ---
attraction1 = TouristAttraction(
    name="วัดพระศรีรัตนศาสดาราม (วัดพระแก้ว)",
    province="กรุงเทพมหานคร",
    category="โบราณสถาน / วัฒนธรรม",
    rating=4.8,
    entry_fee=500
)

# เรียกใช้เมธอดผ่านวัตถุที่สร้างขึ้น
attraction1.display_info()