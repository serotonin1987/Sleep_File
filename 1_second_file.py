import time
from concurrent.futures import ThreadPoolExecutor

def create_file(index):
    time.sleep(1)
    with open(f"file_{index}.txt", "w") as f:
        f.write(f"Файл номер {index}")

print("▶ Последовательный запуск...")
start = time.time()
for i in range(100):
    create_file(i)
end = time.time()
print(f" Последовательно: {end - start:.2f} сек\n")

print("▶ Многопоточный запуск...")
start = time.time()
with ThreadPoolExecutor() as executor:
    executor.map(create_file, range(100))
end = time.time()
print(f" Многопоточно: {end - start:.2f} сек")
