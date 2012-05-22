# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView
from iskra.opinat.content.casexit import ICasexit
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName



class FolderCasexit(BrowserView):
    __call__=ViewPageTemplateFile('llistat_casexits.pt')

    def get_casexit(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context,'portal_catalog')

        import pdb; pdb.set_trace()
        total = catalog(object_provides=ICasexit.__identifier__,
                          path='/'.join(context.getPhysicalPath()))

        if len(total)>0:
            return total[0].getObject()
        else: 
            return None

class FolderCaract(BrowserView):
    __call__=ViewPageTemplateFile('llistat_caract.pt')


class FolderQueesnps(BrowserView):
    __call__=ViewPageTemplateFile('llistat_queesnps.pt')

class FolderFunciona(BrowserView):
    __call__=ViewPageTemplateFile('llistat_funciona.pt')


class FolderSoluciones(BrowserView):
    __call__=ViewPageTemplateFile('llistat_soluciones.pt')

