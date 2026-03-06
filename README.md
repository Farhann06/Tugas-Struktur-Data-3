# Praktikum Data Structures & Algorithms (Python)

Repository ini berisi implementasi beberapa algoritma dasar pada mata kuliah **Data Structures & Algorithms** menggunakan bahasa **Python**.

## Daftar Soal

### 1. Modified Binary Search

Program untuk menghitung berapa kali sebuah nilai muncul dalam **sorted list** menggunakan pendekatan **Binary Search**.

**Kompleksitas waktu:**
O(log n)

**Fungsi utama**

* `countOccurrences(sortedList, target)`

**Contoh**

```
Input  : [1,2,4,4,4,4,7,9,12], target = 4
Output : 4
```

---

### 2. Bubble Sort dengan Analisis

Implementasi algoritma **Bubble Sort** yang dimodifikasi untuk:

* Menghitung jumlah **comparisons**
* Menghitung jumlah **swaps**
* Menghitung jumlah **passes**
* Menggunakan **early termination** (berhenti jika array sudah terurut)
* Menampilkan array setelah setiap pass

**Output fungsi**

```
(sorted_list, total_comparisons, total_swaps, passes_used)
```

---

### 3. Hybrid Sort

Algoritma **Hybrid Sort** yang menggabungkan dua algoritma sorting:

* **Insertion Sort** → digunakan jika ukuran array kecil
* **Selection Sort** → digunakan jika ukuran array besar

Tujuan:
Membandingkan jumlah operasi antara:

* Hybrid Sort
* Pure Insertion Sort
* Pure Selection Sort

Pengujian dilakukan pada array acak dengan ukuran:

* 50 elemen
* 100 elemen
* 500 elemen

---

### 4. Merge Tiga Sorted Lists

Program untuk menggabungkan **tiga sorted list** menjadi satu list terurut menggunakan **tiga pointer** dalam **satu pass**.

**Kompleksitas waktu:**
O(n)

**Contoh**

```
Input
A = [1,5,9]
B = [2,6,10]
C = [3,4,7]

Output
[1,2,3,4,5,6,7,9,10]
```

---

### 5. Inversions Counter

Program untuk menghitung jumlah **inversion dalam array**.

Inversion adalah pasangan indeks `(i, j)` dimana:

```
i < j dan arr[i] > arr[j]
```

Dua pendekatan digunakan:

1. **Naive Method**

   * Menggunakan brute force
   * Kompleksitas: O(n²)

2. **Merge Sort Method**

   * Menggunakan modifikasi merge sort
   * Kompleksitas: O(n log n)

Pengujian dilakukan pada ukuran array:

* 1000
* 5000
* 10000

---

## Cara Menjalankan Program

1. Clone repository

```
git clone https://github.com/username/praktikum-algoritma-python.git
```

2. Masuk ke folder project

```
cd praktikum-algoritma-python
```

3. Jalankan program

```
python praktikum.py
```

---

## Teknologi yang Digunakan

* Python 3
* Algoritma Sorting
* Binary Search
* Merge Sort

---

## Tujuan Praktikum

Praktikum ini bertujuan untuk:

* Memahami implementasi algoritma dasar
* Menganalisis kompleksitas algoritma
* Membandingkan performa beberapa metode sorting
* Mengimplementasikan algoritma secara efisien

---

## Author

Nama : **Farhan Bagas F**
Mata Kuliah : **Struktur Data**
