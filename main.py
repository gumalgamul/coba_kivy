from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
import random, time
layar=Window.size


Soal1 = {
    'pertanyaan': 'Apa ibu kota negara Indonesia?',
    'pilihanGanda': ['a. Jakarta', 'b. Surabaya', 'c. Bandung', 'd. Medan'],
    'jawaban': 'a. Jakarta'
}

Soal2 = {
    'pertanyaan': 'Siapa penulis novel "Laskar Pelangi"?',
    'pilihanGanda': ['a. Tere Liye', 'b. Andrea Hirata', 'c. Pramoedya Ananta Toer', 'd. Dewi Lestari'],
    'jawaban': 'b. Andrea Hirata'
}

Soal3 = {
    'pertanyaan': 'Planet apa yang dikenal sebagai planet merah?',
    'pilihanGanda': ['a. Bumi', 'b. Mars', 'c. Venus', 'd. Jupiter'],
    'jawaban': 'b. Mars'
}

Soal4 = {
    'pertanyaan': 'Apa nama gunung tertinggi di dunia?',
    'pilihanGanda': ['a. Gunung Kilimanjaro', 'b. Gunung Elbrus', 'c. Gunung Everest', 'd. Gunung Fuji'],
    'jawaban': 'c. Gunung Everest'
}

Soal5 = {
    'pertanyaan': 'Siapa presiden pertama Republik Indonesia?',
    'pilihanGanda': ['a. Soeharto', 'b. B.J. Habibie', 'c. Abdurrahman Wahid', 'd. Soekarno'],
    'jawaban': 'd. Soekarno'
}

Soal6 = {
    'pertanyaan': 'Sungai terpanjang di dunia adalah?',
    'pilihanGanda': ['a. Sungai Amazon', 'b. Sungai Nil', 'c. Sungai Mississippi', 'd. Sungai Yangtze'],
    'jawaban': 'b. Sungai Nil'
}

Soal7 = {
    'pertanyaan': 'Dalam sistem periodik unsur, simbol kimia untuk emas adalah?',
    'pilihanGanda': ['a. Ag', 'b. Au', 'c. Fe', 'd. Hg'],
    'jawaban': 'b. Au'
}

Soal8 = {
    'pertanyaan': 'Negara mana yang memenangkan Piala Dunia FIFA 2018?',
    'pilihanGanda': ['a. Brasil', 'b. Jerman', 'c. Prancis', 'd. Argentina'],
    'jawaban': 'c. Prancis'
}

Soal9 = {
    'pertanyaan': 'Berapakah jumlah pulau di Indonesia menurut data Kementerian Dalam Negeri pada tahun 2021?',
    'pilihanGanda': ['a. 10.000 pulau', 'b. 13.466 pulau', 'c. 17.508 pulau', 'd. 20.000 pulau'],
    'jawaban': 'c. 17.508 pulau'
}

Soal10 = {
    'pertanyaan': 'Siapakah tokoh proklamator kemerdekaan Indonesia?',
    'pilihanGanda': ['a. Soekarno dan Moh. Hatta', 'b. Jendral Sudirman dan Moh. Hatta', 'c. Soekarno dan Jendral Sudirman', 'd. Soekarno dan Ki Hajar Dewantara'],
    'jawaban': 'a. Soekarno dan Moh. Hatta'
}

Soal11 = {
    'pertanyaan': 'Lagu kebangsaan Indonesia adalah?',
    'pilihanGanda': ['a. Indonesia Raya', 'b. Tanah Airku', 'c. Garuda Pancasila', 'd. Rayuan Pulau Kelapa'],
    'jawaban': 'a. Indonesia Raya'
}

Soal12 = {
    'pertanyaan': 'Siapa presiden ketiga Indonesia?',
    'pilihanGanda': ['a. Soekarno', 'b. Soeharto', 'c. B.J. Habibie', 'd. Megawati Soekarnoputri'],
    'jawaban': 'c. B.J. Habibie'
}

Soal13 = {
    'pertanyaan': 'Binatang tercepat di darat adalah?',
    'pilihanGanda': ['a. Singa', 'b. Kuda', 'c. Cheetah', 'd. Gazelle'],
    'jawaban': 'c. Cheetah'
}

Soal14 = {
    'pertanyaan': 'Berapakah jumlah warna pada pelangi?',
    'pilihanGanda': ['a. 5', 'b. 6', 'c. 7', 'd. 8'],
    'jawaban': 'c. 7'
}

Soal15 = {
    'pertanyaan': 'Ibu kota dari negara Jepang adalah?',
    'pilihanGanda': ['a. Tokyo', 'b. Osaka', 'c. Kyoto', 'd. Nagoya'],
    'jawaban': 'a. Tokyo'
}

Soal16 = {
    'pertanyaan': 'Siapa penemu bola lampu?',
    'pilihanGanda': ['a. Albert Einstein', 'b. Nikola Tesla', 'c. Thomas Alva Edison', 'd. Alexander Graham Bell'],
    'jawaban': 'c. Thomas Alva Edison'
}

Soal17 = {
    'pertanyaan': 'Dimana letak Menara Eiffel?',
    'pilihanGanda': ['a. London', 'b. Roma', 'c. Paris', 'd. Berlin'],
    'jawaban': 'c. Paris'
}

Soal18 = {
    'pertanyaan': 'Apa nama ibukota Australia?',
    'pilihanGanda': ['a. Sydney', 'b. Melbourne', 'c. Canberra', 'd. Perth'],
    'jawaban': 'c. Canberra'
}

Soal19 = {
    'pertanyaan': 'Benua terkecil di dunia adalah?',
    'pilihanGanda': ['a. Australia', 'b. Eropa', 'c. Antartika', 'd. Amerika Selatan'],
    'jawaban': 'a. Australia'
}

Soal20 = {
    'pertanyaan': 'Siapa penemu telepon?',
    'pilihanGanda': ['a. Albert Einstein', 'b. Nikola Tesla', 'c. Thomas Alva Edison', 'd. Alexander Graham Bell'],
    'jawaban': 'd. Alexander Graham Bell'
}

Soal21 = {
    'pertanyaan': 'Laut terbesar di dunia adalah?',
    'pilihanGanda': ['a. Laut China Selatan', 'b. Laut Karibia', 'c. Laut Kaspia', 'd. Laut Mediterania'],
    'jawaban': 'c. Laut Kaspia'
}

Soal22 = {
    'pertanyaan': 'Siapa pelukis terkenal dari lukisan "Mona Lisa"?',
    'pilihanGanda': ['a. Pablo Picasso', 'b. Vincent van Gogh', 'c. Leonardo da Vinci', 'd. Claude Monet'],
    'jawaban': 'c. Leonardo da Vinci'
}

Soal23 = {
    'pertanyaan': 'Dimanakah letak Piramida Agung Giza?',
    'pilihanGanda': ['a. Meksiko', 'b. Mesir', 'c. Yunani', 'd. India'],
    'jawaban': 'b. Mesir'
}

Soal24 = {
    'pertanyaan': 'Negara mana yang terkenal dengan julukan "Negeri Kincir Angin"?',
    'pilihanGanda': ['a. Belgia', 'b. Belanda', 'c. Denmark', 'd. Finlandia'],
    'jawaban': 'b. Belanda'
}

Soal25 = {
    'pertanyaan': 'Kapan Indonesia merdeka?',
    'pilihanGanda': ['a. 17 Agustus 1945', 'b. 17 Agustus 1950', 'c. 20 Mei 1945', 'd. 28 Oktober 1945'],
    'jawaban': 'a. 17 Agustus 1945'
}

Soal26 = {
    'pertanyaan': 'Apa nama mata uang resmi Jepang?',
    'pilihanGanda': ['a. Won', 'b. Yen', 'c. Rupiah', 'd. Baht'],
    'jawaban': 'b. Yen'
}

Soal27 = {
    'pertanyaan': 'Siapa ilmuwan yang menemukan teori relativitas?',
    'pilihanGanda': ['a. Isaac Newton', 'b. Galileo Galilei', 'c. Albert Einstein', 'd. Nikola Tesla'],
    'jawaban': 'c. Albert Einstein'
}

Soal28 = {
    'pertanyaan': 'Apa nama ibu kota Italia?',
    'pilihanGanda': ['a. Milan', 'b. Florence', 'c. Roma', 'd. Venesia'],
    'jawaban': 'c. Roma'
}

Soal29 = {
    'pertanyaan': 'Siapa penemu mesin uap?',
    'pilihanGanda': ['a. James Watt', 'b. Michael Faraday', 'c. Alessandro Volta', 'd. Nikola Tesla'],
    'jawaban': 'a. James Watt'
}

Soal30 = {
    'pertanyaan': 'Hewan apa yang dikenal sebagai mamalia terbesar di dunia?',
    'pilihanGanda': ['a. Gajah', 'b. Paus Biru', 'c. Jerapah', 'd. Hiu Paus'],
    'jawaban': 'b. Paus Biru'
}

Soal31 = {
    'pertanyaan': 'Negara mana yang terletak paling selatan di dunia?',
    'pilihanGanda': ['a. Australia', 'b. Argentina', 'c. Selandia Baru', 'd. Chili'],
    'jawaban': 'b. Argentina'
}

Soal32 = {
    'pertanyaan': 'Manakah dari berikut ini yang merupakan logam mulia?',
    'pilihanGanda': ['a. Besi', 'b. Tembaga', 'c. Emas', 'd. Aluminium'],
    'jawaban': 'c. Emas'
}

Soal33 = {
    'pertanyaan': 'Di negara mana Taj Mahal berada?',
    'pilihanGanda': ['a. India', 'b. Pakistan', 'c. Afghanistan', 'd. Bangladesh'],
    'jawaban': 'a. India'
}

Soal34 = {
    'pertanyaan': 'Berapakah jumlah pemain dalam satu tim sepak bola?',
    'pilihanGanda': ['a. 9', 'b. 10', 'c. 11', 'd. 12'],
    'jawaban': 'c. 11'
}

Soal35 = {
    'pertanyaan': 'Benua apa yang terbesar di dunia?',
    'pilihanGanda': ['a. Amerika Utara', 'b. Eropa', 'c. Afrika', 'd. Asia'],
    'jawaban': 'd. Asia'
}

Soal36 = {
    'pertanyaan': 'Sistem pemerintahan apa yang diterapkan di Indonesia?',
    'pilihanGanda': ['a. Monarki', 'b. Demokrasi', 'c. Oligarki', 'd. Anarki'],
    'jawaban': 'b. Demokrasi'
}

Soal37 = {
    'pertanyaan': 'Manakah negara yang bukan anggota ASEAN?',
    'pilihanGanda': ['a. Indonesia', 'b. Malaysia', 'c. Jepang', 'd. Thailand'],
    'jawaban': 'c. Jepang'
}

Soal38 = {
    'pertanyaan': 'Lagu “Bohemian Rhapsody” dibawakan oleh band apa?',
    'pilihanGanda': ['a. The Beatles', 'b. Queen', 'c. Rolling Stones', 'd. Pink Floyd'],
    'jawaban': 'b. Queen'
}

Soal39 = {
    'pertanyaan': 'Berapa lama waktu yang dibutuhkan Bumi untuk mengelilingi Matahari?',
    'pilihanGanda': ['a. 30 hari', 'b. 365 hari', 'c. 24 jam', 'd. 6 bulan'],
    'jawaban': 'b. 365 hari'
}

Soal40 = {
    'pertanyaan': 'Di manakah negara dengan jumlah penduduk terbanyak di dunia?',
    'pilihanGanda': ['a. Amerika Serikat', 'b. India', 'c. Cina', 'd. Rusia'],
    'jawaban': 'c. Cina'
}

Soal41 = {
    'pertanyaan': 'Gunung tertinggi di Indonesia adalah?',
    'pilihanGanda': ['a. Gunung Semeru', 'b. Gunung Kerinci', 'c. Gunung Jayawijaya', 'd. Gunung Merbabu'],
    'jawaban': 'c. Gunung Jayawijaya'
}

Soal42 = {
    'pertanyaan': 'Siapa yang menciptakan Facebook?',
    'pilihanGanda': ['a. Mark Zuckerberg', 'b. Bill Gates', 'c. Steve Jobs', 'd. Larry Page'],
    'jawaban': 'a. Mark Zuckerberg'
}

Soal43 = {
    'pertanyaan': 'Siapa presiden Amerika Serikat saat ini (2024)?',
    'pilihanGanda': ['a. Barack Obama', 'b. Donald Trump', 'c. Joe Biden', 'd. Kamala Harris'],
    'jawaban': 'c. Joe Biden'
}

Soal44 = {
    'pertanyaan': 'Dimana letak Benteng Rotterdam?',
    'pilihanGanda': ['a. Jakarta', 'b. Surabaya', 'c. Makassar', 'd. Medan'],
    'jawaban': 'c. Makassar'
}

Soal46 = {
    'pertanyaan': 'Siapa penulis novel "Harry Potter"?',
    'pilihanGanda': ['a. J.R.R. Tolkien', 'b. George R.R. Martin', 'c. J.K. Rowling', 'd. Stephen King'],
    'jawaban': 'c. J.K. Rowling'
}

Soal47 = {
    'pertanyaan': 'Apa nama ibu kota Brasil?',
    'pilihanGanda': ['a. Rio de Janeiro', 'b. Sao Paulo', 'c. Brasilia', 'd. Salvador'],
    'jawaban': 'c. Brasilia'
}

Soal48 = {
    'pertanyaan': 'Dalam sistem tata surya, planet apa yang berada paling dekat dengan Matahari?',
    'pilihanGanda': ['a. Venus', 'b. Mars', 'c. Merkurius', 'd. Bumi'],
    'jawaban': 'c. Merkurius'
}

Soal49 = {
    'pertanyaan': 'Apa nama laut yang membatasi Afrika dan Eropa?',
    'pilihanGanda': ['a. Laut Karibia', 'b. Laut Tengah', 'c. Laut Atlantik', 'd. Laut Hindia'],
    'jawaban': 'b. Laut Tengah'
}

Soal50 = {
    'pertanyaan': 'Siapa presiden pertama Indonesia?',
    'pilihanGanda': ['a. Soeharto', 'b. Sukarno', 'c. B.J. Habibie', 'd. Megawati Soekarnoputri'],
    'jawaban': 'b. Sukarno'
}

Soal51 = {
    'pertanyaan': 'Negara apa yang terkenal dengan Menara Eiffel?',
    'pilihanGanda': ['a. Inggris', 'b. Spanyol', 'c. Italia', 'd. Prancis'],
    'jawaban': 'd. Prancis'
}

Soal52 = {
    'pertanyaan': 'Siapa penyanyi lagu “Shape of You”?',
    'pilihanGanda': ['a. Ed Sheeran', 'b. Justin Bieber', 'c. Shawn Mendes', 'd. Bruno Mars'],
    'jawaban': 'a. Ed Sheeran'
}

Soal53 = {
    'pertanyaan': 'Apa ibu kota dari Korea Selatan?',
    'pilihanGanda': ['a. Busan', 'b. Incheon', 'c. Seoul', 'd. Daegu'],
    'jawaban': 'c. Seoul'
}

Soal54 = {
    'pertanyaan': 'Di manakah Menara Pisa berada?',
    'pilihanGanda': ['a. Roma', 'b. Milan', 'c. Pisa', 'd. Florence'],
    'jawaban': 'c. Pisa'
}

Soal55 = {
    'pertanyaan': 'Hewan apa yang paling cepat di darat?',
    'pilihanGanda': ['a. Cheetah', 'b. Singa', 'c. Kuda', 'd. Antelop'],
    'jawaban': 'a. Cheetah'
}

Soal56 = {
    'pertanyaan': 'Siapa penemu bola lampu?',
    'pilihanGanda': ['a. Thomas Edison', 'b. Alexander Graham Bell', 'c. Benjamin Franklin', 'd. Nikola Tesla'],
    'jawaban': 'a. Thomas Edison'
}

Soal57 = {
    'pertanyaan': 'Apa nama unsur kimia dengan simbol O?',
    'pilihanGanda': ['a. Oksigen', 'b. Ozon', 'c. Osmium', 'd. Organium'],
    'jawaban': 'a. Oksigen'
}

Soal58 = {
    'pertanyaan': 'Siapa tokoh utama dalam film "The Matrix"?',
    'pilihanGanda': ['a. Neo', 'b. Morpheus', 'c. Trinity', 'd. Smith'],
    'jawaban': 'a. Neo'
}

Soal59 = {
    'pertanyaan': 'Di manakah letak Patung Liberty?',
    'pilihanGanda': ['a. Los Angeles', 'b. Washington, D.C.', 'c. New York', 'd. Chicago'],
    'jawaban': 'c. New York'
}

Soal60 = {
    'pertanyaan': 'Apa ibu kota dari Thailand?',
    'pilihanGanda': ['a. Bangkok', 'b. Phnom Penh', 'c. Kuala Lumpur', 'd. Manila'],
    'jawaban': 'a. Bangkok'
}

Soal61 = {
    'pertanyaan': 'Planet apa yang dikenal sebagai "Planet Merah"?',
    'pilihanGanda': ['a. Bumi', 'b. Mars', 'c. Jupiter', 'd. Venus'],
    'jawaban': 'b. Mars'
}

Soal62 = {
    'pertanyaan': 'Siapa penyanyi lagu “Thriller”?',
    'pilihanGanda': ['a. Michael Jackson', 'b. Prince', 'c. Elton John', 'd. Freddie Mercury'],
    'jawaban': 'a. Michael Jackson'
}

Soal63 = {
    'pertanyaan': 'Bahasa apa yang paling banyak digunakan di dunia?',
    'pilihanGanda': ['a. Bahasa Inggris', 'b. Bahasa Spanyol', 'c. Bahasa Mandarin', 'd. Bahasa Hindi'],
    'jawaban': 'c. Bahasa Mandarin'
}

Soal64 = {
    'pertanyaan': 'Apa nama gunung tertinggi di dunia?',
    'pilihanGanda': ['a. Gunung Kilimanjaro', 'b. Gunung Elbrus', 'c. Gunung Everest', 'd. Gunung K2'],
    'jawaban': 'c. Gunung Everest'
}

Soal65 = {
    'pertanyaan': 'Di manakah piramida Mesir yang terkenal berada?',
    'pilihanGanda': ['a. Kairo', 'b. Giza', 'c. Luxor', 'd. Alexandria'],
    'jawaban': 'b. Giza'
}

Soal93 = {
    'pertanyaan': 'Negara manakah yang memiliki bendera merah putih?',
    'pilihanGanda': ['a. Indonesia', 'b. Jepang', 'c. Thailand', 'd. Malaysia'],
    'jawaban': 'a. Indonesia'
}

Soal94 = {
    'pertanyaan': 'Siapa penemu lampu neon?',
    'pilihanGanda': ['a. Thomas Edison', 'b. Nikola Tesla', 'c. George Claude', 'd. Alexander Graham Bell'],
    'jawaban': 'c. George Claude'
}

Soal45 = {
    'pertanyaan': 'Planet mana yang dikenal sebagai planet gas raksasa?',
    'pilihanGanda': ['a. Saturnus', 'b. Uranus', 'c. Jupiter', 'd. Neptunus'],
    'jawaban': 'a. Saturnus'
}

Soal66 = {
        'pertanyaan': 'Siapa penemu mesin uap?',
        'pilihanGanda': ['a. James Watt', 'b. Thomas Edison', 'c. Nikola Tesla', 'd. Alexander Graham Bell'],
        'jawaban': 'a. James Watt'
    }

Soal67 = {
        'pertanyaan': 'Apa nama ibukota Italia?',
        'pilihanGanda': ['a. Roma', 'b. Madrid', 'c. Paris', 'd. Berlin'],
        'jawaban': 'a. Roma'
    }
Soal68 = {
        'pertanyaan': 'Siapa penulis novel "1984"?',
        'pilihanGanda': ['a. Aldous Huxley', 'b. George Orwell', 'c. Ray Bradbury', 'd. J.D. Salinger'],
        'jawaban': 'b. George Orwell'
    }
Soal69 = {
        'pertanyaan': 'Apa nama lautan terbesar di dunia?',
        'pilihanGanda': ['a. Lautan Atlantik', 'b. Lautan Pasifik', 'c. Lautan Hindia', 'd. Lautan Arktik'],
        'jawaban': 'b. Lautan Pasifik'
    }
Soal70 = {
        'pertanyaan': 'Apa yang dimaksud dengan DNA?',
        'pilihanGanda': ['a. Asam Deoksiribonukleat', 'b. Asam Ribonukleat', 'c. Deoksiribonukleat Asam', 'd. Ribonukleat Asam'],
        'jawaban': 'a. Asam Deoksiribonukleat'
    }
Soal71 =  {
        'pertanyaan': 'Siapa yang dikenal sebagai Bapak Ilmu Pengetahuan?',
        'pilihanGanda': ['a. Isaac Newton', 'b. Albert Einstein', 'c. Galileo Galilei', 'd. Stephen Hawking'],
        'jawaban': 'a. Isaac Newton'
    }
Soal73 = {
        'pertanyaan': 'Apa nama alat yang digunakan untuk mengukur tekanan udara?',
        'pilihanGanda': ['a. Termometer', 'b. Barometer', 'c. Anemometer', 'd. Higrometer'],
        'jawaban': 'b. Barometer'
    }
Soal74 =  {
        'pertanyaan': 'Apa nama festival yang terkenal di Spanyol?',
        'pilihanGanda': ['a. Carnival', 'b. La Tomatina', 'c. Oktoberfest', 'd. Diwali'],
        'jawaban': 'b. La Tomatina'
    }
Soal75 = {
        'pertanyaan': 'Apa nama organ terbesar dalam tubuh manusia?',
        'pilihanGanda': ['a. Jantung', 'b. Hati', 'c. Kulit', 'd. Paru-paru'],
        'jawaban': 'c. Kulit'
    }
Soal76 = {
        'pertanyaan': 'Apa yang dimaksud dengan ekosistem?',
        'pilihanGanda': ['a. Hubungan antar makhluk hidup', 'b. Lingkungan tanpa makhluk hidup', 'c. Proses fotosintesis', 'd. Rantai makanan'],
        'jawaban': 'a. Hubungan antar makhluk hidup'
    }
Soal77 = {
        'pertanyaan': 'Siapa pemimpin perang kemerdekaan Indonesia?',
        'pilihanGanda': ['a. Soekarno', 'b. Jenderal Sudirman', 'c. R.A. Kartini', 'd. Sutan Sjahrir'],
        'jawaban': 'b. Jenderal Sudirman'
    }
Soal78 = {
        'pertanyaan': 'Apa nama hewan nasional Indonesia?',
        'pilihanGanda': ['a. Harimau', 'b. Garuda', 'c. Orangutan', 'd. Badak'],
        'jawaban': 'b. Garuda'
    }
Soal79 = {
        'pertanyaan': 'Apa nama benua terbesar di dunia?',
        'pilihanGanda': ['a. Eropa', 'b. Asia', 'c. Afrika', 'd. Amerika'],
        'jawaban': 'b. Asia'
    }
Soal80 = {
        'pertanyaan': 'Siapa yang menciptakan teori relativitas?',
        'pilihanGanda': ['a. Isaac Newton', 'b. Albert Einstein', 'c. Niels Bohr', 'd. Richard Feynman'],
        'jawaban': 'b. Albert Einstein'
    }
Soal81 = {
        'pertanyaan': 'Apa nama alat yang digunakan untuk mengukur suhu?',
        'pilihanGanda': ['a. Termometer', 'b. Barometer', 'c. Hygrometer', 'd. Anemometer'],
        'jawaban': 'a. Termometer'
    }
Soal82 = {
        'pertanyaan': 'Apa yang dimaksud dengan fotosintesis?',
        'pilihanGanda': ['a. Proses penyerapan air', 'b. Proses produksi makanan oleh tumbuhan', 'c. Proses pernapasan hewan', 'd. Proses pembuangan limbah'],
        'jawaban': 'b. Proses produksi makanan oleh tumbuhan'
    }
Soal83 = {
        'pertanyaan': 'Apa yang menjadi sumber energi utama bagi bumi?',
        'pilihanGanda': ['a. Bulan', 'b. Bintang', 'c. Matahari', 'd. Angin'],
        'jawaban': 'c. Matahari'
    }
Soal84 = {
        'pertanyaan': 'Siapa penulis lagu "Imagine"?',
        'pilihanGanda': ['a. Paul McCartney', 'b. John Lennon', 'c. Bob Dylan', 'd. Elton John'],
        'jawaban': 'b. John Lennon'
    }
Soal85 = {
        'pertanyaan': 'Apa yang dimaksud dengan tsunami?',
        'pilihanGanda': ['a. Gelombang laut besar', 'b. Angin kencang', 'c. Hujan deras', 'd. Banjir bandang'],
        'jawaban': 'a. Gelombang laut besar'
    }
Soal86 = {
        'pertanyaan': 'Apa nama ibukota Mesir?',
        'pilihanGanda': ['a. Kairo', 'b. Addis Ababa', 'c. Tripoli', 'd. Nairobi'],
        'jawaban': 'a. Kairo'
    }
Soal87 = {
        'pertanyaan': 'Apa nama alat musik tiup tradisional dari Indonesia?',
        'pilihanGanda': ['a. Gamelan', 'b. Angklung', 'c. Serunai', 'd. Piano'],
        'jawaban': 'c. Serunai'
    }
Soal88 =  {
        'pertanyaan': 'Apa nama presiden ke-4 Indonesia?',
        'pilihanGanda': ['a. Abdurrahman Wahid', 'b. Megawati Soekarnoputri', 'c. Susilo Bambang Yudhoyono', 'd. Joko Widodo'],
        'jawaban': 'a. Abdurrahman Wahid'
    }
Soal89 = {
        'pertanyaan': 'Apa nama alat yang digunakan untuk mengukur jarak?',
        'pilihanGanda': ['a. GPS', 'b. Kompas', 'c. Mikrometer', 'd. Penggaris'],
        'jawaban': 'a. GPS'
    }
Soal90 = {
        'pertanyaan': 'Siapa pelukis terkenal asal Belanda?',
        'pilihanGanda': ['a. Vincent van Gogh', 'b. Pablo Picasso', 'c. Claude Monet', 'd. Leonardo da Vinci'],
        'jawaban': 'a. Vincent van Gogh'
    }
Soal91 = {
        'pertanyaan': 'Apa nama program luar angkasa yang pertama kali mengirim manusia ke bulan?',
        'pilihanGanda': ['a. Apollo 11', 'b. Gemini', 'c. Mercury', 'd. Voyager'],
        'jawaban': 'a. Apollo 11'
    }
Soal92 = {
        'pertanyaan': 'Apa nama virus yang menyebabkan COVID-19?',
        'pilihanGanda': ['a. Influenza', 'b. SARS-CoV-2', 'c. MERS-CoV', 'd. HIV'],
        'jawaban': 'b. SARS-CoV-2'
    }
Soal72 = {
        'pertanyaan': 'Apa nama bintang terdekat dengan Bumi?',
        'pilihanGanda': ['a. Sirius', 'b. Proxima Centauri', 'c. Betelgeuse', 'd. Alpha Centauri'],
        'jawaban': 'b. Proxima Centauri'
    }


class Game(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.listSoal=[Soal1,Soal2,Soal3,Soal4,Soal5,Soal6,Soal7,Soal8,Soal9,Soal10,Soal11,Soal12,Soal13,Soal14,Soal15,Soal16,Soal17,Soal18,Soal19,Soal20,Soal21,Soal22,Soal23,Soal24,Soal25,Soal26,Soal27,Soal28,Soal29,Soal30,Soal31,Soal32,Soal33,Soal34,Soal35,Soal36,Soal37,Soal38,Soal39,Soal40,Soal41,Soal42,Soal43,Soal44,Soal45,Soal46,Soal47,Soal48,Soal49,Soal50,Soal51,Soal52,Soal53,Soal54,Soal55,Soal56,Soal57,Soal58,Soal59,Soal60,Soal61,Soal62,Soal63,Soal64,Soal65,Soal66,Soal67,Soal68,Soal69,Soal70,Soal71,Soal72,Soal73,Soal74,Soal75,Soal76,Soal77,Soal78,Soal79,Soal80,Soal81,Soal82,Soal83,Soal84,Soal85,Soal86,Soal87,Soal88,Soal89,Soal90,Soal91,Soal92,Soal93,Soal94]
        self.SoalTerpilih=[]
        self.SoalPilihan=''
        self.soalKe=0
        self.jumlahSoal=10
        self.jawabanBenar=''
        self.jawaban=''
        self.result=''
        self.teks=''
        self.skor=0
        self.intro='TES IQ GAME\n\nby: gumalgamul\n\n\nyoutu.be/@gumalgamul\nfb.com/gumalgamul\n\n\nsilahkan mencoba'
        self.label=Label(text=self.teks, size=(layar[0],layar[1]/2),pos=(1,layar[1]/2), text_size=(layar[0],None),halign='center')
        self.add_widget(self.label)
        self.ButtonA=Button(text='A', pos=(layar[0]/3,layar[1]-400),halign='center', size=(50,50))
        self.ButtonB=Button(text='B', pos=(layar[0]/3+(100),layar[1]-400),halign='center', size=(50,50))
        self.ButtonC=Button(text='C', pos=(layar[0]/3+(200),layar[1]-400),halign='center', size=(50,50))
        self.ButtonD=Button(text='D', pos=(layar[0]/3+(300),layar[1]-400),halign='center', size=(50,50))
        self.ButtonYes=Button(text='YES', pos=(layar[0]/3,layar[1]-400),halign='center', size=(50,50))
        self.ButtonNo=Button(text='NO', pos=(layar[0]/3+(400),layar[1]-400),halign='center', size=(50,50))
        Clock.schedule_once(self.IntroGame,0.5)
    def ResetGame(self):
        self.SoalPilihan=''
        self.soalKe=0
        self.jumlahSoal=10
        self.jawabanBenar=''
        self.jawaban=''
        self.result=''
        self.teks=''
        self.skor=0
        self.label=Label(text=self.teks, size=(layar[0],layar[1]/2),pos=(1,layar[1]/2), text_size=(layar[0],None),halign='center')
        self.add_widget(self.label)
        self.ButtonA=Button(text='A', pos=(layar[0]/3,layar[1]-400),halign='center', size=(50,50))
        self.add_widget(self.ButtonA)
        self.ButtonB=Button(text='B', pos=(layar[0]/3+(100),layar[1]-400),halign='center', size=(50,50))
        self.add_widget(self.ButtonB)
        self.ButtonC=Button(text='C', pos=(layar[0]/3+(200),layar[1]-400),halign='center', size=(50,50))
        self.add_widget(self.ButtonC)
        self.ButtonD=Button(text='D', pos=(layar[0]/3+(300),layar[1]-400),halign='center', size=(50,50))
        self.add_widget(self.ButtonD)
        self.ButtonYes=Button(text='YES', pos=(layar[0]/3,layar[1]-400),halign='center', size=(50,50))
        self.ButtonNo=Button(text='NO', pos=(layar[0]/3+(400),layar[1]-400),halign='center', size=(50,50))
    def ConfirmPlay(self):
        self.add_widget(self.ButtonYes)
        self.add_widget(self.ButtonNo)
        self.ButtonYes.bind(on_press=self.PlayAgain)
        self.ButtonNo.bind(on_press=self.NotPlayAgain)
    def PlayAgain(self,instance):
        self.remove_widget(self.ButtonYes)
        self.remove_widget(self.ButtonNo)
        self.teks=''
        self.label.text=self.teks
        self.ResetGame()
        Clock.schedule_once(self.GameStart,0.5)
    def NotPlayAgain(self,instance):
        self.remove_widget(self.ButtonYes)
        self.remove_widget(self.ButtonNo)
        self.ResetGame()
        App.get_running_app().stop()
    def IntroGame(self,dt):
        self.label.text=self.intro
        Clock.schedule_once(self.GameStart,5)
    def GameStart(self,dt):
        Clock.unschedule(self.IntroGame)
        if self.ButtonA not in self.children and self.ButtonB not in self.children  and self.ButtonC not in self.children and self.ButtonD not in self.children:
            self.add_widget(self.ButtonA)
            self.add_widget(self.ButtonB)
            self.add_widget(self.ButtonC)
            self.add_widget(self.ButtonD)
        else:pass
        if self.soalKe<self.jumlahSoal:
            self.GenerateSoal()
        else:
            self.GameEnd()
    def GameEnd(self):
        self.teks=f" nilai anda {self.skor} \n\n\nanda ingin bermain lagi?"
        self.label.text=self.teks
        self.remove_widget(self.ButtonA)
        self.remove_widget(self.ButtonB)
        self.remove_widget(self.ButtonC)
        self.remove_widget(self.ButtonD)
        self.ConfirmPlay()
    def GenerateSoal(self):
        self.soalKe+=1
        self.SoalPilihan=random.choice(self.listSoal)
        if self.SoalPilihan in self.SoalTerpilih:self.SoalPilihan=random.choice(self.listSoal)
        else:self.SoalTerpilih.append(self.SoalPilihan)
        self.jawabanBenar=self.SoalPilihan['jawaban']
        self.teks= f" soal ke {self.soalKe} dari {self.jumlahSoal} \n\n {self.SoalPilihan['pertanyaan']} \n\n "+'\n'.join(self.SoalPilihan['pilihanGanda'])
        self.label.text=self.teks
        self.ButtonA.bind(on_press=self.InputJawabanA)
        self.ButtonB.bind(on_press=self.InputJawabanB)
        self.ButtonC.bind(on_press=self.InputJawabanC)
        self.ButtonD.bind(on_press=self.InputJawabanD)
    def InputJawabanA(self,instance):
        self.jawaban=self.SoalPilihan['pilihanGanda'][0]
        self.CekJawaban()
    def InputJawabanB(self,instance):
        self.jawaban=self.SoalPilihan['pilihanGanda'][1]
        self.CekJawaban()
    def InputJawabanC(self,instance):
        self.jawaban=self.SoalPilihan['pilihanGanda'][2]
        self.CekJawaban()
    def InputJawabanD(self,instance):
        self.jawaban=self.SoalPilihan['pilihanGanda'][3]
        self.CekJawaban()
    def CekJawaban(self):
            t=self.makeTimer()
            Clock.unschedule(self.GameStart)
            if self.jawaban == self.jawabanBenar:
                self.result=f"BENAR\n\n jawaban soal \n\n '{ self.SoalPilihan['pertanyaan']}' adalah \n\n {self.jawaban} \n\n load soal in {t} "
                self.skor+=10
            else:
                self.result=f"SALAH\n\n jawaban soal \n\n '{ self.SoalPilihan['pertanyaan']}' adalah \n\n {self.jawabanBenar} \n\n load soal in"
                self.skor+=0
            self.label.text=self.result
            Clock.schedule_once(self.GameStart,4)
    def makeTimer(self):
            t=time.time()
            return t
            
class MyApp(App):
    def build(self):
        self.Game=Game()
        return self.Game

MyApp().run()
        
