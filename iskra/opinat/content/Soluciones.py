from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class ISoluciones(form.Schema):
    form.model('Soluciones.xml')

class View(grok.View):
    grok.context(ISoluciones)
    grok.require('zope2.View')
  
   


