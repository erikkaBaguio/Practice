create table users (
   id serial8 primary key,
   name text,
   username text unique,
   password text,
   done boolean
);

create or replace function newuser(par_name  text, par_username text, par_password text, par_done boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin

       insert into users (name, username, password, done) values (par_name, par_username, par_password, par_done);
       loc_res = 'OK';
       return loc_res;
  end;
$$
 language 'plpgsql';

--select newuser('remarc', 'remarcbalisi', 'a', false); 
--select newtask(2, 'Learn Python','Need to find a good Python tutorial on the web', false); 