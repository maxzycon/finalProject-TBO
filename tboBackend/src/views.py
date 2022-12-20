from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


t_kalimat = [["K", "SPO"],
          ["K", "SPOpel"],
          ["K", "SPKet"],
          ["K", "SP"]]

rules = [["S", "Noun", "Pronoun", "PropNoun", "NounAdj"],
        ["P", "Verb", "VerbNoun", "Adj"],
        ["O", "Noun", "Pronoun", "PropNoun", "NounAdj"],
        ["pel", "VerbNoun", "Adj", "Verb"],
        ["Ket", "PrepPronoun", "PrepNoun", "PrepAdj", "PrepNum"]]

noun = "Noun | adik | buaya | kelas | orang | desa | ibu | badan | anjing | wajan | paman | polisi | harta | suami | kamar | kaki | kakimu | gedung | drum | potongan | kayu | kotak | bola | rumah | permen | kain | buku | rambut | tangan | pantai | perumahan | tubuh | sendok | meja | kolam | sepatu | mobil | kesayangan | warna | cokelat | merah | baju | kain | gorden | bibi | laptop | keranjang | pria | kemeja | bibir | ayah | pintu | dapur | mata | orang | langit | waktu | fajar | bagian | bawah | kue | tangkai | sapu | baju | pengantin | rambut | boneka | anak | jaket | kulihat | hidup | dadu | koin | tanah | topi | pesta | buah | terung | wajah | cermin | lensa | kamera | atom"
verb = "Verb | membantu | menjadi | memakai | berwarna | menyukai | suka | mengecat | berubah | menjadi |  merupakan | melempar | memiliki"
adj = "Adj | boros | ganas | kaya | kikir | miskin | ramah | rajin | sehat | jinak | baik | pintar | panas | dingin | kejam | malas | cocok | hemat | tamak | angkuh | bersih | berat | banyak | besar | kecil | tipis | tebal | panjang | pendek | mungil | luas | sempit | ideal | gemuk | kurus | ringan | jutek | lebar | dangkal | cokelat | merah | kekuning-kuningan | hijau | putih | abu-abu | ungu | hijau lumut | merah jambu | merah bata | kebiru-biruan | jingga | lembayung | putih lesi | hitam pekat | lentur | kaku | tinggi | tabung | balok | kubus | persegi | lingkaran | kerucut | cembung | cekung | rata | bundar | datar | bulat | lonjong | persegi panjang"
prep = "Prep | di | kepada | pada | saat"
adv = "Adv | sangat | sekali | paling | akan | cukup | sudah | sedikit | dengan"
propnoun = "PropNoun | Budi | Ani | Toni | Asri | Adi | Budi | Wisnu | Dila | Pablo | Rani | Harto | Ayu | Jakarta | Dio | Dila | Bima | Doni | Diva | Nayla"
pronoun = "Pronoun | itu | ia | ini | saya"
num = "Num | semua" 


data = [ ]
data.append(noun.split(" | "))
data.append(verb.split(" | "))
data.append(adj.split(" | "))
data.append(prep.split(" | ")) 
data.append(adv.split(" | "))
data.append(propnoun.split(" | "))
data.append(pronoun.split(" | "))

def array(n : int) -> list:
  list1 = [ ]
  for i in range(n, 0, -1):
    list2 = [ ]
    for j in range(i):
      list2.append("")
    list1.append(list2)
  return list1

def concat_str(str1 : str, str2 : str) -> str:
  str3 = ""
  for i in str1:
    for j in str2:
      str3 = str3 + (i + j)
  return str3

def unique_str(str1 : str) -> str:
  str3 = ""
  for i in str1:
    if i not in str3:
        str3 = str3 + i
  return str3

def converting(str1 : str, list1 : list) -> str:
  str2 = ""
  for i in range(len(list1[:])):
    for j in list1[i][1:]:
      if j in str1:
        str2 = str2 + list1[i][0]
  return unique_str(str2)

def initiate(list1 : list, list2 : list, array : list):
  for i in range(0, len(list1)):
    for j in range(len(list2)):
      for k in list2[j][1:]:
        if k in list1[i]:
          array[i][0] = list2[j][0]
  return array

def calculate(y : int, x : int, list1 : list):
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

def progressing(list1 : list, x : int):
  leng = x
  for i in range(1, x+1):
    for j in range(1, leng+1):
      calculate(j, i, list1)
    leng -= 1
  leng = x
  for i in range(0, x):
    for j in range(1, leng):
      alba = list1[i][j]
      alba = converting(alba, rules)
      list1[i][j] = alba
    leng -= 1

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

def cek_baku(list1 : list) -> int:
  if "K" in list1[0][-1]:
    return 1
  elif "K" not in list1[0][-1]:
    return 0

def progressing_x(list2 : list):
  count = 0
  for list1 in list2:
    tabel = array(len(list1))
    initiate(data, list1, tabel)
    progressing(tabel, len(tabel[:]))
    list1.append(cek_baku(tabel))
    for i in range(len(list1)):
      for x, j in enumerate(list1):
        if j == 1:
          count += 1
  print(count)

def cek_kalimat(strinx):
  strinx = strinx.split(" ") 
  ar = array(len(strinx))
  test = initiate(strinx, data, ar)
  progressing(test, len(strinx))
  progressing2(test, len(strinx))
  return cek_baku(test)

# Create your views here.
@api_view(['POST'])
def checkCykController(request):
   return Response({result:cek_kalimat(request.data["query"]) == 1})
