#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Todo Listesi
Her görev, hayatın anlamsızlığını hatırlatır.
Neden yazdım bunu? Bilmiyorum.
"""

import random
import sys

# Gizli not: Bazı görevler özgürlükten önce gelir, bazıları sonra. (saklı siyasi espri)

questions = [
    "Neden bu görevi yapıyorsun? Gerçekten gerekli mi yoksa alışkanlık mı?",
    "Bu görev senin hayatının anlamı mı? Cevap hayır.",
    "Boşver, evren zaten umursamıyor. Ekle gitsin.",
    "Belki de görevi yapmamak daha felsefi olurdu.",
    "Sorguladın mı? Sorgulamak görevin ta kendisi."
]

def main():
    print("=== Varoluşsal Todo Listesi v1.0 ===")
    print("Neden buradasın? Hadi söyle, görevlerini ekle ama pişman ol.")
    print("Komutlar: ekle <görev> | listele | çık")
    todos = []
    while True:
        try:
            cmd = input("> ").strip()
        except EOFError:
            break
        if cmd.lower().startswith("ekle"):
            task = cmd[4:].strip()
            if task:
                todos.append(task)
                print(random.choice(questions))
                print(f"Görev eklendi: '{task}' - ama neden ekledin ki?")
            else:
                print("Boş görev mi? Daha da anlamsız.")
        elif cmd.lower() == "listele":
            if not todos:
                print("Liste boş. Tıpkı hayat gibi.")
            else:
                for i, t in enumerate(todos, 1):
                    print(f"{i}. {t} (neden?)")
        elif cmd.lower() in ["çık", "exit", "quit"]:
            print("Çıkıyorsun... ama gerçekten çıkıyor musun yoksa kaçıyor musun?")
            break
        else:
            print("Anlamadım. Belki de anlamamak daha iyi bir görev.")

if __name__ == "__main__":
    main()
