from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from datetime import date
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from Products.CMFPlone.browser.navigation import get_view_url
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFPlone.interfaces import IPloneSiteRoot
#from Products.CMFPlone import utils

from iskra.opinat.content.carpeta_opiant import ICarpeta_opiant
from iskra.opinat.content.baner import IBaner
from iskra.opinat.content.casexit import ICasexit
from iskra.opinat.content.Caracteristicas import ICaracteristicas
from iskra.opinat.content.Soluciones import ISoluciones
from iskra.opinat.content.Funcionalidad import IFuncionalidad

from Products.ATContentTypes.interfaces.document import IATDocument

from plone.app.folder.folder import IATUnifiedFolder

from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface

####################
# HOME PAGE VIEWLETS
####################


class viewletinicial(ViewletBase):
    """ Viewlet del banner d'entrada """
    render = ViewPageTemplateFile('viewlet.pt')

    def available(self):
        context = self.context
        if INavigationRoot.providedBy(context.__parent__) and IATDocument.providedBy(context):
            # Product is not installed
            return True
        else:
            return False

    def get_banner(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context,'portal_catalog')
        total = catalog(object_provides=IBaner.__identifier__,)
        # if len(total)>0:
        #     return total[0].getObject()
        # else: 
        #    return None
        return total




    def get_banner2(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context,'portal_catalog')
        total = catalog(object_provides=IBaner.__identifier__,
                          path='/'.join(context.getPhysicalPath()))
        return total




class queesnpsViewlet(ViewletBase):
    render = ViewPageTemplateFile('queesnps.pt')


class nuestroNpsViewlet(ViewletBase):
    """ Viewlet del NPS de la home page """
    render = ViewPageTemplateFile('nuestronps.pt')

    def available(self):
        context = self.context
        if INavigationRoot.providedBy(context.__parent__) and not(IATUnifiedFolder.providedBy(context)):
            # Product is not installed
            return True
        else:
            return False


class casosdexitViewlet(ViewletBase):
    """ Viewlet dels casos d'exit de la home page """
    render = ViewPageTemplateFile('casosexit.pt')

    def available(self):
        context = self.context
        if INavigationRoot.providedBy(context.__parent__) and IATDocument.providedBy(context):
            # Product is not installed
            return True
        else:
            return False

    def get_casexit(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')

        total = catalog(object_provides=ICasexit.__identifier__,sort_on='created',sort_order='ascending',)

        return total


    def get_casexit2(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        
        return pc.searchResults(portal_type="casexit")


class peu(ViewletBase):

    render = ViewPageTemplateFile('footer.pt')

    def update(self):
        self.year = date.today().year


#####################
# 1er NIVELL VIEWLETS
#####################


class baner1rnivell(ViewletBase):
    render = ViewPageTemplateFile('baner1rnivell.pt')

    def available(self):
        context = self.context
        if ICarpeta_opiant.providedBy(context.__parent__):
            # Product is not installed
            return True
        elif ICarpeta_opiant.providedBy(context):
            return True
        else:
            return False

    def carpeta(self):
        context = self.context
        if ICarpeta_opiant.providedBy(context):
            return context
        elif ICarpeta_opiant.providedBy(context.__parent__):
            return context.__parent__
        else:
            return None