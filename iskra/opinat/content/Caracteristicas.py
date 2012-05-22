from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class ICaracteristicas(form.Schema):
    form.model('Caracteristicas.xml')

class View(grok.View):
    grok.context(ICaracteristicas)
    grok.require('zope2.View')