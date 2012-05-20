
use food;

create table menuItems (
	id int not null auto_increment primary key,
	restid int not null,
	menu varchar(100) not null,
	description varchar(200),
	image text,
	thumbnail text,
	
	CONSTRAINT ikf_restid FOREIGN KEY ('restid')
	REFERENCES restaurant(id)
);
