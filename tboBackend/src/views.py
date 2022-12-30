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

noun = "Noun | adik | buaya | kelas | orang | desa | ibu | badan | anjing | wajan | paman | polisi | harta | suami | kamar | kaki | kakimu | gedung | drum | potongan | kayu | kotak | bola | rumah | permen | kain | buku | rambut | tangan | pantai | perumahan | tubuh | sendok | meja | kolam | sepatu | mobil | kesayangan | warna | baju | gorden | bibi | laptop | keranjang | pria | kemeja | bibir | ayah | pintu | dapur | mata | langit | waktu | fajar | bagian | bawah | kue | tangkai | sapu | pengantin | boneka | anak | jaket | kulihat | hidup | dadu | koin | tanah | topi | pesta | buah | terung | wajah | cermin | lensa | kamera | atom | kura-kura | pidato | bapak | seminar | bocah | usia | guci | ketua | periode | barang | lapangan | teman | pohon | mangga | rumah-rumah | jeda | daki | celana | kursi | TV | ular | rongga | mulut | sakura | tembok | kemenangan | kemarin | petir | hukuman | malam | kucingnya | keputusan | prestasinya | keberhasilan | hal | kisah | perjuangan | suara | masakan | parfum | bunga | nanas | motor | lukisan | pisau | tembok | lantai | kulit | obat | teh | tulisan | layar | ingin | antara | bulan | dahulu | zaman | guru | saat | matematika | kakek | kemarin | ujian | dinding | peraturan | kuliah | penyakit | bantuan | kepanitiaan | sedih | vaksin | pramuka | pancasila | lemari | audisi | puncak | mangga | lawan | ikan | ketenarannya | setahun | pertandingan | prestasinya | sungai | hari | nanti | nenek | minggu | akhir | cupang | tahun | periode | barang | lapangan | temanku | pohon | tembok | jeda | daki | celana | kursi | tv | ular | rongga | mulut | kemenangan | petir | hukuman | kucingnya | keputusan | sifat | keberhasilan | hal | kisah | perjuangan | suara | masakan | parfum | bunga | nanas | motor | lukisan | pisau | kulit | obat | teh | tulisan | layar | ingin | antara | bulan | dia | kakek |  makanan | gaun | biru | kursi | tua | sepeda | martabak | kampung | murid | kucing | pak | guru | hunian | lurah | pencuri | tante | keripik | ikan | pasar | pekerjaan | kampung | sekolah | putri | payung | hitam | kakak | karyawan | masakan | sepeda | motor | otak | kematian | sedih | fasilitas | umum | kemarin | garam | roti | pohon | lampu | kota | sikap | juara | kabar | mereka | tembok | usul | mungkin | kenyataan | mahasiswa | korban | bencana | alam | uang | tugas | beban| gereja | makanan | hak | manusia | UUD | 1945 | kultur | jaringan | wadah | masalah | presentasi | suara | barang | sepeda | taman | bermain |dia | gaun | acara | pasar | motor | pekarangan | sayur-sayuran | kursi | bengkel | atas | harga | martabak | manis | pertigaan | jalan | kucing | kampung | kami | guru | diri | pak | keliling | lapangan | pohon | jati | mawar | rasa | air | laut | sekolahku | hatinya | hujan | celana | permainan | siswa | keluarga | asap | rokok | pipi | kainnya | matahari | gadis | jendela | berita | senja | kebun | bunga | bis | tangisan | bayi | kopinya | gadis-gadis | pekerjaan | pertanyaan | meter"

verb = "Verb | membantu | menjadi | memakai | berwarna | menyukai | suka | mengecat | berubah | menjadi |  merupakan | melempar | memiliki | pulang | berjalan | tinggal | berlangsung | dimulai | belajar | membuka | mengetuk | berdebat | berpamitan | pergi | menginjak | adalah | membeli | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | sayang | melawan | melakukan | berteriak | merasa | ada | membenci | mengajar | tersebut | lalu | menang | melihat | berhasil | berjalan | tinggal | berlangsung | dimulai | belajar | membuka | mengetuk | berdebat | berpamitan | pergi | menginjak | adalah | membeli | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | dilewati | sayang | melawan | melakukan | berteriak | merasa | membawa | menggunakan | adalah | meduduki | ditaruh | membeli | berkeliaran | memperkenalkan | memberikan | menghukum | menangkap | membuat | dikenal | mendapatkan |menjadi | memiliki | mendengar | berprilaku | mewarnai | menolak | menyatakan | dibuat | menerima | dihukum | lulus | menjawab | mengungsi | mencuri | berlari | tidur | meminjam | mengerjakan | mengangkat | mengantuk | membawa | disebutkan | dilakukan | dijelaskan | melaju | menyukai | percaya | mengajak | pergi | tersebut | adalah | berhenti | mencuci | membeli | menggunakan | menduduki | diperbaiki | ditaruh | berkeliaran | menyuruh | murid | memperkenalkan | menghukum | lari | memiliki | turun | terkena | menjadi | membuat | merupakan | ada | menggembirakan | melangkahkan | belajar | menghampiri | berjalan | terdengar | mengerjakan | menjawab | berharga | berukuran | ulang | berbentuk"

adj = "Adj | boros | ganas | kaya | kikir | miskin | ramah | rajin | sehat | jinak | baik | pintar | panas | dingin | kejam | malas | cocok | hemat | tamak | angkuh | bersih | berat | banyak | besar | kecil | tipis | tebal | panjang | pendek | mungil | luas | sempit | ideal | gemuk | kurus | ringan | jutek | lebar | dangkal | cokelat | merah | kekuning-kuningan | hijau | putih | abu-abu | ungu | hijau lumut | merah jambu | merah bata | kebiru-biruan | jingga | lembayung | putih lesi | hitam pekat | lentur | kaku | tinggi | tabung | balok | kubus | persegi | lingkaran | kerucut | cembung | cekung | rata | bundar | datar | bulat | lonjong | persegi-panjang | larut | lambat | lama | singkat | perlahan | mendadak | baru | kuno | antik | primitif | lawas | lelet | dekat | jauh | akrab | lebat | rapat | besar | sempit | luas | bangga | bosan | takut | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | jahat | merdu | lezat | harum | semerbak | manis | asam | tampan | serak | bising | nyaring | indah | tajam | kasar | licin | halus | tebal | pahit | dingin | rapi | basah | lebar | hebat | suka | puas | bersih | lama | pudar | kotor | rajin | sakit | dewasa | larut | lambat | singkat | perlahan | mendadak | baru | kuno | antik | primitif | lawas | lelet | dekat | jauh | akrab | lebat | rapat | besar | sempit | luas | bangga | bosan | takut | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | jahat | merdu | lezat | harum | semerbak | manis | asam | tampan | serak | bising | nyaring | indah | tajam | kasar | licin | halus | tebal | pahit | dingin | rapi | basah | lebar | hebat | suka | baik | tua | rusak | manis | liar | baru | nakal | termuda | lihai | pedas | asin | dalam | kaya | mewah | cerdas | baik | terenak | mahal | umum | luas | kokoh | sakit | indah | kecewa | ketus | senang | panik | ramah | muda | sepi | tegas | semanis | setegar | berat | ragu | secepat | tenang | banyak | semampu | kuat | enak | asasi | jelas | steril | sombong | singkat | hijau | cepat | merdu | murah | baru | kecil | baik | tua | kotor | suka | segar | biru | rusak | mewah | mahal | liar | baru | nakal | kokoh | asin | dekat | resah | gundah | kepanjangan | menyenangkan | basah | elok | bahagia | patah | pintar | harmonis | kemerahan | menyeramkan | kering | terik | langsing | besar | kebesaran | kemerah-merahan | megah | yakin | ragu-ragu | secepatnya | sebaik-baiknya | sungguh-sungguh | takut | malam | cepat | nyaring | panas | cantik | hati-hati | rajin | benar"

prep = "Prep | di | kepada | pada | saat | dengan | jika | dari | untuk | atas | terhadap | dalam | sejak | ke | dekat | ketika | sehingga | yang | karena"

adv = "Adv | sangat | sekali | paling | akan | cukup | sedikit | dengan | sudah | segera | sedang | jarang | sering | selalu | agak | baru | telah | belum | ingin | mau | harus | mesti | terlalu | tidak | masih | rasa | diam | secara | begitu | jangan | sekitar"

propnoun = "PropNoun | Budi | Ani | Toni | Asri | Adi | Wisnu | Dila | Pablo | Rani | Harto | Ayu | Jakarta | Dio | Bima | Doni | Diva | Nayla | Andi | Indra | Dalang | Upin | Saputra | Susi | Banu | Wahyu | Intan | Dara | Syifa | Kadek | Indah | Abi | Putri | Wati | Manda | Dian | Arya | Diah | Citra | Bali | Steven | Matthew | Wahyu | Roni | Dito | Susi | Banu | Intan | Dara | Syifa | Kadek | Indah | Abi | Putri | Wati | Amanda | Dian | Arya | Citra | Sultan | Jihan | David | Rina | Dina | Agus | Nanda | Kinan | Ari | Gusde | Gunggus | Agung | Wawan | Gung | Frady | Raindra | Burj | Khalifa"

pronoun = "Pronoun | itu | ia | ini | saya | aku | kami | hamba | kita | kamu | anda | engkau | kalian | dia | beliau | mereka"

num = "Num | semua | sembilan | banyak | suatu | setiap | satu | dua | tiga | empat | lima | enam | tujuh | delapan | 828"


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
