import csv
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTPRecipientsRefused

def sendmail(mailmessage,toaddrs):
    try:
        print("Sending mail to: " + sponsor)
        #From and To
        fromaddr = 'svpoltringen@tueit.de'  
        toaddrs  = toaddrs

        #Constructing the MIME Mail Message
        msg = MIMEMultipart('alternative')
        msg.set_charset('utf8')
        msg["FROM"] = fromaddr
        msg["To"] = toaddrs
        msg["Cc"] = "sv.poltringen@arcor.de"
        msg['Subject'] = Header(
            "SV Poltringen Feldsponsor".encode('utf-8'),
            'UTF-8'
        ).encode()

        #Mailcontent
        _attach = MIMEText(mailmessage.encode('utf-8'), 'html', 'UTF-8')        
        msg.attach(_attach)

        # The actual mail send  
        password = 'zqACp4WpDlM2vHtasb'
        server = smtplib.SMTP('smtp.tueit.de:587')  
        server.starttls()  
        server.login(fromaddr,password)
        server.send_message(msg)
        server.quit()
    except SMTPRecipientsRefused as e:
        print("Error sending to Addr: " + toaddrs + " " +  str(e))



if __name__ == "__main__":

    with open('generate_email_from_csv/mailmessage.html') as mailfile:
        messagetemplate = mailfile.read()

    with open('generate_email_from_csv/unpaied_reservations.csv') as csvfile:
        
        #Parse the CSV-File
        reader = dict_reader = csv.DictReader(csvfile)
        line_count = 0
        collection = {}
        for row in reader:
            #First Row => Column Names
            if line_count == 0:
                column_names = row
                print(row)
                line_count += 1
            #Content
            else:
                feld = row["id"]
                price = row["price"]
                email = row["email"]
                feldbuchung = [feld,price]
                try:
                    collection[email].append(feldbuchung) 
                except KeyError:
                    collection[email] = []
                    collection[email].append(feldbuchung)
                line_count +=1

        #Dump unpaied reservations to json file
        with open('generate_email_from_csv/unpaied_reservations.json', 'w') as outfile:
            json.dump(collection, outfile)

        #Create and send Emails
        for sponsor,feldbuchungen in collection.items():
            felder = ""
            price_sum = 0
            for feldbuchung in feldbuchungen:
                if(felder != ""):
                    felder += ", " + feldbuchung[0]
                else:
                    felder = feldbuchung[0]
                price_sum += int(feldbuchung[1])
            mailmessage = messagetemplate.format(feld=felder,price=price_sum)
            #sendmail(mailmessage,sponsor)
            
        
        
            