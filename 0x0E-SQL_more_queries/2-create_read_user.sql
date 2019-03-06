-- Creates the DB hbtn_0d_2 and the user user_0d_2
-- user should have SELECT in DB hbtn_0d_2; password: user_0d_2_pwd
-- if it exists it shouldn't fail
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
