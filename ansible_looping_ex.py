- name: showing off loops in ansible
  hosts: localhost
  connection: local

  vars:
    books:
    - Title: Watchmen
      Author: Alan Moore
    - Title: Eragon
      Author: Christopher Paolini
    - Title: The Hobbit
      Author: J.R.R. Tolkien
    - Title: Ender's Game
      Author: Orson Scott Card

        # for item in books:
        #   print(item)
  tasks:
   - name: print out a bunch o' books
     debug:
       msg: "{{ item.Title }} by {{item.Author}} is my favorite book!"
     loop: "{{ books }}"

