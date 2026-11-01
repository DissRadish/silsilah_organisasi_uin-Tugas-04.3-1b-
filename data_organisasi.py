from node import Node
from tree import StrukturOrganisasiTree

def inisialisasi_organisasi_uin():
    """Fungsi untuk membangun struktur awal organisasi UIN Suska Riau"""
    rektor = Node("001", "Prof. Dr. H. Edi Erwan", "Rektor (Root)")
    org_tree = StrukturOrganisasiTree(rektor)

    # Tingkat Rektorat & Senat
    org_tree.insert_node("Rektor (Root)", Node("002", "Senat Universitas", "Senat Universitas"))
    org_tree.insert_node("Rektor (Root)", Node("003", "Dr. Zulkifli", "Wakil Rektor I (Bidang Akademik)"))
    org_tree.insert_node("Rektor (Root)", Node("004", "Dr. M. Ali", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)"))
    org_tree.insert_node("Rektor (Root)", Node("005", "Dr. Alex", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)"))
    org_tree.insert_node("Rektor (Root)", Node("006", "Dr. Cut Dewi", "Dekan Fakultas Sains dan Teknologi"))

    # Tingkat Dekanat FST
    org_tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("007", "Dr. Aulia", "Wakil Dekan I (Bidang Akademik & Kelembagaan)"))
    org_tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("008", "Dr. Rahmat", "Wakil Dekan II (Bidang AUPK)"))
    org_tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("009", "Dr. Fitri", "Wakil Dekan III (Bidang Kemahasiswaan)"))
    org_tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("010", "Dr. M. Afdhal", "Ketua Program Studi Teknik Informatika"))

    # Tingkat Program Studi & Lab
    org_tree.insert_node("Ketua Program Studi Teknik Informatika", Node("011", "Siti, M.T.", "Sekretaris Program Studi"))
    org_tree.insert_node("Ketua Program Studi Teknik Informatika", Node("012", "Budi, M.Kom.", "Kepala Laboratorium Komputer"))
    org_tree.insert_node("Kepala Laboratorium Komputer", Node("013", "Ahmad", "Asisten Laboratorium"))
    org_tree.insert_node("Kepala Laboratorium Komputer", Node("014", "Doni", "Teknisi Laboratorium"))

    # Tingkat Dosen & Mahasiswa
    org_tree.insert_node("Ketua Program Studi Teknik Informatika", Node("015", "Dr. Irwan", "Koordinator Dosen"))
    org_tree.insert_node("Koordinator Dosen", Node("016", "Dr. Rahma", "Dosen Pembimbing Akademik"))
    org_tree.insert_node("Dosen Pembimbing Akademik", Node("017", "Radish (Mahasiswa)", "Mahasiswa Bimbingan (Leaf)"))
    org_tree.insert_node("Koordinator Dosen", Node("018", "Dr. Zaki", "Dosen Pengampu Mata Kuliah"))

    return org_tree