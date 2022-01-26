# TA_Face_ALPR_Indonesia

B.	Perancangan Sistem 
Sistem yang dibuat merupakan prototype gerbang berbasis citra plat kendaraan dan wajah pengendara. Sistem ini menggunakan Raspberry Pi 4 sebagai mikrokontroler dan mikroprosessor. Dalam sistem terdapat komponen penyusunan berikut penjelasaannya : 
1.	Komponen pertama pada sistem ini yaitu webcam sebagai sensor visual untuk mengambil citra plat kendaraan dan wajah pengendara. 
2.	Komponen push button berfungsi sebagai trigger untuk memulai sistem dan sebagai tombol emergency apabila led merah menyala.
3.	Komponen servo berfungsi untuk menggerakkan palang gerbang.
4.	Subsistem face recognition berfungsi untuk proses pengenalan wajah yaitu mencocokkan citra wajah yang ditangkap oleh webcam 	dengan data wajah yang telah didaftarkan.
5.	Subsistem plate recognition berfungsi untuk proses pengenalan plat kendaraan yang terbaca. 
6.	Subsistem matching data with database berfungsi untuk mencocokkan wajah dan plat nomor kendaraan yang telah didaftarkan.
 
 ![image](https://user-images.githubusercontent.com/85490178/140569700-7f7a922e-7e98-4bc3-8d12-a2cbaab723d2.png)


C.	Perancangan Mekanik
Desain perancangan mekanik dapat dilihat pada gambar di bawah. Terdapat 2 box yang akan digunakan pada proyek akhir ini agar dapat bekerja dengan apa yang telah direncanakan. 
 
Box pertama yaitu sebagai tempat dimana servo dan palang gerbang diletakkan. Box pertama mempunyai dimensi 10 cm  x 5 cm x 40 cm. Box kedua sebagai tempat dari led dan push button memiliki dimensi yang lebih kecil yaitu  10 cm x 5 cm x 30 cm. Material yang akan digunakan dalam pembuatan box adalah akrilik 1 mm. 

![image](https://user-images.githubusercontent.com/85490178/140569732-6385f03c-360a-4a67-93ec-e4b935849e1e.png)

D.	Perancangan Rangkaian Elektronik
Pengkabelan atau wiring berfungsi sebagai I/O untuk mengontrol sudut putaran servo, led dan push button. Raspberry Pi bertugas untuk mendapatkan sinyal yang diberikan push button dan memberikan sinyal ke led dan motor servo. Perancangan wiring dapat dilihat pada gambar di bawah.
 
![image](https://user-images.githubusercontent.com/85490178/140569787-68e9d8ad-4e4b-4ca0-b39e-70d558dd5307.png)


E.	Perancangan Perangkat Lunak
1. Pengenalan Wajah
Pengenalan wajah dapat dilakukan setelah melakukan training dan menghasilkan sebuah model, model tersebut digunakan untuk melakukan pengenalan pada wajah pada foto. Jalankan program dan hadapkan wajah pada web camera kemudian wajah akan dideteksi kemudian dikenali dengan muncul nama di bagian wajah. Nama tersebut didapat setelah sistem mengenali wajah dengan cara mencocokan wajah yang ada di kamera dengan wajah yang ada pada database. Diagram blok pengenalan wajah ditunjukkan pada gambar di bawah. 

![image](https://user-images.githubusercontent.com/85490178/140569861-db20f868-d498-4792-aaeb-37cc3c59121e.png)

2.	Pengenalan Citra Plat Nomor
Sistem otomatisasi gerbang berbasis citra plat kendaraan dan wajah pengendara memiliki cara kerja yang cukup sederhana dalam menjalankan fungsi. Pada sistem umum diagram alur yang dibangun dijelaskan pada gambar di bawah.

![image](https://user-images.githubusercontent.com/85490178/140569922-82e98fa0-910e-4a79-b233-4322e13bbe6f.png)
