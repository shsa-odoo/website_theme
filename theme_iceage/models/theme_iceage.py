from odoo import models

#changes file name accordingly
class ThemeIceage(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_iceage_post_copy(self, mod):
        self.enable_view('website.template_footer_minimalist')


# This Python code is part of an Odoo module.
# Odoo is an open-source ERP (Enterprise Resource Planning) software
# that uses a MVC (Model-View-Controller) architecture. 

# The code defines a class `Themeiceage` that inherits from `theme.utils`,
# an abstract model in Odoo. This class has a method
# `_theme_iceage_post_copy(self, mod)` which is likely to be a hook method
# that gets called after a copy operation related to the theme.

# In this method, it calls `self.enable_view('website.template_footer_minimalist')`.
# This line is enabling a specific view, in this case, a minimalist footer for the website.
# This suggests that the method is used to customize the appearance of the website after a copy operation,
# specifically to ensure that the footer is set to a minimalist style.
