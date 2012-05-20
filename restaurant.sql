create database food;

use food;

drop table restaurant;

create table restaurant (
	id int not null auto_increment primary key,
	name varchar(100) not null,
	street varchar(150),
	city varchar(50),
	state varchar(50),
	zip varchar(10),
	country varchar(30),
	latlng varchar(50),
	index(name),
	index(city),
	index(state),
	index(zip),
	index(street),
	index(country)
);

desc restaurant;

