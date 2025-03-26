Feature: Automasi Login & Checkout di Saucedemo

  Scenario: Pengguna berhasil login dan checkout
    Given Pengguna membuka halaman login
    When Pengguna memasukkan username dan password
    And Pengguna menekan tombol login
    Then Pengguna berhasil login
    When Pengguna memilih produk dan menambahkannya ke keranjang
    Then Produk berhasil ditambahkan ke keranjang
    When Pengguna menuju halaman checkout
    And Pengguna mengisi informasi checkout
    And Pengguna menekan tombol continue dan menyelesaikan checkout
    Then Checkout berhasil
    Then Tutup browser
