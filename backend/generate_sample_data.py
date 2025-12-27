import json, random, datetime

authors = []
for i in range(1, 41):
    authors.append({
        "model": "catalog.author",
        "pk": i,
        "fields": {"name": f"Tác giả {i}", "birth_year": random.randint(1940, 1990)}
    })

categories = []
for i in range(1, 11):
    categories.append({
        "model": "catalog.category",
        "pk": i,
        "fields": {"name": f"Thể loại {i}"}
    })

publishers = []
for i in range(1, 11):
    publishers.append({
        "model": "catalog.publisher",
        "pk": i,
        "fields": {"name": f"NXB {i}", "address": f"Địa chỉ {i}"}
    })

books = []
for i in range(1, 41):
    books.append({
        "model": "catalog.book",
        "pk": i,
        "fields": {
            "title": f"Sách {i}",
            "author": random.randint(1, 40),
            "category": random.randint(1, 10),
            "publisher": random.randint(1, 10),
            "publish_year": random.randint(1980, 2025),
            "quantity": random.randint(1, 20)
        }
    })

borrowers = []
for i in range(1, 41):
    borrowers.append({
        "model": "catalog.borrower",
        "pk": i,
        "fields": {
            "name": f"Độc giả {i}",
            "email": f"reader{i}@example.com",
            "phone": f"09000000{i:02d}"
        }
    })

loans = []
for i in range(1, 41):
    loans.append({
        "model": "catalog.loan",
        "pk": i,
        "fields": {
            "book": random.randint(1, 40),
            "borrower": random.randint(1, 40),
            "borrow_date": str(datetime.date(2025, random.randint(1, 12), random.randint(1, 28))),
            "return_date": None if i % 2 == 0 else str(datetime.date(2025, random.randint(1, 12), random.randint(1, 28)))
        }
    })

data = authors + categories + publishers + books + borrowers + loans

with open("sample_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ sample_data.json đã được tạo với dữ liệu mẫu!")
