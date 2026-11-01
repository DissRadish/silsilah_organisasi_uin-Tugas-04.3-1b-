from node import Node
from data_organisasi import inisialisasi_organisasi_uin

def main():
    # Load data organisasi
    org_tree = inisialisasi_organisasi_uin()

    # MENU INTERAKTIF CLI
    while True:
        print("\n" + "="*50)
        print("   APLIKASI MANAJEMEN SILSILAH ORGANISASI UIN   ")
        print("="*50)
        print("1. Tampilkan Hasil Traversal (Preorder, Inorder, Postorder)")
        print("2. Cari Data Pegawai/Jabatan (search_node)")
        print("3. Tambah Jabatan Baru (insert_node)")
        print("4. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            print("\n--- HASIL ALGORITMA TRAVERSAL ---")
            print("\n[1] Pre-order Traversal:")
            print(org_tree.preorder_traversal(org_tree.root))
            
            print("\n[2] In-order Traversal:")
            print(org_tree.inorder_traversal(org_tree.root))
            
            print("\n[3] Post-order Traversal:")
            print(org_tree.postorder_traversal(org_tree.root))
            
        elif pilihan == "2":
            keyword = input("\nMasukkan nama atau jabatan yang dicari: ")
            hasil = org_tree.search_node(org_tree.root, keyword)
            if hasil:
                print(f"\n[DITEMUKAN] ID: {hasil.id_pegawai} | Nama: {hasil.nama} | Jabatan: {hasil.jabatan}")
            else:
                print("\n[TIDAK DITEMUKAN] Data tersebut tidak ada dalam silsilah organisasi.")
                
        elif pilihan == "3":
            print("\n--- FORM TAMBAH JABATAN BARU ---")
            atasan = input("Masukkan nama jabatan atasan (misal: Ketua Program Studi Teknik Informatika): ")
            nid = input("Masukkan ID Pegawai baru: ")
            nnama = input("Masukkan Nama Pegawai baru: ")
            njab = input("Masukkan Nama Jabatan baru: ")
            org_tree.insert_node(atasan, Node(nid, nnama, njab))
            
        elif pilihan == "4":
            print("\nKeluar dari program. Terima kasih!")
            break
        else:
            print("\nPilihan tidak valid, silakan masukkan angka 1-4.")

if __name__ == "__main__":
    main()