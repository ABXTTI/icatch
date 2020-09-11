from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    x_inv = fields.Char('Invisible')
    x_address=fields.Char(string="Address:")
    x_email=fields.Char('Email:')
    x_phone=fields.Char('Phone:')
    x_mobile=fields.Char('Mobile:')
    x_other=fields.Char('Other:')
    x_ntn=fields.Char('NTN:')
    x_gst=fields.Char('GST:')
    x_region = fields.Many2one('region.name',string="Region")
    x_account_man = fields.Many2one('hr.employee',string="Account Manager:")
    x_contact_no = fields.Char('Contact Number:')
    x_customer = fields.Many2one('res.partner',string="Customer:")
    x_brand = fields.Many2one('brand.name',string="Brand:")
    x_campaign = fields.Many2one('campaign.name',string='Campaign:')
    x_job_no = fields.Many2one('sale.order','Job Number:')
    x_stock_quantity = fields.Char('Stock Quantity:')

class BrandName(models.Model):
    _name = 'brand.name'
    _rec_name = 'x_brand'
    x_brand=fields.Char("Brand")

class RegionName(models.Model):
    _name = 'region.name'
    _rec_name = 'x_region'
    x_region=fields.Char("Region")

class CampaignName(models.Model):
    _name = 'campaign.name'
    _rec_name = 'x_campaign'
    x_campaign=fields.Char("Campaign")

class ResPartner(models.Model):
    _inherit = 'res.partner'
    x_brands=fields.Many2one('brand.name', string="Brand")

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    x_med=fields.Many2one('medium.type',string="Medium Type")
    x_city=fields.Many2one('region.name',string="City")
    x_med_descs = fields.Many2one('medium.desc',string="Medium Description")
    x_measures=fields.Many2one('measurement.unit',string="Square Feet/Inches")
    x_height = fields.Float("Height")
    x_width = fields.Float("Width")
    x_quantity=fields.Float("Quantity")

    @api.depends('x_height','x_width','x_measures')
    def size(self):
        for rec in self:
            rec.x_size=rec.x_height*rec.x_width
            rec.x_total_size=rec.x_measures.x_measure*rec.x_size

    x_size = fields.Float("Size", compute='size')
    x_total_size = fields.Float("Total Size", compute='size')

    @api.depends('x_quantity','product_qty')
    def quantity(self):
        for rec in self:
            rec.product_qty = rec.x_total_size*rec.x_quantity

    product_qty=fields.Float("Total Quantity", compute='quantity')

class MediumType(models.Model):
    _name = 'medium.type'
    _rec_name = 'x_med_type'
    x_med_type=fields.Char("Medium Type")

class MediumDesc(models.Model):
    _name = 'medium.desc'
    _rec_name = 'x_med_desc'
    x_med_desc=fields.Char("Medium Description")

class MeasurementUnit(models.Model):
    _name = 'measurement.unit'
    _rec_name = 'x_measure'
    x_measure=fields.Float("Square Feet/Inches", default=1.0)