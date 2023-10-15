# CARA MENGGUNAKAN ANSIBLE API

1. silakan tambahkan hosts terelebih dahulu melalu menu resources pada `ANSIBLE AWX`, dan untuk contoh pengisian variablesnya adalah sebagai berikut : 

```
---
ansible_host: 192.168.18.101
ansible_ssh_user: 'server'
ansible_ssh_pass: 'server'
ansible_python_interpreter: '{{ ansible_playbook_python }}'

```
2. Buatkan `Playbook.yml` di repository github anda dengan contoh isinya seperti dibawah dan jangan lupa di set ke `Public`

 ```
  - name: Ping Two Hosts
  hosts: 
    - host1 # masukkan host anda
    - host2 # masukkan host anda
  gather_facts: no

  tasks:
    - name: Ping Hosts
      ping:

   ```

4. Silahkan tambahkan Project dengan memilih menu `Projects` pada sidebar sebelah kiri ansible awx
   - Masukkan Nama Projek
   - Pilih `Git` pada isian `Source Control Credential Type`
   - dan pastekan link github yang telah dibuat di langkah 2 kedalam
   - selanjutnya pada isian `Options` checklis `Update Revision On Launch`
   - Selanjutnya pilih save untuk menyimpan project

5. Buatkan Inventory
    - Pilih Menu Inventori pada sidebar sebelah kiri
    - Lalu Pilih Add
    - selanjutnya isikan `Name` dan `Description`
    - selanjutnya Pilih Save

6. Buatkan Templae Job
   - Pilih Menu Template pada sidebar sebelah kiri
   - Pilih Add
   - Lalu Masukkan `Name` template
   - selanjutnya pilih `Job Type` ke `Run`
   - selanjutnya Pilih nama `inventory` yang sudah kita buat pada langkah 5
   - seelanjutnya Pilih nama `Project` yang sudah kita buat di langkah 4
   - selanjutnya pilih playbook yang ingin digunakan sesuai dengan nama file di repository `Github` yang kita buat pada langkah 2
   - Selanjutnya pilih save
  
   
