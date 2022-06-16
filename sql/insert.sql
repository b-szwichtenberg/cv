INSERT INTO Region VALUES (1,'Europa');
INSERT INTO Region VALUES (2,'Azja');
INSERT INTO Region VALUES (3,'Ameryka Pó³nocna');
INSERT INTO Region VALUES (4,'Ameryka Po³udniowa');
INSERT INTO Region VALUES (5,'Afryka');

INSERT INTO Klient VALUES (1,'jkowal123','Jan','Kowalski',987654321,'jkowalski@mail.com',098765432,1);
INSERT INTO Klient VALUES (2,'ffrank','Franek','Frankowski',123654321,'frank0w5k1@mail.com',228765432,1);
INSERT INTO Klient VALUES (3,'n0wak123','Anna','Nowak',887154321,'An0wakk@mail.com',333765432,1);
INSERT INTO Klient VALUES (4,'j0hn00','John','Johnson',002763547,'johnson61@mail.com',042000432,3);
INSERT INTO Klient VALUES (5,'mar1a','Maria','Alvarez',421654251,'malvarez@mail.com',028465431,4);

INSERT INTO Sprzedawca VALUES (1,'kkkowa1','Krzysiu','Kowalski',667154321,'kowa1sk1@mail.com',123456789,1);
INSERT INTO Sprzedawca VALUES (2,'w1es1U','Wies³aw','Œwiderek',669242210,'swid3r3k@mail.com',321654987,1);
INSERT INTO Sprzedawca VALUES (3,'t3recha','Teresa','Sztaba',632050231,'szteresa@mail.com',789456123,1);
INSERT INTO Sprzedawca VALUES (4,'mar1e','Laura','Stevenson',321009835,'st3v3ns0n@mail.com',012345678,3);
INSERT INTO Sprzedawca VALUES (5,'lu1z','Luiz','Motta',185097698,'lu1zm0@mail.com',456789321,4);

INSERT INTO Gra VALUES (1,'Firewatch','09-02-2016','GOG','Przygodowa','Campo Santo',64.99);
INSERT INTO Gra VALUES (2,'Jade Empire','27-02-2007','Steam','RPG','Bioware',48.88);
INSERT INTO Gra VALUES (3,'KotOR','18-11-2003','Steam','RPG','Bioware',13.39);
INSERT INTO Gra VALUES (4,'The Medium','28-01-2021','Steam','Horror','Bloober',151.35);
INSERT INTO Gra VALUES (5,'Crysis','14-11-2007','Origin','Strzelanka','Crytek',10.16);

INSERT INTO Reklamacja VALUES (1,1,1,'21-11-2020');
INSERT INTO Reklamacja VALUES (2,1,3,'19-12-2020');
INSERT INTO Reklamacja VALUES (3,5,5,'08-03-2021');
INSERT INTO Reklamacja VALUES (4,3,4,'10-04-2021');
INSERT INTO Reklamacja VALUES (5,1,2,'11-02-2021');

INSERT INTO Reklamacja_Gra VALUES (5,1);
INSERT INTO Reklamacja_Gra VALUES (4,2);
INSERT INTO Reklamacja_Gra VALUES (3,3);
INSERT INTO Reklamacja_Gra VALUES (1,4);
INSERT INTO Reklamacja_Gra VALUES (2,5);

INSERT INTO Faktura VALUES (1,0000001,1,1,'24-11-2020',20);
INSERT INTO Faktura VALUES (2,0000002,5,5,'23-10-2020',0);
INSERT INTO Faktura VALUES (3,0000003,4,4,'07-02-2021',30);
INSERT INTO Faktura VALUES (4,0000004,1,2,'03-05-2021',0);
INSERT INTO Faktura VALUES (5,0000005,3,1,'12-01-2021',5);

INSERT INTO Faktura_Gra VALUES (1,3);
INSERT INTO Faktura_Gra VALUES (3,2);
INSERT INTO Faktura_Gra VALUES (5,1);
INSERT INTO Faktura_Gra VALUES (2,5);
INSERT INTO Faktura_Gra VALUES (4,4);

INSERT INTO Transakcja VALUES (1,'24-11-2020',20,1,1);
INSERT INTO Transakcja VALUES (2,'08-08-2020',0,2,3);
INSERT INTO Transakcja VALUES (3,'21-12-2020',0,5,5);
INSERT INTO Transakcja VALUES (4,'06-03-2021',10,4,4);
INSERT INTO Transakcja VALUES (5,'01-04-2021',15,3,1);

INSERT INTO Transakcja_gry VALUES (1,1,1);
INSERT INTO Transakcja_gry VALUES (1,3,2);
INSERT INTO Transakcja_gry VALUES (1,4,3);
INSERT INTO Transakcja_gry VALUES (1,4,4);
INSERT INTO Transakcja_gry VALUES (1,2,5);