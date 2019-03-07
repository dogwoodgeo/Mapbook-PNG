# Bradley Jones 9/23/2016
import arcpy
import time
arcpy.env.overwriteOutput = True

# Create a text file for logging
log = open(r"C:\Mapbook\mapbookLog.txt", "a")
log.write("***************************************************************************************************\n")


# Define function for sending email.
def send_email(user, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("172.21.1.147")
        server.sendmail(FROM, TO, message)
        server.close()
        log.write(str(time.asctime()) + ": Successfully sent email.\n")
    except:
        log.write(str(time.asctime()) + ": Failed to send email.\n")


try:
    # Export for T1NR11W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1NR11W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1NR11W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1NR11W pages exported.\n")

    # Export for T1NR12W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1NR12W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1NR12W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1NR12W pages exported.\n")

    # Export for T1NR13W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1NR13W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1NR13W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1NR13W pages exported.\n")


    # Export for T1NR14W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1NR14W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1NR14W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1NR14W pages exported.\n")


    # Export for T1SR12W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1SR12W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1SR12W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1SR12W pages exported.\n")


    # Export for T1SR13W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T1SR13W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T1SR13W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T1SR13W pages exported.\n")


    # Export for T2NR12W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T2NR12W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T2NR12W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T2NR12W pages exported.\n")


    # Export for T2NR13W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T2NR13W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T2NR13W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T2NR13W pages exported.\n")


    # Export for T2NR13W
    mxd = arcpy.mapping.MapDocument(r"C:\Mapbook\T2NR14W.mxd")
    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
        mxd.dataDrivenPages.currentPageID = pageNum
        pageName = mxd.dataDrivenPages.pageRow.MSH
        print pageName
        arcpy.AddMessage("Page " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " exported.")
        arcpy.mapping.ExportToPNG(mxd, r"C:\Mapbook\Exports\T2NR14W\11x17" + pageName + ".png", resolution=300)
    del mxd
    log.write(str(time.asctime()) + ": T2NR13W pages exported.\n")

except Exception, e:
    log.write(str(time.asctime()) + ": " + str(e) + "- Script failed to complete.\n")

    # Send email to notify of script failure.
    subj = "Mapbook Script Failure"
    content = "Mapbook script failed to complete: " + str(e)
    pitcher = "EMAIL@DOMAIN.com"
    catchers = "another.email@domain.com"
    send_email(pitcher, catchers, subj, content)

log.close()
