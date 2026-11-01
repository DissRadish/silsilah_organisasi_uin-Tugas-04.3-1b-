class Node:
    """Kelas untuk merepresentasikan setiap simpul/jabatan dalam organisasi"""
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.children = []  # List untuk menampung node anak/bawahan

    def tambah_anak(self, child_node):
        """Menyisipkan node anak/bawahan ke list children"""
        self.children.append(child_node)