from PIL import Image, ImageDraw, ImageFont
import os
import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1dBFzUMXbEMDSPuoyDOi6l2gGnDG-fnK1dNt4h8ei_H0"
workbook = client.open_by_key(sheet_id)

# Load the certificate template
template_path = 'certificate_template.jpg'
template = Image.open(template_path)

# Set up font and text position
font_path = 'font file path/arial.ttf'  # Path to the font file
font_size = 50  # Adjust the size as needed
font = ImageFont.truetype(font_path, font_size)
text_color = (50, 50, 200)  # Color of the text

# Coordinates for the text (adjust these based on your template)
name_x, name_y = 200, 320

# Load participant names
# All The participant names were in this list.
# Can easily generate using pandas
participants = ["ZZZ", "XXX", "YYY"]

# Output directory
output_dir = "certificates"
os.makedirs(output_dir, exist_ok=True)

# Generate certificates
for name in participants:
    # Make a copy of the template
    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    # Add the participant's name
    draw.text((name_x, name_y), name, fill=text_color, font=font)

    # Save the certificate
    output_path = os.path.join(output_dir, f"{name}.jpg")
    cert.save(output_path)
    print(f"Certificate generated for: {name}")

print("All certificates have been generated.")

function sendCertificates() {
  // Spreadsheet information
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Form Responses 1"); 
  var data = sheet.getDataRange().getValues();
  
  // Google Drive folder ID where certificates are stored
  var folderId = "folder_id"; // Replace with your actual folder ID
  var folder = DriveApp.getFolderById(folderId);

  // Iterate over rows in the sheet
  for (var i = 1; i < data.length; i++) { // Start at 1 to skip the header row
    var email = data[i][1]; // B column - Email Address
    var name = data[i][2]; // C column - Full Name
    var subject = "Participation Certificate";
    var body = "Hello " + name + ",\n\n" +
               "Congratulations on successfully <<complete mail..>>";

    // Search for the certificate file by name within the folder
    var files = folder.getFilesByName(name + ".jpg"); // Adjust extension if needed
    
    if (files.hasNext()) {
      var file = files.next();
      MailApp.sendEmail({
        to: email,
        subject: subject,
        body: body,
        attachments: [file.getAs(MimeType.JPEG)] // Adjust MimeType if using a different file format
      });
      Logger.log("Email sent to: " + email);
    } else {
      Logger.log("Certificate not found for: " + name);
    }
  }
}
function sendCertificates() {
  // Spreadsheet information
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet2"); 
  var data = sheet.getDataRange().getValues();
  
  // Google Drive folder ID where certificates are stored
  var folderId = "folder_id"; // Replace with your actual folder ID
  var folder = DriveApp.getFolderById(folderId);

  // Iterate over rows in the sheet
  for (var i = 1; i < data.length; i++) { // Start at 1 to skip the header row
    var email = data[i][1]; // B column - Email Address
    var name = data[i][2].trim().replace(/\s+/g, ' '); // C column - Full Name (trimmed and spaces normalized)
    var subject = "Participation Certificate ";
    var body = "Hello " + name + ",\n\n" +
               "Congratulations on successfully <<complete mail..>>";

    // Search for the certificate file by name within the folder
    var files = folder.getFiles();
    var fileFound = false;

    while (files.hasNext()) {
      var file = files.next();
      var fileName = file.getName().trim().replace(/\s+/g, ' ').toLowerCase();
      
      if (fileName === name.toLowerCase() + ".jpg") { // Adjust extension if needed
        MailApp.sendEmail({
          to: email,
          subject: subject,
          body: body,
          attachments: [file.getAs(MimeType.JPEG)] // Adjust MimeType if using a different file format
        });
        Logger.log("Email sent to: " + email);
        fileFound = true;
        break;
      }
    }

    if (!fileFound) {
      Logger.log("Certificate not found for: " + name);
    }
  }
}
