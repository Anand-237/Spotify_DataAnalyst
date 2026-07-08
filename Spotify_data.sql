use spotify_db;

create table spotify_entity(
	Track_Name varchar(30),
    Artists_Name varchar(30),
    Duration float,
    Album_Id varchar(40),
    ReleaseDate date,
    Playable boolean,
    Disc_Number int,
    Track_Type varchar(10),
    Popularity int
    );
