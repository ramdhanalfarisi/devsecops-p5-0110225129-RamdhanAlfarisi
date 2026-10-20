from tasktracker.service import TaskService

def display_menu():
    print("\n=== TASK TRACKER CLI ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

def run_cli(service: TaskService):
    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ").strip()
        if choice == "1":
            title = input("Masukkan judul: ")
            desc = input("Masukkan deskripsi: ")
            task = service.create_task(title, desc)
            print(f"[+] Tugas berhasil ditambahkan dengan ID: {task.id}")
        elif choice == "2":
            tasks = service.list_tasks()
            for t in tasks:
                print(f"[{t.id}] {t.title} - Status: {t.status}")
        elif choice == "5":
            break