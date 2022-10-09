from fpdf import FPDF
from django.http import HttpResponse
from django.conf import settings
import os

from ..models import Category, CostCenter, ItemDescription, OrderDetails, Ppmp, Prices

class ItemInfo:
	def __init__(self, item:OrderDetails):
		item_specs = []
			
		if item.item_desc.spec_1 != 'None':
			item_specs.append(item.item_desc.spec_1)
		if item.item_desc.spec_2 != 'None':
			item_specs.append(item.item_desc.spec_2)
		if item.item_desc.spec_3 != 'None':
			item_specs.append(item.item_desc.spec_3)
		if item.item_desc.spec_4 != 'None':
			item_specs.append(item.item_desc.spec_4)
		if item.item_desc.spec_5 != 'None':
			item_specs.append(item.item_desc.spec_5)

		self.unit = item.price.unit
		self.name = item.item_desc.item.general_name + "-" + ",".join(item_specs)
		self.unit_price = item.price.price
		self.qty_quart_distrib = (item.first_quart_quant, item.second_quart_quant, item.third_quart_quant, item.fourth_quart_quant)

	def compute_quarter_amnt(self, quarter:int):
		qty = float(self.qty_quart_distrib[quarter-1])
		price = float(self.unit_price)
		amnt = qty * price
		return round(amnt, 2)

	def get_all_quarter_distrib(self):
		out = []

		for i in range(1, len(self.qty_quart_distrib) + 1):
			qty = self.qty_quart_distrib[i-1]
			amnt = self.compute_quarter_amnt(quarter=i)
			out.append((int(qty), amnt))

		return out
class PDF(FPDF):
	def __init__(self, cc_id, ppmp_id, cat_id, debug=False):
		super().__init__(orientation='landscape', format='letter')
		
		self.cc = CostCenter.objects.get(id=cc_id)
		self.ppmp = Ppmp.objects.get(id=ppmp_id)
		self.cat = Category.objects.get(id=cat_id)
		self.orderdetails = OrderDetails.objects.select_related().filter(ppmp_id=ppmp_id).filter(item_desc__item__category_id=cat_id).all()

		self.margin = 8
		self.debug = debug
		self.set_margin(self.margin)
		self.set_title(title=f'''ppmp_{self.ppmp.id}_report''')
		self.auto_page_break = True
		
	def header(self):
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
		summary = {}
		dist_quarters = [0] * 4
		for item in self.orderdetails:
			info = ItemInfo(item)
			distrib = info.get_all_quarter_distrib()
			for i in range(len(distrib)):
				amnt = distrib[i][1]
				dist_quarters[i] += amnt
		
		
		self.set_font('Arial', size=8, style="B")
		self.cell(w=10, txt=" ", border=1, align='C', ln=0, h=5)
		self.cell(w=51, txt="Running Total>>", border=1, align='R', h=5)
		self.cell(w=20, txt="", border=1, align='C', h=5)
		self.cell(w=10, txt="", border=1, align='C', h=5)
		self.cell(w=20, txt=f'''{sum(dist_quarters)}''', border=1, align='C', h=5)

		for ammt in dist_quarters:
			self.cell(w=10, txt=" ", border=1, align='C', h=5)
			self.cell(w=28, txt=f'''{ammt}''', border=1, align='C', h=5)

		
		self.set_y(self.eph - 20)
		print("a:",self.get_y())
		# self.ln(10)
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

	def detail(self, context={}):
		self.set_font('Arial', size=10, style="B")
		self.cell(w=self.epw, txt=f'''PROJECT PROCUREMENT MANAGEMENT PLAN, YYYY''', border=self.debug)
		
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
		self.set_font('Arial', size=9, style='B')
		cell_h = 5
		self.cell(w=10, txt="Unit", border=1, h=10)
		self.cell(w=51, txt="DETAILS", border=1, h=cell_h)
		self.cell(w=20, txt="UNIT", border="LTR", align='C', h=cell_h)
		self.cell(w=30, txt="TOTAL", border=1, align='C', h=cell_h)

		self.cell(w=38, txt="FIRST QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=38, txt="SECOND QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=38, txt="THIRD QUARTER", border=1, align='C', h=cell_h)
		self.cell(w=38, txt="FOURTH QUARTER", border=1, ln=1, align='C', h=cell_h)

		self.cell(w=10, txt=" ", h=cell_h)
		self.cell(w=51, txt="(Nomenclature & Description)", border=1, h=cell_h)
		self.cell(w=20, txt="PRICE", border="LBR", align='C', h=cell_h)
		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=20, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=28, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=28, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=28, txt="AMOUNT", border=1, align='C', h=cell_h)

		self.cell(w=10, txt="QTY", border=1, align='C', h=cell_h)
		self.cell(w=28, txt="AMOUNT", border=1, align='C', h=cell_h, ln=1)
		self.set_font('Arial', size=8)
		
	def items(self):
		for item in self.orderdetails:
					
			self.item_cell(item=ItemInfo(item))
			# add page break
			# modify to depending on the current x and y
			curr_y = self.get_y()
			print("curr_y: ",curr_y)
			if curr_y >= 160:
				self.add_page()
			

	def get_initial_xy(self):
		return (self.get_x(), self.get_y())

	def compute_cell_height(self, word_h, name: str):
		x, y = self.get_initial_xy()
		self.set_draw_color(r=255, g=255, b=255)
		self.set_text_color(r=255, g=255, b=255)
		self.multi_cell(w=10, txt="X", border=1, align='C', ln=0)
		x1 = self.get_x()
		y1 = self.get_y() 
		self.set_xy(x=x1, y=y1-word_h)
		
		self.multi_cell(w=51, txt=name, border=1, h=5)
		x2 = self.get_x()
		y2 = self.get_y()
		
		h = y1-y2 - word_h
		self.set_xy(x=x, y=y-h)
		self.set_draw_color(r=0, g=0, b=0)
		self.set_text_color(r=0, g=0, b=0)

		return h

	def item_cell(self, item:ItemInfo):
		dist_quarters = item.get_all_quarter_distrib()

		ttl_qty = 0
		ttl_ammt = 0

		for qty, ammt in dist_quarters:
			ttl_qty += qty
			ttl_ammt += ammt

		word_h = 3
		x, y = self.get_initial_xy()
		cell_h = self.compute_cell_height(word_h, item.name)

		self.multi_cell(w=10, txt=f'''{item.unit}''', border=1, align='C', ln=0, h=cell_h)
		self.multi_cell(w=51, txt=f'''{item.name}''', border=1, h=5)
		x2 = self.get_x()
		y2 = self.get_y()
		self.set_xy(x=x2, y=y2)

		self.cell(w=20, txt=f'''{item.unit_price}''', border=1, align='C', h=cell_h)
		self.cell(w=10, txt=f'''{ttl_qty}''', border=1, align='C', h=cell_h)
		self.cell(w=20, txt=f'''{ttl_ammt}''', border=1, align='C', h=cell_h)

		for qty, ammt in dist_quarters:
			self.cell(w=10, txt=f'''{qty}''', border=1, align='C', h=cell_h)
			self.cell(w=28, txt=f'''{ammt}''', border=1, align='C', h=cell_h)

		self.set_xy(x=x, y=y-cell_h)

	def build(self):
		self.add_page()
		self.header()
		
		self.items()
		
		self.asignature()

		self.alias_nb_pages(alias='np')
		return self.output()


def create_pdf(request):
	
	cc_id = request.POST['cc_id']
	ppmp_id = request.POST['ppmp_id']
	cat_id = request.POST['cat_id']
	
	pdf = PDF(cc_id=cc_id, ppmp_id=ppmp_id, cat_id=cat_id, debug=False)

	return HttpResponse(bytes(pdf.build()), content_type='application/pdf')