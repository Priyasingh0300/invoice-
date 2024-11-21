from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")




doc.render({"name":"priya"})
doc.save("new_invoice.docx")


