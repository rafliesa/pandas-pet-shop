LINK PWS : http://muhammad-rafli33-pandaspetshop.pbp.cs.ui.ac.id/


# TUGAS 2

## 1.) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
##### Membuat sebuah proyek Django baru
Membuat folder lalu membuat venv python. Setelah itu menginstal beberapa library yang berguna untuk pengembangan. Lalu, inisisai project Django dengan "django-admin startproject (nama project) .".

##### Membuat aplikasi dengan nama main pada proyek tersebut
Melakukan perintah "python manage.py startapp main", lalu menambahkan 'main' di variable INSTALLED_APPS pada berkas settings.py

##### Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
Membuat berkas urls.py di dalam folder main. Lalu, menyematkan method show_main dari vies ke urlpatterns. lakukan hal yang sama pada urls.py dalam direktori projek.

##### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
Membuat subclass dengan nama model yang ingin didenfinisikan dari models.Model dengan atribut wajib tersebut

##### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
Membuat fungsi show_main berisi dictionary yang berisi data yang akan dikirimkan ke tampilan.

##### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Mengisi variable app_name dengan main pada berkas urls.py

##### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Membuat project baru di pws, lalu hubungkan dengan repositori local, lalu push ke pws.



	
## 2.) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://www.figma.com/board/vbT6XJN88CA1fa0em6EhCa/Untitled?node-id=0-1&t=4grBKEOgOdpiik0p-1



## 3.) Jelaskan fungsi git dalam pengembangan perangkat lunak!
1. Menyimpan riwayat perubahan
Git membantu menyimpan riwayat perubahan serta oleh siapa perubahan tersebut dilakukan. Hal ini berguna jika ingin kembali ke versi sebelumnya, misal, karena kesalahan pengembangan versi terbaru, kode atau aplikasi justru semakin hancur.

2. Melakukan pemisahan kode dengan branching
Hal ini bermanfaat jika kita ingin mengembangkan perangkat lunak secara terpisah ari kode Utama.

3. Melakukan penggabungan kode dengan merging
Hal ini bermanfaat jika kita ingin menggabungkan Kembali kode tersebut dengan kode Utama.

4. Kolaborasi
Dengan Git, beberapa pengembang dapat bekerja pada proyek yang sama secara bersamaan. Git mengelola penggabungan perubahan dari berbagai pengembang dan menyelesaikan konflik yang mungkin muncul.



## 4.) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django ditulis dengan bahasa Python yang tergolong mudah dicerna penulisannya. Hal ini memungkinkan pemula berfokus lebih kepada logikanya dibanding dengan sintaks.

## 5.) Mengapa model pada Django disebut sebagai ORM?
Karena Django menyediakan cara untuk berinteraksi dengan database relasional menggunakan objek Python. 


# TUGAS 3

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
##### Membuat input form untuk menambahkan objek model pada app sebelumnya
1. Pertama, saya membuat base HTML di folder root sebagai kerangka dasar.
2. Kedua, saya membuat file forms.py lalu mengimpor django.forms dan model. Pada file tersebut saya membuat class yang merupakan subclass dari forms.ModelForm. ModelForm secara otomatis menangani pembuatan formulir untuk model sehingga saya hanya perlu menyatakan modelnya dan fieldnya saja.
3. Ketiga, saya membuat suatu fungsi pada views.py yang akan menangani tampilan dan pemrosesan form.
4. Keempat, saya membuat template html yang akan menampilkan form, yakni add_item.html pada folder main/templates.
5. Kelima, saya mendaftarkan url yang mengarah pada view form pada urlpatterns di file urls.py pada direktori main.

##### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Pada views.py, saya mengimpor django.http.HttpResponse dan django.core.serializers. Untuk XML dan JSON yang tanpa difilter by id, saya membuat fungsi yang mengambil seluruh object dalam database lalu mengembalikannya ke format yang diinginkan dengan method serialize milik serializers. Untuk object yang difilter dengan id, caranya serupa namun ketika mengambil seluruh data, kita filter bedasarkan id.
Mengambil seluruh data tanpa difilter -> Item.objects.all()
Mengambil seluruh data difilter bedasarkan id -> Item.objects.filter(pk=id)

##### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Cukup daftar url yang sesuai pada urlpatterns di urls.py direktori main dengan format (url, view, nama). Contoh jika ingin menambahkan view show_json kita dapat menambahkan path('json/', show_json, name='show_json'). Contoh lain jika ingin menambahkan view show_json_by_id kita dapat menambahkan path('json/<str:id>/', show_json_by_id, name='show_json_by_id') di urlspattern.

## 5.) Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![alt text](postmanxml.png)
![alt text](postmanjson.png)
![alt text](postmanxmlbyid.png)
![alt text](postmanjsonbyid.png)

# Tugas 4

## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect() ?
Perbedaannya terdapat pada argumen pertamanya. redirect() lebih fleksibel dibandingkan dengan
HttpResponseRedirect() yang hanya bisa diisi oleh url, sedangkan argumen pertama redirect() dapat diisi
oleh model, view, atau url. 

## 2.) Jelaskan cara kerja penghubungan model Product dengan User!
Yaitu dengan menambahkan Foreign Key pada model Product yang akan mengarah ke User.
Potongan code:
user = models.ForeignKey(User, on_delete=models.CASCADE)
argumen pertama berfungsi untuk mengarahkan ke User.
argumen kedua berfungsi untuk memberi kondisi jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

## 3.) Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication  -> Memverifikasi identitas pengguna, contohnya login.
Authorization   -> Memeriksa apa saja yang boleh dilakukan pengguna, contohnya admin dapat melakukan suntingan sedangkan pengguna biasa tidak.

Saat pengguna login, kedua proses tersebut terjadi.

Proses autentikasi
1. Pengguna memasukkan identitas di halaman login.
2. Sistem mencocokkan identitas tersebut dengan data pengguna yang tersimpan dalam database.
3. Jika cocok, pengguna berhasil masuk dan Django membuat sesi untuk pengguna tersebut.
4. Jika tidak cocok, sistem akan meminta pengguna untuk memasukan kembali identitas yang sesuai.

Proses otorisasi
1. Setelah autentikasi berhasil, pengguna dapat meminta akses ke berbagai halaman atau fitur.
2. Django memeriksa hak akses pengguna terhadap permintaan akses terhadap suatu halaman atau fitur.
3. Jika pengguna memiliki otorisasi yang tepat, mereka diperbolehkan untuk mengakses halaman atau fitur tersebut.

Implementasi autentikasi di Django
1. User melakukan submisi form kredensialnya, biasanya username dan password.
2. View melakukan autentikasi dengan fungsi authenticate() yang akan mengecek submisi form pengguna pada database.
3. Jika sesuai, maka Django akan membuat sesi untuk pengguna tersebut.

Implementasi otorisasi di Django
1. Ketika membuat User, Django secara otomatis menambahkan perizinan untuk melakukan sesuatu.
2. Dengan Grouping. Grouping mengelompokan User ke dalam kelompok tertentu dengan perizinan tertentu.
3. Mengecek perizinan pada views dengan menambah dekorator @permission_required

## 4.) Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan cookies dan session. Cookies dan session dapat membuat http yang stateless memiliki holding state. Django tidak menyimpan informasi secara langsung pada cookies dengan alasan keamanan. Cookies pada django hanya menyimpan rangkaian token (sessionid) yang akan dipetakan ke database server yang mana database tersebut menyimpan semua informasi pengguna.

Kegunaan lain dari cookies adalah:
1. Menyimpan preferensi pengguna
2. Melacak aktivitas pengguna

Tidak semua cookies aman digunakan. Ciri-ciri cookies yang tidak aman adalah tidak menggunakan tokenizer. Dengan kata lain, informasi langsung disimpan pada cookies.

## 5.) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
##### Membuat registrasi
1. Mengimpor UserCreationForm untuk membuat form registrasi pengguna.
2. Membuat fungsi dan form registrasi pada views.py dengan class bawaan Django UserCreationForm. Form tersebut dimasukan input user pada request.POST lalu melakukan validasi dengan method is_valid(). Jika form valid, simpan form dan redirect ke view login.
3. Membuat template html untuk registrasi yang akan dirender oleh fungsi yang sebelumnya telah dibuat.
4. Melakukan routing registrasi tadi ke url.py direktori main untuk menambahkan path.

##### Membuat login
1. Mengimpor fungsi authenticate, login yang berguna untuk melakukan autentikasi dan login.
2. Membuat fungsi dan form autentikasi untuk login dengan class bawaan Django AuthenticationForm. AuthenticationForm akan menerima submisi user lalu validasi dengan method is_valid(). Jika valid, maka panggil fungsi login() dengan parameter user yang didapat dari submisi form. Lalu lakukan redirect ke view main.
3. Membuat template html untuk login yang akan dirender oleh fungsi yang sebelumnya dibuat.
4. Melakukan routing login tadi ke url.py direktori main untuk menambahkan path.

##### Membuat logout
1. Mengimpor fungsi logout.
2. Membuat fungsi untuk logout yang akan memanggil fungsi logout. Pemanggilan fungsi logout akan menghapus sesi pengguna yang masuk. Lalu redirect ke view login.
3. Menambahkan tombol logout pada view main.
4. Melakukan routing logout tadi ke url.py direktori main untuk menambahkan path.

##### Menghubungkan model Product dengan User.
1. Mengimpor class User yang telah didefinisikan Django.
2. Tambahkan variabel user pada Product dengan value berupa foreign key dari user untuk menandai bahwa product tersebut terhubung ke suatu User dengan key tertentu.
3. Ubah view untuk menambahkan item sehingga item yang ditambahkan diasosiasikan dengan User yang didapat dari user yang sedang melakukan request.
4. Lakukan migrasi pada model.

##### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Mengimpor datetime serta fungsi reverse dan class HtpResponseRedirect dari Django.
2. Pada fungsi yang mengatur login, atur cookie last_login menjadi waktu tepat pada saat login dengan libary datetime.
3. Ubah value dari dictionary context dengan key 'nama' menjadi nama dari user yang sedang login dari request.
4. Pada dictionary context, tambahkan key last_login dengan value cookies last_login yang telah ditambahkan pada tahap 2.
5. Pada fungsi yang mengatur logout, delete cookie last_login.
6. Tambahkan template variable pada view main yang menampilkan last login user dengan mengambil datanya dari key yang telah ditambahkan pada step 4.

##### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
1. Jalankan server django.
2. Buatlah 2 akun.
3. Tambahkan 3 entry untuk masing-masing akun.


# Tugas 5

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline style, yaitu css yang langsung diterapkan di dalam tag html dengan menggunakan atribut "style".
2. Internal style sheets, yaitu css yang berada pada tag head file html.
3. External style sheets, yaitu css yang berada pada file terpisah dengan file html.
4. Browser default, yaitu css bawaan dari browser.

Pada internal style sheets maupun external style sheets, pemgambilan tersebut memiliki prioritas:
1. ID Selector, permulaannya diawali dengan "#"
2. Class atau Pseudo-class selectors, yang permulaannya diawali dengan "." (titik). untuk pseudo-class, setelah nama class diberi tanda titik 2, lalu nama pseudo-classnya.
3. Type/element, yaitu langsung menggunakan nama tag HTML
4. Universal selector, yaitu dengan menggunakan tanda "*" dengan arti memilih semua elemen.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Agar pengaksesan aplikasi web tersebut memiliki pengalaman pengguna yang sama pada setiap perangkat.
Yang sudah -> Scele / scele.cs.ui.ac.id
Yang belum -> SIAK-NG / academic.ui.ac.id

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
#### Margin
Margin adalah ruang yang berada di luar element, cara mengimplementasikannya adalah dengan menggunakan property margin dan himpunannya.

Contoh:
.foo {
    margin-top: 10px;
    margin-bottom: 15px;
    margin-inline: 5px;
}

Dengan styling seperti itu, kita membuat ruang sebesar 10px di atas foo, 15px di bawah foo, 5px di kanan dan kiri foo. Jika kita ingin membuat ruang dengan besar yang sama di setiap sisi, kita dapat menggunakan "margin: npx;".

#### Border
Border adalah batas dari element html, cara mengimplementasikannya adalah dengan menggunakan property border dan himpunannya.
Contoh, jika ingin menebalkan border dari suatu html sebesar 2px kita dapat melakukan:

.foo {
    border: 2px solid;
}

#### Padding
Padding adalah ruang di antara isi dari element dengan border element, cara mengimplementasikannya adalah dengan menggunakan property padding dan himpunannya.
Contoh, jika ingin memberikan jarak antara border dengan isi element sebesar 20px, kita dapat melakukan:

.foo {
    padding: 20px;
}

Dengan styling seperti itu, pada setiap sisi konten dengan border memiliki jarak sebesar 20px. Sama halnya dengan margin, jika kita ingin memberikan ruang pada salah satu sisi saja, kita dapat menggunakan padding-top, padding-bottom, padding-left, atau padding-right.

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
#### Flex box
Flexbox adalah layout model css yang memungkinkan layout menjadi lebih responsif dan efisien. Flexbox memudahkan pengaturan ruang di antara elemen dalam suatu kontainer dan mengelola ukuran serta penempatan element tersebut.

##### Konsep Flex box

Flex container: Element yang berisi satu atau lebih flex items. Untuk mendefinisikan sebuah elemen sebagai flex container, Kita dapat menggunakan properti CSS display: flex; atau display: inline-flex;.

Flex items: Element yang berada di dalam flex container. Setiap elemen di dalam flex container secara otomatis menjadi flex item.

#### Grid
Grid adalah layout model css yang memiliki konsep baris dan kolom. Hal ini memungkinkan pengembang memiliki kontrol penuh atas penempatan element html. 

##### Konsep Grid
Grid Container: Elemen yang menjadi wadah (container) untuk grid items. Elemen didefinisikan sebagai grid container menggunakan properti display: grid; atau display: inline-grid;.

Grid Items: Elemen-elemen yang berada di dalam grid container. Elemen ini otomatis menjadi grid items setelah grid container didefinisikan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Implementasikan fungsi untuk menghapus dan mengedit product.
Untuk melakukan checklist ini, saya mendefinisikan fungsi yang mengatur view masing-masing. Untuk fitur mengedit, saya menggunakan form item (product) yang saya implementasikan sebagai child class dari form bawaan django. Form tersebut akan dikonstruksi dengan parameter item yang diambil bedasarkan primary keynya. Setelah itu saya membuat template htmlnya dengan menggunakan atribut form yang akan diisi dengan form yang telah saya definisikan sebelumnya. 
Untuk fitur hapus, cukup ambil item bedasarkan primary key lalu lakukan method delete. Setelah itu, routing kedua views tersebut ke urls.py direktori main.

#### Hal-hal yang berkaitan dengan CSS
Saya melakukan checklist ini dengan GSGS (Google sana Gooogle sini). Jika memungkinkan saya menggunakan tailwind, jika tidak saya menggunakan css external. Untuk menjaga agar web tetap responsif, saya menghindari penggunaan satuan px dengan menggunakan satuan vw atau vh.

#### Membuat card beserta tombol untuk edit dan hapus
Saya membuat file html dinamis terpisah khusus untuk card saja. Pada berkas html tersebut saya menggunakan div nesting yang layoutnya diatur dengan flexbox. Pada card tersebut, saya tambahkan detail item dengan menggunakan html dinamis django yang memungkinkan penggunaan variable yang merujuk ke item yang diinginkan. Untuk tombol edit dan hapus, saya menggunakan tag hyperlink yang akan merujuk ke views masing-masing untuk edit atau hapus. Setelah itu dapat dilakukan *styling* dengan css.

Setelah itu saya melakukan iterasi items yang telah ditambahkan ke dalam berkas main.html sehingga akan memunculkan item-item yang telah ditambahkan. Apabila items masih kosong, cetak pesan khusus.

#### Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Pertama, saya membuat file navbar.html pada direktori root/templates/. Setelah itu, saya mengimplementasikan navbar dengan tag "nav" yang akan diisi dengan berbagai element div untuk shortcut yang sesuai dengan kebutuhan. Untuk membuatnya menjadi resposnif, saya menggunakan tailwind untuk menambahkan properti tertentu yang bisa diletakan langsung di dalam atribut class. Salah satu propertinya adalah "hidden md:flex items-center" yang akan menyembuyikan elemen jika ukuran layar dibawah ukuran medium (768px). Kebalikan dari hal tersebut, saya juga membuat hamburger button yang hanya akan munucul jika ukuran layar dibawah ukuran medium. Jika ditekan, hamburger button tersebut akan menampilkan shortcut dalam bentuk stack.

Untuk menambahkan navbar tersebut ke tiap template yang memerlukannya, saya menambahkan templating {% include 'navbar.html' %}.

# Tugas 6

## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Beberapa manfaat dari penggunaan JavaScript adalah:
1. Interaksi menjadi lebih dinamis
Penggunaan JavaScript memungkinkan interaksi pada aplikasi web secara langsung tanpa perlu memuat ulang seluruh halaman (_refresh_).
2. Manipulasi dokumen HTML secara langsung
Hal ini memungkinkan pengembang untuk mengubah, menghapus, atau menambah _element_ pada dokumen HTML yang sedang ditampilkan tanpa perlu memuat ulang seluruh halaman (_refresh_).
3. Asynchronous Processing (AJAX)
Dengan teknologi seperti AJAX, JavaScript memungkinkan pengambilan data dari server secara asinkron tanpa memuat ulang halaman. Ini sangat membantu dalam membuat aplikasi yang cepat dan responsif.

## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Penggunaan await dimaksudkan agar JavaScript menunggu hasil pengambilan data, baik berhasil maupun gagal, dari fungsi fetch() selesai. 

**Apa yang akan terjadi jika kita tidak menggunakan await?**
Program mungkin akan mengalami masalah pemrosesan data, seperti mencoba mengakses data yang belum tersedia atau menggunakan objek yang belum terdefinisi.

Alternatif lain adalah dengan menggunakan ".then()"
    get_item().then((items) => {
    // do something
    });

## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Penggunaan decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi ini. Decorator tersebut digunakan karena permintaan AJAX sering kali tidak dapat menyertakan token CSRF dengan cara yang sama seperti form HTML biasa. Ini bisa menyebabkan permintaan AJAX POST ditolak oleh Django.

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Karena pengguna yang jahat dapat saja mengirimkan permintaan langsung ke server tanpa melalui frontend, misalnya dengan menggunakan Postman. Namun, pembersihan data input pengguna yang dilakukan di frontend juga penting dilakukan sebagai keamanan lapis pertama.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Mengubah kode cards data mood agar dapat mendukung AJAX GET.
Pada views, saya mengubah fungsi add_item pada view dengan menspesifikasikan penerimaan masing-masing fields. Lalu tambahkan decorator "@csrf_exempt", "@require_POST" untuk fungsi tersebut.

Lalu, karena kita akan mendapatkan objek melalui endpoint json, saya mengubah variabel data di fungsi show_xml dan show_json menjadi bedasarkan user.

Setelah itu, saya menghapus bagian yang mengiterasi produk pada main.html menggantikannya dengan element div baru sebagai tempat untuk card yang akan diiterasi dengan menggunakan fetch API. Div tersebut akan saya referensikan sebagai card_div kedepannya.   

Lalu, saya membuat sebuah fungsi JavaScript yang menggunakan fetch API yang akan mengambil data json secara _asynchronous_. Setelah di-fetch, saya tambahkan fungsi then() untuk mengubah data json menjadi object javascript.
Potongan kode:
    async function addItem(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }

Untuk menampilkan cardnya, saya membuat fungsi JavaScript yang akan menambahkan element di card_div dengan setiap card yang dimiliki user. Card tersebut diperoleh dengan memanggil fungsi yang telah didefinisikan di atas. Fungsi ini dapat mengubah berkas HTML tanpa perlu melakukan refresh pada page. Sehingga setiap kali ada perubahan pada database, kita akan memanggil fungsi ini.

#### Membuat sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
Pertama, saya membuat suatu div HTML dibawah card_div yang berfungsi sebagai tampilan serta form untuk menambahkan product. Form tersebut dispesifikasikan inputnya yang harus sesuai dengan field pada model. Div ini akan kita sebut sebagai modal kedepannya.

Setelah itu, saya membuat suatu tombol yang akan terhubung dengan fungsi untuk menambahkan modal. Hal tersebut dapat diimplementasikan dengan menggunakan atribut onclick='fungsi'. Tombol tersebut akan memodifikasi dokumen HTML untuk menampilkan atau menyembunyikan modal jika ditekan.

Setelah itu, saya membuat fungsi yang akan mengirimkan form pada modal lalu mengaitkannya dengan tombol submit pada form modal.

Selain itu, tombol submit juga akan terhubung dengan fungsi add_item yang telah didefinisikan di atas. Sehingga setiap kita menambahkan item, dokumen HTML dimodifikasi sehingga dokumen tersebut menyertakan card item baru dari item yang baru kita buat tanpa perlu refresh page.