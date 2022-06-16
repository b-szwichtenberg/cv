CREATE TABLE Region
(
	Id_Region SERIAL NOT NULL,
	Nazwa CHAR VARYING(20) NOT NULL,
	CONSTRAINT pk_region PRIMARY KEY(Id_Region),
	CONSTRAINT uq_region UNIQUE(Id_Region)
);

CREATE TABLE Klient 
(
	Id_Klient SERIAL NOT NULL,
	Login CHAR VARYING(20) NOT NULL,
	Imie CHAR VARYING(20),
	Nazwisko CHAR VARYING(30),
	Telefon INT,
	Email CHAR VARYING(40) NOT NULL,
	NIP INT,
	Id_Region INT NOT NULL CONSTRAINT fk_region REFERENCES Region(Id_Region),
	CONSTRAINT pk_klient PRIMARY KEY(Id_Klient),
	CONSTRAINT uq_klient UNIQUE(Id_Klient,Login,Email,NIP,Telefon)
);

CREATE TABLE Sprzedawca
(
	Id_Sprzedawca SERIAL NOT NULL,
	Login CHAR VARYING(20) NOT NULL,
	Imie CHAR VARYING(20),
	Nazwisko CHAR VARYING(30),
	Telefon INT,
	Email CHAR VARYING(50) NOT NULL,
	NIP INT,
	Id_Region INT NOT NULL CONSTRAINT fk_region REFERENCES Region(Id_Region),
	CONSTRAINT pk_sprzedawca PRIMARY KEY(Id_Sprzedawca),
	CONSTRAINT uq_sprzedawca UNIQUE(Id_Sprzedawca,Login,Email,NIP)
);
CREATE TABLE Gra
(
	Id_Gra SERIAL NOT NULL CONSTRAINT pk_gra PRIMARY KEY,
	Nazwa CHAR VARYING(30) NOT NULL,
	Premiera DATE NOT NULL,
	Platforma CHAR VARYING(10) NOT NULL,
	Gatunek CHAR VARYING(20) NOT NULL,
	Producent CHAR VARYING(20) NOT NULL,
	Cena INT NOT NULL,
	CONSTRAINT uq_gra UNIQUE(Id_Gra)
);

CREATE TABLE Reklamacja
(
	Id_Reklamacja SERIAL NOT NULL CONSTRAINT pk_reklamacja PRIMARY KEY,
	Id_Sprzedawca INT NOT NULL CONSTRAINT fk_sprzedawca REFERENCES Sprzedawca(Id_Sprzedawca),
	Id_Klient INT NOT NULL CONSTRAINT fk_klient REFERENCES Klient(Id_Klient),
	Data_Reklamacja DATE,
	CONSTRAINT uq_reklamacja UNIQUE(Id_Reklamacja)
);

CREATE TABLE Faktura
(
    Id_Faktura SERIAL NOT NULL CONSTRAINT pk_faktura PRIMARY KEY ,
	Nr_Faktury CHAR(7) NOT NULL,
	Id_Sprzedawca INT NOT NULL CONSTRAINT fk_sprzedawca REFERENCES Sprzedawca(Id_Sprzedawca),
	Id_Klient INT NOT NULL CONSTRAINT fk_klient REFERENCES Klient(Id_Klient),
    Data_Wystawienia DATE NOT NULL,
	Rabat INT,
	CONSTRAINT uq_faktura UNIQUE(Id_Faktura,Nr_Faktury)
);

CREATE TABLE Faktura_Gra
(
	Id_Gra INT CONSTRAINT fk_fakgra REFERENCES Gra(Id_Gra),
	Id_Faktura INT  CONSTRAINT fk_faktura REFERENCES Faktura(Id_Faktura)
);



CREATE TABLE Reklamacja_Gra
(
	Id_Gra INT CONSTRAINT fk_rekgra REFERENCES Gra(Id_Gra),
	Id_Reklamacja INT CONSTRAINT fk_rek REFERENCES Reklamacja(Id_Reklamacja)
);

CREATE TABLE Transakcja
(
	Id_Transakcja SERIAL NOT NULL CONSTRAINT pk_transakcja PRIMARY KEY,
	Data_Transakcji DATE NOT NULL,
	Rabat INT,
	Id_Sprzedawca INT NOT NULL CONSTRAINT fk_sprzedawca REFERENCES Sprzedawca(Id_Sprzedawca),
	Id_Klient INT NOT NULL CONSTRAINT fk_klient REFERENCES Klient(Id_Klient),
	CONSTRAINT uq_transakcja UNIQUE(Id_Transakcja)
);

CREATE TABLE Transakcja_gry
(
	Iloœæ INT,
	Id_Gra INT CONSTRAINT fk_gra REFERENCES Gra(Id_Gra),
	Id_Transakcja INT CONSTRAINT fk_transakcja REFERENCES Transakcja(Id_Transakcja)
);