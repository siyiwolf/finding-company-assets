#!/usr/bin/env python3
"""
Finding Technology - Five Looks Three Decisions Framework (Complete English Version)
Generates comprehensive PDF with full strategic planning structure
Logo: finding_technology_logo_v12.png (V12 version)
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
    PageTemplate, Frame, BaseDocTemplate
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from pathlib import Path
import os

# Paths - Use V12 logo
HOME = Path.home()
SCRIPT_DIR = HOME / "调研报告" / "公司制度"
LOGO_PATH = SCRIPT_DIR / "finding_technology_logo_v12.png"
OUTPUT_PATH = SCRIPT_DIR / "Finding_Technology_WuKanSanDing_Framework_Complete_EN.pdf"

print(f"Logo path: {LOGO_PATH}")
print(f"Logo exists: {LOGO_PATH.exists()}")
print(f"Output path: {OUTPUT_PATH}")

def get_logo_dimensions():
    """Logo dimensions: height=1.5cm, width=5.4cm (3.6:1 aspect ratio)"""
    logo_height = 1.5 * cm
    logo_width = 5.4 * cm
    return logo_width, logo_height

def create_header_footer(canvas, doc):
    canvas.saveState()
    
    # Header: Logo (right-aligned)
    if LOGO_PATH.exists():
        try:
            logo_width, logo_height = get_logo_dimensions()
            logo = Image(str(LOGO_PATH), width=logo_width, height=logo_height)
            logo_x = doc.pagesize[0] - logo_width - 2*cm  # 2cm from right margin
            logo_y = doc.pagesize[1] - 2.5*cm  # Position from top
            logo.drawOn(canvas, logo_x, logo_y)
        except Exception as e:
            print(f"Logo error: {e}")
    
    # Header line (below logo)
    canvas.setStrokeColor(colors.HexColor('#E5E7EB'))
    canvas.setLineWidth(0.5)
    header_line_y = doc.pagesize[1] - 3.0*cm
    canvas.line(2*cm, header_line_y, doc.pagesize[0] - 2*cm, header_line_y)
    
    # Footer line
    footer_line_y = 2*cm
    canvas.setStrokeColor(colors.HexColor('#E5E7EB'))
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, footer_line_y, doc.pagesize[0] - 2*cm, footer_line_y)
    
    # Footer text: "make life easy" (left) + page number (center)
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor('#6B7280'))
    canvas.drawString(2*cm, 1.3*cm, "make life easy")
    
    page_num = f"{doc.page}"
    page_num_width = canvas.stringWidth(page_num, "Helvetica", 9)
    canvas.drawString(doc.pagesize[0] / 2 - page_num_width / 2, 1.3*cm, page_num)
    
    canvas.restoreState()

class FrameworkDocument(BaseDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        self.template = PageTemplate(
            id='test',
            frames=[Frame(
                self.leftMargin, 
                self.bottomMargin + 2*cm,  # Space for footer
                self.width, 
                self.height - 4*cm,  # Space for header and footer
                id='normal',
                showBoundary=0
            )],
            onPage=create_header_footer
        )
        self.addPageTemplates(self.template)

def generate_pdf():
    doc = FrameworkDocument(
        str(OUTPUT_PATH),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=3.5*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#007AFF'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subsection_style = ParagraphStyle(
        'SubSection',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#007AFF'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#334155'),
        alignment=TA_JUSTIFY,
        leading=16.5
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Five Looks Three Decisions Framework", title_style))
    story.append(Paragraph("Finding Technology Strategic Planning Methodology", 
                          ParagraphStyle('Subtitle', parent=styles['Normal'], 
                                       fontSize=12, textColor=colors.HexColor('#6B7280'),
                                       alignment=TA_CENTER, spaceAfter=20)))
    story.append(Spacer(1, 0.5*cm))
    
    # ==================== PART I: LOOK AT INDUSTRY ====================
    story.append(Paragraph("I. Look at Industry", section_style))
    
    story.append(Paragraph("1. Industry Value Chain Analysis", subsection_style))
    story.append(Paragraph("Analyze the value chain to identify high-value zones and profit migration trends:", body_style))
    story.append(Paragraph("a. Decompose the industry value chain into segments. Research total market size, average gross margin, and operating margin for each segment. Analyze trends based on historical data.", body_style))
    story.append(Paragraph("b. Visualize value chain migration trends and profit zones using appropriate charts (e.g., trend lines, bar charts).", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2. Industry Trend Analysis", subsection_style))
    story.append(Paragraph("Must include technology trends and customer demand evolution:", body_style))
    story.append(Paragraph("a. Customer research: Identify customer attribute transformation trends over a 7-year time span.", body_style))
    story.append(Paragraph("b. Technology roadmap: Map out key technologies in the industry and their development trends over a 7-year horizon.", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("3. Track Selection", subsection_style))
    story.append(Paragraph("a. Preliminary selection based on market size, CAGR, average gross margin, and operating margin.", body_style))
    story.append(Paragraph("b. Evaluate industry profitability using Porter's Five Forces model. Assess whether the industry is worth entering. Finalize three alternative tracks.", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("4. PESTEL Analysis", subsection_style))
    story.append(Paragraph("For each selected track, conduct macro-environmental analysis (Political, Economic, Social, Technological, Environmental, Legal) to identify structural risks and opportunities.", body_style))
    story.append(Spacer(1, 12))
    
    # ==================== PART II: LOOK AT MARKET ====================
    story.append(Paragraph("II. Look at Market", section_style))
    
    # Track 1
    story.append(Paragraph("Track 1: [Track Name]", subsection_style))
    story.append(Paragraph("a. Market Segmentation: Segment the track based on value orientation and consumption motivation to identify three sub-segments.", body_style))
    
    for i in range(1, 4):
        story.append(Paragraph(f"Sub-segment {i}: [Name]", subsection_style))
        story.append(Paragraph(f"1) Market Size: Calculate TAM (Total Addressable Market), AM (Addressable Market), and TM (Target Market) through industry reports and market research.", body_style))
        story.append(Paragraph(f"2) User Persona:", body_style))
        story.append(Paragraph("a. Demand Analysis: Use VOC (Voice of Customer) and KANO model to identify high-value user needs as input for product design.", body_style))
        story.append(Paragraph("b. Persona Details: Refine user persona based on application scenarios and VOC analysis.", body_style))
        story.append(Paragraph("c. Sales Path: Design the distribution channel from product to end user.", body_style))
        story.append(Paragraph(f"3) Competitive Analysis:", body_style))
        story.append(Paragraph("a. Existing Competitors: Identify Top 3 competitors by market share. Analyze their strengths, weaknesses, and market positioning. Conduct SWOT analysis.", body_style))
        story.append(Paragraph("b. Potential Competitors: Analyze the industry chain to identify potential entrants.", body_style))
        story.append(Paragraph("c. Strategy: Formulate specific strategies for each competitor.", body_style))
        story.append(Spacer(1, 6))
    
    # Track 2
    story.append(Paragraph("Track 2: [Track Name]", subsection_style))
    story.append(Paragraph("a. Market Segmentation: Segment the track based on value orientation and consumption motivation to identify three sub-segments.", body_style))
    
    for i in range(4, 7):
        story.append(Paragraph(f"Sub-segment {i}: [Name]", subsection_style))
        story.append(Paragraph(f"1) Market Size: Calculate TAM, AM, and TM through industry reports and market research.", body_style))
        story.append(Paragraph(f"2) User Persona:", body_style))
        story.append(Paragraph("a. Demand Analysis: Use VOC and KANO model to identify high-value user needs.", body_style))
        story.append(Paragraph("b. Persona Details: Refine user persona based on application scenarios.", body_style))
        story.append(Paragraph("c. Sales Path: Design the distribution channel.", body_style))
        story.append(Paragraph(f"3) Competitive Analysis:", body_style))
        story.append(Paragraph("a. Existing Competitors: Identify Top 3 competitors and conduct SWOT analysis.", body_style))
        story.append(Paragraph("b. Potential Competitors: Identify potential entrants.", body_style))
        story.append(Paragraph("c. Strategy: Formulate strategies for each competitor.", body_style))
        story.append(Spacer(1, 6))
    
    # Track 3
    story.append(Paragraph("Track 3: [Track Name]", subsection_style))
    story.append(Paragraph("a. Market Segmentation: Segment the track based on value orientation and consumption motivation to identify three sub-segments.", body_style))
    
    for i in range(7, 10):
        story.append(Paragraph(f"Sub-segment {i}: [Name]", subsection_style))
        story.append(Paragraph(f"1) Market Size: Calculate TAM, AM, and TM through industry reports and market research.", body_style))
        story.append(Paragraph(f"2) User Persona:", body_style))
        story.append(Paragraph("a. Demand Analysis: Use VOC and KANO model to identify high-value user needs.", body_style))
        story.append(Paragraph("b. Persona Details: Refine user persona based on application scenarios.", body_style))
        story.append(Paragraph("c. Sales Path: Design the distribution channel.", body_style))
        story.append(Paragraph(f"3) Competitive Analysis:", body_style))
        story.append(Paragraph("a. Existing Competitors: Identify Top 3 competitors and conduct SWOT analysis.", body_style))
        story.append(Paragraph("b. Potential Competitors: Identify potential entrants.", body_style))
        story.append(Paragraph("c. Strategy: Formulate strategies for each competitor.", body_style))
        story.append(Spacer(1, 6))
    
    # ==================== PART III: LOOK AT OURSELVES ====================
    story.append(Paragraph("III. Look at Ourselves", section_style))
    
    story.append(Paragraph("1. Company Profile", subsection_style))
    story.append(Paragraph("Positioning: Pioneer in smart hardware for outdoor sports.", body_style))
    story.append(Paragraph("Vision: make life easy.", body_style))
    story.append(Paragraph("Strategic Goal: Become a leader in intelligent outdoor imaging solutions.", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2. SWOT Analysis", subsection_style))
    story.append(Paragraph("Analyze company strengths and weaknesses based on Finding Technology's profile:", body_style))
    story.append(Paragraph("- Strengths: Technology innovation, supply chain efficiency, agile development.", body_style))
    story.append(Paragraph("- Weaknesses: Brand recognition, distribution channels, scale, cash flow.", body_style))
    story.append(Spacer(1, 12))
    
    # ==================== PART IV: STRATEGIC SUMMARY ====================
    story.append(Paragraph("IV. Strategic Summary", section_style))
    
    story.append(Paragraph("1. Market Consolidation", subsection_style))
    story.append(Paragraph("Summarize the characteristics and recommendations for all nine sub-segments based on industry and market analysis.", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2. Business Planning", subsection_style))
    story.append(Paragraph("Design a 3-5 year business plan based on sub-segment characteristics and company strengths/weaknesses:", body_style))
    story.append(Paragraph("- Year 1: Launch MVP, validate product-market fit, acquire seed users.", body_style))
    story.append(Paragraph("- Year 2: Expand channels (online + offline), iterate product V2.0, achieve X% market share.", body_style))
    story.append(Paragraph("- Year 3: Product line extension, market expansion, ecosystem building.", body_style))
    story.append(Spacer(1, 6))
    
    # Build PDF
    doc.build(story)
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"PDF size: {os.path.getsize(OUTPUT_PATH)} bytes")

if __name__ == "__main__":
    generate_pdf()
