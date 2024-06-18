from fpdf import FPDF

ref = FPDF()
ref.add_page()
ref.set_font('Arial', size=24)
ref.cell(200,100," I am rohit pujari and i am a engineer",align="L")
ref.output("intro pdf")