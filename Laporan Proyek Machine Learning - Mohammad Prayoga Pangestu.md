# Laporan Proyek Machine Learning - Mohammad Prayoga Pangestu

## Sosial dan Budaya 

Batik adalah bentuk seni visual pada bahan tekstil yang diproduksi menggunakan teknik menggambar tradisional yang berasal dari Indonesia. Banyaknya motif di Indonesia menyulitkan untuk identifikasi jenisnya tujuanya adalah untuk mengetahui motif dengan bantuan komputasi dapat membantu dalam pelestarian batik. Convolutional Neural Network (CNN) adalah salah satu metode machine learning dari pengembangan Multi Layer Perceptron (MLP) yang didesain untuk mengolah data dua dimensi.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Mengapa masalah tersebut harus diselesaikan ? iya harus.Dengan perkembangan didalam dunia teknologi informasi serta berkembang pesatnya pembelajaran mengenai AI(Artificial Intelligence) maka tidak salah dan mungkin sangat disarankan untuk mengetahui motif dari batik yang jumlahnya begitu banyak bisa menggunakan proses pembelajaran dari computer vision.
- Bagaimana menyelesaikan masalah tersebut ? Ya. penyelesaian masalah tersebut bisa menggunakan salah satu teknologi perkembangan dari AI yaitu metode deep learning dengan menggunakan algoritma seperti CNN.
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
- Berikut ini merupakan salah satu riset yang digunakan untuk referensi. Referensi didapatkan di google scholar untuk lebih jelasnya bisa langsung melihat referensi dibawah ini :
  
  Referensi: [KLASIFIKASI MOTIF BATIK MENGGUNAKAN METODE DEEP CONVOLUTIONAL NEURAL NETWORK DENGAN DATA AUGMENTATION](http://publication.petra.ac.id/index.php/teknik-informatika/article/view/10519) 

## Business Understanding

Dari pernyataan yang telah dijelaskan sebelumnya, maka akan diperjelas lagi masalah masalah yang mendasari pada project kali ini 
Berikut beberapa statment yang mendasari :

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Batik adalah bentuk seni visual pada bahan tekstil yang diproduksi menggunakan teknik menggambar tradisional yang berasal dari Indonesia oleh karena itu kita perlu melestarikan batik dengan bantuan computer vision untuk mendalami setiap motifnya.
- Banyaknya motif di Indonesia menyulitkan untuk identifikasi jenisnya. dengan bantuin computer vision maka akan lebih membantu untuk mengidentifikasi motif batiknya.
- Identifikasi secara manual akan memakan banyak waktu dan terkadang kurang efektif dengan bantuin dari computer vision maka akan lebih mudah dalam proses pengklasifikasianya.

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Tujuan mengetahui motif dengan bantuan komputasi dapat membantu dalam pelestarian batik.
- Membangun sebuah model yang dapat mengetahui motif dari batik agar dapat lebih mudah melakukan identifikasi motif batik di indonesia.
- membangun model diatas AI dengan metode deep learning dengan implementasi algoritma CNN tujuan tidak lain adalah untuk pengklasifikasian dari motif batik.


**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Terdapat kesalahan dalam mengklasifikasikan batik dikarenakan pola yang dimiliki menganut pola dasar dari motif lain, sehingga akan memunculkan nilai probabilitas yang rendah dan memiliki selisih tipis dengan motif lain.
    - Solusi yang diberikan adalah Melakukan variasi pada metode dengan menggunakan metode objek detection agar bisa mengenali beberapa motif batik dalam satu gambar.
    - Solusi lain yaitu dengan Menambahkan augmentasi yang lebih relevan dengan gambar batik yang beredar saat ini.

## Data Understanding
Berikut ini adalah contoh dataset yang digunakan untuk melakukan pengerjaan project :
[Indonesian Batik Motifs](https://www.kaggle.com/datasets/dionisiusdh/indonesian-batik-motifs).


### Berikut ini adalah uraian mengenai dataset yang digunakan :
- About	: Dataset ini merupakan kumpulan dari gambar yang berisi motif batik dari masing masing daerah yang berada di indonesia
- Dataset	: Dataset ini dikumpulkan dari Bing.com dengan menggunakan Bing image-scraping oleh Ultralytics.
- Isi		: Terdapat 983 gambar (.jpg) dari 20 macam motif Batik Indonesia. 
- Motif	: Batik Bali	Batik Lasem Batik Betawi	Batik Mega Mendung Batik Celup	Batik Parang Batik Cendrawasih	Batik Pekalongan
Batik Ceplok	Batik Priangan Batik Ciamis	Batik Sekar Batik Garutan	Batik Sidoluhur Batik Gentongan	Batik Sidomukti Batik Kawung	Batik Sogan 
Batik Keraton	Batik Tambal 

**Rubrik/Kriteria Tambahan (Opsional)**:
- Karena data ini adalah data image jadi tidak perlu melakukan proses visualisasi data tambahan.

## Data Preparation
Pada project yang dikerjakan kali ini teknik data preparation yang digunakan adalah (data augmentation) dimana data augmentation itu sendiri adalah teknik yang digunakan dalam machine learning untuk meningkatkan jumlah data yang tersedia untuk pelatihan model. Teknik ini melibatkan membuat variasi dari data pelatihan yang ada dengan cara memanipulasi gambar, teks, atau data lainnya secara sistematis. Tujuannya adalah untuk meningkatkan keanekaragaman data pelatihan, mengurangi overfitting, dan meningkatkan kinerja model.


**Rubrik/Kriteria Tambahan (Opsional)**: 
- Proses data preparation yang dilakukan didalam project ini adalah data augmentation 
- Tujuan dari data augmentation yang dilakukan adalah untuk meningkatkan kualitas dataset dan memperkaya variasi data yang tersedia. Data augmentation dapat membantu mengatasi masalah overfitting, yaitu ketika model terlalu mempelajari pola yang ada di dataset pelatihan dan tidak dapat digeneralisasi dengan baik ke data yang belum pernah dilihat sebelumnya

## Modeling
Pada proses modelling saya membagi beberapa tahap modelling sesuai dengan file google colab yang telah diselesaikan :
- Download Arsitektur Resnet : ResNet adalah salah satu yang paling populer dalam klasifikasi gambar dan tugas-tugas pengolahan citra lainnya, terutama untuk data yang kompleks dan sulit untuk dipelajari dengan model yang lebih sederhana.
- Modelling Data		     : Dimana didalam modelling data ini berisi kriteria dari proses Training yang nantinya akan dilakukan didalam proses ini juga terdapat penentuan jumlah epoch yang dipakai dan juga besar dari learning rate(lr) yang digunakan.
- Training & Validation	     : Proses Training adalah tahap di mana model machine learning dipelajari untuk memprediksi label atau kelas yang benar dari data pelatihan. Pada tahap ini, model akan diberikan input data pelatihan dan output yang diharapkan, dan model akan mencoba menyesuaikan parameter-parameter internalnya (misalnya, bobot dan bias dalam jaringan saraf) untuk menghasilkan prediksi yang akurat. sedangkan Proses Validation adalah  tahap di mana model diuji pada data yang belum pernah dilihat sebelumnya untuk menguji kinerjanya. Data validasi adalah data yang dipisahkan dari data pelatihan dan digunakan untuk mengukur seberapa baik model dapat memprediksi label atau kelas yang benar dari data yang belum pernah dilihat sebelumnya. 

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Terdapat kesalahan dalam mengklasifikasikan batik dikarenakan pola yang dimiliki menganut pola dasar dari motif lain, sehingga akan memunculkan nilai probabilitas yang rendah dan memiliki selisih tipis dengan motif lain. oleh karena itu solusi yang bisa dilakukan adalah dengan melakukan variasi pada metode dengan menggunakan metode objek detection agar bisa mengenali beberapa motif batik dalam satu gambar. Selain itu juga solusi lain yang dilakukan adalah dengan Menambahkan augmentasi yang lebih relevan dengan gambar batik yang beredar saat ini.

## Evaluation
Evaluasi matrik yang digunakan adalah F1-Score dimana F1-score adalah sebuah metrik evaluasi yang menggabungkan precision dan recall untuk mengukur performa dari model klasifikasi pada suatu dataset. F1-score didefinisikan sebagai harmonic mean dari precision dan recall, dengan rentang nilai antara 0 dan 1, di mana semakin tinggi nilai F1-score, semakin baik performa dari model.

Hasil pembacaan dari confusion matrik yang diperolah dari model yang telah dibuat sebagai berikut :
- Akurasi keseluruhan model adalah 0,38, yang berarti hanya mengklasifikasikan dengan benar 38 dari 99 contoh. Ini bukan kinerja yang sangat baik, dan menunjukkan bahwa model perlu diperbaiki.
- Dapat dilihat bahwa presisi dan recall sangat bervariasi di antara kelas yang berbeda, mulai dari 0 hingga 1. Untuk beberapa kelas (mis., Kelas 1 dan kelas 8), presisinya tinggi tetapi recallnya rendah, sedangkan untuk yang lain (mis., kelas 11 dan kelas 16), presisi dan recallnya tinggi. Hal ini menunjukkan bahwa model tersebut lebih baik dalam mengidentifikasi kelas tertentu daripada yang lain.
- Skor F1 adalah rata-rata seimbang dari presisi dan recall, dan sering digunakan sebagai metrik tunggal untuk mengevaluasi performa keseluruhan model. Skor F1 juga sangat bervariasi di berbagai kelas, mulai dari 0 hingga 0,91. Makro dan skor F1 rata-rata tertimbang adalah 0,38, yang sama dengan akurasi keseluruhan, menunjukkan bahwa performa model konsisten di semua kelas.
- Kasimpulan dari model yang telah dibuat adalah menunjukkan bahwa model perlu ditingkatkan untuk mencapai akurasi, presisi, dan recall yang lebih baik di semua kelas.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Formula F1-Score	:
	Formula untuk precision, recall, dan F1-score adalah sebagai berikut:	
	Precision (P) = TP / (TP + FP)
	Recall (R) = TP / (TP + FN)
	F1-score = 2 * (P * R) / (P + R)
- F1-score menggabungkan precision dan recall untuk memberikan nilai evaluasi yang seimbang pada performa model klasifikasi. Precision adalah metrik evaluasi yang mengukur seberapa akurat model dalam mengidentifikasi kelas positif, sedangkan recall mengukur seberapa banyak kasus positif yang dapat diidentifikasi oleh model.

Ketika terdapat kelas-kelas yang tidak seimbang dalam distribusi data, metrik evaluasi seperti accuracy dapat memberikan hasil yang menyesatkan. Misalnya, jika terdapat 90% kelas negatif dan hanya 10% kelas positif, model dapat mencapai tingkat akurasi yang tinggi dengan hanya memprediksi semua sampel sebagai kelas negatif.

Dalam kasus seperti itu, F1-score dapat memberikan nilai evaluasi yang lebih bermakna. F1-score menghitung harmonic mean dari precision dan recall, sehingga memberikan nilai yang seimbang antara kedua metrik evaluasi tersebut.

Dalam kasus klasifikasi biner, F1-score dapat dihitung sebagai berikut:

F1-score = 2 * (precision * recall) / (precision + recall)

Nilai F1-score berkisar antara 0 dan 1, di mana nilai 1 menunjukkan performa model yang sempurna dan nilai 0 menunjukkan performa model yang buruk. Semakin tinggi nilai F1-score, semakin baik performa model dalam mengklasifikasikan sampel pada kedua kelas, baik kelas positif maupun kelas negatif.


