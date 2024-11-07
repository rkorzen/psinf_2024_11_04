from datetime import datetime, timezone



t1 = datetime.now(tz=timezone.utc)
print(t1)
print(t1.tzinfo)

t2 = datetime(2024, 11, 5, 14, 40)

print(t1 - t2)

print(t1.tzinfo)