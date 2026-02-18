from django.db import models
from django.utils import timezone

# Predefined Choices from User Notes
# Image 0
PROJECT_CHOICES = [
    ('NASM-SR', 'NASM-SR'),
    ('MIRV', 'MIRV'),
    ('SF VSHORADS', 'SF VSHORADS'),
    ('K5', 'K5'),
    ('RUDRAM-II', 'RUDRAM-II'),
    ('AGNI', 'AGNI'),
    ('AKASH', 'AKASH'),
    ('NAG', 'NAG'),
    ('K15', 'K15'),
    ('PRITHVI', 'PRITHVI'),
    ('TRISHUL', 'TRISHUL'),
    ('ASTRA', 'ASTRA'),
    ('DHANUSH', 'DHANUSH'),
    ('TPNM', 'TPNM'),
    ('LFRJ', 'LFRJ'),
]

# Image 0 (Raw/Input Material)
MATERIAL_CHOICES = [
    ("10' AA2014", "10' AA2014"),
    ("20' AA6061", "20' AA6061"),
    ("30' AA7075", "30' AA7075"),
    ("40' TiAl6V4", "40' TiAl6V4"),
    ("50' SS 304", "50' SS 304"),
    ("60' 15CDV6", "60' 15CDV6"),
    ("70' PH-Steels", "70' PH-Steels"),
    ("80' C-263", "80' C-263"),
    ("90' AISI 4340", "90' AISI 4340"),
    ("100' EN24", "100' EN24"),
    ("110' SS420", "110' SS420"),
    ("120' SS440C", "120' SS440C"),
    ("130' SS316", "130' SS316"),
    ('140" AA2024', '140" AA2024'),
    ("150' AA2219", "150' AA2219"),
]

# Image 1 (Printing/Model Material)
PRINTING_MATERIAL_CHOICES = [
    ('Ti6414V', 'Ti6414V'),
    ('SS316L', 'SS316L'),
    ('AlSi10Mg', 'AlSi10Mg'),
    ('Maraging steel', 'Maraging steel'),
    ('17-4PH Steel', '17-4PH Steel'),
    ('Inconel 718', 'Inconel 718'),
    ('Inconel 625', 'Inconel 625'),
    ('ABS', 'ABS'),
    ('PC-ABS', 'PC-ABS'),
    ('PDSF', 'PDSF'),
]

# Image 1 (Designations)
DESIGNATION_CHOICES = [
    ('SC-B', 'SC-B'),
    ('SC-C', 'SC-C'),
    ('SC-D', 'SC-D'),
    ('TO-A', 'TO-A'),
    ('TO-B', 'TO-B'),
    ('TO-C', 'TO-C'),
    ('STA-B', 'STA-B'),
    ('SC-E', 'SC-E'),
    ('SC-F', 'SC-F'),
    ('SC-G', 'SC-G'),
    ('SC-H', 'SC-H'),
]

# Image 1 (Scientists)
SCIENTIST_NAMES = [
    ('BK Das', 'BK Das'),
    ('V. Kamat', 'V. Kamat'),
    ('G. Gopi', 'G. Gopi'),
    ('Upendra Kumar', 'Upendra Kumar'),
    ('S. Christopher', 'S. Christopher'),
    ('Avinash Chander', 'Avinash Chander'),
]

class WorkRequisition(models.Model):
    # Header Info
    project = models.CharField(max_length=100, choices=PROJECT_CHOICES, verbose_name="Project / Directorate")
    date = models.DateField(default=timezone.now)
    nomenclature = models.TextField(help_text="Separate sheet may be enclosed with list of items & their quantity")
    quantity = models.CharField(max_length=100)
    
    # Required for
    system_subsystem = models.CharField(max_length=200, verbose_name="Required for System/Subsystem")
    
    # Work Details
    work_details_input = models.CharField(max_length=200, verbose_name="Input")
    material = models.CharField(max_length=200, choices=MATERIAL_CHOICES, verbose_name="Material", blank=True, null=True)
    work_details_output = models.CharField(max_length=200, verbose_name="Output")
    cad_model_enclosed = models.BooleanField(default=False, verbose_name="CAD Model Enclosed (Yes/No)")
    drawing_enclosed = models.BooleanField(default=False, verbose_name="Drawing Enclosed (Yes/No)")
    
    # Indentor / User
    indentor_name = models.CharField(max_length=100, choices=SCIENTIST_NAMES, verbose_name="Indentor Name")
    indentor_designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES, verbose_name="Indentor Designation")
    indentor_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone No.")
    
    user_division_head = models.CharField(max_length=100, blank=True, null=True, verbose_name="User Division Head")
    
    # --- For CFAM use only ---
    # Nature of work 
    # Use CharField to store comma-separated values if multiple selected, 
    # but initially we might just let user pick one or use a MultipleChoiceField in form.
    nature_of_work = models.CharField(max_length=100, blank=True, verbose_name="Nature of work")

    model_material = models.CharField(max_length=100, choices=PRINTING_MATERIAL_CHOICES, blank=True, verbose_name="Model Material")
    model_material_qty = models.CharField(max_length=100, blank=True, verbose_name="Model Material Qty")
    
    support_material_qty = models.CharField(max_length=100, blank=True, verbose_name="Support Material Qty")
    estd_printing_time = models.CharField(max_length=100, blank=True, verbose_name="Estd. Printing Time")
    
    # Risk Analysis
    risk_analysis_adequate = models.BooleanField(default=True, verbose_name="Risk analysis Adequate")
    risk_analysis_update_orr = models.BooleanField(default=False, verbose_name="If not adequate, update ORR (Yes/No)")
    
    # Recommendation
    recommendation_name = models.CharField(max_length=100, blank=True, choices=SCIENTIST_NAMES, verbose_name="Recommendation Name")
    recommendation_designation = models.CharField(max_length=100, blank=True, choices=DESIGNATION_CHOICES, verbose_name="Recommendation Designation")
    recommendation_date = models.DateField(null=True, blank=True)
    
    # Approval
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved'),
        ('Pending', 'Pending'),
    ]
    approval_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    head_cfam_name = models.CharField(max_length=100, blank=True, default="Head, CFAM")
    work_no = models.CharField(max_length=100, blank=True, verbose_name="Work No.")
    approval_date = models.DateField(null=True, blank=True, verbose_name="Date")
    
    agreed_pdc = models.DateField(null=True, blank=True, verbose_name="Agreed PDC")
    extended_pdc = models.DateField(null=True, blank=True, verbose_name="Extended PDC")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project} - {self.date}"
