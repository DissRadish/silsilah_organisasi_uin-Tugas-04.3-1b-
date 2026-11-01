class StrukturOrganisasiTree:
    """Kelas untuk mengelola struktur Tree organisasi secara keseluruhan"""
    def __init__(self, root_node):
        self.root = root_node

    def insert_node(self, target_jabatan_atasan, new_node):
        """Menyisipkan pegawai baru di bawah atasan tertentu"""
        atasan = self.search_node(self.root, target_jabatan_atasan)
        if atasan:
            atasan.tambah_anak(new_node)
            print(f"\n[SUKSES] Berhasil menambahkan '{new_node.jabatan} - {new_node.nama}' di bawah '{atasan.jabatan}'")
        else:
            print(f"\n[GAGAL] Atasan dengan jabatan '{target_jabatan_atasan}' tidak ditemukan.")

    def search_node(self, current_node, keyword):
        """Mencari data pegawai berdasarkan nama atau jabatannya"""
        if not current_node:
            return None
        
        # Pencarian case-insensitive
        if current_node.jabatan.lower() == keyword.lower() or current_node.nama.lower() == keyword.lower():
            return current_node

        for child in current_node.children:
            hasil = self.search_node(child, keyword)
            if hasil:
                return hasil
        return None

    def preorder_traversal(self, node, result=None):
        """Preorder Traversal (Root -> Anak)"""
        if result is None:
            result = []
        if node:
            result.append(f"{node.jabatan} ({node.nama})")
            for child in node.children:
                self.preorder_traversal(child, result)
        return result

    def inorder_traversal(self, node, result=None):
        """Inorder Traversal (Anak Kiri -> Root -> Anak Kanan)"""
        if result is None:
            result = []
        if node:
            if len(node.children) > 0:
                self.inorder_traversal(node.children[0], result)
            result.append(f"{node.jabatan} ({node.nama})")
            for child in node.children[1:]:
                self.inorder_traversal(child, result)
        return result

    def postorder_traversal(self, node, result=None):
        """Postorder Traversal (Anak -> Root)"""
        if result is None:
            result = []
        if node:
            for child in node.children:
                self.postorder_traversal(child, result)
            result.append(f"{node.jabatan} ({node.nama})")
        return result