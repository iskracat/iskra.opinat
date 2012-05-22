from plone.directives import form
from five import grok
from Products.ATContentTypes.interfaces.image import IATImage
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.behaviors.related import IRelatedItems

class IBaner(form.Schema):
    form.model('baner.xml')

class View(grok.View):
    grok.context(IBaner)
    grok.require('zope2.View')