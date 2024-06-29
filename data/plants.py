class Plant:
    def __init__(
        self, science_name, en_name, id_name, description, benefits, effects, tips
    ):
        self.science_name = science_name
        self.en_name = en_name
        self.id_name = id_name
        self.description = description
        self.benefits = benefits
        self.effects = effects
        self.tips = tips


ananas_comosus = Plant(
    science_name="Ananas comosus",
    en_name="Pineaple",
    id_name="Nanas",
    description="Nanas (Ananas comosus) adalah tanaman tropis dengan buah yang dapat dimakan dan merupakan tanaman yang paling penting secara ekonomi dalam famili Bromeliaceae. Nanas adalah tumbuhan asli Amerika Selatan, dan telah dibudidayakan di sana selama berabad-abad. Pengenalan nanas ke Eropa pada abad ke-17 menjadikannya sebagai ikon budaya kemewahan yang signifikan. Sejak tahun 1820-an, nanas telah ditanam secara komersial di rumah kaca dan banyak perkebunan tropis. Selain itu, nanas merupakan buah tropis terpenting ketiga dalam produksi dunia.\nNanas adalah tanaman herba yang memiliki batang pendek dan daun panjang, lancip, dan berduri. Daun nanas tersusun dalam roset padat di bagian atas batang. Bunganya kecil dan berwarna kuning, dan tersusun dalam tongkol di tengah roset daun. Buahnya besar, berbentuk oval, dan berwarna kuning kecoklatan saat matang. Daging buahnya berwarna kuning cerah, berair, dan memiliki rasa manis dan asam yang menyegarkan.",
    benefits="Nanas memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Meningkatkan daya tahan tubuh\n- Menjaga kesehatan pencernaan\n- Melancarkan aliran darah\n- Mencegah kanker\n- Menjaga kesehatan jantung\n- Menjaga kesehatan kulit\n- Membantu menurunkan berat badan",
    effects="Nanas umumnya aman dikonsumsi oleh semua orang. Namun, perlu diingat bahwa nanas dapat menyebabkan beberapa efek samping pada beberapa orang, seperti:\n- Alergi: Orang yang alergi terhadap bromelain, enzim yang ditemukan dalam nanas, dapat mengalami reaksi alergi setelah mengkonsumsinya. Gejala alergi nanas dapat berupa gatal-gatal, ruam kulit, bengkak pada wajah dan tenggorokan, dan kesulitan bernapas.\n- Diare: Nanas mengandung serat yang tinggi. Konsumsi nanas yang berlebihan dapat menyebabkan diare pada orang yang tidak terbiasa mengkonsumsinya.\n- Mual dan muntah: Nanas mengandung asam sitrat yang tinggi. Konsumsi nanas yang berlebihan dapat menyebabkan mual dan muntah pada orang yang memiliki masalah pencernaan.",
    tips="- Konsumsi nanas dalam jumlah yang moderat untuk menghindari efek samping.\n- Jika Anda memiliki alergi terhadap bromelain, hindari mengkonsumsi nanas.\n- Jika Anda memiliki masalah pencernaan, konsultasikan dengan dokter sebelum mengkonsumsi nanas.",
)

artocarpus_heterophyllus = Plant(
    science_name="Artocarpus heterophyllus",
    en_name="Jackfruit",
    id_name="Nangka",
    description="Nangka (Artocarpus heterophyllus) adalah pohon besar tropis yang berasal dari Asia Tenggara dan India. Nangka dikenal sebagai penghasil buah terbesar yang bisa dimakan di dunia, beratnya bisa mencapai 36 kg dan ditutupi kulit hijau berbintil. Daging buah nangka muda berwarna hijau dan memiliki rasa netral, sehingga populer sebagai pengganti daging.  Daging buah nangka matang berwarna kuning, lengket, dan memiliki rasa manis dan buah-buahan. Pohon nangka juga dibudidayakan untuk kayunya yang kuat dan tahan lama.",
    benefits="Nangka adalah buah bergizi yang menawarkan berbagai manfaat kesehatan. Berikut beberapa di antaranya:\n- Kaya akan vitamin dan mineral: Nangka merupakan sumber serat, vitamin C, potasium, dan nutrisi penting lainnya yang baik.\n- Membantu pencernaan: Kandungan serat yang tinggi dalam nangka dapat meningkatkan keteraturan dan kesehatan usus.\n- Mendukung kontrol gula darah: Nangka dapat membantu mengatur kadar gula darah karena kandungan seratnya dan adanya senyawa seperti lignan.\n- Memiliki sifat anti-inflamasi: Nangka mengandung antioksidan dan senyawa lain yang dapat membantu mengurangi peradangan dalam tubuh.\n- Sumber prebiotik potensial: Prebiotik adalah serat yang memberi makan bakteri baik dalam usus Anda, meningkatkan kesehatan usus.",
    effects="Nangka umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Reaksi alergi: Orang dengan alergi serbuk sari birch lebih mungkin mengalami reaksi alergi terhadap nangka.\n- Kadar gula darah: Karena potensinya menurunkan gula darah, penderita diabetes atau yang sedang mengonsumsi obat diabetes sebaiknya berkonsultasi dengan dokter sebelum mengonsumsi nangka.\n- Masalah pencernaan: Konsumsi nangka yang berlebihan dapat menyebabkan kembung atau diare pada beberapa orang.",
    tips="- Pilih nangka yang masih keras dan memiliki aroma sedikit manis. Hindari nangka yang lembek atau berbau tajam.\n- Nangka dapat dinikmati dalam keadaan matang atau mentah. Nangka matang bisa dimakan langsung atau digunakan dalam makanan penutup. Nangka muda biasanya digunakan sebagai pengganti daging dalam masakan gurih.\n- Saat memotong nangka, gunakan sarung tangan untuk melindungi tangan Anda dari getah lengket.",
)

carica_papaya = Plant(
    science_name="Carica papaya",
    en_name="Papaya",
    id_name="Pepaya",
    description="Pepaya (Carica papaya) adalah tanaman tropis yang berasal dari Meksiko dan Amerika Tengah. Pepaya adalah tanaman yang tumbuh cepat dan memiliki buah yang besar, berbentuk lonjong, dan berwarna oranye ketika matang. Daging buah pepaya berwarna oranye, berair, dan memiliki rasa manis dan sedikit asam. Pepaya dikenal sebagai buah yang kaya akan enzim papain, yang memiliki sifat antiinflamasi dan pencernaan. Selain itu, pepaya juga mengandung serat, vitamin, dan mineral yang baik untuk kesehatan.",
    benefits="Pepaya memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Meningkatkan pencernaan: Enzim papain dalam pepaya dapat membantu memecah protein dalam makanan dan meningkatkan pencernaan.\n- Menjaga kesehatan kulit: Kandungan vitamin C dan antioksidan dalam pepaya dapat membantu menjaga kesehatan kulit dan melawan penuaan dini.\n- Menjaga kesehatan jantung: Pepaya mengandung serat, kalium, dan antioksidan yang baik untuk kesehatan jantung.\n- Menjaga kesehatan mata: Kandungan vitamin A dalam pepaya dapat membantu menjaga kesehatan mata dan mencegah penyakit mata.\n- Meningkatkan daya tahan tubuh: Pepaya mengandung vitamin C dan antioksidan yang dapat meningkatkan sistem kekebalan tubuh.",
    effects="Pepaya umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Reaksi alergi: Orang yang alergi terhadap lateks mungkin juga alergi terhadap pepaya.\n- Interaksi obat: Pepaya dapat berinteraksi dengan beberapa obat, seperti obat darah, obat diabetes, dan obat tekanan darah. Konsultasikan dengan dokter sebelum mengonsumsi pepaya jika Anda sedang mengonsumsi obat-obatan tersebut.\n- Efek samping: Konsumsi pepaya dalam jumlah yang berlebihan dapat menyebabkan diare atau gangguan pencernaan pada beberapa orang.",
    tips="- Pilih pepaya yang matang dengan warna kulit oranye yang cerah. Pepaya yang matang memiliki aroma manis dan lembut.\n- Pepaya dapat dimakan langsung, dijadikan jus, atau digunakan dalam salad buah.\n- Hindari mengonsumsi biji pepaya, karena dapat menyebabkan gangguan pencernaan.",
)

cocos_nucifera = Plant(
    science_name="Cocos nucifera",
    en_name="Coconut",
    id_name="Kelapa",
    description="Kelapa (Cocos nucifera) adalah pohon tropis yang berasal dari Asia Tenggara dan Kepulauan Pasifik. Kelapa dikenal sebagai pohon serba guna karena hampir semua bagian pohonnya dapat dimanfaatkan. Buah kelapa terdiri dari lapisan kulit keras, daging buah putih, dan air kelapa yang segar. Daging buah kelapa dapat dimakan langsung atau diolah menjadi santan, minyak kelapa, dan produk makanan lainnya. Air kelapa juga dikenal sebagai minuman yang menyegarkan dan kaya akan elektrolit.",
    benefits="Kelapa memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Menjaga kesehatan jantung: Kelapa mengandung asam lemak jenuh yang baik untuk kesehatan jantung.\n- Menjaga kesehatan kulit: Minyak kelapa dapat membantu menjaga kelembapan kulit dan melawan infeksi kulit.\n- Meningkatkan energi: Air kelapa mengandung elektrolit yang dapat membantu menghidrasi tubuh dan meningkatkan energi.\n- Menjaga kesehatan rambut: Minyak kelapa dapat membantu menjaga kesehatan rambut dan mencegah kerusakan akibat panas dan polusi.\n- Meningkatkan sistem kekebalan tubuh: Kelapa mengandung asam laurat, yang memiliki sifat antibakteri, antivirus, dan antijamur.",
    effects="Kelapa umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Kandungan lemak: Kelapa mengandung lemak jenuh yang tinggi. Konsumsi kelapa dalam jumlah yang berlebihan dapat meningkatkan risiko penyakit jantung.\n- Alergi: Beberapa orang mungkin alergi terhadap kelapa. Gejala alergi kelapa dapat berupa gatal-gatal, ruam kulit, bengkak pada wajah dan tenggorokan, dan kesulitan bernapas.\n- Interaksi obat: Minyak kelapa dapat berinteraksi dengan beberapa obat, seperti obat darah, obat diabetes, dan obat kolesterol. Konsultasikan dengan dokter sebelum mengonsumsi minyak kelapa jika Anda sedang mengonsumsi obat-obatan tersebut.",
    tips="- Pilih kelapa yang beratnya terasa penuh dan memiliki suara gemeretak saat dikocok. Hindari kelapa yang terasa ringan atau berbunyi kosong saat dikocok.\n- Kelapa dapat dimakan langsung, diolah menjadi santan, minyak kelapa, atau produk makanan lainnya.\n- Hindari mengonsumsi kelapa dalam jumlah yang berlebihan untuk menghindari efek samping.",
)

musa_spp = Plant(
    science_name="Musa spp",
    en_name="Banana",
    id_name="Pisang",
    description="Pisang (Musa spp) adalah tanaman tropis yang berasal dari Asia Tenggara dan Australia. Pisang adalah tanaman yang tumbuh cepat dan memiliki buah yang berbentuk lonjong, berkulit kuning ketika matang, dan memiliki daging buah yang manis dan lembut. Pisang adalah sumber energi yang baik karena mengandung karbohidrat, serat, vitamin, dan mineral yang penting untuk kesehatan. Selain itu, pisang juga mengandung senyawa antioksidan dan nutrisi lain yang baik untuk kesehatan.",
    benefits="Pisang memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Menjaga kesehatan pencernaan: Pisang mengandung serat yang baik untuk pencernaan dan mencegah sembelit.\n- Menjaga kesehatan jantung: Pisang mengandung kalium dan serat yang baik untuk kesehatan jantung.\n- Meningkatkan energi: Pisang mengandung karbohidrat yang dapat memberikan energi instan.\n- Menjaga kesehatan kulit: Pisang mengandung vitamin C dan antioksidan yang baik untuk kesehatan kulit.\n- Meningkatkan mood: Pisang mengandung triptofan, zat yang dapat meningkatkan mood dan mengurangi stres.",
    effects="Pisang umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Kandungan kalori: Pisang mengandung kalori yang tinggi. Konsumsi pisang dalam jumlah yang berlebihan dapat menyebabkan penambahan berat badan.\n- Alergi: Beberapa orang mungkin alergi terhadap pisang. Gejala alergi pisang dapat berupa gatal-gatal, ruam kulit, bengkak pada wajah dan tenggorokan, dan kesulitan bernapas.\n- Interaksi obat: Pisang dapat berinteraksi dengan beberapa obat, seperti obat darah, obat diabetes, dan obat tekanan darah. Konsultasikan dengan dokter sebelum mengonsumsi pisang jika Anda sedang mengonsumsi obat-obatan tersebut.",
    tips="- Pilih pisang yang berkulit kuning cerah dan tidak terlalu lembek. Hindari pisang yang berwarna hijau atau berbintik hitam.\n- Pisang dapat dimakan langsung, diolah menjadi jus, atau digunakan dalam makanan penutup.\n- Hindari mengonsumsi pisang dalam jumlah yang berlebihan untuk menghindari efek samping.",
)

nephelium_lappaceum = Plant(
    science_name="Nephelium lappaceum",
    en_name="Rambutan",
    id_name="Rambutan",
    description="Rambutan (Nephelium lappaceum) adalah tanaman tropis yang berasal dari Asia Tenggara dan Indonesia. Rambutan dikenal sebagai buah yang memiliki kulit berbulu merah dan daging buah putih yang manis. Buah rambutan mengandung vitamin C, serat, dan antioksidan yang baik untuk kesehatan. Rambutan juga dikenal sebagai buah yang menyegarkan dan enak untuk dinikmati sebagai camilan.",
    benefits="Rambutan memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Menjaga kesehatan kulit: Rambutan mengandung vitamin C dan antioksidan yang baik untuk kesehatan kulit dan melawan penuaan dini.\n- Meningkatkan daya tahan tubuh: Rambutan mengandung vitamin C dan antioksidan yang dapat meningkatkan sistem kekebalan tubuh.\n- Menjaga kesehatan mata: Kandungan vitamin A dalam rambutan dapat membantu menjaga kesehatan mata dan mencegah penyakit mata.\n- Meningkatkan energi: Rambutan mengandung karbohidrat dan gula alami yang dapat memberikan energi instan.\n- Menjaga kesehatan jantung: Rambutan mengandung serat dan antioksidan yang baik untuk kesehatan jantung.",
    effects="Rambutan umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Alergi: Beberapa orang mungkin alergi terhadap rambutan. Gejala alergi rambutan dapat berupa gatal-gatal, ruam kulit, bengkak pada wajah dan tenggorokan, dan kesulitan bernapas.\n- Kandungan gula: Rambutan mengandung gula alami yang tinggi. Konsumsi rambutan dalam jumlah yang berlebihan dapat meningkatkan kadar gula darah pada penderita diabetes.",
    tips="- Pilih rambutan yang berkulit merah dan tidak terlalu lembek. Hindari rambutan yang berwarna hijau atau berbintik hitam.\n- Rambutan dapat dimakan langsung atau diolah menjadi jus.\n- Hindari mengonsumsi rambutan dalam jumlah yang berlebihan untuk menghindari efek samping.",
)

salacca_zalacca = Plant(
    science_name="Salacca zalacca",
    en_name="Salak",
    id_name="Salak",
    description="Salak (Salacca zalacca) adalah tanaman tropis yang berasal dari Indonesia dan Asia Tenggara. Salak dikenal sebagai buah yang memiliki kulit berduri dan daging buah yang manis dan asam. Buah salak mengandung serat, vitamin C, dan antioksidan yang baik untuk kesehatan. Salak juga dikenal sebagai buah yang menyegarkan dan enak untuk dinikmati sebagai camilan.",
    benefits="Salak memiliki banyak manfaat bagi kesehatan, di antaranya:\n- Menjaga kesehatan pencernaan: Salak mengandung serat yang baik untuk pencernaan dan mencegah sembelit.\n- Menjaga kesehatan kulit: Salak mengandung vitamin C dan antioksidan yang baik untuk kesehatan kulit dan melawan penuaan dini.\n- Meningkatkan energi: Salak mengandung karbohidrat dan gula alami yang dapat memberikan energi instan.\n- Menjaga kesehatan jantung: Salak mengandung serat dan antioksidan yang baik untuk kesehatan jantung.\n- Menjaga kesehatan mata: Kandungan vitamin A dalam salak dapat membantu menjaga kesehatan mata dan mencegah penyakit mata.",
    effects="Salak umumnya aman dikonsumsi oleh kebanyakan orang. Namun, ada beberapa hal yang perlu diperhatikan:\n- Alergi: Beberapa orang mungkin alergi terhadap salak. Gejala alergi salak dapat berupa gatal-gatal, ruam kulit, bengkak pada wajah dan tenggorokan, dan kesulitan bernapas.\n- Kandungan gula: Salak mengandung gula alami yang tinggi. Konsumsi salak dalam jumlah yang berlebihan dapat meningkatkan kadar gula darah pada penderita diabetes.",
    tips="- Pilih salak yang berkulit berwarna coklat keemasan dan tidak terlalu lembek. Hindari salak yang berwarna hijau atau berbintik hitam.\n- Salak dapat dimakan langsung, diolah menjadi jus, atau digunakan dalam makanan penutup.\n- Hindari mengonsumsi salak dalam jumlah yang berlebihan untuk menghindari efek samping.",
)

plants = [
    ananas_comosus,
    artocarpus_heterophyllus,
    carica_papaya,
    cocos_nucifera,
    musa_spp,
    nephelium_lappaceum,
    salacca_zalacca,
]
