# ARP_spoofing_detector
-----------------------------------------------
Bu program her 5 saniyede ARP saldırısı olup olmadığını denetler. Herhangi bir girdi almaz. Bunu yaparken Unix sisltemlerde "/proc/net/arp" dosyası üzerindeki ARP tablosunu kullanır. Program çıktı olarak terminal ekranına sürekli ağda bulunan MAC adreslerini yazar. Bir saldırı olması durumunda terminal ekranına "ARP ZEHİRLEME" yazarken aynı zamanda bir masaüstü bildirimi de oluşturur.

Fazladan Bağımlılıklar

python-notify2

sudo apt install python-notify2
