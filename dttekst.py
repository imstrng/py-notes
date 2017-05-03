import datetime

def dttekst(dt):
    '''Retouneert een tekst die afhankelijk is van de datetime die wordt meegestuurd in deze functie.
    Voorbeelden:

    print(  dttekst(datetime.datetime.utcnow()))
    print(  dttekst(datetime.datetime(2016, 8, 1,10,4)))'''

    tekstlijst = ['zo juist', 'een kwartier geleden', '<x> uur geleden', 
    'gisteren', '<x> dagen geleden', 'een week geleden', '<x> weken geleden', 
    'een maand geleden', '<x> maanden geleden', 'meer dan een jaar geleden']
    current = datetime.datetime.utcnow()

    try:    
        diff = current - dt

        # meer dan een jaar geleden
        if diff.days > 365 :
            text = tekstlijst[9]
        # <x> maanden geleden
        elif diff.days > 60:
            val = str(diff.days // 30)
            text = tekstlijst[8]
            text = text.replace('<x>',val)
        # een maand geleden
        elif diff.days > 30:
            text = tekstlijst[7]
        # <x> weken geleden
        elif diff.days > 14:
            val = str(diff.days // 7)
            text = tekstlijst[6]
            text = text.replace('<x>',val)
        # een week geleden
        elif diff.days > 7:
            text = tekstlijst[5]
        # <x> dagen geleden
        elif diff.days > 1:
            val = str(diff.days // 1)
            text = tekstlijst[4]
            text = text.replace('<x>',val)
        # gisteren
        elif diff.days > 0:
            text = tekstlijst[3]
        # <x> uur geleden
        elif diff.seconds > 3600:
            val = str(diff.secconds // 3600)
            text = tekstlijst[2]
            text = text.replace('<x>',val)
        # een kwartier geleden 
        elif diff.seconds > 900:
            text = tekstlijst[1]
        # zo juist
        else:
            text = tekstlijst[0]
    except:
        text = ''

    return text




print(dttekst(datetime.datetime.utcnow()))
print(dttekst(datetime.datetime(2016, 8, 1,10,4)))
print(dttekst(datetime.datetime(2016, 7, 28)))
print(dttekst(datetime.datetime(2016, 7, 20)))
print(dttekst(datetime.datetime(2016, 7, 18)))
print(dttekst(datetime.datetime(2016, 7, 1)))
print(dttekst(datetime.datetime(2016, 6, 1)))
print(dttekst(datetime.datetime(2015, 12, 5)))
print(dttekst(datetime.datetime(2014, 12, 5)))
print(dttekst('ongeldige data'))