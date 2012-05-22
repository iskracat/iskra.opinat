from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class IFuncionalidad(form.Schema):
    form.model('Funcionalidad.xml')



class View(grok.View):
    grok.context(IFuncionalidad)
    grok.require('zope2.View')
    
    def get_funciona(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, "portal_catalog")
        
        total = catalog(object_provides=IFuncionalidad.__identifier__,sort_on='created',sort_order='ascending',)

        valor_de_retorn = []
        for brain in total:
        	if brain.getId == self.context.getId():
        		valor = True
        	else:
        		valor = False
        	valor_de_retorn.append({'brain':brain, 'actiu':valor})
        return valor_de_retorn


