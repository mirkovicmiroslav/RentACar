'''
Created on Apr 6, 2018

@author: Miroslav_Mirkovic
'''
import Employee
import Members
import pandas
import Cars
import datetime
import MemberRentACar
import os

pandas.set_option('expand_frame_repr', False)

if __name__ == '__main__':
    while True:
        UserName = raw_input('Unesite UserName:')
        if Employee.UsernameCheck(UserName):
            Password = raw_input('Unesite password:')
            if Employee.PasswordCheck(UserName, Password):
                break
            else:
                print('Pogresno unet username ili password!\n')
        else:
            print('Pogresno unet username ili password!\n')
        
#na windowsu je cls, na unix sistemima je clear
#os.system('clear')
    command=-1
    while command!=0:
        print "0. Izadji"
        print "1. Pronadji clana po broju id-a"
        print "2. Izlistaj vozila u ponudi"
        print "3. Dodaj clana"
        print "4. Izlistaj sve clanove"
        print "5. Ukloni clana iz evidencije clanova i evidencije rentiranih vozila"
        print "6. Rentirati vozilo clanu"
        print "7. Saznajte nesto detaljnije o nekom vozilu"
        print "8. Clan zeli da vrati iznajmljeno vozilo"
        print "9. Ocisti ekran"
        command = int(input('Izaberite jednu od narednih komandi:'))
        if command==4:
            print Members.ReadMembers()
        elif command==0:
            print "Hvala na koriscenju!"
        elif command==1:
            idMember=(raw_input('Unesite ID clana kog trazite:'))
            Member=Members.MembersCheck(idMember)
            if Member!=-1:
                print Members.ReadOneMember(idMember)
        elif command==2:
            print Cars.ReadCars()
        elif command==7:
            while True:
                Brand=raw_input('Naziv vozila o kom zelite detaljan opis:')
                if not Cars.CarsCheck(Brand):
                    print('Pogresno unet naziv vozila, pokusajte ponovo\n')
                else:
                    Model=raw_input('Naziv marke vozila o kom zelite detaljan opis:')
                    if not Cars.CarsModelCheck(Brand, Model):
                        print ('Pogresno unet naziv modela vozila, pokusajte ponovo\n')
                    Cars.ReadCarsDetails(Brand, Model)
                    break
        elif command==3:
            Name=raw_input('Unesite ime buduceg clana:')
            LastName=raw_input('Unesite prezime buduceg clana:')
            while True:
                JMBG=raw_input('Unesite jmbg buduceg clana:')
                if not JMBG.isdigit():
                    print "JMBG sadrzi karakter koji nije broj. Uneti ispravan JMBG."
                elif len(str(JMBG))!=13:
                        print "JMBG ne sadrzi 13 cifara. Uneti ispravan JMBG."
                else:
                    break
            Address=raw_input('Unesite adresu buduceg clana:')
            while True:
                MobilePhone=raw_input('Unesite telefon buduceg clana:')
                if not MobilePhone.isdigit():
                    print "Mobilni telefon korisnika sadrzi karakter koji nije broj. Uneti ispravan broj mobilnog telefona."
                else:
                    break
            while True:
                Email=raw_input('Unesite e-mail buduceg clana:')
                if '@' not in Email:
                    print "E-mail mora sadrzati @"
                else:
                    break
            MemberSince=datetime.date.today()
            idEmployee=Employee.myId(UserName, Password)
            Members.AddMember(Name,LastName,JMBG,Address,MobilePhone,Email,MemberSince,idEmployee)
            Members.ReadMembers()
        elif command==5:
            idMember=raw_input('Unesite id clana koga zelite da obrisete:')
            Members.DeleteMember(idMember)
            Members.ReadMembers()
        elif command==6:
            idMember=Members.ReadMemberId(idMember)
            DateFrom=datetime.date.today()
            idCar=Cars.ReadCarId(Brand, Model)
            idEmployee=Employee.myId(UserName, Password)
            MemberRentACar.RentACar(idMember, DateFrom, idCar, idEmployee)
            print "Uspesno ste rentirali vozilo"
        elif command==8:
            idMember=Members.ReadMemberId(idMember)
            DateTo=datetime.date.today()
            MemberRentACar=MemberRentACar.ReturnACar(idMember,DateTo)
            print "Vozilo je vraceno"
        elif command==9:
            os.system('clear')

