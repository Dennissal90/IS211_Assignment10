CREATE TABLE Artists (
    ArtistID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE Albums (
    AlbumID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    ArtistID INTEGER,
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID)
);

CREATE TABLE Songs (
    SongID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    AlbumID INTEGER,
    TrackNumber INTEGER,
    Duration INTEGER, -- Duration in seconds
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID)
);