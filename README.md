LINK PWS : http://muhammad-rafli33-pandaspetshop.pbp.cs.ui.ac.id/


# TUGAS 1

## 1.) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
jawab:
**Membuat sebuah proyek Django baru**
	Membuat folder lalu membuat venv python. Setelah itu menginstal beberapa library yang berguna untuk pengembangan. Lalu, inisisai project Django dengan "django-admin startproject (nama project) .".

**Membuat aplikasi dengan nama main pada proyek tersebut**
	Melakukan perintah "python manage.py startapp main", lalu menambahkan 'main' di variable INSTALLED_APPS pada berkas settings.py

**Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
	Membuat berkas urls.py di dalam folder main. Lalu, menyematkan method show_main dari vies ke urlpatterns. lakukan hal yang sama pada urls.py dalam direktori projek.

**Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib**
	Membuat subclass dengan nama model yang ingin didenfinisikan dari models.Model dengan atribut wajib tersebut

**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
	Membuat fungsi show_main berisi dictionary yang berisi data yang akan dikirimkan ke tampilan.

**Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
	Mengisi variable app_name dengan main pada berkas urls.py

**Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**
	Membuat project baru di pws, lalu hubungkan dengan repositori local, lalu push ke pws.



	
## 2.) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
	https://www.figma.com/board/vbT6XJN88CA1fa0em6EhCa/Untitled?node-id=0-1&t=4grBKEOgOdpiik0p-1



## 3.) Jelaskan fungsi git dalam pengembangan perangkat lunak!
	1.) Menyimpan riwayat perubahan
		Git membantu menyimpan riwayat perubahan serta oleh siapa perubahan tersebut dilakukan. Hal ini berguna jika ingin kembali ke versi sebelumnya, misal, karena kesalahan pengembangan versi terbaru, kode atau aplikasi justru semakin hancur.

	2.) Melakukan pemisahan kode dengan branching
		Hal ini bermanfaat jika kita ingin mengembangkan perangkat lunak secara terpisah ari kode Utama.

	3.) Melakukan penggabungan kode dengan merging
		Hal ini bermanfaat jika kita ingin menggabungkan Kembali kode tersebut dengan kode Utama.

	4.) Kolaborasi
		Dengan Git, beberapa pengembang dapat bekerja pada proyek yang sama secara bersamaan. Git mengelola penggabungan perubahan dari berbagai pengembang dan menyelesaikan konflik yang mungkin muncul.



## 4.) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
	Karena Django ditulis dengan bahasa Python yang tergolong mudah dicerna penulisannya. Hal ini memungkinkan pemula berfokus lebih kepada logikanya dibanding dengan sintaks.

## 5.) Mengapa model pada Django disebut sebagai ORM?
	Karena Django menyediakan cara untuk berinteraksi dengan database relasional menggunakan objek Python. 


# TUGAS 2

## 1.) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
	Data delivery dalam pengimplementasian sebuah platform diperlukan sebagai komunikasi antara backend, frontend, dan database sehingga memungkinkan penerimaan, presentasi, dan pengolahan data pada masing-masing stack.

## 2.) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
	JSON lebih baik karena sintaksnya yang simpel sehingga memungkinkan performa yang lebih baik serta penggunaan memori yang lebih rendah. Hal tersebut pula yang membuat JSON lebih populer.

## 3.) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
	Method is_valid() digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua aturan validasi terhadap field-field dalam form yang mungkin memiliki batasan atau aturan khusus, seperti format email, panjang string, atau nilai numeric.
	Hal tersebut dibutuhkan untuk menjaga konsistensi database serta pengolahan data yang tepat.

## 3.) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
	csrf_token memastikan bahwa permintaan yang dikirim ke server berasal dari pengguna yang tidak mencurigakan. Token ini mencegah penyerang dari membuat permintaan palsu menggunakan kredensial pengguna yang asli.
	Jika csrf_token tidak ada,penyerang dapat melakukan eksploitasi dengan membuat permintaan dengan mengatasnamakan pengguna asli.

## 4.) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
	1.) Membuat input form untuk menambahkan objek model pada app sebelumnya
		Pertama, saya membuat base HTML di folder root sebagai kerangka dasar.
		Kedua, saya membuat file forms.py lalu mengimpor django.forms dan model. Pada file tersebut saya membuat class yang merupakan subclass dari forms.ModelForm. ModelForm secara otomatis menangani pembuatan formulir untuk model sehingga saya hanya perlu menyatakan modelnya dan fieldnya saja.
		Ketiga, saya membuat suatu fungsi pada views.py yang akan menangani tampilan dan pemrosesan form.
		Keempat, saya membuat template html yang akan menampilkan form, yakni add_item.html pada folder main/templates.
		Kelima, saya mendaftarkan url yang mengarah pada view form pada urlpatterns di file urls.py pada direktori main.

	2.) Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
		Pada views.py, saya mengimpor django.http.HttpResponse dan django.core.serializers. Untuk XML dan JSON yang tanpa difilter by id, saya membuat fungsi yang mengambil seluruh object dalam database lalu mengembalikannya ke format yang diinginkan dengan method serialize milik serializers. Untuk object yang difilter dengan id, caranya serupa namun ketika mengambil seluruh data, kita filter bedasarkan id.
		Mengambil seluruh data tanpa difilter -> Item.objects.all()
		Mengambil seluruh data difilter bedasarkan id -> Item.objects.filter(pk=id)

	3.) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
		Cukup daftar url yang sesuai pada urlpatterns di urls.py direktori main dengan format (url, view, nama). Contoh jika ingin menambahkan view show_json kita dapat menambahkan path('json/', show_json, name='show_json'). Contoh lain jika ingin menambahkan view show_json_by_id kita dapat menambahkan path('json/<str:id>/', show_json_by_id, name='show_json_by_id') di urlspattern.

## 5.) Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![alt text](postmanxml.png)
![alt text](postmanjson.png)
![alt text](postmanxmlbyid.png)
![alt text](postmanjsonbyid.png)