import re

class LicensePlateSplitter:  
  def __init__(self):
      self.license_plate_numbers = {
          'AA': 'Purworejo, Temanggung, Magelang, Wonosobo, kebumen, Kedu',
          'AD': 'Surakarta, Boyolali, Wonogiri, Sukoharjo, Karanganyar, Sragen, Klaten',
          'K': 'Pati, Kudus, Cepu, Jepara, Grobogan, Rembang, Blora',
          'AA': 'Purworejo, Temanggung, Magelang, Wonosobo, kebumen, Kedu',
          'AD': 'Surakarta, Boyolali, Wonogiri, Sukoharjo, Karanganyar, Sragen, Klaten',
          'K': 'Pati, Kudus, Cepu, Jepara, Grobogan, Rembang, Blora',
          'R': 'Banjarnegara, Banyumas, Cilacap, Purbalingga',
          'G': 'Brebes, Pemalang, Batang, Tegal, Pekalongan',
          'H': 'Semarang, Salatiga, Kendal, Demak','AB': 'Yogyakarta',
          'D': 'Bandung, Cimahi',
          'F': 'Bogor, Sukabumi, Cianjur',
          'E': 'Kuningan, Cirebon, Majalengka, Indramayu',
          'Z': 'Banjar, Garut, Ciamis, Tasikmalaya, Sumedang',
          'T': 'Subang, Purwakarta, Karawang',
          'A': 'Banten, Tangerang, Cilegon, Lebak, Serang, Pandeglang',
          'B': 'DKI Jakarta, Bekasi, Depok',
          'AG': 'Tulungagung, Kediri, Blitar, Trenggalek, Nganjuk',
          'AE': 'Ngawi, Madiun, Pacitan, Ponorogo, Magetan',
          'L': 'Jawa timur, Surabaya',
          'M': 'Madura, Bangkalan, Sampang, Sumenep, Pamekasan',
          'N': 'Malang, Pasuruan, Probolinggo, Batu, Lumajang',
          'S': 'Jombang, Bojonegoro, Lamongan, Mojokerto',
          'W': 'Gresik, Sidoarjo',
          'P': 'Banyuwangi, Besuki, Bondowoso, Jember, situbondo',
          'DK': 'Bali',
          'ED': 'Sumba Timur',
          'EA': 'Sumbawa, Bima, Dompu',
          'EB': 'Nusa Tenggara, Flores',
          'DH': 'Kupang, Rote Ndao, Timor',
          'DR': 'Lombok, Mataram',
          'KU': 'Kalimantan Utara',
          'KT': 'Kalimantan Timur',
          'DA': 'Kalimantan Selatan',
          'KB': 'Kalimantan Barat',
          'KH': 'Kalimantan Tengah',
          'DC': 'Sulawesi Barat',
          'DD': 'Sulawesi selatan',
          'DN': 'Sulawesi Tengah',
          'DT': 'Sulawesi Tenggara',
          'DL': 'Sitaro, Talaud, Sangihe',
          'DM': 'Gorontalo',
          'DB': 'Manado, Minahasa, Tomohon, Bolaang Mongondow',
          'BA': 'Sumatera Barat',
          'BB': 'Sumatera Utara bagian barat',
          'BD': 'Bengkulu',
          'BE': 'Lampung',
          'BG': 'Sumatera Selatan bagian timur',
          'BH': 'Jambi',
          'BK': 'Sumatera Utara',
          'BL': 'Aceh',
          'BM': 'Riau',
          'BN': 'Bangka Belitung',
          'BP': 'Kepulauan Riau',
          'DE': 'Maluku',
          'DG': 'Mauku Utara',
          'PA': 'Papua',
          'PB': 'Papua Barat',
          }
      
  def split_license_plate_numbers(self, data):
      # Define the regular expression pattern
      pattern = r'([A-Za-z]{1,2})\s*(\d{1,4})\s*([A-Za-z]{1,3})'

      # Search for the pattern in the input data
      matches = re.findall(pattern, data)

      # Extract the three parts of each license plate number from the matches
      result = []
      for match in matches:
          part1, part2, part3 = self.extract_parts(match)
          location = self.get_location(part1)
          result.append((location))

      return result

  def extract_parts(self, match):
      part1 = match[0]
      part2 = match[1]
      part3 = match[2]
      return part1, part2, part3

  def get_location(self, part1):
      return self.license_plate_numbers.get(part1, 'Unknown Location')
