from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


t_kalimat = [["K", "SPO"],
          ["K", "SPOpel"],
          ["K", "SPKet"],
          ["K", "SP"],
          ["K", "SPpel"],
          ["K", "SPOKet"]]

rules = [["S", "Noun", "Pronoun", "PropNoun", "NounAdj", "NounVerb", "Num", "NounPropNoun", "NounPronoun", "NounNum", "AdvNoun", "NounNoun"],
        ["P", "Verb", "VerbNoun", "Adj", "AdvVerb", "AdvAdjVerb", "AdjAdv", "AdjPronoun", "AdvAdvAdj", "AdvAdjNoun", "AdvAdjNum", "Adv"],
        ["O", "Noun", "Pronoun", "PropNoun", "NounAdj", "NounVerb", "Num", "NounPropNoun", "NounPronoun", "NounNum", "AdvNoun", "NounNoun"],
        ["pel", "VerbNoun", "Adj", "Verb", "AdjAdv", "AdjPronoun", "AdvAdvAdj", "PrepNoun", "PrepAdvAdj", "PrepNum"],
        ["Ket", "PrepPronoun", "PrepNoun", "PrepAdj", "PrepNum", "PrepAdvAdj"]]

noun = "Noun | adik | buaya | kelas | orang | desa | ibu | badan | badanku | anjing | wajan | paman | polisi | harta | suami | kamar | kaki | gedung | drum | potongan | kayu | kotak | bola | rumah | permen | kain | buku | rambut | tangan | pantai | perumahan | tubuh | sendok | meja | kolam | sepatu | mobil | kesayangan | warna | cokelat | merah | baju | kain | gorden | bibi | laptop | keranjang | pria | kemeja | bibir | ayah | pintu | dapur | mata | orang | langit | waktu | fajar | bagian | bawah | kue | tangkai | sapu | baju | pengantin | rambut | boneka | anak | jaket | lihat | hidup | dadu | koin | tanah | topi | pesta | buah | terung | wajah | cermin | lensa | kamera | persegi | kura-kura | pidato | bapak | seminar | bocah | pintu | rumah | orang | usia | guci | ketua | periode | barang | lapangan | teman | pohon | mangga | rumah-rumah | jeda | daki | celana | kursi | TV | ular | rongga | mulut | sakura | tembok | kemenangan | kemarin | rumah | petir | hukuman | malam | Ayah | kucing | keputusan | prestasi | sifat | keberhasilan | hal | kisah | perjuangan | Ibu | suara | masakan | parfum | bunga | nanas | motor | lukisan | pisau | tembok | lantai | kulit | buku | obat | teh | tulisan | baju | layar | ingin | antara | bulan | dahulu | zaman | guru | matematika | kakek | kakek | ayah | makanan | gaun | biru | orang | kursi | tua | sepeda | meja | martabak | kampung | sepatu | murid | bapak | ibu | kucing | baju | merah | pak | guru | hunian | lurah | pencuri | polisi | tante | keripik | ikan | pasar | pekerjaan | kampung | sekolah | putri | mobil | adik | payung | hitam | kakak | karyawan | masakan | anak | sepeda | motor | rumah | otak | kematian | sedih | fasilitas | umum | kemarin | garam | roti | sifat | pohon | lampu | kota | sikap | juara | kabar | mereka | tembok | dapur | tahun | usul | kue | mungkin | kenyataan | mata | mahasiswa | korban | bencana | alam | uang | tugas | beban| kelas | gereja | pesta | kemarin | ujian | bola | dinding | peraturan | kuliah | penyakit | bantuan | kepanitiaan | sedih | vaksin | pramuka | pancasila | buku | lemari | audisi | puncak | rumah | mangga | lawan | ikan | ketenaran| setahun | pertandingan | prestasi | orang | sungai | hari | nanti | nenek | minggu | akhir | cupang | usia | tahun | warna | pidato | bapak | seminar | bocah | pintu | rasa | usia | guci | ketua | periode | barang | lapangan | temanku | pohon | tembok | jeda | daki | celana | kursi | tv | ular | rongga | mulut | sakura | kemenangan | petir | hukuman | malam | Ayah | kucing | keputusan | sifat | keberhasilan | hal | kisah | perjuangan | ibu | suara | masakan | parfum | bunga | nanas | motor | lukisan | pisau | lantai | kulit | obat | teh | tulisan | baju | layar | ingin | antara | bulan | ibu | makanan | hak | manusia | kultur | jaringan | wadah | sifat | masalah | presentasi | mobil | suara | ayah | barang | sepeda | adik | taman | rumah | gaun | acara | orang | pasar | motor | pekarangan | baju | sayur-sayuran | kursi | bengkel | atas | meja | harga | martabak | manis | pertigaan | jalan | kucing | kampung | sepatu | anaknya | bapak | guru | diri | pak | keliling | lapangan | pohon | jati | tubuh | mawar | rasa | air | laut | sekolah | hatin | hujan | celana | anak | permainan | siswa | kelas | keluarga | asap | rokok | pipi | kain | matahari | gadis | jendela | rumah | berita | senja | langit | gedung | kaki | kebun | bunga | bis | tangisan | bayi | kopi | gadis-gadis | pekerjaan | pertanyaan  |  kecamatam | paman"

verb = "Verb | membantu | menjadi | memakai | berwarna | menyukai | suka | mengecat | berubah | menjadi |  merupakan | melempar | memiliki | pulang | berjalan | tinggal | berlangsung | dimulai | belajar | membuka | mengetuk | berdebat | berpamitan | pergi | menginjak | adalah | membeli | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | sayang | melawan | melakukan | berteriak | merasa | ada | membenci | mengajar | tersebut | membawa | menggunakan | adalah | meduduki | ditaruh | membeli | berkeliaran | memperkenalkan | memberikan | menghukum | menangkap | membuat | dikenal | mendapatkan | menjadi | memiliki | mendengar | berprilaku | mewarnai | menolak | menyatakan | dibuat | menerima | dihukum | lulus | menjawab | mengungsi | mencuri | berlari | tidur | meminjam | mengerjakan | mengangkat | mengantuk | lalu | menang | melihat | berhasil | pulang | berjalan | tinggal | berlangsung | dimulai | belajar | membuka | mengetuk | berdebat | berpamitan | pergi | menginjak | adalah | membeli | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | dilewati | sayang | melawan | melakukan | berteriak | merasa | membawa | disebutkan | dilakukan | dijelaskan | melaju | menyukai | percaya | mengajak | pergi | tersebut | adalah | berhenti | mencuci | membeli | menggunakan | menduduki | diperbaiki | ditaruh | berkeliaran | menyuruh | murid | memperkenalkan | menghukum | lari | memiliki | turun | terkena | menjadi | membuat | merupakan | ada | menggembirakan | melangkahkan | belajar | menghampiri | berjalan | terdengar | mengerjakan | menjawab | berharga | tutup | ditutup | diam | bermain"

adj = "Adj | boros | ganas | kaya | kikir | miskin | ramah | rajin | sehat | jinak | baik | pintar | panas | dingin | kejam | malas | cocok | hemat | tamak | angkuh | bersih | berat | banyak | besar | kecil | tipis | tebal | panjang | pendek | mungil | luas | sempit | ideal | gemuk | kurus | ringan | jutek | lebar | dangkal | cokelat | merah | kekuning-kuningan | hijau | putih | abu-abu | ungu | hijau lumut | merah jambu | merah bata | kebiru-biruan | jingga | lembayung | putih lesi | hitam pekat | lentur | kaku | tinggi | tabung | balok | kubus |  lingkaran | kerucut | cembung | cekung | rata | bundar | datar | bulat | lonjong | panjang | baik | tua | rusak | bulat | manis | liar | baru | nakal | termuda | lihai | pedas | asin | dalam | kaya | mewah | cerdas | baik | terenak | mahal | umum | luas | kokoh | sakit | indah | kecewa | ketus | senang | panik | ramah | muda | sepi | tegas | semanis | setegar | berat | ragu | secepat | tenang | banyak | semampu | kuat | puas | bersih | lama | pudar | kotor | rajin | sakit | dewasa | merah | larut | lambat | singkat | perlahan | mendadak | baru | kuno | antik | primitif | lawas | lelet | dekat | jauh | akrab | lebat | rapat | besar | sempit | luas | bangga | bosan | takut | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | jahat | merdu | lezat | harum | semerbak | manis | asam | tampan | serak | bising | nyaring | indah | tajam | kasar | licin | halus | tebal | pahit | dingin | rapi | basah | lebar | hebat | suka | enak | asasi | jelas | steril | sombong | singkat | hijau | cepat | merdu | murah | baru | kecil | baik | tua | kotor | suka | segar | biru | rusak | bulat | mewah | mahal | liar | baru | nakal | kokoh | merah | asin | dekat | resah | gundah | kepanjangan | menyenangkan | basah | elok | bahagia | patah | pintar | harmonis | kemerahan | menyeramkan | kering | terik | langsing | besar | kebesaran | kemerah-merahan | megah | yakin | ragu-ragu | secepatnya | sebaik-baiknya | sungguh-sungguh | takut | malam | cepat | nyaring | panas | cantik | hati-hati | rajin | benar"

prep = "Prep | di | kepada | pada | dengan | di | jika | pada | dari | untuk | atas | kepada | terhadap | ke | pada | dalam | di | dari | dekat | ketika | sehingga | yang | karena | sejak | dengan | sejak | dalam | dengan | di | jika | pada | dari | saat | untuk | atas | kepada | terhadap | ke | pada | dalam | di | dari | karena | untuk"

adv = "Adv | sangat | sekali | paling | akan | cukup | sudah | sedikit | dengan | sudah | akan | segera | sedang | jarang | sering | sangat | sekali | selalu | agak | baru |  sangat | tidak | masih | sekali | sedang | sudah | sangat | telah | belum | akan | sedang | ingin | mau | harus | mesti | agak | sangat | cukup | terlalu | dengan | secara | begitu | akan | tidak | jangan | sangat | terlalu"

propnoun = "PropNoun | Budi | Ani | Toni | Asri | Adi | Budi | Wisnu | Dila | Pablo | Rani | Harto | Ayu | Jakarta | Dio | Dila | Bima | Doni | Diva | Nayla | Andi | Budi | Indra | Dalang | Upin | Saputra | Susi | Adi | Banu | Wahyu | Intan | Dara | Syifa | Kadek | Indah | Abi | Putri | Wati | Manda | Dian | Arya | Diah | Citra | Bali | Doni | Sultan | Adi | Andi | Jihan | David | Rina | Dina | Agus | Nanda | Saputra | Kinan | Ari | Gusde | Budi | Steven | Matthew | Wahyu | Roni | Dito | Jakarta | Andi | Indra | Upin | Saputra | Susi | Adi | Banu | Intan | Dara | Syifa | Kadek | Indah | Abi | Putri | Wati | Amanda | Dian | Arya | Diah | Citra | Bali | Gunggus | Agung | Wawan | Gung | Frady | Raindra | UUD 1945"

pronoun = "Pronoun | itu | ia | ini | atom | saya | aku | kami | dia | hamba | kami | kita | kamu | anda | engkau | kalian | beliau | mereka"

num = "Num | semua | suatu | setiap | banyak | satu | dua | tiga | empat | lima | enam | tujuh | delapan | sembilan"


# melakukan pemecahan string
data = [ ]
data.append(noun.split(" | "))
data.append(verb.split(" | "))
data.append(adj.split(" | "))
data.append(prep.split(" | ")) 
data.append(adv.split(" | "))
data.append(propnoun.split(" | "))
data.append(pronoun.split(" | "))
data.append(num.split(" | "))

# membuat list yang representasikan segitiga bawah
def listning(n : int) -> list:
  list1 = [ ]
  for i in range(n, 0, -1):
    list2 = [ ]
    for j in range(i):
      list2.append("")
    list1.append(list2)
  return list1

# # penggabungan 2 string
# def gabung(str1 : str, str2 : str) -> str:
#   str3 = ""
#   for i in str1:
#     for j in str2:
#       str3 = str3 + (i + j)
#   return str3

# mencari nilai unik pada string
def unique_str(str1 : str) -> str:
  str3 = ""
  for i in str1:
    if i not in str3:
        str3 = str3 + i
  return str3

# mengubah string dalam notasi kalimat
def converting(str1 : str, list1 : list) -> str:
  str2 = ""
  for i in range(len(list1[:])):
    for j in list1[i][1:]:
      if j in str1:
        str2 = str2 + list1[i][0]
  return unique_str(str2)

# inisiasi tabel filling, perubahan string ke notasi kalimat
def initiate(list1 : list, list2 : list, listning : list):
  for i in range(0, len(list1)):
    for j in range(len(list2)):
      for k in list2[j][1:]:
        if k == list1[i]:
          listning[i][0] = list2[j][0]
  return listning

# menambah string ke tabel filling
def kalkulasi(y : int, x : int, list1 : list):
  x -= 1
  y -= 1
  i = 0
  j = y + 1
  k = x - 1
  while(i < x):
    list1[y][x] = list1[y][i] + list1[j][k]
    i += 1
    j += 1
    k -= 1

# memproses array yang sudah diinisiasi pada fungsi initiate. Fungsi converting, mengubah string ke grammar
def progressing(list1 : list, x : int):
  leng = x
  for i in range(1, x+1):
    for j in range(1, leng+1):
      kalkulasi(j, i, list1)
    leng -= 1
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      alba = converting(alba, rules)
      list1[i][j] = alba
    leng -= 1

# memproses fungsi converting sekali lagi (menentukan nilai K sebagai penentuk kalimat baku)
def progressing2(list1 : list, x : int):
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      alba = converting(alba, t_kalimat)
      list1[i][j] = alba
    leng -= 1
  
  for i in range(0, x):
    print(list1[i][:])

# melakukan pengecekan nilai K pada array
def cek_baku(list1 : list) -> int:
  if "K" in list1[0][-1]:
    return 1
  elif "K" not in list1[0][-1]:
    return 0

# 
# def progressing_x(list2 : list):
#   count = 0
#   for list1 in list2:
#     tabel = listning(len(list1))
#     initiate(data, list1, tabel)
#     progressing(tabel, len(tabel[:]))
#     list1.append(cek_baku(tabel))
#     for i in range(len(list1)):
#       for x, j in enumerate(list1):
#         if j == 1:
#           count += 1
#   print(count)

# melakukan pengecekan kalimat 
def cek_kalimat(sentences):
  sentences = sentences.split(" ")
  tb = listning(len(sentences))
  testing = initiate(sentences, data, tb)
  progressing(testing, len(sentences))
  progressing2(testing, len(sentences))
  return cek_baku(testing)

# Create your views here.
@api_view(['POST'])
def checkCykController(request):
   return Response({"result":cek_kalimat(request.data["query"]) == 1})
