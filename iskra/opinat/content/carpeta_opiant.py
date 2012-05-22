from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class ICarpeta_opiant(form.Schema):
    form.model('carpeta_opiant.xml')

class View(grok.View):
    grok.context(ICarpeta_opiant)
    grok.require('zope2.View')
    grok.name('view')
  
    