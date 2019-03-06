-- Creates the DB hbtn_0d_2 and the user user_0d_2
-- user should have SELECT in DB hbtn_0d_2; password: user_0d_2_pwd
-- if it exists it shouldn't fail
CREATE DATABASE hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost IDENTiFIED BY 'user_0d_2_pwd';
