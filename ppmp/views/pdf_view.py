from datetime import date, datetime
from fpdf import FPDF
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
import os

from ..models import Category, CostCenter, OrderDetails, Ppmp

class ItemInfo:
	def __init__(self, item:OrderDetails):
		self.name = item.item.name
		self.id = item.item.id
		self.cat = item.cat_code
		self.qty_distrib = [item.first_quant, item.second_quant, item.third_quant, item.fourth_quant]
		self.unit = item.item.unit
		self.price = item.item.get_price(datetime=date(year=int(item.ppmp.year), month=1, day=1))

	def compute_quarter_amnt(self, quarter:int):
		if quarter <= 0 and quarter > 4:
			return round(0,2)

		qty = float(self.qty_distrib[quarter-1])
		price = float(self.price)
		amnt = qty * price
		return round(amnt, 2)

	def get_all_quarter_distrib(self):
		out = []

		for i in range(1, len(self.qty_distrib) + 1):
			qty = self.qty_distrib[i-1]
			amnt = self.compute_quarter_amnt(quarter=i)
			out.append((int(qty), amnt))

		return out

class PPMP_PDF(FPDF):
	def __init__(self, cc_code, ppmp_id, cat_code, debug=False):
		super().__init__(orientation='landscape', format='letter')
		
		self.cc = CostCenter.objects.get(code=cc_code)
		self.ppmp = Ppmp.objects.get(id=ppmp_id)
		self.cat = Category.objects.get(code=cat_code)
		self.orderdetails = OrderDetails.objects.select_related().filter(ppmp_id=ppmp_id, cat_code=cat_code).all()

		self.margin = 8
		self.debug = debug
		
		today = datetime.now().strftime("%Y%m%d")
		self.set_margin(self.margin)
		self.set_title(title=f'''ppmp_{today}''')
		self.auto_page_break = True
	
	# override function
	def header(self):
		'''PDF header for PPMP documents
		'''
		msu_iit_seal = os.path.join(settings.TAILWIND_STATIC_DIR, 'images/logo/msu_iit_seal.png')
		qr_code_path = os.path.join(settings.TAILWIND_STATIC_DIR, 'images/logo/sample_qr_code.png')
		self.image(qr_code_path, w=25, h=25, x=self.epw-(25-self.margin), y=self.margin)
		self.set_y(8)
		self.image(msu_iit_seal, w=25, h=25, x=self.epw-50)
		self.set_y(8)
		self.set_font('Times', size=12, style="B")
		self.cell(txt="MSU - ILIGAN INSTITUTE OF TECHNOLOGY", border=self.debug)
		self.ln(10)
		self.set_font('Arial', size=10)
		self.cell(txt="OFFICE OF THE BAC SECRETARIAT (OBS)", border=self.debug)
		self.ln()
		self.set_font('Arial', size=8, style="I")
		self.cell(txt="Tel No. (063) 225-4926", border=self.debug)
		self.ln(12)
		self.cell(w=self.epw, txt=f'''Page {self.page_no()} of np''', align='R')
		self.set_x(8)

		self.detail()
		
		self.order_details()
		
	def asignature(self):
		'''Designated persons who required to sign the documents
		'''
		
		dist_quarters = [0] * 4
		for item in self.orderdetails:
			info = ItemInfo(item)
			distrib = info.get_all_quarter_distrib()
			for i in range(len(distrib)):
				amnt = distrib[i][1]
				dist_quarters[i] += amnt
		
		# summarize all
		self.set_font('Arial', size=8, style="B")
		self.cell(w=14, txt=" ", border=1, align='C', ln=0, h=5)
		self.cell(w=51, txt="Running Total>>", border=1, align='R', h=5)
		self.cell(w=20, txt="", border=1, align='C', h=5)
		self.cell(w=10, txt="", border=1, align='C', h=5)
		self.cell(w=20, txt=f'''{sum(dist_quarters)}''', border=1, align='C', h=5)

		for ammt in dist_quarters:
			self.cell(w=10, txt=" ", border=1, align='C', h=5)
			self.cell(w=27, txt=f'''{ammt}''', border=1, align='C', h=5)

		
		self.set_y(self.eph - 20)
		self.set_font('Arial', size=8)
		self.cell(w=54.6, txt="Prepared By:", border=self.debug)
		self.cell(w=54.6 * 3 - 10, txt="Recommendeding Approval:", border=self.debug)
		self.cell(w=54.6, txt="Approved By:", border=self.debug)
		self.ln(10)
		self.set_font('Arial', size=10, style="")
		self.cell(w=44.6, txt="X", border='B', align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, txt="X", border='B', align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, txt="X", border='B', align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, txt="X", border='B', align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, txt="X", border='B', align='C')
		self.ln()
		self.set_font('Arial', size=8)
		self.cell(w=44.6, h=5, txt="SRA, TAPU", align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, h=5, txt="Directory of Research", align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, h=5, txt="VC for Research and Extension", align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, h=5, txt="Acting Head, Budget Management Office", align='C')
		self.cell(w=10, txt=" ", align='C')
		self.cell(w=44.6, h=5, txt="Chancellor", align='C')

	def detail(self):
		'''PPMP details
		'''
		self.set_font('Arial', size=10, style="B")
		self.cell(w=self.epw, txt=f'''PROJECT PROCUREMENT MANAGEMENT PLAN, {self.ppmp.year}''', border=self.debug)
		
		self.ln(5)

		self.set_font('Arial', size=10)
		self.cell(txt="Cost Center:   ", border=self.debug)
		self.set_font('Arial', size=10, style="BU")
		self.cell(txt=f'''{self.cc.code}''', border=self.debug)
		self.cell(w=10, border=self.debug)
		self.cell(txt=f'''{self.cc.name}''', border=self.debug)
		self.ln(5)

		self.set_font('Arial', size=10)
		self.cell(txt="Source of Fund:   ", border=self.debug)
		self.set_font('Arial', size=10, style="BU")
		self.cell(txt=f'''{self.ppmp.sof.description}''', border=self.debug)
		self.ln(5)

		self.set_font('Arial', size=10)
		self.cell(txt="PPMP ID:   ", border=self.debug)
		self.cell(txt=f'''{self.ppmp.id}''', border=self.debug)
		self.cell(w=10, border=self.debug)
		self.cell(txt=f'''{self.ppmp.type}''', border=self.debug)
		self.ln(5)

		self.set_font('Arial', size=10)
		self.cell(txt="Account Code:   ", border=self.debug)
		self.set_font('Arial', size=10, style="B")
		self.cell(txt=f'''{self.cat.code}''', border=self.debug)
		self.cell(w=10, border=self.debug)
		self.cell(txt=f'''{self.cat.name}''', border=self.debug)
		self.ln(5)

		self.set_font('Arial', size=10)

	def order_details(self):
		'''Order detail table header
		'''
		self.set_font('Arial', size=9, style='B')
		cell_h = 5
		self.cell(w=14, txt="Unit", border=1, align='C', h=10)
		self.cell(w=51, txt="DETAILS", border=1, h=cell_h)
		self.cell(w=20, txt="UNIT", border="LTR", align='C', h=cell_h)
		self.cell(w=30, txt="TOTAL", border=1, align='C', h=cell_h)

		self.cell(w=37, txt="FIRST QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=37, txt="SECOND QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=37, txt="THIRD QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=37, txt="FOURTH QUARTER", border=1, ln=1, align='C', h=cell_h)

		self.cell(w=14, txt=" ", h=cell_h)
		self.cell(w=51, txt="(Nomenclature & Description)", border=1, h=cell_h)
		self.cell(w=20, txt="PRICE", border="LBR", align='C', h=cell_h)
		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=20, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=27, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=27, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=27, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=27, txt="AMOUNT", border=1, align='C', h=cell_h, ln=1)
		self.set_font('Arial', size=8)
		
	def list_all_items(self):
		for item in self.orderdetails:
					
			self.item_cell(item=ItemInfo(item))

			# check current cursor's y position 
			curr_y = self.get_y()
			if curr_y >= 160:
				self.add_page()

	def item_cell(self, item:ItemInfo):
		dist_quarters = item.get_all_quarter_distrib()

		ttl_qty = 0
		ttl_ammt = 0

		for qty, ammt in dist_quarters:
			ttl_qty += qty
			ttl_ammt += ammt

		desc = self.multi_cell(w=51, txt=f'''{item.name}''', align='C',split_only=True)
		
		display=True
		
		border_design = [1,'LTR', 'LR', 'LBR']

		for i in range(len(desc)):
			word = desc[i]
			if len(desc) == 1:
				b = border_design[0]
			elif i == 0:
				b = border_design[1]
			elif i == len(desc) - 1:
				b = border_design[3]
			else:
				b = border_design[2]

			if display:
				self.cell(w=14, txt=f'''{item.unit}''', border=b, align='C', h=5)
			else:
				self.cell(w=14, txt=f''' ''', border=b, align='C', h=5)

			self.cell(w=51,txt=word,border=b, align='C', h=5,)

			if display:
				self.cell(w=20, txt=f'''{item.price}''', border=b, align='C', h=5)
				self.cell(w=10, txt=f'''{ttl_qty}''', border=b, align='C', h=5)
				self.cell(w=20, txt=f'''{ttl_ammt}''', border=b, align='C', h=5)

				for qty, ammt in dist_quarters:
					self.cell(w=10, txt=f'''{qty}''', border=b, align='C', h=5)
					self.cell(w=27, txt=f'''{ammt}''', border=b, align='C', h=5)
			else:
				self.cell(w=20, txt=f''' ''', border=b, align='C', h=5)
				self.cell(w=10, txt=f''' ''', border=b, align='C', h=5)
				self.cell(w=20, txt=f''' ''', border=b, align='C', h=5)

				for qty, ammt in dist_quarters:
					self.cell(w=10, txt=f''' ''', border=b, align='C', h=5)
					self.cell(w=27, txt=f''' ''', border=b, align='C', h=5)
			self.ln()
			display = False
		
	def build(self):
		self.add_page()
		self.header()
		
		self.list_all_items()
		
		self.asignature()

		# for page numbering
		self.alias_nb_pages(alias='np')
		return self.output()

class PR_PDF(FPDF):
	def __init__(self, ppmp_id, debug=False):
		super().__init__(orientation='portrait', format='letter')
		self.debug=debug
		self.margin = 8
		self.set_font('Times', size=12)
		self.set_margin(self.margin)
		self.set_title(title=f'''purchase_request_{ppmp_id}''')
		self.auto_page_break = True

		self.ppmp = Ppmp.objects.get(id=ppmp_id)
		
	def header(self):
		"""Header of the pdf"""
		#TODO: Format header for purchase request pdf
		self.cell(w=51, txt="THIS IS FOR PR", border=1, align='R', h=5)

		self.ln()

	def footer(self):
		"""Footer of the pdf"""
		pass

	def body(self):
		"""Body of the pdf"""
		#TODO: Add a table, one row per pr refer to the img sent
		self.cell(w=15, txt="THIS IS BODY")

	def build(self):
		"""Build the pdf."""
		self.add_page()
		self.body()		
		# for page numbering
		#self.alias_nb_pages(alias='np')
		return self.output()

def create_ppmp_doc(request, ppmp_id, cat_code, cc_code):
	
	pdf = PPMP_PDF(cc_code=cc_code, ppmp_id=ppmp_id, cat_code=cat_code, debug=False)

	return HttpResponse(bytes(pdf.build()), content_type='application/pdf')

def create_pr_doc(request, ppmp_id):
	
	pdf = PR_PDF(ppmp_id=ppmp_id, debug=False)

	return HttpResponse(bytes(pdf.build()), content_type='application/pdf')

